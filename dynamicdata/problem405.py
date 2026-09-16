names = input("Enter names separated by space: ").split()

longest = names[0]

for name in names:
    if len(name) > len(longest):
        longest = name

print("Longest name:", longest)