import pickle


def get_data(name):
    objects = []
    with (open('../data/'+name, "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    return objects

def return_typos_from_pure(name1):
    objects = get_data(name1)
    typos= []
    for item in objects:
        typos_info = item['typos_dns_info']
        for typo in typos_info:
            typos.append(typo)
    return typos