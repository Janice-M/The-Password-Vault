import random
import string

global userList
class User:
    def passGen(size = 69, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        gen = ''.join(random.choice(char) for _ in range(size))
        return gen
    """ The above function helps generate passwords using .random() """
    userList=[]
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
        """ The above code provides a login method for users of the The Password Vault """
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
            newPassword = input()
            userList.append([newUsername, newPassword ])
        elif newPassword == 2:
            generator = passGen()
            print(generator)
            userList.append([newUsername, generator ])
        print(userList)
        """ the elif option is used as it can take in arguements for users who would like to generate passwords """