import math
from tkinter import *

#CONSTANTS 
YELLOW = "#f7f5dd"
PINK = "#e2979c"
GREEN = "#9bdeac"
RED = "#e7305b"
FONT_NAME = "courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
REPS = 0
timer = None

#TIMER RESET 
def reset_timer():
   window.after_cancel(timer)
   canvas.itemconfig(timer_text, text="00:00")
   timer_title.config(text= "Timer", fg=GREEN)
   check_mark.config(text="")
   global REPS
   REPS = 0

#TIMER MECHANISM
def start_time():
  global REPS
  REPS += 1

  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60


  #if 8th rep:
  if REPS % 8 == 0:
    count_down(long_break_sec)
    timer_title.config(text= "Break", fg=RED)
  #even reps:
  elif REPS % 2 == 0:
    count_down(short_break_sec)
    timer_title.config(text= "Break", fg=PINK)
  #odd reps:
  else:
    count_down(work_sec)
    timer_title.config(text= "Work", fg=GREEN)


#COUNTDOWN MECHANISM 
def count_down(count):
  count_min =  math.floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"

  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_time()
    mark = ""
    work_sessions = math.floor(REPS/2)
    for _ in range(work_sessions):
      mark += "✔"
    check_mark.config(text=mark)

#UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="img/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



timer_title = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_title.grid(column=1, row=0)

start_btn = Button(text="Start", highlightthickness=0, command=start_time)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark = Label( fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()