cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def print_grid():
    print("---------")
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("---------")

def check_win(player):
    if cells[0] == cells[1] == cells[2] == player: return True
    if cells[3] == cells[4] == cells[5] == player: return True
    if cells[6] == cells[7] == cells[8] == player: return True
    if cells[0] == cells[3] == cells[6] == player: return True
    if cells[1] == cells[4] == cells[7] == player: return True
    if cells[2] == cells[5] == cells[8] == player: return True
    if cells[0] == cells[4] == cells[8] == player: return True
    if cells[2] == cells[4] == cells[6] == player: return True
    return False

print_grid()
current_player = 'X'

while True:
    coords = input("Enter the coordinates: ").split()

    if len(coords) != 2 or not coords[0].isdigit() or not coords[1].isdigit():
        print("You should enter numbers!")
        continue

    row = int(coords[0])
    col = int(coords[1])

    if not (1 <= row <= 3) or not (1 <= col <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    index = (row - 1) * 3 + (col - 1)

    if cells[index] == 'X' or cells[index] == 'O':
        print("This cell is occupied! Choose another one!")
        continue

    cells[index] = current_player
    print_grid()

    if check_win('X'):
        print("X wins")
        break
    elif check_win('O'):
        print("O wins")
        break
    elif ' ' not in cells:
        print("Draw")
        break

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'