import pickle
import random
import threading
import urllib2

import datetime

import re

import os
import requests
import time
import logging
import sys

from response_html_handler import *

def worker(targetwebsite,object,file_name,typoshandler):
    typos = []
    print targetwebsite

    typos = []
    if targetwebsite != 'fakedomain.com':
        try:
            same_owner_response_codes = typoshandler.response_checker(targetwebsite, object['same_owner_typos'],file_name)
            dif_owner_response_codes = typoshandler.response_checker(targetwebsite, object['dif_owner_typos'],file_name)
            info = {}
            info['key'] = targetwebsite
            info['response_code_for_same_owners'] = same_owner_response_codes
            info['response_code_for_dif_owners'] = dif_owner_response_codes
            pause = random.random()
            logging.debug('Sleeping %0.02f', pause)
            time.sleep(pause)
            typoshandler.save(info,file_name)
            logging.debug('Done')
        except:
            pass
def get_data_saved(file_name):
    print '-------------------------result for alexa top 50 news domain names typos by new tlds-------------------------'
    objects = []
    same_owners= 0
    dif_owners = 0
    with (open(file_name, "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    #print objects
    openfile.close()
    return objects

def response_code_checker(name,file_name):
    objects = get_data_saved(name)
    remaining = len(objects) % 20
    remaining_domains = objects[-remaining+1:]
    #print len(objects),remaining
    for i in range(remaining):
        new_fake_dns_info = {}
        new_fake_dns_info['key'] = 'fakedomain.com'
        new_fake_dns_info['same_owner_typos'] ={}
        new_fake_dns_info['dif_owner_typos'] = {}
        objects.append(new_fake_dns_info)
        #print 'added'
    #get_request_checker_for_same(['bbc.com','foxnews.kr'])
    #import pdb
    #pdb.set_trace()
    print 'we are going to call our threads'
    for a, b,c,d,e,f,g,h,l,m,n,p,q,r,s,a1,w1,e1,r1,y1 in zip(*[iter(objects)] * 20):
        print 'we are calling'
        typoshandler = response_code_Handler()
        t1 = threading.Thread(target=worker, args=(a['key'],a,file_name, typoshandler,))
        t1.start()
        typoshandler = response_code_Handler()
        t2 = threading.Thread(target=worker, args=(b['key'], b,file_name,typoshandler,))
        t2.start()

        typoshandler = response_code_Handler()
        t3 = threading.Thread(target=worker, args=(c['key'],c,file_name, typoshandler,))
        t3.start()
        typoshandler = response_code_Handler()
        t4 = threading.Thread(target=worker, args=(d['key'],d, file_name,typoshandler,))
        t4.start()

        typoshandler = response_code_Handler()
        t5 = threading.Thread(target=worker, args=(e['key'],e,file_name, typoshandler,))
        t5.start()

        typoshandler = response_code_Handler()
        t6 = threading.Thread(target=worker, args=(f['key'],f,file_name, typoshandler,))
        t6.start()


        typoshandler = response_code_Handler()
        t7 = threading.Thread(target=worker, args=(g['key'],g,file_name, typoshandler,))
        t7.start()

        typoshandler = response_code_Handler()
        t8 = threading.Thread(target=worker, args=(h['key'],h,file_name, typoshandler,))
        t8.start()

        typoshandler = response_code_Handler()
        t9 = threading.Thread(target=worker, args=(l['key'],l,file_name, typoshandler,))
        t9.start()
        typoshandler = response_code_Handler()
        t10 = threading.Thread(target=worker, args=(m['key'],m, file_name,typoshandler,))
        t10.start()

        typoshandler = response_code_Handler()
        t11 = threading.Thread(target=worker, args=(n['key'],n,file_name, typoshandler,))
        t11.start()

        typoshandler = response_code_Handler()
        t12 = threading.Thread(target=worker, args=(p['key'],p,file_name, typoshandler,))
        t12.start()


        typoshandler = response_code_Handler()
        t13 = threading.Thread(target=worker, args=(q['key'],q,file_name, typoshandler,))
        t13.start()

        typoshandler = response_code_Handler()
        t14 = threading.Thread(target=worker, args=(r['key'],r,file_name, typoshandler,))
        t14.start()

        typoshandler = response_code_Handler()
        t15 = threading.Thread(target=worker, args=(s['key'],s,file_name, typoshandler,))
        t15.start()

        typoshandler = response_code_Handler()
        t16 = threading.Thread(target=worker, args=(a1['key'],a1,file_name, typoshandler,))
        t16.start()
        typoshandler = response_code_Handler()
        t17 = threading.Thread(target=worker, args=(w1['key'],w1,file_name, typoshandler,))
        t17.start()

        typoshandler = response_code_Handler()
        t18 = threading.Thread(target=worker, args=(e1['key'],e1,file_name, typoshandler,))
        t18.start()

        typoshandler = response_code_Handler()
        t19 = threading.Thread(target=worker, args=(r1['key'],r1,file_name, typoshandler,))
        t19.start()

        typoshandler = response_code_Handler()
        t20 = threading.Thread(target=worker, args=(y1['key'],y1,file_name, typoshandler,))
        t20.start()

        logging.debug('Waiting for worker threads')
        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

if __name__ == "__main__":
    name = sys.argv[1]
    file_name= sys.argv[2]
    now = datetime.datetime.now()

    response_code_checker(name,file_name)
    #registeration_plotter()
    #response_code_plotter()
    #typo_generation_model_stat()