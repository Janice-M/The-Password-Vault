import random
import string

global userList
class User:
    def passGen(size = 69, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        gen = ''.join(random.choice(char) for _ in range(size))
        return gen
        
    userList={}
    print('Rafiki, welcome to The Password Vault')
    
    print("Rafiki,select a number")
    print("1. Login ")
    print("2. Sign up ")
    option_selected = int(input())
    
    if option_selected == 1:
        print( "Welcome consistent rafiki")
        print("Kindly, enter your username:")
        loginUsername= input()
        print("Kindly enter your password")
        loginPassword= input()
        
    else:
        print ("Welcome new rafiki")
        print(" Create your username:")
        newUsername= input()
        print ("Rafiki, select a number")
        print("1. Create your own password")
        print("2. Generate password ")
        newPassword= int(input())
        if newPassword == 1: 
            print("Enter password below")
            input()
        elif newPassword == 2:
            generator = passGen()
            print(generator)
        