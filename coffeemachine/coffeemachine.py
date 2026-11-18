class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "main_menu"
        self.prompt()

    def prompt(self):
        if self.state == "main_menu":
            print("\nWrite action (buy, fill, take, remaining, exit):")
        elif self.state == "buying":
            print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif self.state == "filling_water":
            print("\nWrite how many ml of water do you want to add:")
        elif self.state == "filling_milk":
            print("Write how many ml of milk do you want to add:")
        elif self.state == "filling_beans":
            print("Write how many grams of coffee beans do you want to add:")
        elif self.state == "filling_cups":
            print("Write how many disposable cups of coffee do you want to add:")

    def print_state(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def make_coffee(self, need_water, need_milk, need_beans, cost):
        if self.water < need_water:
            print("Sorry, not enough water!")
        elif self.milk < need_milk:
            print("Sorry, not enough milk!")
        elif self.beans < need_beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= need_water
            self.milk -= need_milk
            self.beans -= need_beans
            self.cups -= 1
            self.money += cost

    def handle_input(self, user_input):
        if self.state == "main_menu":
            if user_input == "buy":
                self.state = "buying"
            elif user_input == "fill":
                self.state = "filling_water"
            elif user_input == "take":
                print(f"\nI gave you {self.money}")
                self.money = 0
            elif user_input == "remaining":
                self.print_state()
            elif user_input == "exit":
                self.state = "off"
                return
        elif self.state == "buying":
            if user_input == "1":
                self.make_coffee(250, 0, 16, 4)
                self.state = "main_menu"
            elif user_input == "2":
                self.make_coffee(350, 75, 20, 7)
                self.state = "main_menu"
            elif user_input == "3":
                self.make_coffee(200, 100, 12, 6)
                self.state = "main_menu"
            elif user_input == "back":
                self.state = "main_menu"
        elif self.state == "filling_water":
            self.water += int(user_input)
            self.state = "filling_milk"
        elif self.state == "filling_milk":
            self.milk += int(user_input)
            self.state = "filling_beans"
        elif self.state == "filling_beans":
            self.beans += int(user_input)
            self.state = "filling_cups"
        elif self.state == "filling_cups":
            self.cups += int(user_input)
            self.state = "main_menu"

        self.prompt()


machine = CoffeeMachine()
while machine.state != "off":
    machine.handle_input(input())