Habit Tracker CLI App

A simple command-line habit tracker that allows users to log daily habits, add new habits, or delete existing ones. Habit data is stored in a local JSON file, and daily logs are saved to a text file.

Features

Add, delete, and view a customizable list of habit questions

Record daily habit logs through terminal prompts

Prevents duplicate logs for the same day

Automatically creates habit data file if not found or empty

File Structure

habit_tracker.py : main Python file containing all core logic

habits.json : stores the user's list of habit questions

habit_log.txt : stores daily logs of habit responses

How to Use

Run the script:

python habit_tracker.py

If no habit list exists or the existing list is empty, you will be prompted to create your habits.

After setup, you can:

Edit the habit list

Log today's habits (only if not already logged)

Your answers will be stored in habit_log.txt

Example Habit Questions

Did you exercise today?

Did you drink enough water?

Did you sleep at least 7 hours?

Requirements

Python 3.7+

Future Improvements

Move to SQLite or CSV storage

Add summary/stats feature

Optional GUI version

Made with focus and coffee ☕

