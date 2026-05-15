import tkinter as tk
from tkinter import messagebox
from question import quiz_data


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz Platform")
        self.root.geometry("700x500")
        self.root.config(bg="#f4f4f4")

        self.question_index = 0
        self.score = 0

        self.title_label = tk.Label(
            root,
            text="Online Quiz Platform",
            font=("Arial", 24, "bold"),
            bg="#f4f4f4",
            fg="#2c3e50"
        )
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(
            root,
            text="",
            font=("Arial", 16),
            wraplength=600,
            justify="left",
            bg="#f4f4f4"
        )
        self.question_label.pack(pady=20)

        self.selected_option = tk.StringVar()

        self.option_buttons = []
        for _ in range(4):
            rb = tk.Radiobutton(
                root,
                text="",
                variable=self.selected_option,
                value="",
                font=("Arial", 14),
                bg="#f4f4f4",
                anchor="w",
                padx=20
            )
            rb.pack(fill="x", padx=50, pady=5)
            self.option_buttons.append(rb)

        self.next_button = tk.Button(
            root,
            text="Next",
            font=("Arial", 14, "bold"),
            bg="#3498db",
            fg="white",
            command=self.next_question,
            width=10
        )
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.question_index < len(quiz_data):
            current = quiz_data[self.question_index]
            self.question_label.config(
                text=f"Q{self.question_index + 1}: {current['question']}"
            )

            self.selected_option.set(None)

            for i, option in enumerate(current['options']):
                self.option_buttons[i].config(text=option, value=option)
        else:
            self.show_result()

    def next_question(self):
        selected = self.selected_option.get()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select an option before proceeding."
            )
            return

        correct_answer = quiz_data[self.question_index]['answer']

        if selected == correct_answer:
            self.score += 1

        self.question_index += 1
        self.load_question()

    def show_result(self):
        total_questions = len(quiz_data)
        percentage = (self.score / total_questions) * 100

        messagebox.showinfo(
            "Quiz Completed",
            f"Your Score: {self.score}/{total_questions}\n"
            f"Percentage: {percentage:.2f}%"
        )

        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


