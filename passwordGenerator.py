# Generator haseł.
# Program generuje dla użytkownika hasło łatwe do zapamiętania,
# albo generuje zupełnie randomowy ciąg znaków.

import random
# Powitanie użytkownika i wyjaśnienie działania programu.
print("""
Welcome in generating passwords program. Generator will generate minimum 6 characters
password for You, which can be made from semi random string of characters, or personalized,
easy to remebmer, but hard to break password.
""")


# Funkcja produkująca hasło składające się z randomowego ciagu znaków o podanej
# przez użytownika długości, jednak minimum 6 znaków.
def total_random_password(num_char):
    password = ''
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(0, num_char):
        lett = random.choice(alph)
        coin = random.randrange(1,3)
        if coin == 1:
            password += lett.lower()
        elif coin == 2:
            password += lett.upper()
    return password

# Funcja produkująca hasło składające się z pierwszych znaków podanego przez
# użytkownika zdania.
def personal_password(sentence):
    pass_list = sentence.split()
    password = ''
    for element in pass_list:
        coin = random.randrange(1,3)
        if element[0].lower() == 's' and coin == 1:
            password += '$'
        elif element[0].lower() == 'a' and coin == 1:
            password += '@'
        elif element[0].lower() == 'i' and coin == 1:
            password += '!'
        elif coin == 1:
            password += element[0].lower()
        elif coin == 2:
            password += element[0].upper()
    return password

# Pobranie od użytkownika jego wyboru co do opcji.
choice = input("""
Would You like totally random password - R
Or personalized password - P""")
choice = choice.lower()

if choice.lower() == 'r':
    num_char = int(input("How long would you like your password to be?(6-16): "))
    while num_char < 6 or num_char > 16:
        num_char = int(input("Password can be between 6 and 16 characters."))
    user_password = total_random_password(num_char)
elif choice.lower() == 'p':
    sentence = input("""
    
Write a sentence, that you can easily remember, program will generate from it unique password,
some characters may be replaced with visually similliar characters, and size of letters will be randomize.
Sentence must contain at least 6 words and at least 1 digit.
""")
    cipher = range(0,10)
    while len(sentence.split()) < 6:
        sentence = input("""
Sentence should be at least 6 words 
long and have at least 1 digit.

""")
    
    if any(i.isdigit() for i in sentence) != True:
        sentence = list(sentence)
        sentence.append(str(random.choice(range(0,10))))
        sentence = " ".join(sentence)
    user_password = personal_password(sentence)


# Faza końcowa programu, w której użytkownik dostaje swoje hasło oraz poradę co
# do jego rozpowszechniania.
print("""
Your password is:

{}


Remember your password, and NEVER EVER pass it to anyone.""".format(user_password))

input("Press ENTER to exit program.")
