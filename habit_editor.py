import habit_utils as hu 
import json
from settings import SEPARATOR

def add_habit(habit_dict):
    """
    Prompt the user to add a new habit to the dictionary.

    Parameters:
        habit_dict (dict): The current habit dictionary to update.
    """
    print("\n-- Add a new habit --")
    while True:
        key = input("Enter a unique habit key (e.g., 'exercise'): ").strip()
        if key in habit_dict:
            print("That key already exists. Please choose another.")
            continue
        elif not key:
            print("Key cannot be empty.")
            continue
        elif not hu.is_valid_key(key):
            print("❌ Invalid key! Use lowercase letters and underscores only.")
            continue
        else:
            break

    description = input("Enter the habit question: ").strip()
    if description:
        habit_dict[key] = description
        print(f"Habit '{key}' added successfully!\n")
    else:
        print("Habit not added. Description cannot be empty.")


def delete_habit(habit_dict):
    """
    Prompt the user to delete a habit by its key.

    Parameters:
        habit_dict (dict): The current habit dictionary.
    """
    print("\n-- Delete a habit --")
    key = input("Enter the key of the habit you want to delete: ").strip()
    if key in habit_dict:
        del habit_dict[key]
        print(f"Habit '{key}' deleted.\n")
    else:
        print("Habit key not found.")


def prompt_edit_menu():
    """
    Display a menu for the user to choose an edit action.

    Returns:
        str: One of 'add', 'delete', or 'exit'.
    """
    print("\n Edit Habit Menu")
    print("1. Add a new habit")
    print("2. Delete an existing habit")
    print("3. Exit habit editor")

    while True:
        choice = input("Select an option (1/2/3): ").strip()
        if choice == "1":
            return "add"
        elif choice == "2":
            return "delete"
        elif choice == "3":
            return "exit"
        else:
            print("Invalid input. Please enter 1, 2, or 3.")


def edit_habit_questions(path):
    """
    Allows the user to edit habit questions interactively.
    If all habits are deleted, forces at least one to be added again.

    Parameters:
        path (str): Path to the habits JSON file.
    """
    with open(path,"r", encoding="utf-8") as file:
        habit_questions = json.load(file)
    print("\nYour current habits:")
    print(SEPARATOR)

    for habits, description in habit_questions.items():
        print(f"{habits} : {description}")

    print(SEPARATOR)
    sentinel_value = True

    while sentinel_value:
        modify = input("Do you want to modify the habits? (y/n): ")
        if modify != "y" and modify !="n":
            print("Please reenter proper value")
            continue

        elif modify == "n":
            sentinel_value = False
        
        elif modify == "y":
            keep_editing = True

            while keep_editing:
                action = prompt_edit_menu()

                if action == "add":
                    print("\n Current habits:")
                    for key, desc in habit_questions.items():
                        print(f"- {key}: {desc}")
                    add_habit(habit_questions)

                elif action == "delete":
                    print("\n Current habits:")
                    for key, desc in habit_questions.items():
                        print(f"- {key}: {desc}")
                    delete_habit(habit_questions)

                elif action == "exit":
                    keep_editing = False

            hu.save_habits(path, habit_questions)
    
            if not habit_questions:
                print("All habits were deleted. You must add at least one habit.")

                while not habit_questions:
                    add_habit(habit_questions)
                hu.save_habits(path, habit_questions)
                print("Habit file updated.\n")
                keep_editing = True  # Re-enter the edit menu loop

            else:
                sentinel_value = False


def create_habit_questions(path):
    """
    Prompt the user to create a new set of habit questions and save them to a JSON file.

    Parameters:
        path (str): File path where the new habit JSON will be saved.
    """
    habit_questions = {}
    question_done = True
    print("Enter your habit questions. Type 'done' to finish.\n")
    while question_done:
        key = input("Enter the habit name (or type 'done' to finish): ").strip()
        if key.lower() == "done":
            break

        if not hu.is_valid_key(key):
            print("Invalid key! Use lowercase letters and underscores only.")
            continue

        if key in habit_questions:
            print("That habit already exists. Try a different name.")
            continue

        value = input("Enter the description for this habit: ").strip()
        if value:
            habit_questions[key] = value
        else:
            print("Description cannot be empty. Skipping...\n")

    hu.save_habits(path,habit_questions)
