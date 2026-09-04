roman = input("Enter Roman numeral: ").upper()

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

total = 0
previous = 0

for char in reversed(roman):
    value = values.get(char, 0)

    if value < previous:
        total -= value
    else:
        total += value
        previous = value

print("Integer value:", total)