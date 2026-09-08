text = input("Enter a sentence: ")

words = text.split()
count = sum(1 for word in words if len(word) > 5)

print("Words with more than 5 characters:", count)