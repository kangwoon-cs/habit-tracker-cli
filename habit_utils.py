import json
import os
from settings import SEPARATOR

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
        file.write(SEPARATOR) # Separator for visual clarity