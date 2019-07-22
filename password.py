import random
import string
import pyperclip

global userList

def passGen(size = 8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    gen = ''.join(random.choice(char) for _ in range(size))
    return gen
    
class User:
    def __init__(self,loginUsername,loginPassword):
        self.loginUsername =loginUsername
        self.loginPassword =loginPassword 
    
    userList =[]
    
    print('Rafiki, welcome to The Password Vault')
    while  True:
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
        
        elif option_selected == 2:
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
            
                userList.append([newUsername,newPassword])
                print(userList)
            
            elif newPassword == 2:
                generator = passGen()
                userList.append([newUsername,generator])
                print(userList)
                """ saveUser is to save the user details using the method above  """          
                """ the elif option is used as it can take in arguements for users who would like to generate passwords """
        
                print("Your Password Vault has been created successfully rafiki, " +newUsername)
                print ("Please do login now")
                print( "Welcome consistent rafiki")
                print("Kindly, enter your username:")
                loginUsername= input()
                print("Kindly enter your password")
                loginPassword= input()
        else:
            break
    

class Credential:
    
    """ The above function helps generate passwords using .random() """

    """ this class holds the different credentials the users need to be kept in the Password Vault """

    apps=[]
    """ apps list contains the apps and passwords that the user wants stored in the password vault """
    vaultUser= []
    """  vaultUser list contains the credentials created in the user class """
    
    @classmethod
    def verify(cls, loginUsername, loginPassword):
        onlineUser = ''
        """ the for loop checks through to the list to confirm whether the credetnials are a match """
        for user in User.userList:
            if (user.loginUsername == loginUsername and user.loginPassword == loginPassword):
                onlineUser= user.loginUsername
        return onlineUser 

    def __init__(self, appName , appUsername, appPassword):
        self.appUsername = appUsername
        self.appName = appName
        self.appPassword = appPassword    