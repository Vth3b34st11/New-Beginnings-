fifty_cal = ["avocado","cantaloupe","honeydew melon","pineapple","strawberries","tangerine"]
sixty_cal = ["grapefruit","nectarine",'peach']
ninty_cal = ["grapes","kiwifruit"]
hundred_cal = ["pear","sweet cherries"]
rest_of_fruits = ["apple","banana","lemon","lime","orange","plums","watermelon"] 
cal = [15,20,50,60,70,80,90,100,110,130]
item = input("Item: ").lower()
if item in fifty_cal: 
    print(("Calories: " + str(cal[2])))
elif item in ninty_cal: 
    print(("Calories: " + str(cal[6])))
elif item in sixty_cal: 
    print(("Calories: " + str(cal[3])))
elif item in hundred_cal: 
    print(("Calories: " + str(cal[7])))
elif item == rest_of_fruits[1]: 
    print(("Calories: " + str(cal[8])))
elif item == rest_of_fruits[2]: 
    print(("Calories: " + str(cal[0])))
elif item == rest_of_fruits[3]: 
    print(("Calories: " + str(cal[1])))
elif item == rest_of_fruits[6]: 
    print(("Calories: " + str(cal[5])))
elif item == rest_of_fruits[5]: 
    print(("Calories: " + str(cal[4])))
elif item in rest_of_fruits[0]: 
    print(("Calories: " + str(cal[9])))


    





