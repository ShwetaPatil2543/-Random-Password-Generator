import random
import string

length =int(input("enter length:"))

chars=string.ascii_letters
chars+=string.digits
chars+=string.punctuation

#Begin the password as an empty string

password=""

for i in range(length):
    password+=random.choice(chars)
    
password=' '.join([random.choice(chars)for i in range(length)])

#Output the randomly generated password
print("Your random password is:",password)               
