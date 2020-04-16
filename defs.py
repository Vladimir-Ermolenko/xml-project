import xml.etree.ElementTree as et


def menu():
    opt = int(input(lc.menu))
    print()

    return opt


def lang():
    lng = input('Choose the language:'
                '\n 1. English'
                '\n 2. Russian'
                '\n')
    print()
    if lng == '1' or lng.lower() == 'english':
        return 1
    elif lng == '2' or lng.lower() == 'russian':
        return 2
    else:
        print('Input error, try again' + '\n')
        return lang()


if lang() == 1:
    import loceng as lc
else:
    import locru as lc


# the func that parses the xml file and returns a dict with ids as keys and all other props as values
# 'try' + 'while True' are needed not to count the number of books
def parse(file):
    bk_dct = {}
    tree = et.parse(file)
    root = tree.getroot()

    bk = 0
    try:
        while True:
            bk_dct[root[bk].attrib['id']] = []
            for pr in range(9):
                bk_dct[root[bk].attrib['id']].append(str(root[bk][pr].text).replace('\n', ''))
            bk += 1
    except IndexError:
        pass

    return bk_dct


def id_search(dct):
    nl = lc.id_search_lst
    id_ = input(lc.id_search_inp)

    for pr in range(len(dct[id_])):
        print(nl[pr] + dct[id_][pr])
    print()


def isbn_search(dct):
    dct1 = {}

    # adds an id to the list and deletes
    for id_ in dct:
        dct[id_].insert(0, id_)

    # makes the ISBN the key and deletes it from the value list
    for id_1 in dct:
        dct1[dct[id_1][1]] = dct[id_1]
        dct[id_1].pop(2)

    # prints the result
    nl = lc.isbn_search_lst
    isbn = input(lc.isbn_search_inp).replace('-', '')

    for pr in range(len(dct1[isbn])):
        print(nl[pr] + dct1[isbn][pr])
    print()


def bk_qt(dct):
    bk_num = 0
    year = input(lc.bk_qt_inp)

    for id_ in dct:
        if dct[id_][-3] == year:
            bk_num += 1

    print(lc.bk_qt_prt.format(year) + str(bk_num))
    print()


def avg_price(dct):
    pub_st = set()
    fl_dct = {}

    for id_ in dct:
        pub_st.add(dct[id_][4])

    pub_lst = list(pub_st)

    for pub in range(len(pub_lst)):
        bk_num = 0
        bk_pr = 0
        for id_ in dct:
            if dct[id_][4] == pub_lst[pub]:
                bk_num += 1
                bk_pr += float(dct[id_][-1])

        fl_dct[pub_lst[pub]] = bk_pr / bk_num

    print(lc.avg_price)
    for pub1 in fl_dct:
        print(pub1 + ': ' + str(round(fl_dct[pub1], 2)))
    print()


def m_exp(dct):
    pub = input(lc.m_exp_pub)
    year = input(lc.m_exp_year)
    print()
    fl_dct = {}
    dct1 = {}

    for id_ in dct:
        dct[id_].insert(0, id_)

    for id_1 in dct:
        if dct[id_1][5].lower() == pub.lower():
            if dct[id_1][-3] == year:
                fl_dct[dct[id_1][4]] = float(dct[id_1][-1])

    for id_2 in dct:
        dct1[dct[id_2][4]] = dct[id_2]
        dct1[dct[id_2][4]].pop(7)
        dct1[dct[id_2][4]].pop(5)

    hp = sorted(list(fl_dct.values()), reverse=True)[0]
    bn = []
    for bk in fl_dct:
        if fl_dct[bk] == hp:
            bn.append(bk)

    nl = lc.m_exp_lst
    for id_3 in dct1:
        if id_3 in bn:
            print(lc.m_exp_prt.format(pub, year))
            for pr in range(len(dct1[id_3])):
                print(nl[pr] + dct1[id_3][pr])
    print()
