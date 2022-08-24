from random import choice
import string

string_with_all_characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

new_password = ""
password_lenght = int(input('How many characters do you want for your password: '))

i = 0
while i <= password_lenght:
    new_password += choice(string_with_all_characters)
    i += 1
print(f'Your new password is: {new_password}')