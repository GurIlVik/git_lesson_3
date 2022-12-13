from datetime import datetime as dt
from datetime import timedelta
import time
from tkinter import *

def date_now(windows):
    dt_now = dt.now().strftime("%d/%m/%y %H:%M:%S")
    Label_time_now = Label(windows, text=dt_now)
    Label_time_now.grid(column=0, columnspan=3, row= 1)
    windows.after(1000, date_now, windows)

def date_new_yers(windows):
    dt_stop = dt(2023, 1, 1, 0, 0, 0,)
    # dt_now = dt.now().strftime("%d/%m/%y %H:%M:%S")
    dt_wivid = dt_stop - dt.now()
    print(dt_wivid.microseconds)
    print(dt_wivid.days)
    print(dt_wivid.seconds)
    dt_wivid -= timedelta(microseconds = dt_wivid.microseconds)
    # dt_wivid = dt_wivid.strftime("%d/%m/%y %H:%M:%S")
    # print(dt_wivid.strftime("%d/%m/%y %H:%M:%S"))
    seconds_to_ny = dt_wivid.seconds + dt_wivid.days * 86400
    Label_time_yer1 = Label(windows, text=seconds_to_ny)
    Label_time_yer1.grid(column=0, columnspan=3, row= 3)
    Label_time_yer = Label(windows, text=dt_wivid)
    Label_time_yer.grid(column=0, columnspan=3, row= 4)
    windows.after(1000, date_new_yers, windows)

# class day_new_yer:


def start_prog():
    windows = Tk()
    windows.title('Счетчик времени')
    windows.geometry('400x400')
    lab_n= Label(windows, text='До Нового Года осталось:')
    lab_n.grid(column=1, row=2)
    date_now(windows)
    date_new_yers(windows)
    windows.mainloop()

if __name__ == "__main__":
    start_prog()