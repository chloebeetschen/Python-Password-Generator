#potenital code to see saved passwords
    #hash them once stored

#set a pin
pin = input("Enter a security pin:")
pin = 1234


count = 3
inputPin = input("Enter a security pin:")
if inputPin == pin:
    print("Here is your generated password: " + generatedPass)
else:
    count =- 1
    if count == 0:
        print("No more attempts remaining.")
        
        
        
    print("Sorry pin incorrect, please try again.")
    print("You have " + count + " more attempts remaining.")