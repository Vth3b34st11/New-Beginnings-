#Display Amount Due 
amount = 50
#Develop a loop 
while amount > 0: 
    print("Amount Due: " , amount)
    #Call for input to insert coin
    coin_insert = int(input("Insert Coin: ")) 
    #Use list 
    if coin_insert in [25,10,5]:
        amount = amount - coin_insert
    else: 
        print("Amount Due: " , 50) 
    #Change Owed 
    if amount <= 0: 
        print("Change Owed:" , abs(amount)) #Prints the absolute value i.e regardless of sign






