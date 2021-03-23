from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
TICK = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    label1.config(text="Timer",fg=GREEN)
    label2.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps%8 == 0:
        label1.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps%2 == 0:
        label1.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label1.config(text="Work", fg=GREEN)
        count_down(work_sec)






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    minutes = math.floor(count/60)
    sec = count%60
    if sec<10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{sec}")
    if count>0:
        global timer
        timer = window.after(50,count_down,count-1)
    else:
        start_timer()
        if reps%2==0:
            label2.config(text=TICK*(reps//2))

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

# Label 1
label1 = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME,35,"bold"))
label1.grid(column=1,row=0)


canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
image_data = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image_data)
timer_text = canvas.create_text(102,130,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



# Button

button1 = Button(text="Start",highlightthickness=0, command=start_timer)
button1.grid(column=0,row=2)

button2 = Button(text="Reset",highlightthickness=0, command=reset)
button2.grid(column=2,row=2)

# Label

label2 = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,20,"bold"))
label2.grid(column=1,row=3)


window.mainloop()