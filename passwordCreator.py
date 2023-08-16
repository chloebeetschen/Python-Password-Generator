#import library
import random

def PasswordGenerator(passLen):
    
    password = ""
    
    #character options to be used
    upperChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowerChars = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '012345678'
    specialChars = '!@£#$%^&*()_-{[]}\/"><.,?'
    
    characters = ""
    
    #check what can be in the password
    ans = str(input("Can the password contain all character types? (Y/N) "))
    if ans == 'N':
        if str(input("Are CAPITAL Alphabets allowed ? (Y/N) ")) == "Y":
            characters += upperChars
        if str(input("Are lowercase Alphabets allowed ? (Y/N) ")) == "Y":
            characters += upperChars
        if str(input("Are Special Charecters allowed ? (Y/N) ")) == "Y":
            characters += numbers
        if str(input("Are Special Charecters allowed ? (Y/N) ")) == "Y":
            characters += specialChars
    else:
        characters = upperChars + lowerChars + numbers + specialChars
    

    
    #passLen = length requested
    passLen = int(input("How long do you want your password to be? "))
    #generating the password
    for i in range(passLen):
        password.append(random.choice(characters))

    password.shuffle
        
    return(password) 