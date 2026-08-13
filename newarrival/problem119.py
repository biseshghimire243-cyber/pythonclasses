workouts = []


def add_workout():

    exercise = input("Exercise Name: ")
    sets = int(input("Number of Sets: "))
    reps = int(input("Reps per Set: "))
    weight = float(input("Weight in kg: "))

    if sets <= 0 or reps <= 0 or weight < 0:
        raise Exception("Invalid workout values.")

    workout = {
        "Exercise": exercise,
        "Sets": sets,
        "Reps": reps,
        "Weight": weight
    }

    workouts.append(workout)

    print("Workout added.")


def view_workouts():

    if not workouts:
        print("No workouts recorded.")
        return

    print("\n========== WORKOUT HISTORY ==========")

    for workout in workouts:

        volume = (
            workout["Sets"]
            * workout["Reps"]
            * workout["Weight"]
        )

        print("--------------------------")
        print("Exercise:", workout["Exercise"])
        print("Sets:", workout["Sets"])
        print("Reps:", workout["Reps"])
        print("Weight:", workout["Weight"], "kg")
        print("Training Volume:", volume, "kg")


def total_volume():

    total = 0

    for workout in workouts:

        total += (
            workout["Sets"]
            * workout["Reps"]
            * workout["Weight"]
        )

    print("Total Training Volume:", total, "kg")


while True:

    try:

        print("\n========== WORKOUT TRACKER ==========")
        print("1. Add Workout")
        print("2. View Workouts")
        print("3. Total Volume")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            add_workout()

        elif choice == 2:
            view_workouts()

        elif choice == 3:
            total_volume()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)