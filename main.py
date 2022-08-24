from calendar import c
from random import choice, randint
from re import A
import string
from this import d

new_password = ""
password_lenght = int(input('How many characters do you want for your passwor, must be more than 4: ')) 
while password_lenght < 4:
        password_lenght = int(input('How many characters do you want for your password, must be more than 4: '))
        

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

a = randint(1, (password_lenght - 3))
print(a)
if 0 < a and a < password_lenght: 
    b = randint(1, (password_lenght - a - 2))
    print(b)
    if 0 < a + b  and a + b < password_lenght:
        c = randint(1, (password_lenght - a- b - 1))
        print(c)
        if 0 < a + b + c and a + b + c < password_lenght:
            d = randint(1, (password_lenght - a - b - c))
            print(f'koniec{d}')
        else:
            password_lenght = a + b + c
            print(password_lenght)
    else:
        password_lenght = a

# i = 0
# while i <= password_lenght:
#     new_password += choice(string_with_all_characters)
#     i += 1
# print(f'Your new password is: {new_password}')