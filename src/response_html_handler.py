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

import whois as whois

class response_code_Handler(object):
    def __init__(self):
        self.lock = threading.Lock()

        self.dns_dictionary = {}
        typos = []

    def response_checker(self,targetwebsite, same_dif_owner_typos,folder_name):
        try:
            counter = 0
            ok_typos = []
            redirect_typos = []
            bad_request_typos = []
            response_code = {}
            redirected_to = {}
            for typo in same_dif_owner_typos:
                try:
                    response = requests.get("http://" + typo)
                    if response.history:
                        redirect_typos.append(typo)
                        redirected_to[typo] = response.url
                        redirected_to_response = requests.get(response.url)
                        html_content = redirected_to_response.content
                    else:
                        ok_typos.append(typo)
                        html_content = response.content
                    if not os.path.exists(folder_name+'/html_files' + '/' + targetwebsite):
                        os.makedirs(folder_name+'/html_files' + '/' + targetwebsite)
                    with open(folder_name+'/html_files' + '/' + targetwebsite + '/' + typo + '.html', 'w') as f:
                        f.write(html_content)
                        print typo,':       saved'
                        counter = counter+1

                except:
                    bad_request_typos.append(typo)
                    #print 'errrorrrr', ValueError
                    pass
        except:
            #print 'error', ValueError
            print 'we had a problem'
            pass
        # print bad_request_typos

        response_code['ok_typos'] = ok_typos
        response_code['redirect_typos'] = redirect_typos
        response_code['bad_typos'] = bad_request_typos
        response_code['redirected_to'] = redirected_to
        # print response_code
        print '# of typos files',counter,'have been saved'
        return response_code


    def save(self,info,file_name):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            pickle_out = open("response_codes_for_"+file_name, "a+b")
            pickle.dump(info, pickle_out)
            pickle_out.close()

        finally:
            self.lock.release()









