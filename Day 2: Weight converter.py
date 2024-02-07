print("Next block of code? A weight converter!")
weight= int(input("Weight: "))
unit= input("(K)g or (L)bs: ")


if unit == "l" or unit == "L":
    converted = weight * 0.45
    print("Weight in kgs: " + str(converted))
elif unit == "k" or unit == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))


