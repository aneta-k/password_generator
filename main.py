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
password_lenght -= lenght_1
lenght_2 = randint(1, (password_lenght - 2))
password_lenght -= lenght_2
lenght_3 = randint(1, (password_lenght - 1))
lenght_4 = password_lenght - lenght_3      

variable_1 = choice(bucket_of_variables)
bucket_of_variables.remove(variable_1)
variable_2 = choice(bucket_of_variables)
bucket_of_variables.remove(variable_2)
variable_3 = choice(bucket_of_variables)
bucket_of_variables.remove(variable_3)
variable_4 = bucket_of_variables[0]

new_password_1 = sample(variable_1, lenght_1)
new_password_2 = sample(variable_2, lenght_2)
new_password_3 = sample(variable_3, lenght_3)
new_password_4 = sample(variable_4, lenght_4)

new_password = new_password_1 + new_password_2 + new_password_3 + new_password_4
shuffle(new_password)
new_password = "".join(new_password)
print(f'Your new password iz: {new_password}')
