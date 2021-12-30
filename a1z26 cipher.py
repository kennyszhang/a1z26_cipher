#a1z26 cipher by kenny zhang

def main():
    menu = 'a1z26 cipher menu'
    print(menu)
    print('-'*len(menu))
    print('[1] cipher a message\n[2] decipher a message\n[3] quit')
    option = input('\nenter a menu option and ENTER: ')
    if option == '1':
        cipher()
    elif option == '2':
        decipher()
    else:
        quit()

def cipher():
    inp = input('\nenter a message: ')
    print('\n\ninput:  ', inp)
    inp = inp.lower()
    inp = inp.replace(' ','')
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for x in inp:
        if not x.isalpha():
            continue
        else:
            result += str(alphabet.find(x) + 1)
            result += ' '
    print('output: ', result)
    print('\n\n')
    main()

def decipher():
    inp = input('\nenter a message: ')
    print('\n\ninput:  ', inp)
    result = ''
    for x in inp.split(' '):
        result += chr(int(x) + 96)
    print('output: ', result)
    print('\n\n')
    main()    

main()