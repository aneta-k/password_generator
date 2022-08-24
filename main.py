from random import choice, randint
import string

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

b = randint(1, (password_lenght - a - 2))
print(b)

c = randint(1, (password_lenght - a- b - 1))
print(c)

d = password_lenght - a - b - c
print(f'koniec{d}')

# i = 0
# while i <= password_lenght:
#     new_password += choice(string_with_all_characters)
#     i += 1
# print(f'Your new password is: {new_password}')