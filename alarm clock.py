from tkinter import *
import datetime
import time
import winsound
from threading import Thread

root = Tk()
root.geometry("400x200")
root.configure(bg='black')
root.title("Alarm clock")

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        if current_time == set_alarm_time:
            print("Wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

def threading_func():
    t1 = Thread(target=alarm)
    t1.start()

label_text = "Set Time(24 hours format) \n Hour:  minute:  seconds"
Label(root, text=label_text, font=("Helvetica 9 bold"), fg="white", bg="black").pack()

frame = Frame(root, bg="black")
frame.pack()

hour = StringVar(root)
hours = [str(i).zfill(2) for i in range(25)]
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.config(bg="black",fg="white")
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = [str(i).zfill(2) for i in range(61)]
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.config(bg="black", fg="white")
mins.pack(side=LEFT)

second = StringVar(root)
seconds = [str(i).zfill(2) for i in range(61)]
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.config(bg="black", fg="white")
secs.pack(side=LEFT)

button_text = "Set Alarm"
Button(root, text=button_text, font=("Helvetica 15"), command=threading_func, bg="black", fg="light blue").pack(pady=20)

def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    time_label.config(text=" Current Time(IST): " + current_time + " \n Current Date: " + current_date)
    root.after(1000, update_time)


time_label = Label(root, text="Current Time:", font=("Helvetica 9 bold"), fg="white", bg="black")
time_label.pack(side=BOTTOM)

update_time()

root.mainloop()
