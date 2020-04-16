
from defs import menu, parse, id_search, isbn_search, bk_qt, avg_price, m_exp

opt = 0
while opt != 6:
    bk_dict = parse('books.xml')
    opt = menu()
    if opt == 1:
        id_search(bk_dict)
    elif opt == 2:
        isbn_search(bk_dict)
    elif opt == 3:
        bk_qt(bk_dict)
    elif opt == 4:
        avg_price(bk_dict)
    elif opt == 5:
        m_exp(bk_dict)
