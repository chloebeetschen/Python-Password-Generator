# main page where you will go to chosen menu option and get a result
import Tools.Generator.passwordGenerator
import Tools.Cracker.passwordCracker
import Tools.Forgot.forgotPassword
import Tools.Manager.passwordManager
import Tools.Recovery.fileRecovery
import Tools.Checker.passwordStrengthCheck

def options():
    #please select an option... 
    print("Please select an option/tool you would like to use: \n")
    print("1) Password Generator")
    print("2) Password Cracker")
    print("3) Forgotten Password")
    print("4) Password Manager")
    print("5) File Recovery")
    print("6) Password Strength Checker")
    print("7) Encrypt your password\n")
    
    #get user choice
    choice = int(str(input("Please enter the option number of your choice: ")))
    
    #placer to be removed
    
    #go to option of choice
    if choice == 1:
        Tools.Generator.passwordGenerator.PasswordGenerator()
            
    elif choice == 2:
        placer = 1 
            
    elif choice == 2:
        placer = 1 
            
    elif choice == 2:
        placer = 1 

    elif choice == 2:
        placer = 1 
        
    elif choice == 2:
        placer = 1 

    elif choice == 2:
        placer = 1 
    
    else:
        print("\nOption not in the list, please try again.\n")
        return
        

def main():
    
    print("\nWelcome to my python multi-tool program!\n")
    
    run = True
    while run:
        options()
        
        userAns = str(input("Would you like to pick an option again? (Y/N) ")).upper()
        
        if userAns == "N":
            run = False
            
    print("\nThank you and goodbye.\n")
    exit()
    
if __name__ == "__main__":
    main()