# Define a function that prompts the user for a vanity plate. and then output Valid if meets all of the requirements or Invalid if it does not. 

#Define main 
def main(): 
    plate = input("Plate: ")
    if is_valid(plate) == True: 
        print("Valid")
    else: 
        print("Invalid")
#Define is valid
def is_valid(s):
    #Contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) < 2 or len(s) > 6: 
        return False
    #“All vanity plates must start with at least two letters.
    if s[0].isalpha() == False or s[1].isalpha == False:
        return False
    
    #Numbers cannot be used in the middle of a plate; they must come at the end
    num = 0 #Define new marker variable called num
    while num < len(s): #While the marker is within the string 
        if s[num].isdigit(): #If num comes across a digit in the string
            if not s[num:].isdigit():
                return False
            else: 
                break #Break the while loop if the condition is satisfied
        num += 1 #Prevents infinite loop 

    #The first number used cannot be a ‘0’.”
    i = 0 #define i as a marker/indicator of elements in the string
    while i < len(s): #This ensures that we don't move past the length of the string and only look at elements in the string
        if s[i].isalpha() == False: #If our i marker comes across a number
            if s[i] == "0": #If that number is zero 
                return False #Not valid
            else: #Otherwise
                break #Stop the loop
        i+= 1 # i is not always equal to zero, this breaks us out of the infinite loop
    
    #“No periods, spaces, or punctuation marks are allowed.
    for punc in s: #Define a variable called punc to represent special characters 
        if punc in [" ",".","?","!"]: #If punc is in the list of special characters
            return False

    return True # If all conditions satisifed, return true
        
main()
