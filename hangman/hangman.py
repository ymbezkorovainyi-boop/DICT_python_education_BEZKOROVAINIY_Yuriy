import random

print("HANGMAN")

words = ["python", "java", "javascript", "php"]

while True:
    action = input('Type "play" to play the game, "exit" to quit: ')

    if action == "play":
        secret_word = random.choice(words)
        revealed = list("-" * len(secret_word))
        guessed_letters = set()
        lives = 8

        while lives > 0:
            print()
            print("".join(revealed))

            letter = input("Input a letter: ")

            if len(letter) != 1:
                print("You should input a single letter")
            elif not ("a" <= letter <= "z"):
                print("Please enter a lowercase English letter")
            elif letter in guessed_letters:
                print("You've already guessed this letter")
            else:
                guessed_letters.add(letter)

                if letter in secret_word:
                    for i in range(len(secret_word)):
                        if secret_word[i] == letter:
                            revealed[i] = letter

                    if "-" not in revealed:
                        print(f"You guessed the word {secret_word}!")
                        print("You survived!")
                        break
                else:
                    print("That letter doesn't appear in the word")
                    lives -= 1
        else:
            print("You lost!")

    elif action == "exit":
        break