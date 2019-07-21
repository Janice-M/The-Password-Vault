import random
import string

global userList
class User:
    def __init__(self,loginUsername,loginPassword):
        self.loginUsername =loginUsername
        self.loginPassword =loginPassword 
    
    def passGen(size = 8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
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
            userList.append([newUsername, generator ])
        
        """ the elif option is used as it can take in arguements for users who would like to generate passwords """
        
        print("Your Password Vault has been created successfully rafiki, " +newUsername)
        print ("Please do login now")
        print( "Welcome consistent rafiki")
        print("Kindly, enter your username:")
        loginUsername= input()
        print("Kindly enter your password")
        loginPassword= input()
        
class Credential:

    """ this class holds the different credentials the users need to be kept in the Password Vault """

    apps=[]
    """ apps list contains the apps and passwords that the user wants stored in the password vault """
    vaultUser= []
    """  vaultUser list contains the credentials created in the user class """
    def __init__(self,loginUsername , loginPassword ):
        
