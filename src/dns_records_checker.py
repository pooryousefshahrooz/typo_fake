import datetime
import numpy as np
import matplotlib.pyplot as plt
import pickle
import numpy as np
import matplotlib.pyplot as plt
import glob, os
from typo_generation_models import *
from OwnerChecker import *
import sys
import socket

file_name = 'file_name'
def get_news_data():
    objects = []
    same_owners= 0
    dif_owners = 0
    with (open("news_dns.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break

    with (open("50news_newtld.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break

    print '----------------the last try'

    with (open("50news_newtld.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    return objects

def get_sport_data():
    same_owners= 0
    dif_owners = 0
    print '-------------------------result for alexa top 50 sport domain names by general typos,!!!!!!FINISHED!!!!!-------------------------'
    objects = []
    with (open("sport_dns.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break

    # try for zero domains
    print 'and for thoes domain we got zero'
    with (open("sport_zero.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    return objects

def get_sience_data():
    same_owners= 0
    dif_owners = 0
    print '-------------------------result for alexa top 50 science domain names by new tlds typos-------------------------'
    objects = []
    with (open("science_dns.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    with (open("science_dns_second_round.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break

    return objects

def get_shopping_data():
    same_owners= 0
    dif_owners = 0
    print '-------------------------result for alexa top 50 shopping domain names typos by new tlds-------------------------'
    objects = []
    with (open("shopping_dns.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    return objects

def get_adult_data():
    same_owners= 0
    dif_owners = 0
    objects = []
    with (open("ad_dns.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    return objects
def get_society_data():
    same_owners= 0
    dif_owners = 0
    print '-------------------------result for alexa top 50 society domain names by general typos-------------------------'
    objects = []
    with (open("society_dns.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break

    print 'Second Round for sociery'

    with (open("society_dns_second_round.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break

    print 'third'
    with (open("society_dns_third_Round.pickle", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    return objects

def registeration_plotter():
    print 'plotted'
    same_news,dif_news = get_news_same_dif()


    same_sport,dif_sport = get_sport_same_dif()


    same_science, dif_science = get_sience_same_dif()


    same_shopping, dif_shopping = get_shopping_same_dif()


    same_adult, dif_adult = get_adult_same_dif()


    same_society, dif_society = get_society_same_dif()

    print 'same for news',same_news
    print 'dif for news',dif_news
    print '------------------'
    print 'same for sport',same_sport
    print 'dif for sport',dif_sport
    print '------------------'

    print 'same for science',same_science
    print 'dif for science',dif_science
    print '------------------'

    print 'same for shopping',same_shopping
    print 'dif for shopping',dif_shopping
    print '------------------'

    print 'same for adult', same_adult
    print 'dif for adult', dif_adult
    print '------------------'

    print 'same for society',same_society
    print 'dif for society',dif_society

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


def registeration_plotter():
    print 'plotted'
    same_news,dif_news = get_news_same_dif()


    same_sport,dif_sport = get_sport_same_dif()


    same_science, dif_science = get_sience_same_dif()


    same_shopping, dif_shopping = get_shopping_same_dif()


    same_adult, dif_adult = get_adult_same_dif()


    same_society, dif_society = get_society_same_dif()

    print 'same for news',same_news
    print 'dif for news',dif_news
    print '------------------'
    print 'same for sport',same_sport
    print 'dif for sport',dif_sport
    print '------------------'

    print 'same for science',same_science
    print 'dif for science',dif_science
    print '------------------'

    print 'same for shopping',same_shopping
    print 'dif for shopping',dif_shopping
    print '------------------'

    print 'same for adult', same_adult
    print 'dif for adult', dif_adult
    print '------------------'

    print 'same for society',same_society
    print 'dif for society',dif_society

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

def get_data_saved(file_name):
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

    print 'all'

def is_valid(charnum):
    return ((charnum >= ord('0') and charnum <= ord('9')) or
            (charnum >= ord('a') and charnum <= ord('z')) or
            (charnum >= ord('A') and charnum <= ord('Z')) or
             charnum == ord('-'))


def typo_generation_model_stat():
    found_models = {}
    found_models['Original*'] = 0
    found_models['Replacement'] = 0
    found_models['Addition'] = 0
    found_models['Transposition'] = 0
    found_models['Vowel-swap'] = 0
    found_models['Omission'] = 0
    found_models['Repetition'] = 0
    found_models['Transposition'] = 0
    models = get_generation_model_news()
    found_models['Original*'] = found_models['Original*']+models['Original*']


    print found_models


        # for typo in typos_dns_info:
        #     print typo
        #     for info in typos_dns_info[typo]:
        #         print info
        #
        #     #print item
    import pdb
    pdb.set_trace()

def get_response_code():
    same_ok = 0
    same_bad = 0
    same_redirect = 0
    dif_ok = 0
    dif_bad = 0
    dif_redirect = 0
    response_codes = {}
    objects = get_news_data()
    objects.extend(get_society_data())
    objects.extend(get_adult_data())
    objects.extend(get_shopping_data())
    objects.extend(get_sience_data())
    objects.extend(get_sport_data())
    for item in objects:
        same_ok = same_ok+item['ok_response_for_same_owner_typos']
        same_bad = same_bad + item['bad_response_for_same_owner_typos']
        same_redirect = same_redirect + item['redirec_response_for_same_owner_typos']
        dif_ok = dif_ok+item['ok_response_for_dif_owner_typos']
        dif_bad = dif_bad + item['bad_response_for_dif_owner_typos']
        dif_redirect = dif_redirect + item['redirec_response_for_dif_owner_typos']

    response_codes['same_ok'] = same_ok
    response_codes['same_bad'] = same_bad
    response_codes['same_redirect'] = same_redirect
    response_codes['dif_ok'] = dif_ok
    response_codes['dif_bad'] = dif_bad
    response_codes['dif_redirect'] = dif_redirect
    return response_codes
def usage():
    print "Usage:"
    print "Plotter.py category"
    print ""
    print "example:"
    print "Plotter.py news"
    print ""
def response_code_plotter():
    response_codes = get_response_code()
    import matplotlib.pyplot as plt
    colors = ['gray', 'white', 'silver']
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Ok_response_same', 'redirected_same', 'bad_request_same'
    sizes = [response_codes['same_ok'], response_codes['same_redirect'], response_codes['same_bad']]
    explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    #plt.show()

    labels = 'Ok_response_code_dif', 'redirected_dif', 'bad_request_dif'
    sizes = [response_codes['dif_ok'], response_codes['dif_redirect'], response_codes['dif_bad']]
    explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def worker(targetwebsite,typo_infos,file_name,typoshandler):
    typos = []
    if targetwebsite != 'fakedomain.com':
        info = typoshandler.check_owner(targetwebsite, typo_infos)
        #print info
        pause = random.random()
        #logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        typoshandler.save(info,file_name)
        #logging.debug('Done')

def owner_checking(name,file_name):
    objects = get_data_saved(name)
    #for item in objects:
        #print item['key']
    remaining = len(objects) % 20
    remaining_domains = objects[-remaining+1:]
    #print len(objects),remaining
    for i in range(remaining):
        new_fake_dns_info = {}
        new_fake_dns_info['key'] = 'fakedomain.com'
        new_fake_dns_info['typos_dns_info'] = {}
        objects.append(new_fake_dns_info)
    #print len(objects)
    # import pdb
    # pdb.set_trace()
    #for item in objects:
        #print item['key']
    #for a in objects:
        #print a['key']
        #print a['typos_dns_info']

    for a, b,c,d,e,f,g,h,l,m,n,p,q,r,s,a1,w1,e1,r1,y1  in zip(*[iter(objects)] * 20):

        typoshandler = TyposHandler()
        t1 = threading.Thread(target=worker, args=(a['key'],a['typos_dns_info'],file_name, typoshandler,))
        t1.start()
        typoshandler = TyposHandler()
        t2 = threading.Thread(target=worker, args=(b['key'], b['typos_dns_info'],file_name,typoshandler,))
        t2.start()

        typoshandler = TyposHandler()
        t3 = threading.Thread(target=worker, args=(c['key'],c['typos_dns_info'],file_name, typoshandler,))
        t3.start()
        typoshandler = TyposHandler()
        t4 = threading.Thread(target=worker, args=(d['key'],d['typos_dns_info'], file_name,typoshandler,))
        t4.start()

        typoshandler = TyposHandler()
        t5 = threading.Thread(target=worker, args=(e['key'],e['typos_dns_info'],file_name, typoshandler,))
        t5.start()

        typoshandler = TyposHandler()
        t6 = threading.Thread(target=worker, args=(f['key'],f['typos_dns_info'],file_name, typoshandler,))
        t6.start()


        typoshandler = TyposHandler()
        t7 = threading.Thread(target=worker, args=(g['key'],g['typos_dns_info'],file_name, typoshandler,))
        t7.start()

        typoshandler = TyposHandler()
        t8 = threading.Thread(target=worker, args=(h['key'],h['typos_dns_info'],file_name, typoshandler,))
        t8.start()



        typoshandler = TyposHandler()
        t9 = threading.Thread(target=worker, args=(l['key'],l['typos_dns_info'],file_name, typoshandler,))
        t9.start()
        typoshandler = TyposHandler()
        t10 = threading.Thread(target=worker, args=(m['key'],m['typos_dns_info'], file_name,typoshandler,))
        t10.start()

        typoshandler = TyposHandler()
        t11 = threading.Thread(target=worker, args=(n['key'],n['typos_dns_info'],file_name, typoshandler,))
        t11.start()

        typoshandler = TyposHandler()
        t12 = threading.Thread(target=worker, args=(p['key'],p['typos_dns_info'],file_name, typoshandler,))
        t12.start()


        typoshandler = TyposHandler()
        t13 = threading.Thread(target=worker, args=(q['key'],q['typos_dns_info'],file_name, typoshandler,))
        t13.start()

        typoshandler = TyposHandler()
        t14 = threading.Thread(target=worker, args=(r['key'],r['typos_dns_info'],file_name, typoshandler,))
        t14.start()

        typoshandler = TyposHandler()
        t15 = threading.Thread(target=worker, args=(s['key'],s['typos_dns_info'],file_name, typoshandler,))
        t15.start()


        typoshandler = TyposHandler()
        t16 = threading.Thread(target=worker, args=(a1['key'],a1['typos_dns_info'],file_name, typoshandler,))
        t16.start()


        typoshandler = TyposHandler()
        t17 = threading.Thread(target=worker, args=(w1['key'],w1['typos_dns_info'],file_name, typoshandler,))
        t17.start()


        typoshandler = TyposHandler()
        t18 = threading.Thread(target=worker, args=(e1['key'],e1['typos_dns_info'],file_name, typoshandler,))
        t18.start()


        typoshandler = TyposHandler()
        t19 = threading.Thread(target=worker, args=(r1['key'],r1['typos_dns_info'],file_name, typoshandler,))
        t19.start()


        typoshandler = TyposHandler()
        t20 = threading.Thread(target=worker, args=(y1['key'],y1['typos_dns_info'],file_name, typoshandler,))
        t20.start()

        logging.debug('Waiting for worker threads')
        main_thread = threading.currentThread()
        for t in threading.enumerate():
            if t is not main_thread:
                t.join()

if __name__ == "__main__":
    name = sys.argv[1]
    now = datetime.datetime.now()

    owner_checking(name,now.isoformat()+'_'+name)





