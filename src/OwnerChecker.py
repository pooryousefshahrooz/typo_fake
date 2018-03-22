import pickle
import threading

global num_same_owners
global num_registered_typos
global num_same_owners_genral_typos
global num_same_owners_by_newtlds_typos
global num_dif_owners
global num_dif_owners_general_typo
global num_dif_owners_newtlds_typo
global num_official_refused
global num_general_typo_refused
global num_newtlds_typo_refused
global num_registered_by_same_email
global num_same_country
global num_dif_country
global num_not_registere_typos
global num_refused_typoes
import logging
import re
from response_code_handler import *

import whois as whois

class TyposHandler(object):
    def __init__(self):
        self.lock = threading.Lock()

        self.dns_dictionary = {}
        typos = []
    def get_domain(self,email_address):
        emails_domain = []
        # print email_address
        # print 'type is',type(email_address)
        if isinstance(email_address, list):
            # print 'this is an array',email_address
            for email in email_address:
                # print 'email',email
                emails_domain.append(email[email.find("@"):])
                # print 'emaiul domains',emails_domain
        else:
            # print 'this is an string',email_address
            # print email_address
            if email_address:
                emails_domain.append(email_address[email_address.find("@"):])
        # print emails_domain
        return emails_domain
    def check_email_records(self,original_info,typo_info):
        try:
            typo_email_domains = self.get_domain(typo_info['emails'])
            original_email_domains = self.get_domain(original_info.emails)
            #print  'emails',typo_info['emails'],original_info.emails
            for email in typo_email_domains:
                if email in  original_email_domains:
                    #print email,original_email_domains
                    #print 'same'
                    return True

            #print 'dif',typo_info['registrar'],original_info.registrar
            return False

        except:
            try:
                typo_email_domains = self.get_domain(typo_info['admin_email'])
                original_email_domains = self.get_domain(original_info.emails)
                # print  'emails',typo_info['emails'],original_info.emails
                for email in typo_email_domains:
                    if email in original_email_domains:
                        # print email,original_email_domains
                        # print 'same'
                        return True

                # print 'dif',typo_info['registrar'],original_info.registrar
                return False

            except:
            #print 'dif',typo_info['registrar'],original_info.registrar
                return False



    def check_owner(self,official_web_site, typos_dns_info):

        un_returned_official_domains = []
        same_owner_typos = []
        dif_owner_typos = []

        global official_refused_websites
        typo_info = {}
        thread_specific_dns_dictionary = {}
        offficial_registar = ''

        try:
            official_dns_info = whois.whois(official_web_site)
            offficial_registar = official_dns_info.registrar
        except:
            pass

        if offficial_registar:
            typo_infos = typos_dns_info
            print 'len of typos for',official_web_site, len(typo_infos)
            for info in typo_infos:
                print info
                info_dic = typo_infos[info]
                typo_registrar = info_dic['registrar']
                treg = typo_registrar
                off_reg = offficial_registar
                if typo_registrar:
                    print 'typo_registrar',typo_registrar
                    offficial_registar = offficial_registar.replace(" ", "")
                    typo_registrar = typo_registrar.replace(" ", "")
                    offficial_registar = offficial_registar.replace(",", "")
                    typo_registrar = typo_registrar.replace(",", "")
                    offficial_registar = offficial_registar.replace(")", "")
                    typo_registrar = typo_registrar.replace(")", "")
                    offficial_registar = offficial_registar.replace("(", "")
                    typo_registrar = typo_registrar.replace("(", "")
                    offficial_registar = offficial_registar.replace(".", "")
                    typo_registrar = typo_registrar.replace(".", "")

                    if offficial_registar.lower() in typo_registrar.lower() or typo_registrar.lower() in offficial_registar.lower() or typo_registrar.lower()[2:] in offficial_registar.lower() or typo_registrar.lower()[:-2] in offficial_registar.lower():
                        same_owner_typos.append(info)
                        #print 'same',offficial_registar.lower(),typo_registrar.lower()
                        print 'same:', off_reg, '         and        ', treg
                    elif len(offficial_registar.lower())>8 and offficial_registar.lower()[:-3] in typo_registrar.lower() or offficial_registar.lower()[:-2] in typo_registrar.lower():
                            same_owner_typos.append(info)
                            print 'same:',off_reg,'         and        ',treg
                    elif self.check_email_records(official_dns_info,info_dic):
                        #try:
                            #print '=============================================',self.get_domain(typo_info['emails']),self.get_domain(offficial_registar.emails)
                        same_owner_typos.append(info)
                        print 'same:', off_reg, '         and        ', treg
                        #except:
                            #print 'we got True from email checking but we also have gor an error for',official_web_site,info
                            #pass
                    else:
                        dif_owner_typos.append(info)
                        print 'dif:', off_reg, '         and        ', treg
                else:

                    print 'there is no registrar info for typo',info
            print 'number of same and dif owner detectedted for',official_web_site,'are',len(same_owner_typos),len(dif_owner_typos)
        else:
            un_returned_official_domains.append(official_web_site)

        # response_code_for_same = get_request_checker_for_same(same_owner_typos)
        # thread_specific_dns_dictionary["responce_code_for_same"] = response_code_for_same


        # response_code_for_dif = get_request_checker_for_same(dif_owner_typos)
        #
        # thread_specific_dns_dictionary["responce_code_for_dif"] = response_code_for_dif

        thread_specific_dns_dictionary['key'] = official_web_site
        thread_specific_dns_dictionary['origin_owner'] = offficial_registar
        thread_specific_dns_dictionary['num_same_owner'] = len(same_owner_typos)
        thread_specific_dns_dictionary['num_dif_owner'] = len(dif_owner_typos)
        thread_specific_dns_dictionary['same_owner_typos'] = same_owner_typos
        thread_specific_dns_dictionary['dif_owner_typos'] = dif_owner_typos

        return thread_specific_dns_dictionary

    def save(self,info,file_name):
        #logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            #logging.debug('Acquired lock')

            pickle_out = open("same_dif_typos_for_"+file_name, "a+b")
            pickle.dump(info, pickle_out)
            pickle_out.close()

        finally:
            self.lock.release()









