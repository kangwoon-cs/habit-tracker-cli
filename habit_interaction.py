# File: habit_interaction.py
# Description: Contains the function that interacts with the user to answer habit questions.


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