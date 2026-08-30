salary1 = float(input("Enter first salary: "))
salary2 = float(input("Enter second salary: "))

if salary1 > salary2:
    difference = salary1 - salary2
    print("First salary is higher by", difference)

elif salary2 > salary1:
    difference = salary2 - salary1
    print("Second salary is higher by", difference)

else:
    print("Both salaries are equal")