formatters = [
    "plain", "bold", "italic", "header", "link",
    "inline-code", "ordered-list", "unordered-list", "new-line"
]
result = ""

while True:
    choice = input("Choose a formatter: ")
    if choice == "!help":
        print("Available formatters:", " ".join(formatters))
        print("Special commands: !help !done")
    elif choice == "!done":
        with open("output.md", "w", encoding="utf-8") as file:
            file.write(result)
        break
    elif choice not in formatters:
        print("Unknown formatting type or command")
    else:
        if choice == "plain":
            result += input("Text: ")
        elif choice == "bold":
            result += f"**{input('Text: ')}**"
        elif choice == "italic":
            result += f"*{input('Text: ')}*"
        elif choice == "inline-code":
            result += f"`{input('Text: ')}`"
        elif choice == "link":
            label = input("Label: ")
            url = input("URL: ")
            result += f"[{label}]({url})"
        elif choice == "header":
            while True:
                level = int(input("Level: "))
                if 1 <= level <= 6:
                    break
                print("The level should be within the range of 1 to 6")
            text = input("Text: ")
            result += f"{'#' * level} {text}\n"
        elif choice == "new-line":
            result += "\n"
        elif choice in ("ordered-list", "unordered-list"):
            while True:
                rows = int(input("Number of rows: "))
                if rows > 0:
                    break
                print("The number of rows should be greater than zero")
            for i in range(1, rows + 1):
                row_text = input(f"Row #{i}: ")
                if choice == "ordered-list":
                    result += f"{i}. {row_text}\n"
                else:
                    result += f"- {row_text}\n"
        print(result)