

# Habit Tracker
This Habit Tracker application helps users manage and track their daily and weekly habits. Users can add, update, analyze, and delete habits, as well as view their longest and shortest streaks. The app saves habit data to a JSON file, ensuring persistence between sessions.

 Features
- Add a Habit: Create a new habit with a name, frequency (daily or weekly), and optional start date.
- Mark Habit as Complete: Record completion dates for each habit.
- View All Habits: List all habits, separated by daily and weekly frequency.
- Analyze Habits: View detailed analytics for each habit, including start date, current streak, missed check-ins, and completion history.
- View Longest Streak: Display the habit with the longest streak, accounting for daily and weekly habits.
- View Shortest Streaks: Display the three habits with the shortest streaks (struggling habits).
- Delete a Habit: Permanently delete a habit from the tracker.
- Data Persistence: All habit data is stored in `data/habits.json`, allowing the user’s progress to be saved between sessions.

 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/habit-tracker.git
   cd habit-tracker
   
2. Install dependencies:
   This project requires Python 3.7 or higher. Additionally, install required packages using pip:
   ```bash
   pip install tabulate
   ```
3. Run the application:
   Run the `habit_tracker.py` file to start the Habit Tracker:
   ```bash
   python habit_tracker.py
   ```
 Usage
1. Start the App: Run the `habit_tracker.py` file in your terminal to access the main menu.
2. Choose Options:
   - Select options by entering the corresponding number at the prompt.
   - Options include adding, marking, viewing, analyzing, and deleting habits.
3. Data Persistence: All data is saved automatically in `data/habits.json` to persist between sessions.

# Example Menu Options
1. Add a Habit: 
   - Enter habit name, frequency (daily/weekly), and optional start date (YYYY-MM-DD). If no start date is provided, today’s date is used.
   
2. Mark Habit as Complete:
   - Enter the habit name and completion date (YYYY-MM-DD).
   
3. List All Habits:
   - View all habits grouped by daily and weekly frequency.
   
4. Analyze Habits:
   - View a table of details for each habit, including streak, missed check-ins, and completion dates.
   
5. View Longest Streak:
   - See the habit with the longest streak.
   
6. View Shortest Streaks:
   - Display the three habits with the shortest streaks, categorized as “struggling habits.”
   
7. Delete a Habit:
   - Enter the name of the habit to permanently delete it from the tracker.

8. Exit and Save:
   - Save all data and exit the application.

 Project Structure

```plaintext
habit-tracker/
├── data/
│   └── habits.json             # Data file for storing habit information
├── habit.py                    # Habit class defining habit properties and methods
├── tracker.py                  # Main HabitTracker class handling habit management
└── habit_tracker.py            # Main script to run the Habit Tracker app
```

 Technical Details
- Habit Class (`habit.py`): Defines a habit with attributes such as `name`, `frequency`, `start_date`, `history` of check-offs, and `streak`. Methods include `mark_complete` to record a completion.
- HabitTracker Class (`tracker.py`): Manages all habits, providing methods to add, mark complete, delete, list, and analyze habits, as well as save/load data to/from `habits.json`.
- Data Storage (`data/habits.json`): JSON file stores all habit data persistently, allowing habit tracking across sessions.

 Requirements
- Python 3.7+
- Tabulate (for table display in the terminal)

 Future Enhancements
- Add support for additional frequencies (e.g., monthly habits).
- Add graphical user interface (GUI) for ease of use.
- Integrate reminders and notifications for missed habits.

 License
This project is open-source 

 Author Bothwell Shumba


