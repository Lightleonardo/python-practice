name = input("Enter your name: ")
Grade = int(input("Enter your Score: "))
if Grade >= 70 and Grade <= 100:
    print(f"Student {name}, Congrats your Grade is A")
elif Grade >= 65 and Grade < 70:
    print(f"Student {name}, wow your Grade is B+. very very good")
elif Grade >= 60 and Grade < 65:
    print(f"Student {name}, Nice your Grade is B-. very good")
elif Grade >= 55 and Grade < 60:
    print(f"Student {name}, Good job your Grade is C+")
elif Grade >= 50 and Grade < 55:
    print(f"Student {name}, Keep up the good work your Grade is C")
elif Grade >= 45 and Grade < 50:
    print(f"Student {name}, you can do better your Grade is C-")
elif Grade >= 40 and Grade < 45:
    print(f"Student {name}, you need to work harder your Grade is D")
elif Grade >= 35 and Grade < 40:
    print(f"Student {name}, hmm your Grade is E")
elif Grade > 0 and Grade < 35:
    print(f"Student {name}, your Grade is F, Failed!!")
else:
    print(f"Invalid grade, please enter a valid grade between 0 and 100")
