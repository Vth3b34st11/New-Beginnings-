print("This is a goal tally evaluation prompt I made using Python :)")
goals = input("Goals Scored?")
goals = int(goals)
if goals > 25:
    print("Golden Boot OP")
    print("Alan Sheerer esque")
elif goals > 20:
    print("Star Scorer")
elif goals > 10:
    print("Keep going")
else:
    print("START SCORING!!")
