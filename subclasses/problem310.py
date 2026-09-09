keys = input("Enter keys: ").split()
values = input("Enter values: ").split()

if len(keys) != len(values):
    print("Both lists must have the same number of elements")
else:
    result = dict(zip(keys, values))
    print("Dictionary:", result)