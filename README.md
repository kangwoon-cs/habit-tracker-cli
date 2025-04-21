# 📝 Habit Tracker CLI

A simple command-line habit tracking application written in Python.  
Users can define their own daily habits, answer prompts, and save responses to a log file.

---

## 📂 Project Structure

habit_tracker/
├── habit_tracker.py         # Main entry point
├── habit_editor.py          # Habit creation/editing functions
├── habit_interaction.py     # User input collection
├── habit_utils.py           # Utility functions (I/O, validation, etc.)
├── settings.py              # Global settings and file paths
├── habit_log.txt            # (Auto-created) Habit log file
└── habits.json              # (Auto-created) Habit questions


---

## ⚙️ Features

- Add, edit, or delete your own custom daily habits
- Answer prompts using ✅ / ❌ input
- Automatically logs your responses with timestamps
- Prevents duplicate entries for the same day
- Modular structure with clean function separation
- Optional CSV logging (future upgrade planned)

---

## 🚀 How to Run

```bash
python habit_tracker.py
If it's your first time, you'll be prompted to enter your custom habits.

💾 Log Format (habit_log.txt)
markdown
[2025-04-20]
exercise: Did you exercise? ✅
study: Did you study today? ❌
---------------------------------------------------------------------------
(Future CSV format support planned!)

🧱 Tech Stack
Python 3.x

CLI-based interaction (input())

JSON for habit storage

TXT (or CSV) for log saving

✨ To-Do / Future Plans
- CSV-based logging with description fields

- Optional GUI version

- Command-line options via argparse

- Add test suite using unittest or pytest

- Add summary/stats feature

📌 Author
Made by Kangwoon Lee (이강운)

## Example Habit Questions
- Did you exercise today?
- Did you drink enough water?
- Did you sleep at least 7 hours?

## Requirements
- Python 3.7+

## Future Improvements
- Move to SQLite or CSV storage



---
Made with focus and coffee ☕

