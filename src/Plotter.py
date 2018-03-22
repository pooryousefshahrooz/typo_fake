import numpy as np
import matplotlib.pyplot as plt
import pickle
import numpy as np
import matplotlib.pyplot as plt
import glob, os

from typo_gen_model_checker import *
from typo_generation_models import *

import sys
import socket

file_name = 'file_name'

import weakref

def registeration_plotter():
    #print 'plotted'


    # print 'same for news',same_news
    # print 'dif for news',dif_news
    # print '------------------'
    # print 'same for sport',same_sport
    # print 'dif for sport',dif_sport
    # print '------------------'
    #
    # print 'same for science',same_science
    # print 'dif for science',dif_science
    # print '------------------'
    #
    # print 'same for shopping',same_shopping
    # print 'dif for shopping',dif_shopping
    # print '------------------'
    #
    # print 'same for adult', same_adult
    # print 'dif for adult', dif_adult
    # print '------------------'
    #
    # print 'same for society',same_society
    # print 'dif for society',dif_society

    import pdb
    #pdb.set_trace()
    import numpy as np
    import matplotlib.pyplot as plt
    import glob, os

    N = 6
    same = (same_news, same_shopping, same_sport, same_science, same_society,same_adult)
    dif = (dif_news, dif_shopping, dif_sport, dif_science, dif_society,dif_adult)
    menStd = (0, 0, 0, 0, 0,0)
    womenStd = (0, 0, 0, 0, 0,0)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.32  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, same, width, color='#ffffff', yerr=menStd)
    p2 = plt.bar(ind, dif, width,
                 bottom=same,color='#969393', yerr=womenStd)

    plt.ylabel('number of registered')
    plt.title('registered typo candidates by same or different authority from their original one')
    plt.xticks(ind, ('News', 'Shopping', 'Sport', 'Science', 'Society','Adult'))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('Registered by same authority', 'Registered by dif ahutority'))


    """
    Attach a text label above each bar displaying its height
    """
    for rect in p1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height),
                ha='center', va='bottom')

    for rect in p2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height),
                ha='center', va='bottom')

    plt.show()



def get_data(name):
    objects = []
    with (open('../data/'+name, "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    return objects
def get_same_dif(name):
    objects = []
    whole_same_owners= 0
    whole_dif_owners = 0
    objects = get_data(name)
    redirect_to =[]
    for item in objects:
        # print item
        same_owners = 0
        dif_owners = 0
        #print item["key"]
        #print item['key']
        num_dif_owners = item['num_dif_owner']
        num_same_owners  = item['num_same_owner']
        whole_dif_owners = whole_dif_owners+num_dif_owners
        whole_same_owners = whole_same_owners+num_same_owners
    return whole_same_owners,whole_dif_owners
def get_same_dif(name):
    objects = []
    whole_same_owners= 0
    whole_dif_owners = 0
    objects = get_data(name)
    redirect_to =[]
    for item in objects:
        # print item
        same_owners = 0
        dif_owners = 0
        #print item["key"]
        #print item['key']
        #print item
        response_code_for_dif_owners = item['response_code_for_dif_owners']
        response_code_for_same_owners  = item['response_code_for_dif_owners']
        #print response_code_for_dif_owners['redirected_to']
        #print len(response_code_for_dif_owners['redirected_to'])
       # {'same_owner_typos': ['newsweek.sg', 'newsweek.com.sg', 'newsweek.st', 'newsweek.fr', 'newsweek.la',
        #                      'newsweek.com.ro'], 'num_dif_owner': 38, 'key': 'newsweek.com',
         #'origin_owner': u'MarkMonitorInc',
         #'dif_owner_typos': ['newsweek.cz', 'newsweek.com.gs', 'newsweek.com.wtf', 'newsweek.am', 'newsweek.cc',
         #                    'newsweek.top', 'newsweek.cn', 'newsweek.com.in', 'newsweek.pub', 'newsweek.com.gal',
         #                    'newsweek.so', 'newsweek.com.nu', 'newsweek.se', 'newsweek.com.tax', 'newsweek.com.lt',
         #                    'newsweek.su', 'newsweek.com.cam', 'newsweek.com.tl', 'newsweek.com.cab',
         #                    'newsweek.com.law', 'newsweek.com.tv', 'newsweek.com.eus', 'newsweek.com.am',
         #                    'newsweek.com.ru', 'newsweek.ro', 'newsweek.tv', 'newsweek.mx', 'newsweek.com.cn',
         #                    'newsweek.in', 'newsweek.com.top', 'newsweek.kr', 'newsweek.com.mx', 'newsweek.com.pub',
         #                    'newsweek.com.cc', 'newsweek.rs', 'newsweek.com.cx', 'newsweek.ru', 'newsweek.com.cz'],
         #'num_same_owner': 6}

       # {'response_code_for_same_owners': {'bad_typos': ['newsweek.la'],
        #                                   'redirected_to': {'newsweek.fr': u'https://www.thedailybeast.com/newsweek',
        #                                                    'newsweek.st': u'http://www.newsweek.com/'},
        #                                   'redirect_typos': ['newsweek.st', 'newsweek.fr'],
        #                                   'ok_typos': ['newsweek.sg', 'newsweek.com.sg', 'newsweek.com.ro']},
        # 'response_code_for_dif_owners': {
        #     'bad_typos': ['newsweek.com.gs', 'newsweek.com.wtf', 'newsweek.cc', 'newsweek.top', 'newsweek.com.in',
        #                   'newsweek.com.gal', 'newsweek.so', 'newsweek.se', 'newsweek.com.tax', 'newsweek.com.lt',
        #                   'newsweek.com.cam', 'newsweek.com.tl', 'newsweek.com.cab', 'newsweek.com.law',
        #                   'newsweek.com.tv', 'newsweek.com.eus', 'newsweek.com.am', 'newsweek.ro', 'newsweek.tv',
        #                   'newsweek.com.cn', 'newsweek.com.top', 'newsweek.com.cc', 'newsweek.com.cx', 'newsweek.ru'],
        #     'redirected_to': {'newsweek.cz': u'http://www.forbes.cz/', 'newsweek.mx': u'http://www.newsweek.mx/',
        #                       'newsweek.am': u'http://www.newsweek.com/',
        #                       'newsweek.com.pub': u'http://www.tldnic.net/portfolio/com.pub/?utm_medium=redirsub&utm_source=com.pub',
        #                       'newsweek.rs': u'http://www.adriamediagroup.com/',
        #                       'newsweek.com.cz': u'https://www.ignum.cz/'},
        #     'redirect_typos': ['newsweek.cz', 'newsweek.am', 'newsweek.mx', 'newsweek.com.pub', 'newsweek.rs',
        #                        'newsweek.com.cz'],
        #     'ok_typos': ['newsweek.cn', 'newsweek.pub', 'newsweek.com.nu', 'newsweek.su', 'newsweek.com.ru',
        #                  'newsweek.in', 'newsweek.kr', 'newsweek.com.mx']}, 'key': 'newsweek.com'}

        for key, value in response_code_for_dif_owners['redirected_to'].iteritems():
            #print key, value
            redirect_to.append(value)
        same_owners = same_owners + int(len(response_code_for_same_owners['bad_typos']))+int(len(response_code_for_same_owners['redirect_typos']))+int(len(response_code_for_same_owners['ok_typos']))
        dif_owners = dif_owners + int(len(response_code_for_dif_owners['bad_typos']))+int(len(response_code_for_dif_owners['redirect_typos']))+int(len(response_code_for_dif_owners['ok_typos']))

        #print 'same, dif,return 200 same,,return 200 dif, reditect-same,redirectdir'
        #print same_owners,dif_owners,len(response_code_for_same_owners['ok_typos']),len(response_code_for_dif_owners['ok_typos']),len(response_code_for_same_owners['redirect_typos']),len(response_code_for_dif_owners['redirect_typos'])
        #len(response_code_for_same_owners['redirect_typos'])
        #print 'dif for',item['key'],'are',dif_owners
        whole_same_owners = whole_same_owners + same_owners
        whole_dif_owners =whole_dif_owners+dif_owners


    #print 'redirect to',redirect_to
    from itertools import groupby
    #print  [len(list(group)) for key, group in groupby(redirect_to)]
    return whole_same_owners,whole_dif_owners

def registeration_plotter(name):
    #print 'plotted'
    generated_typos = 10503
    #generated typos for top 15  media web sites10503
    same_typos,dif_typos = get_same_dif(name)
    #
    # import matplotlib.pyplot as plt;
    # plt.rcdefaults()
    # import numpy as np
    # import matplotlib.pyplot as plt
    #
    # objects = ('Generated Typos', 'Registered Typos by same authority', 'registered typos by different authority')
    # y_pos = np.arange(len(objects))
    # performance = [generated_typos, same_typos, dif_typos]
    #
    # plt.bar(y_pos, performance, align='center', alpha=0.5)
    # plt.xticks(y_pos, objects)
    # plt.ylabel('#')
    # plt.title('generated and registered typos')
    #plt.show()
    #plt.savefig('reg_same_dif' + name + '.pdf')
    #
    # print '#same for ',name,'is',same_news
    # print '#dif for news',name,'is',dif_news
    # print '------------------'
    #
    import pdb
    #pdb.set_trace()
    import numpy as np
    import matplotlib.pyplot as plt
    import glob, os

    N = 2
    same = (same_typos, 0)
    dif = (dif_typos, 0)
    menStd = (0, 0)
    womenStd = (0, 0)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.32  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, same, width, color='#ffffff', yerr=menStd)
    p2 = plt.bar(ind, dif, width,
                 bottom=same,color='#969393', yerr=womenStd)

    plt.ylabel('# registered by same or different authority')
    plt.title('registered typo candidates by same or different authority from their original one')
    plt.xticks(ind, ('top 50 news web sites', 'cat1'))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('Registered by same authority', 'Registered by dif ahutority'))
    #plt.suptitle("Registered by same or different authority of origin")

    """
    Attach a text label above each bar displaying its height
    """
    for rect in p1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height),
                ha='center', va='bottom')

    for rect in p2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height),
                ha='center', va='bottom')

    plt.show()
    plt.savefig('Stat/reg_same_dif'+name+'.pdf')
    #

