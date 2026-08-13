teams = {}
matches = []


def add_team():

    name = input("Team Name: ")

    if name in teams:
        raise Exception("Team already exists.")

    teams[name] = {
        "Played": 0,
        "Won": 0,
        "Lost": 0,
        "Points": 0
    }

    print("Team added.")


def record_match():

    team1 = input("Team 1: ")
    team2 = input("Team 2: ")

    if team1 not in teams or team2 not in teams:
        raise Exception("Team not found.")

    if team1 == team2:
        raise Exception("A team cannot play against itself.")

    winner = input("Winner: ")

    if winner not in [team1, team2]:
        raise Exception("Winner must be one of the teams.")

    teams[team1]["Played"] += 1
    teams[team2]["Played"] += 1

    if winner == team1:

        teams[team1]["Won"] += 1
        teams[team1]["Points"] += 3
        teams[team2]["Lost"] += 1

    else:

        teams[team2]["Won"] += 1
        teams[team2]["Points"] += 3
        teams[team1]["Lost"] += 1

    matches.append((team1, team2, winner))

    print("Match recorded.")


def show_table():

    if not teams:
        print("No teams.")
        return

    ranking = sorted(
        teams.items(),
        key=lambda item: item[1]["Points"],
        reverse=True
    )

    print("\n========== TOURNAMENT TABLE ==========")

    print(
        "Team | Played | Won | Lost | Points"
    )

    for name, data in ranking:

        print(
            name,
            "|",
            data["Played"],
            "|",
            data["Won"],
            "|",
            data["Lost"],
            "|",
            data["Points"]
        )


while True:

    try:

        print("\n========== SPORTS TOURNAMENT ==========")
        print("1. Add Team")
        print("2. Record Match")
        print("3. Show Table")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            add_team()

        elif choice == 2:
            record_match()

        elif choice == 3:
            show_table()

        elif choice == 4:
            print("Tournament Manager Closed.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)