text = input("Enter a word: ")

if text.lower() == text[::-1].lower():
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")