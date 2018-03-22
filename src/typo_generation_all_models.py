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

__author__ = 'Shahrooz'
__version__ = '1.0'
__email__ = 'shahrooz@cs.umass.edu'

import re
import sys
import socket
import signal
import time
import argparse
import threading
from random import randint
from os import path
import smtplib
import json

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

DIR = path.abspath(path.dirname(sys.argv[0]))
DIR_DB = 'database'
FILE_GEOIP = path.join(DIR, DIR_DB, 'GeoIP.dat')
FILE_TLD = path.join(DIR, DIR_DB, 'effective_tld_names.dat')
#FILE_NEW_TLD = path.join(DIR, DIR_DB, 'tlds-alpha-by-domain.txt')
DB_GEOIP = path.exists(FILE_GEOIP)
DB_TLD = path.exists(FILE_TLD)


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
class DomainFuzz():

    def __init__(self, domain):
        self.domain, self.tld = self.__domain_tld(domain)
        self.domains = []
        self.qwerty = {
         '1': '2a'
        }
        self.qwerty = {
        '1': '2q', '2': '3wq1', '3': '4ew2', '4': '5re3', '5': '6tr4', '6': '7yt5', '7': '8uy6', '8': '9iu7', '9': '0oi8', '0': 'po9',
        'q': '12wa', 'w': '3esaq2', 'e': '4rdsw3', 'r': '5tfde4', 't': '6ygfr5', 'y': '7uhgt6', 'u': '8ijhy7', 'i': '9okju8', 'o': '0plki9', 'p': 'lo0',
        'a': 'qwsz', 's': 'edxzaw', 'd': 'rfcxse', 'f': 'tgvcdr', 'g': 'yhbvft', 'h': 'ujnbgy', 'j': 'ikmnhu', 'k': 'olmji', 'l': 'kop',
        'z': 'asx', 'x': 'zsdc', 'c': 'xdfv', 'v': 'cfgb', 'b': 'vghn', 'n': 'bhjm', 'm': 'njk'
        }
        self.azerty = {
        '1': '2a'
        }
        self.keyboards = [ self.qwerty]

    def __domain_tld(self, domain):
        domain = domain.rsplit('.', 2)

        if len(domain) == 2:
            return domain[0], domain[1]

        if DB_TLD:
            cc_tld = {}
            re_tld = re.compile('^[a-z]{2,4}\.[a-z]{2}$', re.IGNORECASE)

            for line in open(FILE_TLD):
                line = line[:-1]
                if re_tld.match(line):
                    sld, tld = line.split('.')
                    if not tld in cc_tld:
                        cc_tld[tld] = []
                    cc_tld[tld].append(sld)

            sld_tld = cc_tld.get(domain[2])
            if sld_tld:
                if domain[1] in sld_tld:
                    return domain[0], domain[1] + '.' + domain[2]

        return domain[0] + '.' + domain[1], domain[2]

    def __validate_domain(self, domain):
        if len(domain) == len(domain.encode('idna')) and domain != domain.encode('idna'):
            return False
        allowed = re.compile('(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}\.?$)', re.IGNORECASE)
        return allowed.match(domain.encode('idna'))

    def __filter_domains(self):
        seen = set()
        filtered = []
        for d in self.domains:
            #if not self.__validate_domain(d['domain-name']):
                #p_err("debug: invalid domain %s\n" % d['domain-name'])
            if self.__validate_domain(d['domain-name']) and d['domain-name'] not in seen:
                seen.add(d['domain-name'])
                filtered.append(d)

        self.domains = filtered

    def __bitsquatting(self):
        result = []
        masks = [1, 2, 4, 8, 16, 32, 64, 128]
        for i in range(0, len(self.domain)):
            c = self.domain[i]
            for j in range(0, len(masks)):
                b = chr(ord(c) ^ masks[j])
                o = ord(b)
                if (o >= 48 and o <= 57) or (o >= 97 and o <= 122) or o == 45:
                    result.append(self.domain[:i] + b + self.domain[i+1:])

        return result

    def __homoglyph(self):
        glyphs = {
        'a': [u'à', u'á', u'â', u'ã', u'ä', u'å', u'ɑ', u'а', u'ạ', u'ǎ', u'ă', u'ȧ', u'ӓ'],
        'b': ['d', 'lb', 'ib', u'ʙ', u'Ь', u'b̔', u'ɓ', u'Б'],
        'c': [u'ϲ', u'с', u'ƈ', u'ċ', u'ć', u'ç'],
        'd': ['b', 'cl', 'dl', 'di', u'ԁ', u'ժ', u'ɗ', u'đ'],
        'e': [u'é', u'ê', u'ë', u'ē', u'ĕ', u'ě', u'ė', u'е', u'ẹ', u'ę', u'є', u'ϵ', u'ҽ'],
        'f': [u'Ϝ', u'ƒ', u'Ғ'],
        'g': ['q', u'ɢ', u'ɡ', u'Ԍ', u'Ԍ', u'ġ', u'ğ', u'ց', u'ǵ', u'ģ'],
        'h': ['lh', 'ih', u'һ', u'հ', u'Ꮒ', u'н'],
        'i': ['1', 'l', u'Ꭵ', u'í', u'ï', u'ı', u'ɩ', u'ι', u'ꙇ', u'ǐ', u'ĭ'],
        'j': [u'ј', u'ʝ', u'ϳ', u'ɉ'],
        'k': ['lk', 'ik', 'lc', u'κ', u'ⲕ', u'κ'],
        'l': ['1', 'i', u'ɫ', u'ł'],
        'm': ['n', 'nn', 'rn', 'rr', u'ṃ', u'ᴍ', u'м', u'ɱ'],
        'n': ['m', 'r', u'ń'],
        'o': ['0', u'Ο', u'ο', u'О', u'о', u'Օ', u'ȯ', u'ọ', u'ỏ', u'ơ', u'ó', u'ö', u'ӧ'],
        'p': [u'ρ', u'р', u'ƿ', u'Ϸ', u'Þ'],
        'q': ['g', u'զ', u'ԛ', u'գ', u'ʠ'],
        'r': [u'ʀ', u'Г', u'ᴦ', u'ɼ', u'ɽ'],
        's': [u'Ⴝ', u'Ꮪ', u'ʂ', u'ś', u'ѕ'],
        't': [u'τ', u'т', u'ţ'],
        'u': [u'μ', u'υ', u'Ս', u'ս', u'ц', u'ᴜ', u'ǔ', u'ŭ'],
        'v': [u'ѵ', u'ν', u'v̇'],
        'w': ['vv', u'ѡ', u'ա', u'ԝ'],
        'x': [u'х', u'ҳ', u'ẋ'],
        'y': [u'ʏ', u'γ', u'у', u'Ү', u'ý'],
        'z': [u'ʐ', u'ż', u'ź', u'ʐ', u'ᴢ']
        }

        result = []

        for ws in range(0, len(self.domain)):
            for i in range(0, (len(self.domain)-ws)+1):
                win = self.domain[i:i+ws]

                j = 0
                while j < ws:
                    c = win[j]
                    if c in glyphs:
                        win_copy = win
                        for g in glyphs[c]:
                            win = win.replace(c, g)
                            result.append(self.domain[:i] + win + self.domain[i+ws:])
                            win = win_copy
                    j += 1

        return list(set(result))

    def __hyphenation(self):
        result = []

        for i in range(1, len(self.domain)):
            result.append(self.domain[:i] + '-' + self.domain[i:])

        return result

    def __insertion(self):
        result = []

        for i in range(1, len(self.domain)-1):
            for keys in self.keyboards:
                if self.domain[i] in keys:
                    for c in keys[self.domain[i]]:
                        result.append(self.domain[:i] + c + self.domain[i] + self.domain[i+1:])
                        result.append(self.domain[:i] + self.domain[i] + c + self.domain[i+1:])

        return list(set(result))

    def __omission(self):
        result = []

        for i in range(0, len(self.domain)):
            result.append(self.domain[:i] + self.domain[i+1:])

        n = re.sub(r'(.)\1+', r'\1', self.domain)

        if n not in result and n != self.domain:
            result.append(n)

        return list(set(result))

    def __repetition(self):
        result = []

        for i in range(0, len(self.domain)):
            if self.domain[i].isalpha():
                result.append(self.domain[:i] + self.domain[i] + self.domain[i] + self.domain[i+1:])

        return list(set(result))

    def __replacement(self):
        result = []

        for i in range(0, len(self.domain)):
            for keys in self.keyboards:
                if self.domain[i] in keys:
                    #print self.domain[i],'is in',keys
                    for c in keys[self.domain[i]]:
                        result.append(self.domain[:i] + c + self.domain[i+1:])
                        #print 'the result is',self.domain[:i] + c + self.domain[i+1:]

        # print result
        # import pdb
        # pdb.set_trace()
        return list(set(result))

    def __subdomain(self):
        result = []

        for i in range(1, len(self.domain)):
            if self.domain[i] not in ['-', '.'] and self.domain[i-1] not in ['-', '.']:
                result.append(self.domain[:i] + '.' + self.domain[i:])

        return result

    def __transposition(self):
        result = []

        for i in range(0, len(self.domain)-1):
            if self.domain[i+1] != self.domain[i]:
                result.append(self.domain[:i] + self.domain[i+1] + self.domain[i] + self.domain[i+2:])

        return result

    def __vowel_swap(self):
        vowels = 'aeiou'
        result = []

        for i in range(0, len(self.domain)):
            for vowel in vowels:
                if self.domain[i] in vowels:
                    result.append(self.domain[:i] + vowel + self.domain[i+1:])
        #print '---------------------------------------------------------------------------------------------',set(result)
        new_result = []
        for item in result:
            if item  != self.domain:
                new_result.append(item)

        return (new_result)


    def __appending_new_tlds(self):
        result = []

    def __addition(self):
        result = []

        for i in range(97, 123):
            result.append(self.domain + chr(i))

        return result

    def generate(self):
        self.domains.append({ 'fuzzer': 'Original*', 'domain-name': self.domain + '.' + self.tld })
        for domain in self.__addition():
            self.domains.append({ 'fuzzer': 'Addition', 'domain-name': domain + '.' + self.tld })
        for domain in self.__omission():
            self.domains.append({ 'fuzzer': 'Omission', 'domain-name': domain + '.' + self.tld })
        for domain in self.__repetition():
            self.domains.append({ 'fuzzer': 'Repetition', 'domain-name': domain + '.' + self.tld })
        for domain in self.__replacement():
            self.domains.append({ 'fuzzer': 'Replacement', 'domain-name': domain + '.' + self.tld })
        for domain in self.__transposition():
            self.domains.append({ 'fuzzer': 'Transposition', 'domain-name': domain + '.' + self.tld })
        for domain in self.__vowel_swap():
            self.domains.append({ 'fuzzer': 'Vowel-swap', 'domain-name': domain + '.' + self.tld })



