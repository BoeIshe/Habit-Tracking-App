# tracker.py

import json
import os
from datetime import datetime, timedelta
from habit import Habit
from tabulate import tabulate

class HabitTracker:
    """A class to manage habit tracking."""

    def __init__(self, data_file="data/habits.json"):
        self.data_file = data_file
        self.habits = []
        self.load_data()  # Load data when initializing the tracker

    def add_habit(self, name: str, frequency: str, start_date: str = None):
        """Add a new habit to the tracker."""
        start_date = start_date.strip() if start_date else None
        habit = Habit(name, frequency, start_date)
        self.habits.append(habit)
        print(f"Habit '{name}' added with start date {habit.start_date}.")

    def mark_habit_complete(self, name: str, date_input: str):
        """Mark a habit as complete for a specific date."""
        date = datetime.strptime(date_input, "%Y-%m-%d").date()
        habit = next((h for h in self.habits if h.name == name), None)
        if habit:
            habit.mark_complete(date)
            print(f"Updated habit '{name}' after check-off on {date}. Current streak: {habit.streak}")
        else:
            print(f"Habit '{name}' not found.")

    def delete_habit(self, name: str):
        """Delete a habit and all its details by name, then save the updated data."""
        initial_count = len(self.habits)
        self.habits = [habit for habit in self.habits if habit.name != name]
        
        if len(self.habits) < initial_count:
            print(f"Habit '{name}' has been deleted.")
            self.save_data()  # Save immediately to update the database
        else:
            print(f"Habit '{name}' not found.")

    def list_habits(self):
        """Display a simple list of all habits with basic information, separated by frequency."""
        daily_habits = []
        weekly_habits = []
        
        for habit in self.habits:
            entry = [
                habit.name,
                habit.start_date.strftime("%Y-%m-%d"),
                habit.streak
            ]
            if habit.frequency == "daily":
                daily_habits.append(entry)
            elif habit.frequency == "weekly":
                weekly_habits.append(entry)

        headers = ["Habit Name", "Start Date", "Current Streak"]
        
        print("\nDaily Habits:")
        print(tabulate(daily_habits, headers=headers, tablefmt="pretty"))
        
        print("\nWeekly Habits:")
        print(tabulate(weekly_habits, headers=headers, tablefmt="pretty"))

    def analyze_habits(self):
        """Analyze and display details for each habit."""
        table = []

        for habit in self.habits:
            habit_name = habit.name
            periodicity = "Daily" if habit.frequency == "daily" else "Weekly"
            start_date = habit.start_date.strftime("%Y-%m-%d")
            
            if habit.history:
                last_completed_date = max(habit.history)
                if habit.frequency == "daily":
                    habit.streak = (last_completed_date - habit.start_date).days + 1
                elif habit.frequency == "weekly":
                    habit.streak = ((last_completed_date - habit.start_date).days // 7) + 1
            else:
                habit.streak = 0

            check_off_dates = ", ".join([date.strftime("%Y-%m-%d") for date in habit.history])
            missed_check_ins = self.calculate_missed_check_ins(habit)

            table.append([
                habit_name,
                periodicity,
                start_date,
                habit.streak,
                check_off_dates,
                missed_check_ins
            ])

        headers = [
            "Habit Name", "Periodicity", "Start Date", "Streak",
            "Check-Off Dates", "Missed Check-Ins"
        ]
        print(tabulate(table, headers=headers, tablefmt="pretty"))

    def calculate_missed_check_ins(self, habit):
        """Calculate the number of missed check-ins based on the habit's frequency."""
        if not habit.history:
            return 0

        sorted_history = sorted(habit.history)
        missed_check_ins = 0
        period = timedelta(days=1 if habit.frequency == "daily" else 7)

        for i in range(1, len(sorted_history)):
            expected_next_date = sorted_history[i - 1] + period
            while expected_next_date < sorted_history[i]:
                missed_check_ins += 1
                expected_next_date += period

        return missed_check_ins

    def query_longest_streak(self):
        """Find and display the habit with the longest streak, considering frequency."""
        if not self.habits:
            print("No habits available to analyze.")
            return

        longest_streak_habit = max(
            self.habits,
            key=lambda h: h.streak * (7 if h.frequency == "weekly" else 1),
            default=None
        )
        
        if longest_streak_habit and longest_streak_habit.streak > 0:
            print(f"The habit with the longest streak is '{longest_streak_habit.name}' "
                  f"with a streak of {longest_streak_habit.streak} "
                  f"{'weeks' if longest_streak_habit.frequency == 'weekly' else 'days'}.")
        else:
            print("No habits with a streak found.")

    def query_lowest_streaks(self):
        """Display the three habits with the lowest streaks, considering frequency."""
        if not self.habits:
            print("No habits available to analyze.")
            return

        sorted_habits = sorted(
            self.habits,
            key=lambda h: h.streak * (7 if h.frequency == "weekly" else 1)
        )
        lowest_streaks = sorted_habits[:3]

        print("\nThree habits with the lowest streaks (struggling habits):")
        for habit in lowest_streaks:
            print(f"Habit: {habit.name}, Streak: {habit.streak} "
                  f"{'weeks' if habit.frequency == 'weekly' else 'days'}")

    def save_data(self):
        """Save habit data to a JSON file, creating the directory if it doesn't exist."""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        data = [
            {"name": habit.name, "frequency": habit.frequency, "start_date": habit.start_date.isoformat(),
             "history": [date.isoformat() for date in habit.history]}
            for habit in self.habits
        ]
        with open(self.data_file, "w") as f:
            json.dump(data, f)

    def load_data(self):
        """Load habit data from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                for item in data:
                    habit = Habit(item["name"], item["frequency"], start_date=item["start_date"])
                    habit.history = [datetime.fromisoformat(date).date() for date in item["history"]]
                    self.habits.append(habit)
            print("Habit data loaded successfully.")
        else:
            print("No habit data found. Starting with an empty tracker.")