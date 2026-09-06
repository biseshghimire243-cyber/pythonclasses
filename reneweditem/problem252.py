text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if len(text1) != len(text2):
    print("Strings must have the same length.")
else:
    distance = 0

    for a, b in zip(text1, text2):
        if a != b:
            distance += 1

    print("Hamming distance:", distance)