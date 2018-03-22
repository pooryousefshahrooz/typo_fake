import pickle
import os,sys
import whois as whois

objects = []
same_owners = 0
dif_owners = 0
name = sys.argv[1]
all = sys.argv[2]
with (open(name, "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
counter_domain = 0

counter_typo = 0
for item in objects:
    print '--------------------------'
    print item['key']
    counter_domain = counter_domain +1

    try:
        typos  =  item['typos_dns_info']
        for typo in typos:
            counter_typo = counter_typo +1
    except:
        pass
    # responce_code_for_dif  =  item['responce_code_for_dif']
    #
    # bad_typos = responce_code_for_dif['bad_typos']
    # ok_typos = responce_code_for_dif['ok_typos']
    # redirect_typos = responce_code_for_dif['redirect_typos']
    # print 'get_ok_response_codes',ok_typos
    # print 'get_redirect_response_code',redirect_typos
    # print 'get_bad_request',bad_typos
    # print '--------------------------'
    # typo_infos = item['typo_infos']
    # try:
    #     official_dns_info = whois.whois(item['key'])
    #     offficial_registar = official_dns_info.registrar
    # except:
    #     pass
    # for info in typo_infos:
    #     info_dic = typo_infos[info]
    #     typo_registrar = info_dic['registrar']
    #     print typo_registrar,offficial_registar
    # print item['ok_response_for_same_owner_typos'],item['ok_response_for_dif_owner_typos']
    # print item['redirec_response_for_same_owner_typos'],item['redirec_response_for_dif_owner_typos']
    # print item['bad_response_for_same_owner_typos'],item['bad_response_for_dif_owner_typos']
    # print item['same_owner_typos']
    # print item['dif_owner_typos']

    if all =='all':
        print item
print counter_domain
print counter_typo