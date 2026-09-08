marks = list(map(float, input("Enter marks: ").split()))
weights = list(map(float, input("Enter weights: ").split()))

if len(marks) != len(weights):
    print("Marks and weights must have the same length")
else:
    weighted_sum = sum(m * w for m, w in zip(marks, weights))
    total_weight = sum(weights)

    average = weighted_sum / total_weight

    print("Weighted average:", average)