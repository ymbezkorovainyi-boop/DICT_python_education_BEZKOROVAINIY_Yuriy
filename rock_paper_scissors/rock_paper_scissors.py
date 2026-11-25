import random

name = input("Enter your name: ")
print(f"Hello, {name}")

score = 0
try:
    with open("rating.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2 and parts[0] == name:
                score = int(parts[1])
                break
except FileNotFoundError:
    pass

options_input = input()
if options_input:
    options = options_input.split(",")
else:
    options = ["rock", "paper", "scissors"]

print("Okay, let's start")

while True:
    user_choice = input()
    if user_choice == "!exit":
        print("Bye!")
        break
    if user_choice == "!rating":
        print(f"Your rating: {score}")
        continue
    if user_choice not in options:
        print("Invalid input")
        continue

    comp_choice = random.choice(options)
    if user_choice == comp_choice:
        print(f"There is a draw ({comp_choice})")
        score += 50
    else:
        idx = options.index(user_choice)
        other_options = options[idx + 1:] + options[:idx]
        beaten_by = other_options[:len(other_options) // 2]
        if comp_choice in beaten_by:
            print(f"Sorry, but the computer chose {comp_choice}")
        else:
            print(f"Well done. The computer chose {comp_choice} and failed")
            score += 100