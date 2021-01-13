from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
run_time = 0
tim = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    windows.after_cancel(tim)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global run_time
    if run_time == 0 or run_time == 2 or run_time == 4 or run_time == 6:
        timer_label.config(text="Work", fg=RED)
        count_down(WORK_MIN * 60)
        mark = " "
        for _ in range(run_time):
            mark += "✔"
            checkmark_label.config(text=mark)
    elif run_time == 1 or run_time == 3 or run_time == 5:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        mark = " "
        for _ in range(run_time):
            mark += "✔"
            checkmark_label.config(text=mark)
    elif run_time == 7:
        timer_label.config(text="Break", fg=GREEN)
        count_down(LONG_BREAK_MIN * 60)
        mark = " "
        for _ in range(run_time):
            mark += "✔"
            checkmark_label.config(text=mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global tim
    minute = math.floor(count / 60)
    sec = count % 60
    if sec >= 0 and minute >= 0:
        canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
        if sec < 10:
            canvas.itemconfig(timer_text, text=f"{minute}:0{sec}")
        if minute == 0 and sec == 0:
            global run_time
            run_time += 1
            start_timer()
        tim = windows.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)
# label for Timer text
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
# label for checkmark
checkmark_label = Label(fg=GREEN, bg=YELLOW)
# canvas for the tomato picture
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=my_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# created a button called start
start_button = Button(text="Start", bg=YELLOW, command=start_timer)
# created a button called restart
reset_button = Button(text="Reset", bg=YELLOW, command=reset)
# grid all of them together
timer_label.grid(row=0, column=3)
canvas.grid(row=1, column=3)
start_button.grid(row=2, column=1)
reset_button.grid(row=2, column=4)
checkmark_label.grid(row=3, column=3)
windows.mainloop()
