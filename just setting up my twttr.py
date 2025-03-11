vowels = ["a","A","e","E","i","I","o","O","u","U"] #List out the vowels
original = input("Input: ") #Call for string input from the user and make case insensitive
for char in vowels: #For the range of characters present in the list of vowels
    original = original.replace(char, "") #Replace the vowels present in the string input with blanks

print(original) #Display new string 
