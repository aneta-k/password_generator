from random import choice, randint, sample, shuffle
import string       

new_password = ""
password_lenght = int(input('How many characters do you want for your passwor, must be more than 4: ')) 
while password_lenght < 4:
        password_lenght = int(input('How many characters do you want for your password, must be more than 4: '))
        

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

bucket_of_variables = [lowercase, uppercase, digits, punctuation]

lenght_1 = randint(1, (password_lenght - 3))
print(lenght_1)
password_lenght -= lenght_1
lenght_2 = randint(1, (password_lenght - 2))
print(lenght_2)
password_lenght -= lenght_2
lenght_3 = randint(1, (password_lenght - 1))
print(lenght_3)
lenght_4 = password_lenght - lenght_3      
print(f'koniec{lenght_4}')

variable_1 = choice(bucket_of_variables)
print(variable_1)
bucket_of_variables.remove(variable_1)
variable_2 = choice(bucket_of_variables)
print(variable_2)
bucket_of_variables.remove(variable_2)
variable_3 = choice(bucket_of_variables)
print(variable_3)
bucket_of_variables.remove(variable_3)
variable_4 = bucket_of_variables[0]
print(variable_4)

new_password_1 = sample(variable_1, lenght_1)
print(new_password_1)
new_password_2 = sample(variable_2, lenght_2)
print(new_password_2)
new_password_3 = sample(variable_3, lenght_3)
print(new_password_3)
new_password_4 = sample(variable_4, lenght_4)
print(new_password_4)

new_password = new_password_1 + new_password_2 + new_password_3 + new_password_4
print(new_password)
shuffle(new_password)
print(new_password)
new_password = "".join(new_password)
print(new_password)
