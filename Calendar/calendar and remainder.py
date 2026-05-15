import tkinter as tk
from tkinter import ttk, messagebox
import calendar
from datetime import datetime
import json
import os

REMINDER_FILE = "reminders.json"


class CalendarReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar and Reminder App")
        self.root.geometry("900x600")
        self.root.configure(bg="white")

        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        
        self.reminders = self.load_reminders()

        self.create_widgets()
        self.show_calendar()

    # ----------------------------
    # Load reminders from file
    # ----------------------------
    def load_reminders(self):
        if os.path.exists(REMINDER_FILE):
            with open(REMINDER_FILE, "r") as file:
                return json.load(file)
        return {}

    # ----------------------------
    # Save reminders to file
    # ----------------------------
    def save_reminders(self):
        with open(REMINDER_FILE, "w") as file:
            json.dump(self.reminders, file, indent=4)

    # ----------------------------
    # Create UI
    # ----------------------------
    def create_widgets(self):
        # Top frame
        top_frame = tk.Frame(self.root, bg="white")
        top_frame.pack(pady=10)

        tk.Button(top_frame, text="<< Previous",
                  command=self.prev_month,
                  bg="#3498db", fg="white",
                  width=12).grid(row=0, column=0, padx=10)

        self.title_label = tk.Label(
            top_frame,
            text="",
            font=("Arial", 20, "bold"),
            bg="white"
        )
        self.title_label.grid(row=0, column=1, padx=20)

        tk.Button(top_frame, text="Next >>",
                  command=self.next_month,
                  bg="#3498db", fg="white",
                  width=12).grid(row=0, column=2, padx=10)

        # Calendar frame
        self.calendar_frame = tk.Frame(self.root, bg="white")
        self.calendar_frame.pack(pady=10)

        # Reminder frame
        reminder_frame = tk.LabelFrame(
            self.root,
            text="Add Reminder",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        reminder_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(reminder_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(reminder_frame, width=15)
        self.date_entry.grid(row=0, column=1, padx=5)

        tk.Label(reminder_frame, text="Reminder:").grid(row=0, column=2, padx=5)
        self.reminder_entry = tk.Entry(reminder_frame, width=40)
        self.reminder_entry.grid(row=0, column=3, padx=5)

        tk.Button(
            reminder_frame,
            text="Add Reminder",
            command=self.add_reminder,
            bg="green",
            fg="white"
        ).grid(row=0, column=4, padx=10)

        # Reminder list
        list_frame = tk.LabelFrame(
            self.root,
            text="Saved Reminders",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.reminder_listbox = tk.Listbox(list_frame, font=("Arial", 11))
        self.reminder_listbox.pack(fill="both", expand=True)

        tk.Button(
            list_frame,
            text="Delete Selected Reminder",
            command=self.delete_reminder,
            bg="red",
            fg="white"
        ).pack(pady=5)

        self.update_reminder_list()

    # ----------------------------
    # Show calendar
    # ----------------------------
    def show_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        self.title_label.config(
            text=f"{calendar.month_name[self.current_month]} {self.current_year}"
        )

        # Days header
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for col, day in enumerate(days):
            tk.Label(
                self.calendar_frame,
                text=day,
                font=("Arial", 10, "bold"),
                width=10,
                bg="#dfe6e9"
            ).grid(row=0, column=col, padx=1, pady=1)

        month_calendar = calendar.monthcalendar(
            self.current_year,
            self.current_month
        )

        for row, week in enumerate(month_calendar, start=1):
            for col, day in enumerate(week):
                if day == 0:
                    tk.Label(
                        self.calendar_frame,
                        text="",
                        width=10,
                        height=3,
                        bg="white"
                    ).grid(row=row, column=col, padx=1, pady=1)
                else:
                    date_str = f"{self.current_year}-{self.current_month:02d}-{day:02d}"

                    # Highlight if reminder exists
                    bg_color = "#ffeaa7" if date_str in self.reminders else "#74b9ff"

                    btn = tk.Button(
                        self.calendar_frame,
                        text=str(day),
                        width=10,
                        height=3,
                        bg=bg_color,
                        command=lambda d=date_str: self.select_date(d)
                    )
                    btn.grid(row=row, column=col, padx=1, pady=1)

    # ----------------------------
    # Select date
    # ----------------------------
    def select_date(self, date_str):
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, date_str)

        if date_str in self.reminders:
            messagebox.showinfo(
                "Reminder",
                f"{date_str}\n\n{self.reminders[date_str]}"
            )

    # ----------------------------
    # Add reminder
    # ----------------------------
    def add_reminder(self):
        date = self.date_entry.get().strip()
        reminder = self.reminder_entry.get().strip()

        if not date or not reminder:
            messagebox.showwarning(
                "Input Error",
                "Please enter both date and reminder."
            )
            return

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(
                "Invalid Date",
                "Please enter date in YYYY-MM-DD format."
            )
            return

        self.reminders[date] = reminder
        self.save_reminders()

        self.reminder_entry.delete(0, tk.END)
        self.update_reminder_list()
        self.show_calendar()

        messagebox.showinfo("Success", "Reminder added successfully!")

    # ----------------------------
    # Update reminder list
    # ----------------------------
    def update_reminder_list(self):
        self.reminder_listbox.delete(0, tk.END)

        for date in sorted(self.reminders.keys()):
            self.reminder_listbox.insert(
                tk.END,
                f"{date} - {self.reminders[date]}"
            )

    # ----------------------------
    # Delete reminder
    # ----------------------------
    def delete_reminder(self):
        selected = self.reminder_listbox.curselection()

        if not selected:
            messagebox.showwarning(
                "Selection Error",
                "Please select a reminder to delete."
            )
            return

        item = self.reminder_listbox.get(selected[0])
        date = item.split(" - ")[0]

        del self.reminders[date]
        self.save_reminders()
        self.update_reminder_list()
        self.show_calendar()

        messagebox.showinfo("Deleted", "Reminder deleted successfully!")

    # ----------------------------
    # Previous month
    # ----------------------------
    def prev_month(self):
        self.current_month -= 1
        if self.current_month == 0:
            self.current_month = 12
            self.current_year -= 1
        self.show_calendar()

    # ----------------------------
    # Next month
    # ----------------------------
    def next_month(self):
        self.current_month += 1
        if self.current_month == 13:
            self.current_month = 1
            self.current_year += 1
        self.show_calendar()


# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarReminderApp(root)
    root.mainloop()