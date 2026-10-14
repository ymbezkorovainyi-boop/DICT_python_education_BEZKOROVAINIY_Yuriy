import random

num_friends = int(input("Enter the number of friends joining (including you):\n"))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_friends):
        name = input()
        friends[name] = 0

    total_amount = float(input("Enter the total amount:\n"))

    split_amount = round(total_amount / num_friends, 2)
    for name in friends:
        friends[name] = split_amount

    lucky_choice = input(
        'Do you want to use the "Who is lucky?" feature? Write Yes/No:\n'
    )

    if lucky_choice == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")

        if num_friends > 1:
            new_split = round(total_amount / (num_friends - 1), 2)
        else:
            new_split = 0

        for name in friends:
            if name == lucky_one:
                friends[name] = 0
            else:
                friends[name] = new_split

        print(friends)
    else:
        print("No one is going to be lucky")
        print(friends)