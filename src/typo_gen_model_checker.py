import pickle

from typo_generation_models import *
def get_data(name):
    objects = []
    with (open('../data/'+name, "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    return objects
def get_used_models(name):
    found_models = {}
    found_models['Original*'] = 0
    found_models['Replacement'] = 0
    found_models['Addition'] = 0
    found_models['Transposition'] = 0
    found_models['Vowel-swap'] = 0
    found_models['Omission'] = 0
    found_models['Repetition'] = 0
    found_models['Transposition'] = 0
    found_models['PhillipaSuggestion'] = 0
    found_models['moving_dot_position'] = 0
    modesl = {}
    objects = get_data(name)
    same_owners = 0
    dif_owners = 0
    same_typos_list = []
    #print 'check the generation models manually'
    for item in objects:
        # print item
        Downloaded_typos = []
        #print item
        original_domain = item['key']
        typo_infos = item['same_owner_typos']


        for key in typo_infos:
            typo = key
            Downloaded_typos.append(typo)
            same_typos_list.append(typo)
            #print typo
        #import pdb
        #pdb.set_trace()
        dfuzz = DomainFuzz(original_domain)
        #print original_domain
        import pdb

        #pdb.set_trace()
        dfuzz.generate()
        Generated_Domains = dfuzz.domains
        #print 'origin',original_domain
        #print 'generated',Generated_Domains
        #print 'downloaded typos',Downloaded_typos
        #pdb.set_trace()

        for analyaed_typo in Downloaded_typos:
            analyzed = analyaed_typo.split('.')
            # print split
            if len(analyzed) == 2:
                analyzed_TLD = analyzed[1]
                analyzed_WebSiteName = analyzed[0]
            # print WebSiteName + "," +Domain_Name
            elif len(analyzed) == 3:
                analyzed_TLD = analyzed[2]
                analyzed_WebSiteName = analyzed[0] + "." + analyzed[1]
            #print 'here the analyzed typo and downloaded typo is',analyzed_WebSiteName
            for raw_typo in Generated_Domains:
                raw = raw_typo['domain-name']
                if analyzed_WebSiteName in  raw:
                    print analyaed_typo,raw,raw_typo['fuzzer']
                    found_models[raw_typo['fuzzer']] = found_models[raw_typo['fuzzer']] + 1
                #print 'raw_typo[domain-name]',raw_typo


        #print 'found models',found_models
        #print 'Downloaded_typos',Downloaded_typos
        #print 'typo_infos',typo_infos
    import pdb
    #pdb.set_trace()
    #print '-------------------------------------------------------------------',same_typos_list
    return found_models
def get_used_models_dif(name):
    found_models = {}
    found_models['Original*'] = 0
    found_models['Replacement'] = 0
    found_models['Addition'] = 0
    found_models['Transposition'] = 0
    found_models['Vowel-swap'] = 0
    found_models['Omission'] = 0
    found_models['Repetition'] = 0
    found_models['Transposition'] = 0
    found_models['PhillipaSuggestion'] = 0
    found_models['moving_dot_position'] = 0
    modesl = {}
    objects = get_data(name)
    same_owners = 0
    dif_owners = 0
    same_typos_list = []
    print 'check the generation models manually'
    for item in objects:
        # print item
        Downloaded_typos = []
        #print item
        original_domain = item['key']
        typo_infos = item['dif_owner_typos']


        for key in typo_infos:
            typo = key
            Downloaded_typos.append(typo)
            same_typos_list.append(typo)
            #print typo
        #import pdb
        #pdb.set_trace()
        dfuzz = DomainFuzz(original_domain)
        print original_domain
        import pdb

        #pdb.set_trace()
        dfuzz.generate()
        Generated_Domains = dfuzz.domains
        print 'origin',original_domain
        print 'generated',Generated_Domains
        print 'downloaded typos',Downloaded_typos
        #pdb.set_trace()

        for analyaed_typo in Downloaded_typos:
            analyzed = analyaed_typo.split('.')
            # print split
            if len(analyzed) == 2:
                analyzed_WebSiteName = analyzed[0]
            # print WebSiteName + "," +Domain_Name
            elif len(analyzed) == 3:
                analyzed_WebSiteName = analyzed[0] + "." + analyzed[1]
            print 'here the analyzed typo and downloaded typo is',analyzed_WebSiteName
            for raw_typo in Generated_Domains:
                raw = raw_typo['domain-name']
                if analyzed_WebSiteName in  raw:
                    found_models[raw_typo['fuzzer']] = found_models[raw_typo['fuzzer']] + 1
                #print 'raw_typo[domain-name]',raw_typo


    #print found_models

    #print '-------------------------------------------------------------------',same_typos_list
    return found_models
