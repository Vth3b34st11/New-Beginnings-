score = int(input("Score: "))
if 85 <= score <= 100:
    print("Grade: HD")
elif 75 <= score < 85:
    print("Grade: DI")
elif 65 <= score < 75:
    print("Grade: CR")
elif 50 <= score < 65:
    print("Grade: PS")
else:
    print("Grade: Fail")
