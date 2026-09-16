text = input("Enter a paragraph: ")

count = 0

for char in text:
    if char in ".!?":
        count += 1

print("Number of sentences:", count)