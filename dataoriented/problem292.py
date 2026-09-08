text = input("Enter a string: ")

length = len(text)

if length % 2 == 1:
    print("Middle character:", text[length // 2])
else:
    middle1 = text[length // 2 - 1]
    middle2 = text[length // 2]
    print("Middle characters:", middle1 + middle2)