def get_news_data_saved(file_name):
    #print '-------------------------result for alexa top 50 news domain names typos by new tlds-------------------------'
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
def get_meeting_data_saved():
    objects = []
    same_owners= 0
    dif_owners = 0
    with (open("short_list_richab2.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    #print objects
    return objects
def plot_all():

    print ('all')

def is_valid(charnum):
    return ((charnum >= ord('0') and charnum <= ord('9')) or
            (charnum >= ord('a') and charnum <= ord('z')) or
            (charnum >= ord('A') and charnum <= ord('Z')) or
             charnum == ord('-'))




def get_generation_model_same(name):
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
                raw = raw_typo['domain-name'].split('.')
                #print 'raw_typo[domain-name]',raw_typo
                # print split
                if len(raw) == 2:
                    raw_TLD = raw[1]
                    raw_WebSiteName = raw[0]
                # print WebSiteName + "," +Domain_Name
                elif len(raw) == 3:
                    raw_TLD = raw[2]
                    raw_WebSiteName = raw[0] + "." + raw[1]

                if analyzed_WebSiteName == raw_WebSiteName:
                    #rint 'analyzed_WebSiteName================================================',analyzed_WebSiteName
                    #print 'raw_WebSiteName================================================',raw_WebSiteName,raw_typo['domain-name']
                    #print 'raw_typo[fuzzer]=============================================',raw_typo['fuzzer']
                    #print found_models[raw_typo['fuzzer']]
                    found_models[raw_typo['fuzzer']] = found_models[raw_typo['fuzzer']] + 1
                    #print found_models[raw_typo['fuzzer']]

    #print found_models
    #print '-------------------------------------------------------------------',same_typos_list
    return found_models
def get_generation_model_dif(name):
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

    for item in objects:
        # print item
        Downloaded_typos = []
        original_domain = item['key']
        typo_infos = item['dif_owner_typos']
        for key in typo_infos:
            typo = key
            Downloaded_typos.append(typo)
            #print typo
        #import pdb
        #pdb.set_trace()
        dfuzz = DomainFuzz(original_domain)
        dfuzz.generate()
        Generated_Domains = dfuzz.domains
        #print 'origin',original_domain
        #print 'generated',Generated_Domains
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

            for raw_typo in Generated_Domains:
                raw = raw_typo['domain-name'].split('.')
                # print split
                if len(raw) == 2:
                    raw_TLD = raw[1]
                    raw_WebSiteName = raw[0]
                # print WebSiteName + "," +Domain_Name
                elif len(raw) == 3:
                    raw_TLD = raw[2]
                    raw_WebSiteName = raw[0] + "." + raw[1]

                if analyzed_WebSiteName == raw_WebSiteName:
                    found_models[raw_typo['fuzzer']] = found_models[raw_typo['fuzzer']] + 1


    return found_models

def typo_generation_model_stat(name):

    models = get_generation_model_same(name)

    #print 'returned'
    #print models
    #models = {'Omission': 0, 'Addition': 0, 'Transposition': 0, 'moving_dot_position': 0, 'Vowel-swap': 0, 'PhillipaSuggestion': 178, 'Repetition': 0, 'Original*': 205, 'Replacement': 0}
    import matplotlib.pyplot as plt
    colors = ['gray', 'white', 'silver']
    #print 'after colors'
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'new_tld_expansion', 'Replacement', 'Addition',\
             'Transposition','Vowel-swap','Omission','Repetition','Transposition','PhillipaSuggestion','Moving_dot_position'
    sizes = [models['Original*'], models['Replacement'], models['Addition'],
             models['Transposition'],models['Vowel-swap'],models['Omission'],models['Repetition'],models['Transposition'],models['PhillipaSuggestion'],models['moving_dot_position']]
    explode = (0, 0, 0,0, 0, 0,0, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #print 'after explode'
    #print '=======================================================t',models['Vowel-swap']
    #print '=======================================================t',models['PhillipaSuggestion']

    #print '=======================================================t',models['moving_dot_position']

    fig1, ax1 = plt.subplots()
    #print 'after fig1'
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%',
            shadow=True, startangle=90)
    #print 'after ax1.pie'
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #plt.show()
    plt.suptitle('used typo generation models for same owner registered typos')
    fig1.savefig('Stat/used_model_same'+name+'.pdf')
    #print 'saved'




    models = get_generation_model_dif(name)

    #print 'returned'
    #print models
    #models = {'Omission': 0, 'Addition': 0, 'Transposition': 0, 'moving_dot_position': 0, 'Vowel-swap': 0, 'PhillipaSuggestion': 178, 'Repetition': 0, 'Original*': 205, 'Replacement': 0}
    import matplotlib.pyplot as plt
    colors = ['gray', 'white', 'silver']
    #print 'after colors'
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'new_tld_expansion', 'Replacement', 'Addition',\
             'Transposition','Vowel-swap','Omission','Repetition','Transposition','PhillipaSuggestion','Moving_dot_position'
    sizes = [models['Original*'], models['Replacement'], models['Addition'],
             models['Transposition'],models['Vowel-swap'],models['Omission'],models['Repetition'],models['Transposition'],models['PhillipaSuggestion'],models['moving_dot_position']]
    explode = (0, 0, 0,0, 0, 0,0, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #print 'after explode'
    fig2, ax2 = plt.subplots()
    #print 'after fig1'
    ax2.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%',
            shadow=True, startangle=90)
    #print 'after ax1.pie'
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.suptitle('used typo generation models for different owner registered typos')

    plt.show()

    fig1.savefig('Stat/used_model_dif'+name+'.pdf')
    #print 'saved'

def get_response_code(name):
    same_ok = 0
    same_bad = 0
    same_redirect = 0
    dif_ok = 0
    dif_bad = 0
    dif_redirect = 0
    typo_counter = 0
    response_codes = {}
    redirect_to_official_same = []
    redirect_to_official_dif = []
    redirected_typos = []
    objects = get_data(name)
    for item in objects:
        #print item
        domain = item['key']

        responce_code_for_same = item['response_code_for_same_owners']
        responce_code_for_dif = item['response_code_for_dif_owners']
        redirect_to_same = responce_code_for_same['redirected_to']
        redirected_to_dif=responce_code_for_dif['redirected_to']
        same_ok = same_ok+len(responce_code_for_same['ok_typos'])

        same_bad = same_bad + len(responce_code_for_same['bad_typos'])
        same_redirect = same_redirect + len(responce_code_for_same['redirect_typos'])

        dif_ok = dif_ok+len(responce_code_for_dif['ok_typos'])
        dif_bad = dif_bad + len(responce_code_for_dif['bad_typos'])
        dif_redirect = dif_redirect + len(responce_code_for_dif['redirect_typos'])
        for typo, value in redirect_to_same.iteritems():
            if domain in value:
                redirect_to_official_same.append(typo)
            redirected_typos.append(typo)
        for typo, value in redirected_to_dif.iteritems():
            if domain in value:
                redirect_to_official_dif.append(typo)
            redirected_typos.append(typo)

    response_codes['same_ok'] = same_ok
    response_codes['same_bad'] = same_bad
    response_codes['same_redirect'] = same_redirect
    response_codes['dif_ok'] = dif_ok
    response_codes['dif_bad'] = dif_bad
    response_codes['dif_redirect'] = dif_redirect

    print 'number of redirected',len(redirected_typos)
    print 'number of redirected to official domains in same',len(redirect_to_official_same)
    print 'number of redirected to official domains in dif',len(redirect_to_official_dif)

    return response_codes

def response_code_plotter(name):
    response_codes = get_response_code(name)
    import matplotlib.pyplot as plt
    colors = ['gray', 'white', 'silver']
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels1 = 'Ok_response', 'redirected', 'bad_request'
    sizes1 = [response_codes['same_ok'], response_codes['same_redirect'], response_codes['same_bad']]
    explode1 = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes1, explode=explode1, labels=labels1, colors=colors,autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #plt.title('Response code returned for typos registered by same authority')
    fig1.savefig('Stat/res_code_same'+name+'.pdf')

    #plt.show()

    labels2 = 'Ok_response', 'redirected', 'bad_request'
    sizes2 = [response_codes['dif_ok'], response_codes['dif_redirect'], response_codes['dif_bad']]
    explode2 = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #plt.title('Response code returned for typos registered by different authority')
    fig2, ax2 = plt.subplots()
    ax2.pie(sizes2, explode=explode2, labels=labels2, colors=colors,autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
    fig2.savefig('Stat/res_code_dif'+name+'.pdf')
    plt.show()

def worker(targetwebsite,typo_infos,file_name,typoshandler):
    typos = []
    info = typoshandler.check_owner(targetwebsite, typo_infos)
    #print info
    pause = random.random()
    logging.debug('Sleeping %0.02f', pause)
    time.sleep(pause)
    typoshandler.save(info,file_name)
    logging.debug('Done')

def printer(name):
    items2 = []
    items = []
    objects = get_data(name)
    for item in objects:
        #print item
        items2.append(item['key'])
        if item not in items:
            items.append(item['key'])

        #print item
        #print items

    #print len(items)
    #print len(items2)
    #print len(list(set(items2)))
def get_same_dif2(name):
    objects = []
    whole_same_owners= 0
    whole_dif_owners = 0
    objects = get_data(name)
    redirect_to =[]
    for item in objects:
        # print item
        same_owners = 0
        dif_owners = 0
        #print item["key"]
        #print item['key']
        #print item
        num_dif_owner = item['num_dif_owner']
        num_same_owner = item['num_same_owner']
        #print num_same_owner,num_dif_owner
        #print item['same_owner_typos'],item['dif_owner_typos']
        whole_same_owners = whole_same_owners+num_same_owner
        whole_dif_owners = whole_dif_owners+num_dif_owner
    #print 'whole same and dif',whole_same_owners,whole_dif_owners
    return whole_same_owners,whole_dif_owners



def per_news_media_top():

    #news = "same_dif_typos_for_2018-02-04T14:34:49.945480_50news_saved_dns.pickle"
    #news = "same_dif_typos_for_2018-02-13T17:22:58.930284_50news_saved_dns.pickle"
    media_three = 'same_dif_typos_for_2018-02-13T19:05:34.745815_new_version_sixth_week_three_model.pickle'
    media_all = 'same_dif_typos_for_2018-02-13T18:58:21.000143_dns_info_for_2018-02-08T21:22:36.802943_News_media_in_the_United_States.txt.pickle'
    news = 'same_dif_typos_for_2018-02-13T17:59:18.613430_50news_saved_dns.pickle'# after using and in check if len(regi)>8


    news_same_typos, news_dif_typos = get_same_dif2(news)


    media_all_same, media_all_dif = get_same_dif2(media_all)
    media_three_same,media_three_dif = get_same_dif2(media_three)
    #print news_same_typos,news_dif_typos


    import numpy as np
    import matplotlib.pyplot as plt

    N = 3
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = [media_three_same+media_three_dif,media_all_dif+media_all_same,news_dif_typos + news_same_typos]
    rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    zvals = [media_three_same,media_all_same,news_same_typos]
    rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    kvals = [media_three_dif,media_all_dif,news_dif_typos]
    rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')

    ax.set_ylabel('Scores')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('top15_three_method','top_15_all_models','news_all_models'))
    ax.legend((rects1[0], rects2[0], rects3[0]),
              ('#found domains', '#registered by same entity', '#registered by different entity'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.show()


def per_cat():

    news = 'same_dif_typos_for_2018-02-13T17:59:18.613430_50news_saved_dns.pickle'  # after using and in check if len(regi)>8
    sport = "same_dif_typos_for_2018-02-04T13:23:05.936240_sport_saved_dns.pickle"
    sciece = "same_dif_typos_for_2018-02-04T13:24:38.483653_science_saved_dns.pickle"
    society = "same_dif_typos_for_2018-02-04T13:25:47.409418_society_saved_dns.pickle"
    adult = "same_dif_typos_for_2018-02-04T13:28:26.684995_ad_saved.pickle"

    news_same_typos, news_dif_typos = get_same_dif2(news)
    sport_same_typos, sport_dif_typos = get_same_dif2(sport)
    sciece_same_typos, sciece_dif_typos = get_same_dif2(sciece)
    society_same_typos, society_dif_typos = get_same_dif2(society)
    adult_same_typos, adult_dif_typos = get_same_dif2(adult)

    #print news_same_typos, news_dif_typos
    #print sport_same_typos, sport_dif_typos
    #print sciece_same_typos, sciece_dif_typos
    #print society_same_typos, society_dif_typos
    #print adult_same_typos, adult_dif_typos

    import numpy as np
    import matplotlib.pyplot as plt

    N = 6
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = [ news_dif_typos + news_same_typos,
             sport_dif_typos + sport_same_typos,
             sciece_dif_typos + sciece_same_typos, society_dif_typos + society_same_typos,
             adult_dif_typos + adult_same_typos, 7]
    rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    zvals = [ news_same_typos, sport_same_typos, sciece_same_typos, society_same_typos,
             adult_same_typos, 7]
    rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    kvals = [news_dif_typos, sport_dif_typos, sciece_dif_typos, society_dif_typos,
             adult_dif_typos, 7]
    rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')

    ax.set_ylabel('Scores')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('news', 'sport', 'science', 'society',
                        'shopping', 'adult'))
    ax.legend((rects1[0], rects2[0], rects3[0]),
              ('#found domains', '#registered by same entity', '#registered by different entity'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.show()
def owner():
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.ticker as mtick

    data = [1, 12, 15, 17, 18, 18.5]
    perc = np.linspace(0, 100, len(data))

    fig = plt.figure(1, (7, 4))
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(perc, data)

    fmt = '%.0f%%'  # Format you want the ticks, e.g. '40%'
    xticks = mtick.FormatStrFormatter(fmt)
    ax.xaxis.set_major_formatter(xticks)

    plt.show()


def extract_email_domain(email_address):
    emails_domain = []
    #print email_address
    #print 'type is',type(email_address)
    if isinstance(email_address, list):
        #print 'this is an array',email_address
        for email in email_address:
            #print 'email',email
            emails_domain.append(email[ email.find("@") : ])
        #print 'emaiul domains',emails_domain
    else:
        #print 'this is an string',email_address
        #print email_address
        if email_address:
            emails_domain.append(email_address[email_address.find("@"):])
    #print emails_domain
    return emails_domain
def purelize_registrar(registrar):
    offficial_registar = registrar.replace(" ", "")
    offficial_registar = offficial_registar.replace(",", "")
    offficial_registar = offficial_registar.replace(")", "")
    offficial_registar = offficial_registar.replace("(", "")
    offficial_registar = offficial_registar.replace(".", "")
    return offficial_registar




def do_for_top_50_all():
    objects = []
    with (open('dns_info_for_2018-02-06T19:40:45.449529_AlexaTopNewsWebSites.txt.pickle', "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    coun = 0
    for a in objects:
        # print 'len of typos for', a['key'], len(a['typos_dns_info'])
        coun = coun + len(a['typos_dns_info'])
    # print '-----------------------------------------number of found typoes is', coun
    whole_registrars = []
    not_available_email_typos = []
    whole_email_domains = []
    emails_dic = {}
    registrars_dic = {}
    for a in objects:
        typo_infos = a['typos_dns_info']
        # print a['key']
        target_typo_emails_domains = []
        target_typos_registrars = []
        for typo in typo_infos:
            info_dic = typo_infos[typo]
            try:
                # print typo
                emails_domains = extract_email_domain(info_dic['emails'])
                if emails_domains:
                    for domain in emails_domains:
                        whole_email_domains.append(domain)
                        target_typo_emails_domains.append(domain)

            except:
                not_available_email_typos.append(typo)
            try:
                typo_registrar = info_dic['registrar']
                # typo_registrar =purelize_registrar(typo_registrar)
                whole_registrars.append(typo_registrar)
                target_typos_registrars.append(typo_registrar)
            except:
                pass

        emails_dic[a['key']] = target_typo_emails_domains
        registrars_dic[a['key']] = target_typos_registrars
        # print a['key'], len(typo_infos)
        # print len(target_typo_emails_domains), len(set(target_typo_emails_domains))
        # print len(target_typos_registrars), len(set(target_typos_registrars))

    email_counter = {}
    for email in whole_email_domains:
        if email in email_counter:
            email_counter[email] += 1
        else:
            email_counter[email] = 1
    popular_words = sorted(email_counter, key=email_counter.get, reverse=True)
    # print popular_words
    top_1 = popular_words[:1]
    # print top_1
    top_2 = popular_words[:2]
    # print top_2
    top_3 = popular_words[:3]
    # print top_3
    top_4 = popular_words[:4]
    # print top_4
    top_5 = popular_words[:5]
    # print top_5
    top_6 = popular_words[:6]
    # print top_6
    top_7 = popular_words[:7]
    # print top_7
    top_8 = popular_words[:8]
    # print top_8
    top_9 = popular_words[:9]
    # print top_9

    email_counter = {}
    for email in whole_email_domains:
        if email in email_counter:
            email_counter[email] += 1
        else:
            email_counter[email] = 1
    popular_words = sorted(email_counter, key=email_counter.get, reverse=True)
    registrar_counter = {}
    for registrar in whole_registrars:
        if registrar in registrar_counter:
            registrar_counter[registrar] += 1
        else:
            registrar_counter[registrar] = 1
    popular_registrar = sorted(registrar_counter, key=registrar_counter.get, reverse=True)

    # print popular_words
    top_1 = popular_words[:1]
    # print top_1
    top_2 = popular_words[:2]
    # print top_2
    top_3 = popular_words[:3]
    # print top_3
    top_4 = popular_words[:4]
    # print top_4
    top_5 = popular_words[:5]
    # print top_5

    top_6 = popular_words[:6]
    # print top_6
    top_7 = popular_words[:7]
    # print top_7
    top_8 = popular_words[:8]

    top_9 = popular_words[:9]

    email_by_happening = {}
    registrar_by_happening = {}
    number_of_happening_of_emails = {i: whole_email_domains.count(i) for i in whole_email_domains}

    number_of_happening_of_registrar = {i: whole_registrars.count(i) for i in whole_registrars}
    for field, possible_values in number_of_happening_of_emails.iteritems():
        # print field, possible_values
        if field in top_6:
            email_by_happening[field] = possible_values

            # print email_by_happening
            # print '------------'

    for field, possible_values in number_of_happening_of_registrar.iteritems():
        #print field, possible_values
        if field in popular_registrar[:6]:
            registrar_by_happening[field] = possible_values

    # print email_by_happening
    # print registrar_by_happening
    email_domain = []
    email_domain_counter = []
    for item, value in email_by_happening.iteritems():
        email_domain.append(item)
        email_domain_counter.append(value)
    # print 'do_for_top_50_all'
    # print email_domain
    # print email_domain_counter
    # print '--------'
    regis_ = []
    reg_counter = []
    for item, value in registrar_by_happening.iteritems():
        regis_.append(item)
        reg_counter.append(value)
    print (regis_)
    print (reg_counter)

def do_for_top_15_all():
    objects = []
    with (open('dns_info_for_2018-02-08T21:22:36.802943_News_media_in_the_United_States.txt.pickle', "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    coun = 0
    for a in objects:
        #print 'len of typos for', a['key'], len(a['typos_dns_info'])
        coun = coun + len(a['typos_dns_info'])
    #print '-----------------------------------------number of found typoes is', coun
    whole_registrars = []
    not_available_email_typos = []
    whole_email_domains = []
    emails_dic = {}
    registrars_dic = {}
    for a in objects:
        typo_infos = a['typos_dns_info']
        # print a['key']
        target_typo_emails_domains = []
        target_typos_registrars = []
        for typo in typo_infos:
            info_dic = typo_infos[typo]
            try:
                # print typo
                emails_domains = extract_email_domain(info_dic['emails'])
                if emails_domains:
                    for domain in emails_domains:
                        whole_email_domains.append(domain)
                        target_typo_emails_domains.append(domain)

            except:
                not_available_email_typos.append(typo)
            try:
                typo_registrar = info_dic['registrar']
                # typo_registrar =purelize_registrar(typo_registrar)
                whole_registrars.append(typo_registrar)
                target_typos_registrars.append(typo_registrar)
            except:
                pass

        emails_dic[a['key']] = target_typo_emails_domains
        registrars_dic[a['key']] = target_typos_registrars
        #print a['key'], len(typo_infos)
        #print len(target_typo_emails_domains), len(set(target_typo_emails_domains))
        #print len(target_typos_registrars), len(set(target_typos_registrars))

    email_counter = {}
    for email in whole_email_domains:
        if email in email_counter:
            email_counter[email] += 1
        else:
            email_counter[email] = 1
    popular_words = sorted(email_counter, key=email_counter.get, reverse=True)
    #print popular_words
    top_1 = popular_words[:1]
    #print top_1
    top_2 = popular_words[:2]
    #print top_2
    top_3 = popular_words[:3]
    #print top_3
    top_4 = popular_words[:4]
    #print top_4
    top_5 = popular_words[:5]
    #print top_5
    top_6 = popular_words[:6]
    #print top_6
    top_7 = popular_words[:7]
    #print top_7
    top_8 = popular_words[:8]
    #print top_8
    top_9 = popular_words[:9]
    #print top_9

    email_counter = {}
    for email in whole_email_domains:
        if email in email_counter:
            email_counter[email] += 1
        else:
            email_counter[email] = 1
    popular_words = sorted(email_counter, key=email_counter.get, reverse=True)
    registrar_counter = {}
    for registrar in whole_registrars:
        if registrar in registrar_counter:
            registrar_counter[registrar] += 1
        else:
            registrar_counter[registrar] = 1
    popular_registrar = sorted(registrar_counter, key=registrar_counter.get, reverse=True)

    #print popular_words
    top_1 = popular_words[:1]
    #print top_1
    top_2 = popular_words[:2]
    #print top_2
    top_3 = popular_words[:3]
    #print top_3
    top_4 = popular_words[:4]
    #print top_4
    top_5 = popular_words[:5]
    #print top_5

    top_6 = popular_words[:6]
    #print top_6
    top_7 = popular_words[:7]
   #print top_7
    top_8 = popular_words[:8]

    top_9 = popular_words[:9]

    email_by_happening = {}
    registrar_by_happening = {}
    number_of_happening_of_emails = {i: whole_email_domains.count(i) for i in whole_email_domains}

    number_of_happening_of_registrar = {i: whole_registrars.count(i) for i in whole_registrars}
    for field, possible_values in number_of_happening_of_emails.iteritems():
        #print field, possible_values
        if field in top_6:
            email_by_happening[field] = possible_values

   # print email_by_happening
   # print '------------'

    for field, possible_values in number_of_happening_of_registrar.iteritems():
        #print field, possible_values
        if field in popular_registrar[:6]:
            registrar_by_happening[field] = possible_values

    #print email_by_happening
    #print registrar_by_happening
    email_domain = []
    email_domain_counter = []
    for item, value in email_by_happening.iteritems():
        email_domain.append(item)
        email_domain_counter.append(value)
    # print 'top 15 all '
    # print email_domain
    # print email_domain_counter
    # print '--------'
    regis_ = []
    reg_counter = []
    for item, value in registrar_by_happening.iteritems():
        regis_.append(item)
        reg_counter.append(value)

    # print regis_
    # print reg_counter
def email_tracker(name):
    #print 'emails'
    #objects = get_data(name)
    objects = []
    with (open(name, "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    coun = 0
    for a in objects:
        #print 'len of typos for', a['key'], len(a['typos_dns_info'])
        coun = coun+len(a['typos_dns_info'])
    #print '-----------------------------------------number of found typoes is',coun
    whole_registrars = []
    not_available_email_typos = []
    whole_email_domains = []
    emails_dic={}
    registrars_dic = {}
    for a in objects:
        typo_infos = a['typos_dns_info']
        #print a['key']
        target_typo_emails_domains = []
        target_typos_registrars = []
        for typo in typo_infos:
            info_dic = typo_infos[typo]
            try:
                #print typo
                emails_domains = extract_email_domain(info_dic['emails'])
                if emails_domains:
                    for domain in emails_domains:
                        whole_email_domains.append(domain)
                        target_typo_emails_domains.append(domain)

            except:
                not_available_email_typos.append(typo)
            try:
                typo_registrar = info_dic['registrar']
                #typo_registrar =purelize_registrar(typo_registrar)
                whole_registrars.append(typo_registrar)
                target_typos_registrars.append(typo_registrar)
            except:
                pass

        emails_dic[a['key']] = target_typo_emails_domains
        registrars_dic[a['key']] = target_typos_registrars
        #print a['key'],len(typo_infos)
        #print len(target_typo_emails_domains),len(set(target_typo_emails_domains))
        #print len(target_typos_registrars),len(set(target_typos_registrars))

    email_counter = {}
    for email in whole_email_domains:
        if email in email_counter:
            email_counter[email] += 1
        else:
            email_counter[email] = 1
    popular_words = sorted(email_counter, key=email_counter.get, reverse=True)
    #print popular_words
    top_1 = popular_words[:1]
    #print top_1
    top_2 = popular_words[:2]
    #print top_2
    top_3 = popular_words[:3]
    #print top_3
    top_4 = popular_words[:4]
    #print top_4
    top_5 = popular_words[:5]
    #print top_5
    top_6 = popular_words[:6]
    #print top_6
    top_7 = popular_words[:7]
    #print top_7
    top_8 = popular_words[:8]
    #print top_8
    top_9 = popular_words[:9]
    #print top_9


    email_counter = {}
    for email in whole_email_domains:
        if email in email_counter:
            email_counter[email] += 1
        else:
            email_counter[email] = 1
    popular_words = sorted(email_counter, key=email_counter.get, reverse=True)
    registrar_counter = {}
    for registrar in whole_registrars:
        if registrar in registrar_counter:
            registrar_counter[registrar] += 1
        else:
            registrar_counter[registrar] = 1
    popular_registrar = sorted(registrar_counter, key=registrar_counter.get, reverse=True)

    #print popular_words
    top_1 = popular_words[:1]
    #print top_1
    top_2 = popular_words[:2]
    #print top_2
    top_3 = popular_words[:3]
    #print top_3
    top_4 = popular_words[:4]
    #print top_4
    top_5 = popular_words[:5]
    #print top_5

    top_6 = popular_words[:6]
    #print top_6
    top_7 = popular_words[:7]
    #print top_7
    top_8 = popular_words[:8]
    #print top_8
    top_9 = popular_words[:9]
    #print top_9
    #for item in top_5:
        #print
    email_by_happening = {}
    registrar_by_happening = {}
    number_of_happening_of_emails = {i: whole_email_domains.count(i) for i in whole_email_domains}

    number_of_happening_of_registrar = {i: whole_registrars.count(i) for i in whole_registrars}
    for field, possible_values in number_of_happening_of_emails.iteritems():
        #print field, possible_values
        if field in top_6:
            email_by_happening[field] = possible_values

    #print email_by_happening
    #print '------------'



    for field, possible_values in number_of_happening_of_registrar.iteritems():
        #print field, possible_values
        if field in popular_registrar[:6]:
            registrar_by_happening[field] = possible_values

    #print email_by_happening
    #print registrar_by_happening
    email_domain = []
    email_domain_counter = []
    for item,value in email_by_happening.iteritems():
        email_domain.append(item)
        email_domain_counter.append(value)
    #print email_domain
    ##print email_domain_counter
    #print '--------'
    regis_ = []
    reg_counter = []
    for item,value in registrar_by_happening.iteritems():
        regis_.append(item)
        reg_counter.append(value)
    #print regis_
    #print reg_counter

    do_for_top_15_all()
    do_for_top_50_all()

    #
    # try:
    #     N = 6
    #     print 'after N=6'
    #     ind = np.arange(N)  # the x locations for the groups
    #     width = 0.27  # the width of the bars
    #     print 'after width'
    #     fig = plt.figure()
    #     print 'after fig'
    #     ax = fig.add_subplot(111)
    #
    #     yvals = [email_domain_counter[0],
    #              email_domain_counter[1],
    #              email_domain_counter[2] ,  email_domain_counter[3],
    #              email_domain_counter[4], email_domain_counter[5]]
    #     rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    #     print 'after rects1'
    #     # zvals = [news_same_typos, sport_same_typos, sciece_same_typos, society_same_typos,
    #     #          adult_same_typos, 7]
    #     # rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    #     # kvals = [news_dif_typos, sport_dif_typos, sciece_dif_typos, society_dif_typos,
    #     #          adult_dif_typos, 7]
    #     # rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')
    #
    #     ax.set_ylabel('Scores')
    #     ax.set_xticks(ind + width)
    #     ax.set_xticklabels((email_domain[0], email_domain[1], email_domain[2], email_domain[3],
    #                         email_domain[4],email_domain[5]))
    #     ax.legend((rects1[0]),
    #               ('#found domains', '#registered by same entity', '#registered by different entity'))
    #     print '+++++++++++++++++++++++++++++++++++++'
    #     def autolabel(rects):
    #         for rect in rects:
    #             h = rect.get_height()
    #             ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
    #                     ha='center', va='bottom')
    #
    #     autolabel(rects1)
    #     print '-----------------------------'
    #     from matplotlib.backends.backend_pdf import PdfPages
    #
    #     #plt.show()
    #     f = plt.figure()
    #     f.savefig("foo.pdf", bbox_inches='tight')
    #
    # except ValueError:
    #     print 'error',ValueError
    #
    #         # for key in registrars_dic:
    # #     print key



def Owner_Tracker(name):
    dns_objects = get_data(name)
    whole_registrars = []
    not_available_registrar_typos = []
    typo_counter = 0
    for a in dns_objects:
        typo_infos = a['typos_dns_info']
        # print a['key']

        for typo in typo_infos:
            typo_counter = typo_counter + 1
            info_dic = typo_infos[typo]
            typo_emails = {}
            try:
                # print typo
                print info_dic
                registrar = (info_dic['registrar'])
                print registrar
                if registrar:
                    whole_registrars.append(registrar)

            except:
                try:
                    registrar = (info_dic['registrar'])
                    if registrar:
                        whole_registrars.append(registrar)


                except:
                    print 'shit===================='
                    print typo, info_dic

                    not_available_registrar_typos.append(typo)
        # print typo_emails
        print len(not_available_registrar_typos)
    registrar_counter = {}

    print len(whole_registrars)
    print whole_registrars
    whole_registrars2 = []
    for item in whole_registrars:
        item = purelize_registrar(item)
        whole_registrars2.append(item)
    #print len(set(whole_registrars))
    for reg in whole_registrars2:
        if reg in registrar_counter:
            registrar_counter[reg] += 1
        else:
            registrar_counter[reg] = 1
    print 'registrar_counter',registrar_counter
    popular_words = sorted(registrar_counter, key=registrar_counter.get, reverse=True)
    # print popular_words
    top_1 = popular_words[:1]
    reg_by_happening = {}
    print 'popular_words' ,popular_words
    registrar_by_happening = {}
    number_of_happening_of_registrars = {i: whole_registrars2.count(i) for i in whole_registrars2}

    for field, possible_values in number_of_happening_of_registrars.iteritems():
        # print field, possible_values
        if field in popular_words[:6]:
            reg_by_happening[field] = possible_values

            # print email_by_happening
            # print '------------'
    # for key, value in sorted(number_of_happening_of_registrars.iteritems(), key=lambda (k, v): (v, k)):
    #     print "%s: %s" % (key, value)

    print 'reg_by_happening',reg_by_happening
    registrars = []
    registrar_counter = []
    for item, value in reg_by_happening.iteritems():
        registrars.append(item)
        registrar_counter.append(value)
    # print 'do_for_top_50_all'

    print typo_counter
    print 'top registrars',(registrars)
    print 'top count of registrars',registrar_counter
    for item in whole_registrars2:
        print item

    N = 6
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = [registrar_counter[0],
             registrar_counter[1],
             registrar_counter[2], registrar_counter[3],
             registrar_counter[4], registrar_counter[5]]
    rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    # zvals = [news_same_typos, sport_same_typos, sciece_same_typos, society_same_typos,
    #          adult_same_typos, 7]
    # rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    # kvals = [news_dif_typos, sport_dif_typos, sciece_dif_typos, society_dif_typos,
    #          adult_dif_typos, 7]
    # rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')

    ax.set_ylabel('#used email domain')
    ax.set_xticks(ind + width)
    ax.set_xticklabels((registrars[0], registrars[1], registrars[2], registrars[3],
                        registrars[4], registrars[5]))

    # ax.legend((rects1[0]),
    #           ('#found domains', '#registered by same entity', '#registered by different entity'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    autolabel(rects1)

    plt.show()
    plt.savefig('emails_15_three.pdf')
def new_tld_Tracker(name):
    print 'done'
    objects = get_data(name)
    same_tlds = []
    dif_tlds = []
    same_typo_counter = 0
    dif_typo_counter = 0
    for item in objects:
        same_typos = item['same_owner_typos']
        dif_typos = item['dif_owner_typos']
        for typo in same_typos:
            same_typo_counter = same_typo_counter +1
            domain_tld = typo.split('.')
            if len(domain_tld) ==2:
                tld = domain_tld[1]
            elif len(domain_tld) ==3:
                tld = domain_tld[2]
            same_tlds.append(tld)

        for typo in dif_typos:
            dif_typo_counter = dif_typo_counter +1
            domain_tld = typo.split('.')
            print domain_tld
            if len(domain_tld) ==2:
                tld = domain_tld[1]
            elif len(domain_tld) ==3:
                tld = domain_tld[2]
            dif_tlds.append(tld)
    print same_typo_counter
    print len(same_tlds)
    print len(dif_tlds)
    tld_counter = {}
    for tld in same_tlds:
        if tld in tld_counter:
            tld_counter[tld] += 1
        else:
            tld_counter[tld] = 1
    popular_words = sorted(tld_counter, key=tld_counter.get, reverse=True)

    tld_by_happening = {}

    number_of_happening_of_tlds = {i: same_tlds.count(i) for i in same_tlds}

    for field, possible_values in number_of_happening_of_tlds.iteritems():
        # print field, possible_values
        if field in popular_words[:6]:
            tld_by_happening[field] = possible_values

            # print email_by_happening
            # print '------------'
    for key, value in sorted(number_of_happening_of_tlds.iteritems(), key=lambda (k, v): (v, k)):
        print "%s: %s" % (key, value)

    print tld_by_happening
    tlds = []
    tld_counter = []
    for item, value in tld_by_happening.iteritems():
        tlds.append(item)
        tld_counter.append(value)
    # print 'do_for_top_50_all'
    print tlds
    print tld_counter
    print same_typo_counter
    print len(same_typos)
    print len(same_tlds)
    print len(set(same_tlds))
    N = 6
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = [100 * tld_counter[0]/same_typo_counter,
             100 *tld_counter[1]/same_typo_counter,
            100 * tld_counter[2]/same_typo_counter, 100 *tld_counter[3]/same_typo_counter,
             100 *tld_counter[4]/same_typo_counter, 100 *tld_counter[5]/same_typo_counter]
    rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    # zvals = [news_same_typos, sport_same_typos, sciece_same_typos, society_same_typos,
    #          adult_same_typos, 7]
    # rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    # kvals = [news_dif_typos, sport_dif_typos, sciece_dif_typos, society_dif_typos,
    #          adult_dif_typos, 7]
    # rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')

    ax.set_ylabel('% of using new tlds in reg typos by same entity')
    ax.set_xticks(ind + width)
    ax.set_xticklabels((tlds[0], tlds[1], tlds[2], tlds[3],
                        tlds[4], tlds[5]))

    # ax.legend((rects1[0]),
    #           ('#found domains', '#registered by same entity', '#registered by different entity'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    autolabel(rects1)

    plt.show()
    plt.savefig('emails_15_three.pdf')



    tld_counter = {}
    for tld in dif_tlds:
        if tld in tld_counter:
            tld_counter[tld] += 1
        else:
            tld_counter[tld] = 1
    popular_words = sorted(tld_counter, key=tld_counter.get, reverse=True)

    tld_by_happening = {}

    number_of_happening_of_tlds = {i: dif_tlds.count(i) for i in dif_tlds}

    for field, possible_values in number_of_happening_of_tlds.iteritems():
        # print field, possible_values
        if field in popular_words[:6]:
            tld_by_happening[field] = possible_values

            # print email_by_happening
            # print '------------'
    for key, value in sorted(number_of_happening_of_tlds.iteritems(), key=lambda (k, v): (v, k)):
        print "%s: %s" % (key, value)

    print tld_by_happening
    tlds = []
    tld_counter = []
    for item, value in tld_by_happening.iteritems():
        tlds.append(item)
        tld_counter.append(value)
    # print 'do_for_top_50_all'
    print tlds
    print tld_counter
    print dif_typo_counter
    print len(dif_tlds)
    print len(set(dif_tlds))
    print len(dif_typos)
    print tld_counter[0]
    N = 6
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = [100 * tld_counter[0] /dif_typo_counter,
             100 * tld_counter[1] / dif_typo_counter,
             100 * tld_counter[2] / dif_typo_counter, 100 * tld_counter[3] / dif_typo_counter,
             100 * tld_counter[4] / dif_typo_counter, 100 * tld_counter[5] / dif_typo_counter]
    rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    # zvals = [news_same_typos, sport_same_typos, sciece_same_typos, society_same_typos,
    #          adult_same_typos, 7]
    # rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    # kvals = [news_dif_typos, sport_dif_typos, sciece_dif_typos, society_dif_typos,
    #          adult_dif_typos, 7]
    # rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')

    ax.set_ylabel('% of using new tlds in reg typos by different entity')
    ax.set_xticks(ind + width)
    ax.set_xticklabels((tlds[0], tlds[1], tlds[2], tlds[3],
                        tlds[4], tlds[5]))

    # ax.legend((rects1[0]),
    #           ('#found domains', '#registered by same entity', '#registered by different entity'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    autolabel(rects1)

    plt.show()
    plt.savefig('emails_15_three.pdf')





def email_plotter(dns_file_name,same_dif_file_name):
    dns_objects = get_data(dns_file_name)
    same_dif_objects = get_data(same_dif_file_name)
    whole_registrars = []
    not_available_email_typos = []
    whole_email_domains = []
    emails_dic = {}
    my_dic = {}
    email_set_typos = 0
    typos_email = {}
    registrars_dic = {}
    typo_counter = 0
    for a in dns_objects:
        typo_infos = a['typos_dns_info']
        # print a['key']
        target_typo_emails_domains = []
        target_typos_registrars = []
        for typo in typo_infos:
            typo_counter = typo_counter +1
            info_dic = typo_infos[typo]
            typo_emails = {}
            try:
                # print typo
                emails_domains = extract_email_domain(info_dic['emails'])
                if emails_domains:
                    email_set_typos = email_set_typos +1
                    for domain in emails_domains:
                        whole_email_domains.append(domain)

                    typo_emails[typo] = emails_domains

            except :
                try:
                    # print typo
                    emails_domains = extract_email_domain(info_dic['admin_email'])
                    if emails_domains:
                        email_set_typos = email_set_typos +1
                        for domain in emails_domains:
                            whole_email_domains.append(domain)
                        typo_emails[typo] = emails_domains
                except:
                    print 'shit===================='
                    print typo,info_dic

                    not_available_email_typos.append(typo)
        #print typo_emails
        print len(not_available_email_typos)
    email_counter = {}
    for email in whole_email_domains:
        if email in email_counter:
            email_counter[email] += 1
        else:
            email_counter[email] = 1
    popular_words = sorted(email_counter, key=email_counter.get, reverse=True)
    # print popular_words
    top_1 = popular_words[:1]


    email_counter = {}
    for email in whole_email_domains:
        if email in email_counter:
            email_counter[email] += 1
        else:
            email_counter[email] = 1
    popular_words = sorted(email_counter, key=email_counter.get, reverse=True)
    email_by_happening = {}
    registrar_by_happening = {}
    number_of_happening_of_emails = {i: whole_email_domains.count(i) for i in whole_email_domains}

    for field, possible_values in number_of_happening_of_emails.iteritems():
        # print field, possible_values
        if field in popular_words[:6]:
            email_by_happening[field] = possible_values

            # print email_by_happening
            # print '------------'
    for key, value in sorted(number_of_happening_of_emails.iteritems(), key=lambda (k, v): (v, k)):
        print "%s: %s" % (key, value)

    print email_by_happening
    email_domain = []
    email_domain_counter = []
    for item, value in email_by_happening.iteritems():
        email_domain.append(item)
        email_domain_counter.append(value)
    # print 'do_for_top_50_all'
    print email_domain
    print email_domain_counter
    print typo_counter
    print len(whole_email_domains)
    print len(set(whole_email_domains))
    N = 6
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = [100.0 * (email_domain_counter[0])/email_set_typos,
             100.0 * (email_domain_counter[1]) / email_set_typos,
             100.0 * (email_domain_counter[2]) / email_set_typos, 100.0 * (email_domain_counter[3])/email_set_typos,
             100.0 * (email_domain_counter[4]) / email_set_typos, 100.0 * (email_domain_counter[5])/email_set_typos]
    rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    # zvals = [news_same_typos, sport_same_typos, sciece_same_typos, society_same_typos,
    #          adult_same_typos, 7]
    # rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    # kvals = [news_dif_typos, sport_dif_typos, sciece_dif_typos, society_dif_typos,
    #          adult_dif_typos, 7]
    # rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')

    ax.set_ylabel('(% )percent of used email domain')
    ax.set_xticks(ind + width)
    ax.set_xticklabels((email_domain[0], email_domain[1], email_domain[2], email_domain[3],
                        email_domain[4], email_domain[5]))

    # ax.legend((rects1[0]),
    #           ('#found domains', '#registered by same entity', '#registered by different entity'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    plt.xticks(rotation=45)
    plt.show()
    plt.savefig('Percent og emails_used.pdf')


    # import pdb
    # pdb.set_trace()
    # for dns_object in dns_objects:
    #     key = dns_object['key']
    #     for item in same_dif_objects:
    #         sec_key = item['key']
    #         if sec_key == key:
    #             typos  = item['dif_owner_typos']
    #             dns_info  = dns_object[dns_info]
    #             for same_dif_typo in typos:
    #                 dns_info = dns_object['typos_dns_info']
    #                 for pure_typo in dns_info:
    #                     if pure_typo == same_dif_typo:
    #                         print 'ok'
    #     # print 'len of typos for', a['key'], len(a['typos_dns_info'])
    # # print '-----------------------------------------number of found typoes is', coun
    #
    #
    # registrar_counter = {}
    # for registrar in whole_registrars:
    #     if registrar in registrar_counter:
    #         registrar_counter[registrar] += 1
    #     else:
    #         registrar_counter[registrar] = 1
    # popular_registrar = sorted(registrar_counter, key=registrar_counter.get, reverse=True)
    #
    # # print popular_words
    # top_1 = popular_words[:1]
    # # print top_1
    # top_2 = popular_words[:2]
    # # print top_2
    # top_3 = popular_words[:3]
    # # print top_3
    # top_4 = popular_words[:4]
    # # print top_4
    # top_5 = popular_words[:5]
    # # print top_5
    #
    # top_6 = popular_words[:6]
    # # print top_6
    # top_7 = popular_words[:7]
    # # print top_7
    # top_8 = popular_words[:8]
    #
    # top_9 = popular_words[:9]
    #
    #
    # print '--------'
    # regis_ = []
    # reg_counter = []
    # for item, value in registrar_by_happening.iteritems():
    #     regis_.append(item)
    #     reg_counter.append(value)
    # print (regis_)
    # print (reg_counter)
    # for field, possible_values in number_of_happening_of_emails.iteritems():
    #     print field, possible_values
    #

    #
    #
    #
    #
    # N = 6
    # ind = np.arange(N)  # the x locations for the groups
    # width = 0.27  # the width of the bars
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    #
    # yvals = [35,
    #          94,
    #          32, 52,
    #          75, 45]
    # rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    # # zvals = [news_same_typos, sport_same_typos, sciece_same_typos, society_same_typos,
    # #          adult_same_typos, 7]
    # # rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    # # kvals = [news_dif_typos, sport_dif_typos, sciece_dif_typos, society_dif_typos,
    # #          adult_dif_typos, 7]
    # # rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')
    #
    # ax.set_ylabel('#used email domain')
    # ax.set_xticks(ind + width)
    # ax.set_xticklabels(('@ename.com', '@nic.mx', 'service.aliyun.com', '@22.cn',
    #                     '@qq.com', '@gmail'))
    #
    # # ax.legend((rects1[0]),
    # #           ('#found domains', '#registered by same entity', '#registered by different entity'))
    #
    # def autolabel(rects):
    #     for rect in rects:
    #         h = rect.get_height()
    #         ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
    #                 ha='center', va='bottom')
    #
    # autolabel(rects1)
    #
    # plt.show()
    # plt.savefig('emails15_all.pdf')
    #


   # # {'@ename.com': 35, '@nic.mx': 94, '@service.aliyun.com': 32, '@22.cn': 52, '@qq.com': 75, '@gmail.com': 45}
   #

def plot_per_model(models):
    print 'ok'

def Plotting_per_model(name):

    #print 'per model plots'
    models_for_same = get_used_models(name)
    models_for_dif=get_used_models_dif(name)
    #for item,value in models_for_same.iteritems():
        #print item,value
    #print '-------------'
    #for item,value in models_for_dif.iteritems():
        #print item,value
    import numpy as np
    import matplotlib.pyplot as plt
    expansion = models_for_same['Original*']+models_for_dif['Original*']

    #print expansion
    import pdb
    #pdb.set_trace()
    N = 3
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)
    print 'models_for_same',models_for_same
    import pdb
    #pdb.set_trace()
    yvals = [models_for_same['Original*']+models_for_dif['Original*'], models_for_same['Omission']+models_for_dif['Omission'], models_for_same['Repetition']+models_for_dif['Repetition']]
    rects1 = ax.bar(ind, yvals, width, color='#424949')
    zvals = [models_for_same['Original*'],models_for_same['Omission'] , models_for_same['Repetition']]
    rects2 = ax.bar(ind + width, zvals, width, color='#E5E7E9')
    kvals = [models_for_dif['Original*'], models_for_dif['Omission'], models_for_dif['Repetition']]
    rects3 = ax.bar(ind + width * 2, kvals, width, color='#E6B0AA')

    ax.set_ylabel('#found domains')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('by_new_tld', 'Omission', 'Repetition'))
    ax.legend((rects1[0], rects2[0], rects3[0]), ('all_found_domain_by_this_method', 'reg_by_official_owner', 'reg_by_dif_entity'))
    #plt.xticks(rotation=90)
    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.show()

def targeted_domains(media_three_models):
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
    objects = get_data(media_three_models)
    same_owners = 0
    dif_owners = 0
    got_typos = []
    typo_counter = 0
    same_typos_list = []
    got_typos = []
    Original_typos = []

    DB__NEW_TLD = []
    with open("tlds-alpha-by-domain.txt") as f:
        websitescontent = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
    websitescontent = [x2.strip() for x2 in websitescontent]
    for item in websitescontent:
        if len(item) < 4:
            DB__NEW_TLD.append(item)
    print 'check the generation models manually'
    for item in objects:
        # print item
        Downloaded_typos = []
        # print item
        tld_used_counter = []
        original_domain = item['key']
        domain = original_domain.split('.')
        if len(domain) ==2:
            domain = domain[0]
        elif len(domain) ==3:
            domain = domain[0]+'.'+domain[1]

        typo_infos = item['same_owner_typos']
        #print len(typo_infos)
        #print len(item['dif_owner_typos'])
        #print '----------------------------------'

        typo_infos.extend(item['dif_owner_typos'])
        #print len(typo_infos)
        #print typo_infos
        import pdb
        #pdb.set_trace()
        for key in typo_infos:
            typo_counter = typo_counter+1
            if domain in key:
                tld_used_counter.append(key)
                Original_typos.append(key)
        #print original_domain,100*(len(tld_used_counter) / len(DB__NEW_TLD))
        #print original_domain,len(tld_used_counter),len(DB__NEW_TLD)
        print original_domain,len(tld_used_counter),len(DB__NEW_TLD), 100.0 * len(tld_used_counter)/len(DB__NEW_TLD)
    #         typo = key
    #         got_typos.append(key)
    #         typo_counter = typo_counter +1
    #         Downloaded_typos.append(typo)
    #         same_typos_list.append(typo)
    #         # print typo
    #     # import pdb
    #     # pdb.set_trace()
    #     dfuzz = DomainFuzz(original_domain)
    #     #print original_domain
    #     import pdb
    #
    #     # pdb.set_trace()
    #     dfuzz.generate()
    #     Generated_Domains = dfuzz.domains
    #     #print 'origin', original_domain
    #     #print 'generated', Generated_Domains
    #     #print 'downloaded typos', Downloaded_typos
    #     # pdb.set_trace()
    #
    #     for analyaed_typo in Downloaded_typos:
    #         analyzed = analyaed_typo.split('.')
    #         # print split
    #         if len(analyzed) == 2:
    #             analyzed_TLD = analyzed[1]
    #             analyzed_WebSiteName = analyzed[0]
    #         # print WebSiteName + "," +Domain_Name
    #         elif len(analyzed) == 3:
    #             analyzed_TLD = analyzed[2]
    #             analyzed_WebSiteName = analyzed[0] + "." + analyzed[1]
    #         #print 'here the analyzed typo and downloaded typo is', analyzed_WebSiteName
    #         for raw_typo in Generated_Domains:
    #             raw = raw_typo['domain-name'].split('.')
    #             #print 'raw_typo[domain-name]', raw_typo
    #             # print split
    #             if len(raw) == 2:
    #                 raw_TLD = raw[1]
    #                 raw_WebSiteName = raw[0]
    #             # print WebSiteName + "," +Domain_Name
    #             elif len(raw) == 3:
    #                 raw_TLD = raw[2]
    #                 raw_WebSiteName = raw[0] + "." + raw[1]
    #
    #             if analyzed_WebSiteName == raw_WebSiteName:
    #                 #print 'analyzed_WebSiteName================================================', analyzed_WebSiteName
    #                 #print 'raw_WebSiteName================================================', raw_WebSiteName, \
    #                 raw_typo['domain-name']
    #                 #print 'raw_typo[fuzzer]=============================================', raw_typo['fuzzer']
    #                 #print found_models[raw_typo['fuzzer']]
    #                 found_models[raw_typo['fuzzer']] = found_models[raw_typo['fuzzer']] + 1
    #                 #print found_models[raw_typo['fuzzer']]
    #
    # # print found_models
    # #print '-------------------------------------------------------------------', same_typos_list
    # print found_models
    #for i in Original_typos:
        #print i
    print typo_counter,len(Original_typos)

def targeted_domains2(name):
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
    got_typos = []
    typo_counter = 0
    same_typos_list = []
    got_typos = []
    Original_typos = []

    DB__NEW_TLD = []
    with open("tlds-alpha-by-domain.txt") as f:
        websitescontent = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
    websitescontent = [x2.strip() for x2 in websitescontent]
    for item in websitescontent:
        if len(item) < 4:
            DB__NEW_TLD.append(item)
    print 'check the generation models manually'
    for item in objects:
        # print item
        Downloaded_typos = []
        # print item
        tld_used_counter = []
        original_domain = item['key']
        domain = original_domain.split('.')
        if len(domain) == 2:
            domain = domain[0]
        elif len(domain) == 3:
            domain = domain[0] + '.' + domain[1]

        typo_infos = item['typos_dns_info']
        # print len(typo_infos)
        # print len(item['dif_owner_typos'])
        # print '----------------------------------'

        # print len(typo_infos)
        # print typo_infos
        import pdb
        # pdb.set_trace()
        for key in typo_infos:
            typo_counter = typo_counter + 1
            if domain in key:
                tld_used_counter.append(key)
                Original_typos.append(key)
        # print original_domain,100*(len(tld_used_counter) / len(DB__NEW_TLD))
        print original_domain, len(tld_used_counter), len(DB__NEW_TLD)

def Plotting_per_model_per_site(media_three_models):
    print 'per site'
    targeted_domains = {}
    modesl = {}
    objects = get_data(media_three_models)
    same_owners = 0
    dif_owners = 0
    same_typos_list = []
    dif_typos_list = []
    # print 'check the generation models manually'
    for item in objects:
        each_site_dic = {}

        same_found_models = {}
        same_found_models['Original*'] = 0
        same_found_models['Replacement'] = 0
        same_found_models['Addition'] = 0
        same_found_models['Transposition'] = 0
        same_found_models['Vowel-swap'] = 0
        same_found_models['Omission'] = 0
        same_found_models['Repetition'] = 0
        same_found_models['Transposition'] = 0
        same_found_models['PhillipaSuggestion'] = 0
        same_found_models['moving_dot_position'] = 0
        # print item
        Downloaded_typos = []
        # print item
        original_domain = item['key']

        same_typo_infos = item['same_owner_typos']
        for key in same_typo_infos:
            typo = key
            Downloaded_typos.append(typo)
            same_typos_list.append(typo)
            # print typo
        # import pdb
        # pdb.set_trace()
        dfuzz = DomainFuzz(original_domain)
        # print original_domain
        import pdb

        # pdb.set_trace()
        dfuzz.generate()
        Generated_Domains = dfuzz.domains
        # print 'origin',original_domain
        # print 'generated',Generated_Domains
        # print 'downloaded typos',Downloaded_typos
        # pdb.set_trace()

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
            # print 'here the analyzed typo and downloaded typo is',analyzed_WebSiteName
            for raw_typo in Generated_Domains:
                raw = raw_typo['domain-name']
                if analyzed_WebSiteName in raw:
                    #print analyaed_typo, raw, raw_typo['fuzzer']
                    same_found_models[raw_typo['fuzzer']] = same_found_models[raw_typo['fuzzer']] + 1
        print original_domain,'same_found_models',same_found_models

        dif_found_models = {}
        dif_found_models['Original*'] = 0
        dif_found_models['Replacement'] = 0
        dif_found_models['Addition'] = 0
        dif_found_models['Transposition'] = 0
        dif_found_models['Vowel-swap'] = 0
        dif_found_models['Omission'] = 0
        dif_found_models['Repetition'] = 0
        dif_found_models['Transposition'] = 0
        dif_found_models['PhillipaSuggestion'] = 0
        dif_found_models['moving_dot_position'] = 0
        dif_typo_infos = item['dif_owner_typos']
        Downloaded_typos = []
        dif_typos_list = []
        for key in dif_typo_infos:
            typo = key
            Downloaded_typos.append(typo)
            dif_typos_list.append(typo)
            # print typo
            # import pdb
            # pdb.set_trace()
        dfuzz = DomainFuzz(original_domain)
        # print original_domain
        import pdb

        # pdb.set_trace()
        dfuzz.generate()
        Generated_Domains = dfuzz.domains
        # print 'origin',original_domain
        # print 'generated',Generated_Domains
        # print 'downloaded typos',Downloaded_typos
        # pdb.set_trace()

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
            # print 'here the analyzed typo and downloaded typo is',analyzed_WebSiteName
            for raw_typo in Generated_Domains:
                raw = raw_typo['domain-name']
                if analyzed_WebSiteName in raw:
                    #print analyaed_typo, raw, raw_typo['fuzzer']
                    dif_found_models[raw_typo['fuzzer']] = dif_found_models[raw_typo['fuzzer']] + 1
        print original_domain,'dif_found_models',dif_found_models
        each_site_dic['same_found_models'] = same_found_models
        each_site_dic['dif_found_models'] = dif_found_models
        targeted_domains[original_domain] = each_site_dic
    attacked_sites = []
    attacked_sites_same = []
    attacked_sites_dif = []
    for key,value in targeted_domains.iteritems():
        print key
        print value

        attacked_sites.append(key)

        same = value['same_found_models']
        dif = value['dif_found_models']
        attacked_sites_same.append(same['Original*'])
        attacked_sites_dif.append(dif['Original*'])
    import numpy as np
    import matplotlib.pyplot as plt

    N = 6
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = [attacked_sites_dif[0] + attacked_sites_same[0],
             attacked_sites_dif[1] + attacked_sites_same[1],
             attacked_sites_dif[2] + attacked_sites_same[2], attacked_sites_dif[3] + attacked_sites_same[3],
             attacked_sites_dif[4] + attacked_sites_same[4], attacked_sites_dif[5] + attacked_sites_same[5]]
    rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    zvals = [attacked_sites_same[0], attacked_sites_same[1], attacked_sites_same[2], attacked_sites_same[3],
             attacked_sites_same[4], attacked_sites_same[5]]
    rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    kvals = [attacked_sites_dif[0], attacked_sites_dif[1], attacked_sites_dif[2], attacked_sites_dif[3],
             attacked_sites_dif[4], attacked_sites_dif[5]]
    rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')

    ax.set_ylabel('#found domains')
    ax.set_xticks(ind + width)
    ax.set_xticklabels((attacked_sites[0], attacked_sites[1], attacked_sites[2], attacked_sites[3],
                        attacked_sites[4], attacked_sites[5]))
    ax.legend((rects1[0], rects2[0], rects3[0]),
              ('#registered the official domain by new tlds', '#registered by official domain owner', '#registered by different entity'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    plt.xticks(rotation=30)
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.show()
    fig.savefig('attacked_sites_first_6.pdf')
    N = 7
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = [attacked_sites_dif[6] + attacked_sites_same[6],
             attacked_sites_dif[7] + attacked_sites_same[7],
             attacked_sites_dif[8] + attacked_sites_same[8], attacked_sites_dif[9] + attacked_sites_same[9],
             attacked_sites_dif[10] + attacked_sites_same[10], attacked_sites_dif[11] + attacked_sites_same[11],attacked_sites_dif[12] + attacked_sites_same[12]]
    rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    zvals = [attacked_sites_same[6], attacked_sites_same[7], attacked_sites_same[8], attacked_sites_same[9],
             attacked_sites_same[10], attacked_sites_same[11],attacked_sites_same[12]]
    rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    kvals = [attacked_sites_dif[6], attacked_sites_dif[7], attacked_sites_dif[8], attacked_sites_dif[9],
             attacked_sites_dif[10], attacked_sites_dif[11],attacked_sites_dif[12]]
    rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')

    ax.set_ylabel('#found domains')
    ax.set_xticks(ind + width)
    ax.set_xticklabels((attacked_sites[6], attacked_sites[7], attacked_sites[8], attacked_sites[9],
                        attacked_sites[10], attacked_sites[11],attacked_sites[12]))
    ax.legend((rects1[0], rects2[0], rects3[0]),
              ('#registered the official domain by new tlds', '#registered by official domain owner',
               '#registered by different entity'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    plt.xticks(rotation=35)
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.show()
    fig.savefig('attacked_sites_last_7.pdf')

    N = 13
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = [attacked_sites_dif[0] + attacked_sites_same[0],
             attacked_sites_dif[1] + attacked_sites_same[1],
             attacked_sites_dif[2] + attacked_sites_same[2], attacked_sites_dif[3] + attacked_sites_same[3],
             attacked_sites_dif[4] + attacked_sites_same[4], attacked_sites_dif[5] + attacked_sites_same[5],
             attacked_sites_dif[6] + attacked_sites_same[6],
             attacked_sites_dif[7] + attacked_sites_same[7],
             attacked_sites_dif[8] + attacked_sites_same[8], attacked_sites_dif[9] + attacked_sites_same[9],
             attacked_sites_dif[10] + attacked_sites_same[10], attacked_sites_dif[11] + attacked_sites_same[11],
             attacked_sites_dif[12] + attacked_sites_same[12]]
    rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    zvals = [attacked_sites_same[0], attacked_sites_same[1], attacked_sites_same[2], attacked_sites_same[3],
             attacked_sites_same[4], attacked_sites_same[5], attacked_sites_same[6], attacked_sites_same[7],
             attacked_sites_same[8], attacked_sites_same[9],
             attacked_sites_same[10], attacked_sites_same[11], attacked_sites_same[12]]
    rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    kvals = [attacked_sites_dif[0], attacked_sites_dif[1], attacked_sites_dif[2], attacked_sites_dif[3],
             attacked_sites_dif[4], attacked_sites_dif[5], attacked_sites_dif[6], attacked_sites_dif[7],
             attacked_sites_dif[8], attacked_sites_dif[9],
             attacked_sites_dif[10], attacked_sites_dif[11], attacked_sites_dif[12]]
    rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')

    ax.set_ylabel('Scores')
    ax.set_xticks(ind + width)
    ax.set_xticklabels((attacked_sites[0], attacked_sites[1], attacked_sites[2], attacked_sites[3],
                        attacked_sites[4], attacked_sites[5], attacked_sites[6], attacked_sites[7], attacked_sites[8],
                        attacked_sites[9],
                        attacked_sites[10], attacked_sites[11], attacked_sites[12]))
    ax.legend((rects1[0], rects2[0], rects3[0]),
              ('#registered the official domain by new tlds', '#registered by same entity',
               '#registered by different entity'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    plt.xticks(rotation=45)
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.show()
    fig.savefig('attacked_sites.pdf')




    # for item,value in models_for_same.iteritems():
    # print item,value
    # print '-------------'
    # for item,value in models_for_dif.iteritems():
    # print item,value
    # import numpy as np
    # import matplotlib.pyplot as plt
    # expansion = dif_found_models['Original*'] + dif_found_models['Original*']
    #
    # # print expansion
    # import pdb
    # # pdb.set_trace()
    # N = 3
    # ind = np.arange(N)  # the x locations for the groups
    # width = 0.27  # the width of the bars
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # print 'models_for_dif', dif_found_models
    # import pdb
    # # pdb.set_trace()
    # yvals = [same_found_models['Original*'] + dif_found_models['Original*'],
    #          found_models['Omission'] + found_models['Omission'],
    #          found_models['Repetition'] + models_for_dif['Repetition']]
    # rects1 = ax.bar(ind, yvals, width, color='#424949')
    # zvals = [models_for_same['Original*'], models_for_same['Omission'], models_for_same['Repetition']]
    # rects2 = ax.bar(ind + width, zvals, width, color='#E5E7E9')
    # kvals = [models_for_dif['Original*'], models_for_dif['Omission'], models_for_dif['Repetition']]
    # rects3 = ax.bar(ind + width * 2, kvals, width, color='#E6B0AA')
    #
    # ax.set_ylabel('#found domains')
    # ax.set_xticks(ind + width)
    # ax.set_xticklabels(('by_new_tld', 'Omission', 'Repetition'))
    # ax.legend((rects1[0], rects2[0], rects3[0]),
    #           ('all_found_domain_by_this_method', 'reg_by_official_owner', 'reg_by_dif_entity'))
    #
    # # plt.xticks(rotation=90)
    # def autolabel(rects):
    #     for rect in rects:
    #         h = rect.get_height()
    #         ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
    #                 ha='center', va='bottom')
    #
    # autolabel(rects1)
    # autolabel(rects2)
    # autolabel(rects3)
    #
    # plt.show()
def domain_lists(name):
    objects = get_data(name)
    domain_list = []
    for item in objects:
        original = item['key']
        dns_info = item['typos_dns_info']
        for typo in dns_info:
            domain_list.append(typo)
    #print domain_list
    #print len(domain_list)
    try:
        # logging.debug('Acquired lock')

        pickle_out = open("domain_list.pickle", "a+b")
        pickle.dump(domain_list, pickle_out)
        pickle_out.close()
    except:
        pass
    objects = []
    with (open('domain_list.pickle', "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    #print objects
    for item in objects:

        domain_array = item
        for domain in domain_array:
            print domain
def get_typos_number (name1):
    objects = get_data(name1)
    typo_counter = 0
    for item in objects:
        typos_info = item['typos_dns_info']
        for typo in typos_info:
            typo_counter = typo_counter+1
    return typo_counter
def per_day():
    import pandas as pd
    import numpy as np
    # !/usr/bin/python

    from matplotlib import pyplot as plt
    name1 = 'dns_info_for_2018-02-08T21:22:36.802943_News_media_in_the_United_States.txt.pickle'
    name2= 'dns_info_for_2018-02-11T09:44:54.935346_News_media_in_the_United_States.txt.pickle'
    name3 = 'dns_info_for_2018-02-22T19:08:52.872298_News_media_in_the_United_States.txt.pickle'
    name4='dns_info_for_2018-02-23T08:34:54.010634_News_media_in_the_United_States.txt.pickle'
    name5= 'dns_info_for_2018-02-24T01:00:36.066616_News_media_in_the_United_States.txt.pickle'
    name6 = 'dns_info_for_2018-02-25T01:00:43.736438_News_media_in_the_United_States.txt.pickle'

    name1 = 'dns_info_for_2018-02-22T16:11:48.782538_AlexaTopNewsWebSites.txt.pickle'
    name2= 'dns_info_for_2018-02-22T16:11:48.782538_AlexaTopNewsWebSites.txt.pickle'
    name3 = 'dns_info_for_2018-02-22T16:11:48.782538_AlexaTopNewsWebSites.txt.pickle'
    name4='dns_info_for_2018-02-23T01:00:15.892710_AlexaTopNewsWebSites.txt.pickle'
    name5= 'dns_info_for_2018-02-24T01:00:11.382227_AlexaTopNewsWebSites.txt.pickle'
    name6 = 'dns_info_for_2018-02-26T01:00:20.188453_AlexaTopNewsWebSites.txt.pickle'

    day_1_typos = get_typos_number (name1)
    day_2_typos = get_typos_number(name2)
    day_3_typos = get_typos_number(name3)
    day_4_typos = get_typos_number(name4)
    day_5_typos = get_typos_number(name5)
    day_6_typos = get_typos_number(name6)


    N = 6
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = [day_1_typos,
             day_2_typos,
             day_3_typos, day_4_typos,
             day_5_typos, day_6_typos]
    rects1 = ax.bar(ind, yvals, width, color='#AAB7B8')
    # zvals = [news_same_typos, sport_same_typos, sciece_same_typos, society_same_typos,
    #          adult_same_typos, 7]
    # rects2 = ax.bar(ind + width, zvals, width, color='#999999')
    # kvals = [news_dif_typos, sport_dif_typos, sciece_dif_typos, society_dif_typos,
    #          adult_dif_typos, 7]
    # rects3 = ax.bar(ind + width * 2, kvals, width, color='#17202A')

    ax.set_ylabel('% of using new tlds in reg typos by same entity')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('day1', 'day2','day3', 'day4',
                        'day5', 'day6'))

    # ax.legend((rects1[0]),
    #           ('#found domains', '#registered by same entity', '#registered by different entity'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),
                    ha='center', va='bottom')

    autolabel(rects1)

    plt.show()
    plt.savefig('per_day_tracker.pdf')
    #
    # from matplotlib import dates
    # from datetime import datetime
    # import sys
    #
    # d = []
    # t = []
    # for line in sys.stdin:
    #     dstamp, temp = line.rstrip().split('\t')
    #     d.append(datetime.strptime(dstamp, '%Y-%m-%d-%H-%M'))
    #     t.append(int(temp))
    #
    # days = dates.DayLocator()
    # hours = dates.HourLocator(interval=3)
    # dfmt = dates.DateFormatter('              %b %d')
    #
    # datemin = datetime(2015, 1, 4, 0, 0)
    # datemax = datetime(2015, 1, 11, 23, 59, 59)
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.xaxis.set_major_locator(days)
    # ax.xaxis.set_major_formatter(dfmt)
    # ax.xaxis.set_minor_locator(hours)
    # ax.set_xlim(datemin, datemax)
    # ax.set_ylabel('Temperature (F)')
    # ax.grid(True)
    # ax.plot(d, t, linewidth=2)
    # fig.set_size_inches(8, 4)
    # plt.show()
    # plt.savefig('temperatures.pdf', format='pdf')
    #
    # # Read in the csv file and display some of the basic info
    # sales = pd.read_csv("sample-salesv2.csv", parse_dates=['date'])
    # print "Data types in the file:"
    # print sales.dtypes
    # print "Summary of the input file:"
    # print sales.describe()
    # print "Basic unit price stats:"
    # print sales['unit price'].describe()
    #
    # # Filter the columns down to the ones we need to look at for customer sales
    # customers = sales[['name', 'ext price', 'date']]
    #
    # # Group the customers by name and sum their sales
    # customer_group = customers.groupby('name')
    # sales_totals = customer_group.sum()
    #
    # # Create a basic bar chart for the sales data and show it
    # bar_plot = sales_totals.sort(columns='ext price', ascending=False).plot(kind='bar', legend=None,
    #                                                                         title="Total Sales by Customer")
    # bar_plot.set_xlabel("Customers")
    # bar_plot.set_ylabel("Sales ($)")
    # plt.show()
    #
    # # Do a similar chart but break down by category in stacked bars
    # # Select the appropriate columns and group by name and category
    # customers = sales[['name', 'category', 'ext price', 'date']]
    # category_group = customers.groupby(['name', 'category']).sum()
    #
    # # Plot and show the stacked bar chart
    # stack_bar_plot = category_group.unstack().plot(kind='bar', stacked=True, title="Total Sales by Customer",
    #                                                figsize=(9, 7))
    # stack_bar_plot.set_xlabel("Customers")
    # stack_bar_plot.set_ylabel("Sales")
    # stack_bar_plot.legend(["Total", "Belts", "Shirts", "Shoes"], loc=9, ncol=4)
    # plt.show()
    #
    # # Create a simple histogram of purchase volumes
    # purchase_patterns = sales[['ext price', 'date']]
    # purchase_plot = purchase_patterns['ext price'].hist(bins=20)
    # purchase_plot.set_title("Purchase Patterns")
    # purchase_plot.set_xlabel("Order Amount($)")
    # purchase_plot.set_ylabel("Number of orders")
    # plt.show()
    #
    # # Create a line chart showing purchases by month
    # purchase_patterns = purchase_patterns.set_index('date')
    # month_plot = purchase_patterns.resample('M', how=sum).plot(title="Total Sales by Month", legend=None)
    # fig = month_plot.get_figure()
    #
    # # Show the image, then save it
    # plt.show()
    # fig.savefig("total-sales.png")
    #
    # import matplotlib.pyplot as plt

#     from matplotlib import pyplot as plt
#     4
#     from matplotlib import dates
#     5
#     from datetime import datetime
#     6
#     import sys
#     7
#     8
#     d = []
#     9
#     t = []
#
#
# 10
# for line in sys.stdin:
#     11
#     dstamp, temp = line.rstrip().split('\t')
# 12
# d.append(datetime.strptime(dstamp, '%Y-%m-%d-%H-%M'))
# 13
# t.append(int(temp))
# 14
# 15
# days = dates.DayLocator()
# 16
# hours = dates.HourLocator(interval=3)
# 17
# dfmt = dates.DateFormatter('              %b %d')
# 18
# 19
# datemin = datetime(2015, 1, 4, 0, 0)
# 20
# datemax = datetime(2015, 1, 11, 23, 59, 59)
# 21
# 22
# fig = plt.figure()
# 23
# ax = fig.add_subplot(111)
# 24
# ax.xaxis.set_major_locator(days)
# 25
# ax.xaxis.set_major_formatter(dfmt)
# 26
# ax.xaxis.set_minor_locator(hours)
# 27
# ax.set_xlim(datemin, datemax)
# 28
# ax.set_ylabel('Temperature (F)')
# 29
# ax.grid(True)
# 30
# ax.plot(d, t, linewidth=2)
# 31
# fig.set_size_inches(8, 4)
# 32
# 33
# plt.savefig('temperatures.pdf', format='pdf')

    #
    # from datetime import datetime
    # import matplotlib.pyplot as plt
    # import matplotlib.dates as mdates
    # x = []
    # y = []
    # t = []
    # fig = plt.figure()
    # rect = fig.patch
    # rect.set_facecolor('#31312e')
    # readFile = open('data.txt', 'r')
    # sepFile = readFile.read().split('\n')
    # readFile.close()
    # for idx, plotPair in enumerate(sepFile):
    #     if plotPair in '. ':
    #         # skip. or space
    #         continue
    #     if idx > 1:  # to skip the first line
    #         xAndY = plotPair.split(',')
    #         time_string = xAndY[0]
    #         time_string1 = datetime.strptime(time_string, '%d/%m/%Y %H:%M')
    #         t.append(time_string1)
    #         y.append(float(xAndY[1]))
    # ax1 = fig.add_subplot(1, 1, 1, axisbg='white')
    # ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
    # ax1.plot(t, y, 'c', linewidth=3.3)
    # plt.title('IRRADIANCE')
    # plt.xlabel('TIME')
    # fig.autofmt_xdate(rotation=45)
    # fig.tight_layout()
    # plt.show()
#https://www.daniweb.com/programming/software-development/threads/482270/plot-date-and-time-xaxis-versus-a-value-yaxis-using-data-from-txt-file
    # this is my
    # txt
    # file:
    #
    # TimeStamp, Irradiance
    # 21 / 7 / 2014
    # 0:00, 0.66
    # 21 / 7 / 2014
    # 0:00, 0.71
    # 21 / 7 / 2014
    # 0:00, 0.65
    # 21 / 7 / 2014
    # 0:00, 0.67
    # 21 / 7 / 2014
    # 0:01, 0.58
    # 21 / 7 / 2014
    # 0:01, 0.54
    # 21 / 7 / 2014
    # 0:01, 0.63
    # 21 / 7 / 2014
    # 0:01, 0.65
    # 21 / 7 / 2014
    # 0:02, 0.64
    # 21 / 7 / 2014
    # 0:02, 0.63
    # 21 / 7 / 2014
    # 0:02, 0.63
    # 21 / 7 / 2014
    # 0:02, 0.64
    # .
    # .
    # .
    # .
    # 22 / 7 / 2014
    # 23:57, 0.53
    # 22 / 7 / 2014
    # 23:58, 0.69
    # 22 / 7 / 2014
    # 23:58, 0.61
    # 22 / 7 / 2014
    # 23:58, 0.65
    # 22 / 7 / 2014
    # 23:58, 0.59
    # 22 / 7 / 2014
    # 23:59, 0.63
    # 22 / 7 / 2014
    # 23:59, 0.67
    # 22 / 7 / 2014
    # 23:59, 0.68
    # 22 / 7 / 2014
    # 23:59, 0.58
    #

if __name__ == "__main__":
    #name = sys.argv[1]
    name_of_same_dif_file_top_50_a_few_model = 'same_dif_typos_for_2018-02-18T10:20:44.389545_dns_info_for_2018-02-17T01:00:44.804056_AlexaTopNewsWebSites.txt.pickle'
    name_top_50_all_models = 'same_dif_typos_for_2018-02-13T17:59:18.613430_50news_saved_dns.pickle'
    name2 = 'same_dif_typos_for_2018-02-13T17:01:09.463421_dns_info_for_2018-02-08T10:00:11.792562_AlexaTopNewsWebSites.txt.pickle'
    name3 = 'same_dif_typos_for_2018-02-12T13:27:12.440132_dns_info_for_2018-02-11T20:48:42.069677_AlexaTopNewsWebSites.txt.pickle'#wrong
    name4 = 'same_dif_typos_for_2018-02-06T19:01:55.822195_top_news_saved_dns.pickle'
    name5='same_dif_typos_for_2018-02-18T10:20:44.389545_dns_info_for_2018-02-17T01:00:44.804056_AlexaTopNewsWebSites.txt.pickle'
    name5_2 = 'same_dif_typos_for_2018-02-21T15:33:08.196756_dns_info_for_2018-02-21T01:00:10.958060_AlexaTopNewsWebSites.txt.pickle'

    # the most complete file is this
    name5_3 = 'same_dif_typos_for_2018-02-18T19:52:48.579219_dns_info_for_2018-02-06T19:40:45.449529_AlexaTopNewsWebSites.txt.pickle'
    name5_4= 'same_dif_typos_for_2018-02-22T16:00:58.337402_dns_info_for_2018-02-18T10:47:48.853711_AlexaTopNewsWebSites.txt.pickle'
    media_three_models = 'same_dif_typos_for_2018-02-04T13:09:50.633186_new_version_sixth_week_three_model.pickle'
    targeted_domains(media_three_models)
    targeted_domains2('new_version_sixth_week_three_model.pickle')


    #this function use same dif file and plot used typo generation models
    #Plotting_per_model(name5)
    #Plotting_per_model(name5_2)
    #Plotting_per_model(name5_4)


    # the most complete file is this
    #Plotting_per_model(name5_3)



    # For each media web site
    #Plotting_per_model_per_site(media_three_models)

    name = 'dns_info_for_2018-02-17T01:00:44.804056_AlexaTopNewsWebSites.txt.pickle'
    name_3= 'dns_info_for_2018-02-06T19:40:45.449529_AlexaTopNewsWebSites.txt.pickle'
    domain_lists(name_3)
    #this function plot the most used domain name for email address  in dns records
    #email_plotter(name, name5)

    #the most complete files
    #email_plotter(name_3, name5_3)

    #this function plot most top registrar names in dns_info file
    #Owner_Tracker(name)
    # the most complete file
    #Owner_Tracker(name_3)


    #this function plot most used tld in typos
    #new_tld_Tracker(name5)
    # most complete file
    #new_tld_Tracker(name5_3)




    #response_codes_for_responce_code_same_dif_2018-02-18.pickle
    file_for_responce_code_all= 'response_codes_for_responce_code_same_dif_2018-02-18.pickle'
    #response_code_plotter(file_for_responce_code_all)



    #this function track the typo registration per day
    per_day()







    #               you can use below functions for plotting
    # Plotting_per_model(name5)
    # draw plot for all categories
    #per_news_media_top()
    #per_cat()


    #check the owner of domains
    #owner()


    #extract registered, by same antity and different entity in found domins
    #registeration_plotter(name5)


    # extract response code for found domains
    #response_code_plotter(name5)

    # extract the expnsion/ommision and other typo generation models used in found domains
    #typo_generation_model_stat(name5)


    #a function for extracting email domain from dns files
    #email_plotter()
    #email_tracker(name)

    #if name =='all':
        #print 'please merge the stats to gheter'




