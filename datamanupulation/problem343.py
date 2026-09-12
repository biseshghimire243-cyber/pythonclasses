number = int(input("Enter a number: "))

i = 0

while i * i < number:
    i += 1

if i * i == number:
    print("Perfect square")
else:
    print("Not a perfect square")