def generate_typo_by_new_tlds(New_TDLs,WebSite_URL, maindomain):
    #print 'web site url is',WebSite_URL
    Candidate_Typos = []
    split = WebSite_URL.split('.')
    # print split

    if len(split) == 2:
        Domain_Name = split[1]
        WebSiteName = split[0]
    # print WebSiteName + "," +Domain_Name
    elif len(split) == 3:
        Domain_Name = split[2]
        WebSiteName = split[0] + "." + split[1]
    for NTDLS in New_TDLs:
        if len(NTDLS) < len(WebSiteName):
            CTypoName = WebSiteName + "." + NTDLS.lower()
            Candidate_Typos.append(CTypoName)
        # add new TLD to existing domain name
    if len(maindomain) >4:
        if maindomain == WebSiteName:
            for NTDLS in New_TDLs:
                if len(NTDLS) < len(WebSiteName):
                    if "." not in WebSiteName:
                        CTypoName = WebSiteName + "." + Domain_Name + "." + NTDLS.lower()
                        Candidate_Typos.append(CTypoName)
        else:
            for NTDLS in New_TDLs:
                if len(NTDLS) < len(WebSiteName) and len(NTDLS) < 2:
                    if "." not in WebSiteName:
                        CTypoName = WebSiteName + "." + Domain_Name + "." + NTDLS.lower()
                        Candidate_Typos.append(CTypoName)
    #print Candidate_Typos
    if "." not in WebSiteName:
        for item in New_TDLs:
            if WebSiteName[-1:].lower() ==(item).lower():
                tc = WebSiteName[:len(WebSiteName)-1]
                Candidate_Typos.append(tc+"."+item.lower())
            elif WebSiteName[-2:].lower() ==(item).lower():
                tc  = WebSiteName[:len(WebSiteName)-2]
                Candidate_Typos.append(tc+"."+item.lower())
            elif WebSiteName[-3:].lower() == (item).lower():
                tc = WebSiteName[:len(WebSiteName)-3]
                Candidate_Typos.append(tc+"."+item.lower())

    Candidate_Typos = list(set(Candidate_Typos))
    return Candidate_Typos


