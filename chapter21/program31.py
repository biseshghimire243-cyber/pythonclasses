math = float(input("Enter Mathematics marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer marks: "))
social = float(input("Enter Social marks: "))

total = math + science + english + computer + social
percentage = total / 5

print("Total marks:", total)
print("Percentage:", percentage, "%")