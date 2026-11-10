print("How many pencils would you like to use:")
while True:
    pencils_input = input()
    if not pencils_input.lstrip('-').isdigit():
        print("The number of pencils should be numeric")
    elif int(pencils_input) <= 0:
        print("The number of pencils should be positive")
    else:
        pencils = int(pencils_input)
        break

print("Who will be the first (John, Jack):")
while True:
    first_player = input()
    if first_player not in ["John", "Jack"]:
        print("Choose between 'John' and 'Jack'")
    else:
        break

current_player = first_player

while pencils > 0:
    print("|" * pencils)
    print(f"{current_player}'s turn!")

    if current_player == "John":
        while True:
            take_input = input()
            if take_input not in ["1", "2", "3"]:
                print("Possible values: '1', '2' or '3'")
            elif int(take_input) > pencils:
                print("Too many pencils were taken")
            else:
                take = int(take_input)
                break
    else:
        if pencils == 1:
            take = 1
        elif pencils % 4 == 1:
            take = 1
        elif pencils % 4 == 2:
            take = 1
        elif pencils % 4 == 3:
            take = 2
        elif pencils % 4 == 0:
            take = 3
        print(take)

    pencils -= take

    if pencils == 0:
        winner = "Jack" if current_player == "John" else "John"
        print(f"{winner} won!")
        break

    current_player = "Jack" if current_player == "John" else "John"