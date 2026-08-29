numbers = [1, 2, 3, 5, 6, 7, 10, 12, 13, 14]

ranges = []
start = numbers[0]
previous = numbers[0]

for number in numbers[1:]:

    if number == previous + 1:
        previous = number
    else:
        if start == previous:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "-" + str(previous))

        start = number
        previous = number

if start == previous:
    ranges.append(str(start))
else:
    ranges.append(str(start) + "-" + str(previous))

print("Compressed data:", ", ".join(ranges))