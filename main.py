"""
projekt_1.py: první projekt do Engeto Online Python Akademie
Kurz 'Datový analytik s Pythonem'

author: Jana Zamachajeva
email: janazamachajeva@seznam.cz
"""
#ZADANI

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

"""
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
"""
# RESENI

# prevedu tabulku do slovniku reg_users:
reg_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
    }
# vyzadam jmeno a heslo - lze take pomoci fce input(), pro zkraceni je tato 
# moznost zakomentovana
# username = input('Zadej uzivatelske jmeno: ')
# password = input('Zadej heslo: ')
username = 'bob'
password = '123'

# kontroluji jestli je uzivatel registrovany
oddelovac = '-'*60
print(f'username:{username} \npassword:{password}')
print(oddelovac)
if username in reg_users.keys() and password in reg_users.values():
    print(f'Welcome to the app, {username} \nWe have 3 texts to be analysed.')
else:
    print('Unregistered user, terminating the program')
print(oddelovac)

# uzivatel si vybere mezi 3 texty ulozenymi v promenne TEXTS
number = input('Print a number btw. 1 and 3 to select: ')
if not number.isdigit():
    print('Wrong input, terminating the program')
else:
    if 1 <= int(number) <= 3:
        # uprava vstupnich dat, definice promennych
        text = TEXTS[int(number) - 1].split()
        result = {
                'words' : 0,
                'titlecase_words': 0,
                'uppercase_words': 0,
                'lowercase_words': 0,
                'numeric_strings': 0,
                'sum' : 0
                }
        sum_count = 0
        word_number = 0
        # analyza textu 1: statistiky s pocty slov
        for word in text:
            if word:
                result['words'] += 1
                if word.istitle():
                    result['titlecase_words'] += 1
                elif word.isupper():
                    result['uppercase_words'] += 1
                elif word.islower():
                    result['lowercase_words'] += 1
                elif word.isnumeric():
                    result['numeric_strings'] += 1
                    sum_count += int(word)
                    result['sum'] = sum_count
                else:
                    print(f'Neznam slovo \'{word}\'')
        print(f'There are {result['words']} words in the selected text.')   
        print(f'There are {result["titlecase_words"]} titlecase words.')
        print(f'There are {result['uppercase_words']} uppercase words.')
        print(f'There are {result['lowercase_words']} lowercase words.')
        print(f'There are {result['numeric_strings']} numeric strings.')
        print(f'The sum of all the numbers is {result['sum']}.')
        # analyza textu 2: sloupcovy graf s delkami slov
        print(oddelovac, 'LEN|\tOCCURENCES\t|LETTERS', oddelovac, sep='\n')
        for word in text:
            letters = 0
            word_number += 1
            if word:
                for letter in word:
                    letters += 1
                if word_number <10:
                    print('', word_number, f'|{'*'*letters}\t'.expandtabs(20), f'|{str(letters).rjust(0)}')
                else:
                    print(word_number, f'|{'*'*letters}\t'.expandtabs(20), f'|{str(letters).rjust(0)}')
    else:
        print('Wrong number, terminating the program')
