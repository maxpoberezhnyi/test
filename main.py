def rows(file_path, word):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            found_lines = [i + 1 for i, line in enumerate(lines) if word.lower() in line.lower()]

            if found_lines:
                print("Знайдені рядки:")
                for i in found_lines:
                    print(f"{i}. {lines[i-1].strip()}")
            else:
                print(f"Слово '{word}' не знайдено в жодному рядку")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено")

if __name__ == "__main__":
    file_path = r'text.txt'
    word = input("Введіть слово для пошуку: ")

    rows(file_path, word)