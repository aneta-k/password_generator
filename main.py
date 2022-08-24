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

bucket_of_variables = (lowercase, uppercase, digits, punctuation)

lenght_1 = randint(1, (password_lenght - 3))
print(lenght_1)

lenght_2 = randint(1, (password_lenght - lenght_1 - 2))
print(lenght_2)

lenght_3 = randint(1, (password_lenght - lenght_1 - lenght_2 - 1))
print(lenght_3)

lenght_4 = password_lenght - lenght_1 - lenght_2 - lenght_3
print(f'koniec{lenght_4}')

variable_1 = choice(bucket_of_variables)

print(variable_1) 
# i = 0
# while i <= password_lenght:
#     new_password += choice(string_with_all_characters)
#     i += 1
# print(f'Your new password is: {new_password}')