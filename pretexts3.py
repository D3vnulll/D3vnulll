import os
import pyperclip  # Import the pyperclip library

# File to store pretexts
TEXTS_FILE = "pretexts.txt"

# Load pretexts from file or create an empty dictionary
try:
    with open(TEXTS_FILE, "r") as file:
        lines = file.readlines()
        texts = {}
        name = None
        current_text = []
        for line in lines:
            if line.startswith("==="):  # Marker for separating name and text
                if name:
                    texts[name] = "\n".join(current_text)
                name = line.split("===")[1].strip()
                current_text = []
            else:
                current_text.append(line)
        if name:
            texts[name] = "\n".join(current_text)
except FileNotFoundError:
    texts = {}

def display_menu():
    print("\n=== Menu ===")
    print("1. View all pretext names")
    print("2. Add a new pretext")
    print("3. Delete a pretext")
    print("4. Display a specific pretext")
    print("5. Exit")

def view_texts():
    search_string = input("Enter the string to match: ")
    print("\n=== Matching Pretext Names ===")
    matches = [name for name in texts.keys() if search_string.lower() in name.lower()]
    if matches:
        for name in matches:
            print(name)
    else:
        print(f"No pretexts found containing: {search_string}")

def add_text():
    new_name = input("Enter a name for the new pretext: ")
    print("Enter the new pretext (press Enter three times to finish):")
    new_text_lines = []
    consecutive_enters = 0
    while True:
        line = input()
        if line == "":
            consecutive_enters += 1
            if consecutive_enters == 3:
                break
        else:
            consecutive_enters = 0
            new_text_lines.append(line)
    new_text = "\n".join(new_text_lines)
    texts[new_name] = new_text
    save_texts()
    print(f"Pretext added successfully with name: {new_name}")

def delete_text():
    view_texts()
    name_to_delete = input("Enter the name of the pretext to delete: ")
    if name_to_delete in texts:
        del texts[name_to_delete]
        save_texts()
        print("Pretext deleted successfully.")
    else:
        print("Invalid name. Pretext not found.")

def display_specific_text():
    view_texts()
    name_to_display = input("Enter the name of the pretext to display: ")
    if name_to_display in texts:
        pretext_to_copy = texts[name_to_display]
        print(f"\n=== Pretext {name_to_display} ===\n{pretext_to_copy}")
        # Copy the pretext to the clipboard
        pyperclip.copy(pretext_to_copy)
        print("Pretext copied to clipboard.")
    else:
        print("Invalid name. Pretext not found.")

def save_texts():
    with open(TEXTS_FILE, "w") as file:
        for name, text in texts.items():
            file.write(f"\n=== {name} ===\n{text}\n")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_texts()
        elif choice == '2':
            add_text()
        elif choice == '3':
            delete_text()
        elif choice == '4':
            display_specific_text()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
