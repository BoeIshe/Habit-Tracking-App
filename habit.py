# habit.py

from datetime import datetime, timedelta

class Habit:
    """A class representing a habit to track."""

    def __init__(self, name: str, frequency: str, start_date: str = None):
        """
        Initialize a new habit.

        :param name: The name of the habit
        :param frequency: The frequency of the habit ("daily" or "weekly")
        :param start_date: The start date for the habit in "YYYY-MM-DD" format (optional)
        """
        self.name = name
        self.frequency = frequency.lower()
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else datetime.now().date()
        self.history = []  # A list to store completion dates
        self.streak = 0  # Current streak of consecutive completions
        self.longest_streak = 0  # Track longest streak achieved
        self.is_broken = False  # Track if the habit was missed

    def mark_complete(self, date: datetime):
        """
        Mark the habit as complete on a specific date.

        :param date: The date of completion
        """
        if date not in self.history:
            self.history.append(date)
            self.history.sort()  # Ensure dates are sorted after each entry
            self.calculate_streak()  # Update streak immediately after each check-off
            self.is_broken = False  # Reset broken status on completion
            print(f"Habit '{self.name}' checked off on {date}. Current streak: {self.streak}")

    def calculate_streak(self):
        """Calculate the streak based on the difference between the start date and the latest check-off date."""
        if not self.history:
            self.streak = 0
            self.longest_streak = 0
            return

        # Get the latest check-off date
        last_completed_date = max(self.history)
        
        if self.frequency == "daily":
            # Streak is the number of days from start date to the last check-off date
            self.streak = (last_completed_date - self.start_date).days + 1
        elif self.frequency == "weekly":
            # Streak is the number of weeks from start date to the last check-off date
            self.streak = ((last_completed_date - self.start_date).days // 7) + 1

        # Update longest streak if the current streak exceeds it
        self.longest_streak = max(self.longest_streak, self.streak)

    def mark_as_broken(self):
        """Mark the habit as 'broken' if missed within the expected period."""
        self.is_broken = True
        self.streak = 0  # Reset streak on breakage

    def get_total_completions(self) -> int:
        """Return the total number of unique completions for the habit."""
        return len(self.history)

    def __str__(self):
        """String representation of the Habit, showing status and streak."""
        status = "Complete" if not self.is_broken else "Broken"
        return (f"Habit(name={self.name}, frequency={self.frequency}, "
                f"start_date={self.start_date}, streak={self.streak}, "
                f"longest_streak={self.longest_streak}, status={status}, completions={self.history})")
