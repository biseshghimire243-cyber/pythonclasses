age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
    
    choice = input("Enter your candidate: ")

    print("Vote recorded for:", choice)
else:
    print("You are not eligible to vote.")