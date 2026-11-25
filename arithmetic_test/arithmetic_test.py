import random

levels = {
    "1": "simple operations with numbers 2-9",
    "2": "integral squares of 11-29"
}

while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    level = input()
    if level in levels:
        break
    print("Incorrect format.")

score = 0

for _ in range(5):
    if level == "1":
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op = random.choice(["+", "-", "*"])
        if op == "+":
            correct = a + b
        elif op == "-":
            correct = a - b
        else:
            correct = a * b
        print(f"{a} {op} {b}")
    else:
        num = random.randint(11, 29)
        correct = num ** 2
        print(num)

    while True:
        try:
            answer = int(input())
            break
        except ValueError:
            print("Incorrect format.")

    if answer == correct:
        print("Right!")
        score += 1
    else:
        print("Wrong!")

print(f"Your mark is {score}/5. Would you like to save the result? Enter yes or no.")
save = input()

if save in ("yes", "YES", "y", "Yes"):
    print("What is your name?")
    name = input()
    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}: {score}/5 in level {level} ({levels[level]}).\n")
    print('The results are saved in "results.txt".')