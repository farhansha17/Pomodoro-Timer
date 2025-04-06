import tkinter as tk
import time

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        self.label = tk.Label(root, text="Pomodoro Timer", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.time_label = tk.Label(root, text="25:00", font=("Helvetica", 36))
        self.time_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(pady=5)

        self.timer_running = False
        self.time_left = 25 * 60

    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.time_label.config(text="Time's up!")
            self.timer_running = False

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def reset_timer(self):
        self.timer_running = False
        self.time_left = 25 * 60
        self.time_label.config(text="25:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()