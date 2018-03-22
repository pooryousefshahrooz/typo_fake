#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import pickle
import random
import threading
import time

import collections

import urllib2

import collections

import datetime

#from typo_generation_all_models import  __phillipa
from typo_generation_models import __phillipa

__author__ = 'Shahrooz'
__version__ = '1.0'
__email__ = 'shahrooz@cs.umass.edu'

import re
import sys
import time

import threading
from random import randint

from typo_generation_models import *
try:
    import queue
except ImportError:
    import Queue as queue

try:
    import dns.resolver
    from dns.exception import DNSException
    MODULE_DNSPYTHON = True
except ImportError:
    MODULE_DNSPYTHON = False
    pass

try:
    import GeoIP
    MODULE_GEOIP = True
except ImportError:
    MODULE_GEOIP = False
    pass

try:
    import whois
    MODULE_WHOIS = True
except ImportError:
    MODULE_WHOIS = False
    pass

try:
    import ssdeep
    MODULE_SSDEEP = True
except ImportError:
    MODULE_SSDEEP = False

try:
    import requests
    MODULE_REQUESTS = True
except ImportError:
    MODULE_REQUESTS = False
    pass


REQUEST_TIMEOUT_DNS = 5
REQUEST_TIMEOUT_HTTP = 5
REQUEST_TIMEOUT_SMTP = 5
THREAD_COUNT_DEFAULT = 10

if sys.platform != 'win32' and sys.stdout.isatty():
    FG_RND = '\x1b[3%dm' % randint(1, 8)
    FG_RED = '\x1b[31m'
    FG_YEL = '\x1b[33m'
    FG_GRE = '\x1b[32m'
    FG_MAG = '\x1b[35m'
    FG_CYA = '\x1b[36m'
    FG_BLU = '\x1b[34m'
    FG_RST = '\x1b[39m'
    ST_BRI = '\x1b[1m'
    ST_RST = '\x1b[0m'
else:
    FG_RND = ''
    FG_RED = ''
    FG_YEL = ''
    FG_GRE = ''
    FG_MAG = ''
    FG_CYA = ''
    FG_BLU = ''
    FG_RST = ''
    ST_BRI = ''
    ST_RST = ''


DB__NEW_TLD = []
with open("tlds-alpha-by-domain.txt") as f:
    websitescontent = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
websitescontent = [x2.strip() for x2 in websitescontent]
for item in websitescontent:
    if len(item)<4:
        DB__NEW_TLD.append(item)


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )



class TyposHandler(object):
    def __init__(self):
        self.lock = threading.Lock()

        self.dns_dictionary = {}
    def get_dns_info(self,domains,official_web_site):
        dic_typo_dns_info = {}
        #print domains
        thread_specific_dns_dictionary = {}
        try:
            official_dns_info = whois.whois(official_web_site)
            offficial_registar = official_dns_info.registrar
        except:
            pass
        registered_typo = []
        for typo in domains:
            try:
                typo_dns_info = whois.whois(typo)
                if typo_dns_info.registrar:
                    dic_typo_dns_info[typo] = typo_dns_info
            except:
                pass
        thread_specific_dns_dictionary['key'] = official_web_site
        thread_specific_dns_dictionary['typos_dns_info'] = dic_typo_dns_info
        return thread_specific_dns_dictionary


    def save(self,info,saving_file_name):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            pickle_out = open("dns_info_for_"+saving_file_name+".pickle", "a+b")
            pickle.dump(info, pickle_out)
            pickle_out.close()
        finally:
            self.lock.release()

