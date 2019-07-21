class User:

    
    print('Rafiki, welcome to The Password Vault')
    
    print("Rafiki, let us get started")
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
        print("Create your password")
        newPassword= input()