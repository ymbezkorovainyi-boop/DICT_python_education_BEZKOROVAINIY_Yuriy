def parse_num(val):
    return float(val) if '.' in val else int(val)

def read_matrix(prompt_size, prompt_matrix):
    n, m = map(int, input(prompt_size).split())
    print(prompt_matrix)
    matrix = [[parse_num(x) for x in input().split()] for _ in range(n)]
    return n, m, matrix

def print_matrix(matrix):
    print("The result is:")
    for row in matrix:
        print(*row)

def transpose_main(matrix):
    n, m = len(matrix), len(matrix[0])
    return [[matrix[j][i] for j in range(n)] for i in range(m)]

def transpose_side(matrix):
    n, m = len(matrix), len(matrix[0])
    return [[matrix[n - 1 - j][m - 1 - i] for j in range(n)] for i in range(m)]

def transpose_vertical(matrix):
    return [row[::-1] for row in matrix]

def transpose_horizontal(matrix):
    return matrix[::-1]

def get_minor(matrix, row, col):
    return [
        [matrix[i][j] for j in range(len(matrix)) if j != col]
        for i in range(len(matrix)) if i != row
    ]

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    total = 0
    for j in range(n):
        total += ((-1) ** j) * matrix[0][j] * determinant(get_minor(matrix, 0, j))
    return total

def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        return None
    n = len(matrix)
    if n == 1:
        val = round(1 / matrix[0][0], 2)
        return [[0 if val == 0 else val]]
    cofactors = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor = get_minor(matrix, i, j)
            cofactor_row.append(((-1) ** (i + j)) * determinant(minor))
        cofactors.append(cofactor_row)
    adjugate = transpose_main(cofactors)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            val = round(adjugate[i][j] / det, 2)
            row.append(0 if val == 0 else val)
        result.append(row)
    return result

while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    choice = input("Your choice: ")

    if choice == "1":
        n1, m1, a = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
        n2, m2, b = read_matrix("Enter size of second matrix: ", "Enter second matrix:")
        if n1 != n2 or m1 != m2:
            print("The operation cannot be performed.")
        else:
            res = [[a[i][j] + b[i][j] for j in range(m1)] for i in range(n1)]
            print_matrix(res)

    elif choice == "2":
        n, m, a = read_matrix("Enter size of matrix: ", "Enter matrix:")
        c = parse_num(input("Enter constant: "))
        res = [[a[i][j] * c for j in range(m)] for i in range(n)]
        print_matrix(res)

    elif choice == "3":
        n1, m1, a = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
        n2, m2, b = read_matrix("Enter size of second matrix: ", "Enter second matrix:")
        if m1 != n2:
            print("The operation cannot be performed.")
        else:
            res = [[sum(a[i][k] * b[k][j] for k in range(m1)) for j in range(m2)] for i in range(n1)]
            print_matrix(res)

    elif choice == "4":
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        t_choice = input("Your choice: ")
        n, m, a = read_matrix("Enter matrix size: ", "Enter matrix:")
        if t_choice == "1":
            print_matrix(transpose_main(a))
        elif t_choice == "2":
            print_matrix(transpose_side(a))
        elif t_choice == "3":
            print_matrix(transpose_vertical(a))
        elif t_choice == "4":
            print_matrix(transpose_horizontal(a))

    elif choice == "5":
        n, m, a = read_matrix("Enter matrix size: ", "Enter matrix:")
        if n != m:
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            print(determinant(a))

    elif choice == "6":
        n, m, a = read_matrix("Enter matrix size: ", "Enter matrix:")
        if n != m:
            print("The operation cannot be performed.")
        else:
            inv = inverse_matrix(a)
            if inv is None:
                print("This matrix doesn't have an inverse.")
            else:
                print_matrix(inv)

    elif choice == "0":
        break