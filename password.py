import random
import string
import pyperclip

global userList

def passGen(size = 8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    gen = ''.join(random.choice(char) for _ in range(size))
    return gen
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
        print("3. Exit")
        option_selected = int(input())
        if option_selected == 1:
            print( "Welcome good ol'rafiki")
            print("Kindly, enter your username:")
            loginUsername= input()
            print("Kindly enter your password")
            loginPassword= input()
            """ The above code provides a login method for users of the The Password Vault """
            
            for user in userList:
                if loginUsername == user[0] and loginPassword == user[1]:
                    print("Welcome " +loginUsername)
                    print("Hey Rafiki, please create a password vault")
                    while True:
                        """ The while loop will create allow a user to enter all the app details and reset to create another third party app once all unputs are satisfied """
                        print("Enter website name:")
                        appName = input()
                        print("Enter your username in the app above")
                        appUsername= input()
                        print("Would you like to create or generate a password for " + appName + "?")
                        print("1. Create your own password")
                        print("2. Generate password ")
                        app_option_selected = int(input())
                        if app_option_selected == 1: 
                            print("Enter password below")
                            appPassword = input()
                            Credential.apps.append([appName, appUsername, appPassword])
                        elif app_option_selected == 2:
                            generator = passGen()
                            Credential.apps.append([ appName, appUsername , generator])
                        print("App stored succesfully")
                        
                        print("Hey Rafiki, select an option")
                        print("1. View Apps")
                        print("2. Add App")
                        vault_option = int(input()) 
                        if vault_option == 1:
                            print("These are the existing apps in the vault")
                            print(Credential.apps)
                            continue
                        else:
                            continue                   
                else:
                    print("This rafiki does not exist, kindly choose no. 2 to register below")             
        
        elif option_selected == 2:
            print ("Welcome new rafiki")
            print(" Create your username:")
            newUsername= input()
            print ("Rafiki, select a number")
            print("1. Create your own password")
            print("2. Generate password ")
            print("3. Exit ")
            newPassword= int(input())
        
            if newPassword == 1: 
                print("Enter password below")
                newPassword = input()
                userList.append([newUsername,newPassword])
            
            elif newPassword == 2:
                generator = passGen()
                print(generator)
                userList.append([newUsername,generator])
                """ saveUser is to save the user details using the method above  """          
                """ the elif option is used as it can take in arguements for users who would like to generate passwords """
        
        else:
            break
    

