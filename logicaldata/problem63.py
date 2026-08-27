data = [10, 20, 10, 30, 20, 40, 30, 50]

unique_data = []

for item in data:
    if item not in unique_data:
        unique_data.append(item)

print("Original:", data)
print("Without duplicates:", unique_data)