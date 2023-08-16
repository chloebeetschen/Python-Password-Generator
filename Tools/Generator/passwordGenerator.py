import random
import Tools.Checker.passwordStrengthCheck

def PasswordGenerator():
        
    #character options to be used
    upperChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowerChars = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '012345678'
    specialChars = '!@£#$%^&*()_-{[]}\/"><.,?'
    
    characters = ""
    
    #check what can be in the password
    ans = str(input("\nCan the password contain all character types? (Y/N) ")).upper()
    if ans == 'N':
        if str(input("Are CAPITAL Alphabets allowed ? (Y/N) ")).upper() == "Y":
            characters += upperChars
        if str(input("Are lowercase Alphabets allowed ? (Y/N) ")).upper() == "Y":
            characters += upperChars
        if str(input("Are Special Charecters allowed ? (Y/N) ")).upper() == "Y":
            characters += numbers
        if str(input("Are Special Charecters allowed ? (Y/N) ")).upper() == "Y":
            characters += specialChars
    else:
        characters = upperChars + lowerChars + numbers + specialChars
    

    
    #passLen = length requested
    passLen = int(str(input("How long do you want your password to be?")))
    
    password = []
    #generating the password
    for i in range(passLen):
        password.append(random.choice(characters))

    random.shuffle(password)
     
    print("\nHere is your new password: \n\n" + ''.join(password) + "\n")
    
    #test password strength with other file 
    # strength = StrengthChecker(password)
    # print("Password Strength = " + strength)