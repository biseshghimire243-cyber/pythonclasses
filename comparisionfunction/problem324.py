sentence1 = input("Enter first sentence: ").lower().split()
sentence2 = input("Enter second sentence: ").lower().split()

common = set(sentence1) & set(sentence2)

print("Common words:", sorted(common))