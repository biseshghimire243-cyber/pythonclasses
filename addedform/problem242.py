n = int(input("Enter number of people: "))

for i in range(n):
    print("\nPerson", i + 1)

    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print("BMI:", round(bmi, 2))
    print("Category:", category)