def worker(targetwebsite,saving_file_name,typoshandler):
    if targetwebsite !='fakedomain.com':
        typos = []
        dfuzz = DomainFuzz(targetwebsite)
        dfuzz.generate()
        Generated_Domains = dfuzz.domains
        typo_candidates = []
        for dom in Generated_Domains:
            typo_candidates.append(dom['domain-name'])
        tempt_typos = []
        for typo in typo_candidates:
                typo_candidates_by_newtlds = generate_typo_by_new_tlds(DB__NEW_TLD, typo, targetwebsite)
                for n in typo_candidates_by_newtlds:
                    tempt_typos.append(n)
        split = targetwebsite.split('.')
        if len(split) == 2:
            tld = split[1]
            domain = split[0]
        # print WebSiteName + "," +Domain_Name
        elif len(split) == 3:
            tld = split[2]
            domain = split[0] + "." + split[1]
        phillipas_typos = __phillipa(domain,tld)

        tempt_typos.extend(phillipas_typos)
        info = typoshandler.get_dns_info(tempt_typos,targetwebsite)
        print info
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        typoshandler.save(info,saving_file_name)
        logging.debug('Done')
#websites = ["bbc.com","reddit.com","nytimes.com","bloomberg.com"]

web_site_file_name = sys.argv[1]

with open(web_site_file_name) as f:
    websites = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
websites = [x2.strip() for x2 in websites]

now = datetime.datetime.now()
saving_file_name  = now.isoformat()+'_'+web_site_file_name
remaining= len(websites)%20
remaining_domains = websites[-remaining:]
for i in range(remaining):
    websites.append('fakedomain.com')

for q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20 in zip(*[iter(websites)] * 20):
    typoshandler = TyposHandler()
    t1 = threading.Thread(target=worker, args=(q1, saving_file_name, typoshandler,))
    t1.start()
    # import pdb
    # pdb.set_trace()
    typoshandler = TyposHandler()
    t2 = threading.Thread(target=worker, args=(q2, saving_file_name, typoshandler,))
    t2.start()

    typoshandler = TyposHandler()
    t3 = threading.Thread(target=worker, args=(q3, saving_file_name, typoshandler,))
    t3.start()
    typoshandler = TyposHandler()
    t4 = threading.Thread(target=worker, args=(q4, saving_file_name, typoshandler,))
    t4.start()

    t5 = threading.Thread(target=worker, args=(q5, saving_file_name, typoshandler,))
    t5.start()
    typoshandler = TyposHandler()
    t6 = threading.Thread(target=worker, args=(q6, saving_file_name, typoshandler,))
    t6.start()

    typoshandler = TyposHandler()
    t7 = threading.Thread(target=worker, args=(q7, saving_file_name, typoshandler,))
    t7.start()
    typoshandler = TyposHandler()
    t8 = threading.Thread(target=worker, args=(q8, saving_file_name, typoshandler,))
    t8.start()

    t9 = threading.Thread(target=worker, args=(q9, saving_file_name, typoshandler,))
    t9.start()
    typoshandler = TyposHandler()
    t10 = threading.Thread(target=worker, args=(q10, saving_file_name, typoshandler,))
    t10.start()

    typoshandler = TyposHandler()
    t11 = threading.Thread(target=worker, args=(q11, saving_file_name, typoshandler,))
    t11.start()

    typoshandler = TyposHandler()
    t12 = threading.Thread(target=worker, args=(q12, saving_file_name, typoshandler,))
    t12.start()
    typoshandler = TyposHandler()
    t13 = threading.Thread(target=worker, args=(q13, saving_file_name, typoshandler,))
    t13.start()

    t14 = threading.Thread(target=worker, args=(q14, saving_file_name, typoshandler,))
    t14.start()
    typoshandler = TyposHandler()
    t15 = threading.Thread(target=worker, args=(q15, saving_file_name, typoshandler,))
    t15.start()

    typoshandler = TyposHandler()
    t16 = threading.Thread(target=worker, args=(q16, saving_file_name, typoshandler,))
    t16.start()
    typoshandler = TyposHandler()
    t17 = threading.Thread(target=worker, args=(q17, saving_file_name, typoshandler,))
    t17.start()

    t18 = threading.Thread(target=worker, args=(q18, saving_file_name, typoshandler,))
    t18.start()
    typoshandler = TyposHandler()
    t19 = threading.Thread(target=worker, args=(q19, saving_file_name, typoshandler,))
    t19.start()
    typoshandler = TyposHandler()
    t20 = threading.Thread(target=worker, args=(q20, saving_file_name, typoshandler,))
    t20.start()
    logging.debug('Waiting for worker threads')
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()




