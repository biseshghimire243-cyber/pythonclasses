n = int(input("Enter number of intervals: "))

start = float("-inf")
end = float("inf")

for _ in range(n):
    a, b = map(int, input("Enter interval: ").split())

    start = max(start, a)
    end = min(end, b)

if start <= end:
    print("Common intersection:", start, "to", end)
else:
    print("No common intersection.")