height1 = float(input("Enter first person's height: "))
height2 = float(input("Enter second person's height: "))

if height1 > height2:
    print("First person is taller")
elif height2 > height1:
    print("Second person is taller")
else:
    print("Both have the same height")