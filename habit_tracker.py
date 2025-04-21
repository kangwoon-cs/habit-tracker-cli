# File name: habit_tracker
# Description: This is a simple command-line based habit tracker that allows users to check in on daily habits.
# For each predefined habit, the program asks a yes/no question and records the user's responses
# along with the current date.
# The habits are stored as a dictionary for flexibility and future extensibility.
# Daily logs are saved to a plain text file (habit_log.txt), with the date and responses recorded.
# This tool helps build consistency by making habit tracking quick, lightweight, and file-based.
from habit_utils import already_logged, load_habit_questions, habit_file_exists, write_txt
from habit_editor import create_habit_questions, edit_habit_questions
from habit_interaction import collect_answers
from datetime import date
from settings import LOG_FILE, HABITS_FILE       

def main():
    """
    Main program flow:
    - Check for existing habits.json or prompt to create/edit
    - Load habit questions
    - Check if today is already logged
    - Collect answers and write to log
    """
    today = date.today().isoformat()
    


    if not habit_file_exists(HABITS_FILE): # if habit file doesn't exist, create it through user input
        print("You should write your habits!")
        while not habit_file_exists(HABITS_FILE):
            create_habit_questions(HABITS_FILE)


    while load_habit_questions(HABITS_FILE) == {}: # If habit file exists but is empty, prompt user to add habits
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






