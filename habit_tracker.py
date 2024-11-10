# habit_tracker.py

from tracker import HabitTracker
from datetime import datetime

def main():
    tracker = HabitTracker()
    
    while True:
        print("\nHabit Tracker")
        print("1. Add a habit")
        print("2. Mark habit as complete")
        print("3. List all habits")
        print("4. Show analysis for all habits")
        print("5. Show longest habit streak")
        print("6. Show habits with lowest streaks")
        print("7. Delete a habit")
        print("8. Save and exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter habit name: ")
            frequency = input("Enter frequency (daily/weekly): ")
            start_date = input("Enter start date (YYYY-MM-DD) or press Enter for today: ")
            start_date = start_date if start_date else None
            tracker.add_habit(name, frequency, start_date)
        elif choice == "2":
            name = input("Enter habit name to mark complete: ")
            date_input = input("Enter check-off date (YYYY-MM-DD): ")
            tracker.mark_habit_complete(name, date_input)
        elif choice == "3":
            tracker.list_habits()
        elif choice == "4":
            tracker.analyze_habits()
        elif choice == "5":
            tracker.query_longest_streak()
        elif choice == "6":
            tracker.query_lowest_streaks()
        elif choice == "7":
            name = input("Enter the name of the habit to delete: ")
            tracker.delete_habit(name)
        elif choice == "8":
            tracker.save_data()
            print("Exiting the habit tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()