from random import choice, randint, sample, shuffle
import string
import pyperclip

password_length = int(input('How many characters do you want for your passwor, must be more than 4: ')) 
while password_length < 4:
        password_length = int(input('How many characters do you want for your password, must be more than 4: '))

bucket_of_variables = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

# creating 4 random lengths variables
length_1 = randint(1, (password_length - 3))
password_length -= length_1
length_2 = randint(1, (password_length - 2))
password_length -= length_2
length_3 = randint(1, (password_length - 1))
length_4 = password_length - length_3      

# matching lenghts with 4 different types of characters
variable_1 = choice(bucket_of_variables)
bucket_of_variables.remove(variable_1)
variable_2 = choice(bucket_of_variables)
bucket_of_variables.remove(variable_2)
variable_3 = choice(bucket_of_variables)
bucket_of_variables.remove(variable_3)
variable_4 = bucket_of_variables[0]

# creating chunks of password
new_password_1 = sample(variable_1, length_1)
new_password_2 = sample(variable_2, length_2)
new_password_3 = sample(variable_3, length_3)
new_password_4 = sample(variable_4, length_4)

new_password = new_password_1 + new_password_2 + new_password_3 + new_password_4
shuffle(new_password)
new_password = "".join(new_password)
pyperclip.copy(new_password)
print(f'Your new password is: {new_password}')
