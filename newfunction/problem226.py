start1, end1 = map(int, input("Enter first interval: ").split())
start2, end2 = map(int, input("Enter second interval: ").split())

start = max(start1, start2)
end = min(end1, end2)

if start <= end:
    print("Overlapping interval:", start, "to", end)
else:
    print("The intervals do not overlap.")