from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
checkmark = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer
    global reps
    global checkmark_list
    window.after_cancel(str(timer))
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_list = []
    checkmark_label.config(text="".join(checkmark_list))

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        timer_label.config(fg=RED, text="WORK")
        countdown(WORK_MIN * 60)
    elif reps % 8 == 0:
        timer_label.config(fg=PINK, text="BREAK")
        countdown(LONG_BREAK_MIN * 60)
    else:
        timer_label.config(fg=GREEN, text="BREAK")
        countdown(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    minutes = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text,
                      text=f"{minutes}:{seconds}")  # you configure an item of the canvas just give the name of it
    # and the parameters
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        global checkmark_list
        if reps % 2 != 0:
            checkmark_list.append(checkmark)
            checkmarks = "".join(checkmark_list)
            checkmark_label.config(text=checkmarks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=125, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

checkmark_list = []
checkmark_label = Label(bg=YELLOW, fg=GREEN, font=("", 15))
checkmark_label.grid(row=3, column=1)

window.mainloop()
