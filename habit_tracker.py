# File name: habit_tracker
# Description: This is a simple command-line based habit tracker that allows users to check in on daily habits.
# For each predefined habit, the program asks a yes/no question and records the user's responses
# along with the current date.
# The habits are stored as a dictionary for flexibility and future extensibility.
# Daily logs are saved to a plain text file (habit_log.txt), with the date and responses recorded.
# This tool helps build consistency by making habit tracking quick, lightweight, and file-based.
import os
import json
from datetime import date

def is_valid_key(key: str) -> bool:
    """
    Validate a habit key to ensure it contains only lowercase letters and underscores.

    Parameters:
        key (str): The key to validate.

    Returns:
        bool: True if the key is valid, False otherwise.
    """
    if not key:  # empty check
        return False
    for char in key:
        if not (char.islower() or char == "_"):
            return False
    return True



def already_logged(path, today):
    """
    Check whether today's habits have already been logged in the file.

    Parameters:
        path (str): Path to the log file.
        today (str): Current date as a string.

    Returns:
        bool: True if the user has not yet logged today, False otherwise.
    """
    if os.path.exists(path):
        # If the log file exists, scan each line to check for today's date
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if f"{today}" in line:
                    return False # Entry for today already exists
    return True # No log found for today or file doesn't exist


def collect_answers(habit_questions:dict):
    """
    Prompt the user to answer each habit question with yes or no.

    Parameters:
        habit_questions (dict): Dictionary of habit keys and descriptions.

    Returns:
        dict: Dictionary with updated habit descriptions including checkmarks.
    """
    habit_answers = {}
    for hbt_keys, hbt_answers in habit_questions.items():
        # Loop until the user provides a valid input (y/n)
        sentinel_value = 1 
        while sentinel_value == 1: # Repeat until valid 'y' or 'n' input is given
            answer = input(hbt_answers + "(y/n): ")
            if answer != "y" and answer != "n":
                print("Please reenter proper value")
                continue
            elif answer == "y":
                habit_answers[hbt_keys] = hbt_answers + " ✅"
                sentinel_value = 0
            elif answer == "n":
                habit_answers[hbt_keys] = hbt_answers + " ❌"
                sentinel_value = 0
    return habit_answers


def write_txt(path, habit_answers, today):
    """
    Write the user's habit answers to the log file.

    Parameters:
        path (str): Path to the log file.
        habit_answers (dict): User's responses to habit questions.
        today (str): Current date as a string.
    """
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"[{today}]\n")
        for habit_key, result in habit_answers.items():
            file.write(f"{habit_key}: {result}\n")
        file.write("\n")
        file.write("-"*75 + "\n") # Separator for visual clarity


def save_habits(path, habit_dict):
    """
    Save the habit dictionary to a JSON file.

    Parameters:
        path (str): File path to save the habits.
        habit_dict (dict): The habit questions dictionary.
    """
    with open(path, "w", encoding="utf-8") as file:
        json.dump(habit_dict, file, indent=4)
    print("Habit questions have been saved.\n")


def habit_file_exists(path):
    """
    Check if the habits JSON file exists.

    Parameters:
        path (str): Path to the habits file.

    Returns:
        bool: True if file exists, False otherwise.
    """
    if os.path.exists(path):
        return True
    else:
        return False


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

        if not is_valid_key(key):
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

    save_habits(path,habit_questions)


def load_habit_questions(path):
    """
    Load the habit questions from a JSON file.

    Parameters:
        path (str): Path to the habits JSON file.

    Returns:
        dict: Dictionary of habit keys and their questions.
    """
    habit_questions = {}
    with open(path, "r", encoding="utf-8") as file:
        habit_questions = json.load(file)
    return habit_questions


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
        elif not is_valid_key(key):
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
    print("-" * 75)

    for habits, description in habit_questions.items():
        print(f"{habits} : {description}")

    print("-" * 75)
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

            save_habits(path, habit_questions)
    
            if not habit_questions:
                print("All habits were deleted. You must add at least one habit.")

                while not habit_questions:
                    add_habit(habit_questions)
                save_habits(path, habit_questions)
                print("Habit file updated.\n")
                keep_editing = True  # Re-enter the edit menu loop

            else:
                sentinel_value = False
        
        
def main():
    """
    Main program flow:
    - Check for existing habits.json or prompt to create/edit
    - Load habit questions
    - Check if today is already logged
    - Collect answers and write to log
    """
    today = date.today().isoformat()
    
    LOG_FILE = "habit_log.txt"
    HABITS_FILE = "habits.json"

    if not habit_file_exists(HABITS_FILE): # if habit file doesn't exist, create it through user input
        print("You should write your habits!")
        while not habit_file_exists(HABITS_FILE):
            create_habit_questions(HABITS_FILE)

    while load_habit_questions(HABITS_FILE)=={}: # If habit file exists but is empty, prompt user to add habits
            print("Your habit list is currently empty.")
            create_habit_questions(HABITS_FILE)    
    edit_habit_questions(HABITS_FILE)
    
    habit_questions = load_habit_questions(HABITS_FILE)



    # Prevent duplicate logging for the same day
    if already_logged(LOG_FILE, today):
        habit_answers = collect_answers(habit_questions)
        write_txt(LOG_FILE, habit_answers, today)       
        
    else:
        print(" ✓ You've already logged your habits for today.")

if __name__ == "__main__":
    main()






