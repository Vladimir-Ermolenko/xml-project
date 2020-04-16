
def lang():
    lng = input('Choose the language:'
                '\n 1. English'
                '\n 2. Russian'
                '\n')
    if lng == '1' or lng.lower == 'english':
        return 1
    elif lng == '2' or lng.lower == 'russian':
        return 2
    else:
        print('Input error, try again' + '\n')
        return lang()

