import random

char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&()*_/?"

while 1:
    
    password_leng=int(input("What should be the length of you passward: "))
    password_num=int(input("How many password do you want: "))
    for x in range(0,password_num):
        password=""
        for x in range(0,password_leng):
            password_char= random.choice(char)
            password     = password + password_char
        print("Here is your password: ", password )