def __phillipa(domain,tld):
    result = []

    for item in DB__NEW_TLD:
        if domain[-1:].lower() == (item).lower():
            if "." not in domain[-2:]:
                tc = domain[:len(domain) - 1]
                result.append(tc + "." + item.lower())
            else:
                tc = domain[:len(domain) - 1]
                result.append(tc + item.lower())
                # print '-----------------------',tc+"."+item
        if domain[-2:].lower() == (item).lower():
            if "." not in domain[-3:]:
                tc = domain[:len(domain) - 2]
                result.append(tc + "." + item.lower())
            else:
                tc = domain[:len(domain) - 2]
                result.append(tc + item.lower())

        if domain[-3:].lower() == (item).lower():
            if "." not in domain[-4:]:
                tc = domain[:len(domain) - 3]
                result.append(tc + "." + item.lower())
            else:
                tc = domain[:len(domain) - 3]
                result.append(tc + item.lower())

        if domain[-4:].lower() == (item).lower():

            if "." not in domain[-5:]:
                tc = domain[:len(domain) - 4]
                result.append(tc + "." + item.lower())
            else:
                tc = domain[:len(domain) - 4]
                result.append(tc + item.lower())

        if domain[-5:].lower() == (item).lower():
            if "." not in domain[-6:]:
                tc = domain[:len(domain) - 5]
                result.append(tc + "." + item.lower())
            else:
                tc = domain[:len(domain) - 5]
                result.append(tc + item.lower())

                #          if redd.itcom

    # print 'from name just',Candidate_Typos
    # print 'gap',WebSiteName[:len(WebSiteName) - 1],WebSiteName[:len(WebSiteName) - 2],WebSiteName[:len(WebSiteName) - 3],WebSiteName[:len(WebSiteName) - 4]
    for item in DB__NEW_TLD:
        if domain + "." + tld[-1:].lower() == (item).lower():
            if "." not in domain + "." + tld[-2:]:
                tc = domain + "." + tld[:len(domain + "." + tld) - 1]
                result.append(tc + "." + item.lower())
            else:
                tc = domain + "." + tld[:len(domain + "." + tld) - 1]
                result.append(tc + item.lower())
                # print '-----------------------',tc+"."+item
        if domain + "." + tld[-2:].lower() == (item).lower():
            if "." not in domain + "." +tld[-3:]:
                tc = domain + "." + tld[:len(domain + "." + tld) - 2]
                result.append(tc + "." + item.lower())
            else:
                tc = domain + "." + tld[:len(domain + "." + tld) - 2]
                result.append(tc + item.lower())
                # print '---------------------',tc+"."+item
        if domain + "." + tld[-3:].lower() == (item).lower():
            if "." not in domain + "." + tld[-4:]:
                tc = domain + "." + tld[:len(domain + "." + tld) - 3]
                result.append(tc + "." + item.lower())
            else:
                tc = domain + "." + tld[:len(domain + "." + tld) - 3]
                result.append(tc + item.lower())

        if domain + "." + tld[-4:].lower() == (item).lower():

            if "." not in domain + "." + tld[-5:]:
                tc = domain + "." + tld[:len(domain + "." + tld) - 4]
                result.append(tc + "." + item.lower())
            else:
                tc = domain + "." + tld[:len(domain + "." + tld) - 4]
                result.append(tc + item.lower())

        if domain + "." + tld[-5:].lower() == (item).lower():

            if "." not in domain + "." + tld[-6:]:
                tc = domain + "." + tld[:len(domain + "." + tld) - 5]
                result.append(tc + "." + item.lower())
            else:
                tc = domain + "." + tld[:len(domain + "." + tld) - 5]
                result.append(tc + item.lower())

    origindomain = domain + tld
    for item in DB__NEW_TLD:
        if origindomain[-1:].lower() == (item).lower():
            if "." not in origindomain[-2:]:
                tc = origindomain[:len(origindomain) - 1]
                result.append(tc + "." + item.lower())
            else:
                tc = origindomain[:len(origindomain) - 1]
                result.append(tc + item.lower())
                # print '-----------------------',tc+"."+item
        if origindomain[-2:].lower() == (item).lower():
            if "." not in origindomain[-3:]:
                tc = origindomain[:len(origindomain) - 2]
                result.append(tc + "." + item.lower())
            else:
                tc = origindomain[:len(origindomain) - 2]
                result.append(tc + item.lower())
                # print '---------------------',tc+"."+item
        if origindomain[-3:].lower() == (item).lower():
            if "." not in origindomain[-4:]:
                tc = origindomain[:len(origindomain) - 3]
                result.append(tc + "." + item.lower())
            else:
                tc = origindomain[:len(origindomain) - 3]
                result.append(tc + item.lower())

        if origindomain[-4:].lower() == (item).lower():

            if "." not in origindomain[-5:]:
                tc = origindomain[:len(origindomain) - 4]
                result.append(tc + "." + item.lower())
            else:
                tc = origindomain[:len(origindomain) - 4]
                result.append(tc + item.lower())

        if origindomain[-5:].lower() == (item).lower():

            if "." not in origindomain[-6:]:
                tc = origindomain[:len(origindomain) - 5]
                result.append(tc + "." + item.lower())
            else:
                tc = origindomain[:len(origindomain) - 5]
                result.append(tc + item.lower())
    # print 'phillipa suggestion made----------------------------------------',result
    new_results = []
    for item in result:
        split = item.split('.')
        # print split
        if len(split) == 2:
            if split[0] and split[1]:
                new_results.append(item)

        # print WebSiteName + "," +Domain_Name
        elif len(split) == 3:
            if split[0] and split[1] and split[2]:
                new_results.append(item)
            Domain_Name = split[2]
            WebSiteName = split[0] + "." + split[1]
    gen_typos = []
    for item in new_results:
        if item != domain+"."+tld:
            gen_typos.append(item)

    return gen_typos


