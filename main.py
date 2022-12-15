from datetime import datetime as dt
from datetime import timedelta
from tkinter import *
from functools import partial

def get_the_number_of_the_day_of_the_week(show):
    result = ''
    for i in show:
        if i >= '0' and i <='9':
            result += i
        elif i == '-':
            pass
        else:
            break
    return result

def date_now(windows):
    dt_now = dt.now().strftime("%d/%m/%y %H:%M:%S")
    Label_time_now = Label(windows, text=dt_now)
    Label_time_now.grid(column=0, columnspan=3, row= 1)
    windows.after(1000, date_now, windows)
    
def date_13_dec():
    return dt(2022, 12, 13, 0, 0, 0)   

def date_new_yers(windows):
    dt_stop = dt(2023, 1, 1, 0, 0, 0,)
    dt_wivid = dt_stop - dt.now()
    dt_wivid -= timedelta(microseconds = dt_wivid.microseconds)
    seconds_to_ny = dt_wivid.seconds + dt_wivid.days * 86400
    Label_time_yer1 = Label(windows, text=seconds_to_ny)
    Label_time_yer1.grid(column=0, columnspan=3, row= 3)
    Label_time_yer = Label(windows, text=dt_wivid)
    Label_time_yer.grid(column=0, columnspan=3, row= 4)
    Label_weekday = Label(windows, text = '13-е декабря 2022 года был вторник')
    Label_weekday.grid(column=0, columnspan=3, row= 5)
    windows.after(1000, date_new_yers, windows)
 
def weekday_l(num=1): 
    result = {1:'Среда', 2:'Четверг', 3:"Пятница", 4:'Суббота', 5:"Воскресенье", 6:'Понедельник', 0:'Вторник'}
    list_day = []
    if num == 1:
        return result
    else:
        for value in result.values():
            list_day.append(value)
    return list_day
  
def weekday(titl1, titl2, titl3, windows):
    year = int(titl1.get())
    month = int(titl2.get())
    day = int(titl3.get())
    dict_weekday = weekday_l(num=1)
    date_user = dt(year, month, day, 0, 0, 0)
    show = str(date_user - date_13_dec())
    num_d = get_the_number_of_the_day_of_the_week(show)
    num_d = int(num_d)
    num_d = num_d % 7
    lb_weekday = Label(windows, text= f'День недели указанного числа: {dict_weekday[num_d]}')
    lb_weekday.grid(column=0, columnspan=3, row= 20)
 
def the_cycle_of_obtaining_years(number_from_the_dictionary):
    date_lesson = date_13_dec()
    count_top = 5
    count_bootom = 5
    result = []
    year_top = 2023
    year_bootom = 2023
    delta2023 =  dt(year_top, 1, 1) - date_lesson
    if delta2023.days % 7 == number_from_the_dictionary:
        result.append(2023)
    while count_top >= 0 and count_bootom > 0:
        if count_top >= count_bootom:
            for i in range(1, 30):
                year_top += 1
                # num_tech_year = dt(year_top, 1, 1)
                delta = dt(year_top, 1, 1) - date_lesson
                delta = delta.days
                if delta % 7 == number_from_the_dictionary:
                    result.append(year_top)
                    count_top -= 1
                    break
                else:
                    pass
        else:
            for i in range(1, 30):
                year_bootom -= 1
                delta = date_lesson - dt(year_bootom, 1, 1)
                delta = delta.days
                if (delta + 2) % 7 == number_from_the_dictionary:
                    result.append(year_bootom)
                    count_bootom -= 1
                    break
                else:
                    pass       
    return result
             
def year_weekday(week_list_show, windows): 
    d = ''
    for i in week_list_show.curselection():
        d = week_list_show.get(i)
    number_from_the_dictionary = 0
    dict_weekday = weekday_l(num=1)
    for key, val in dict_weekday.items():
        if d == val:
            number_from_the_dictionary = key
    result = the_cycle_of_obtaining_years(number_from_the_dictionary)
    lb_weekday = Label(windows, text= f'Список лет начинающихся со {d}:{result}')
    lb_weekday.grid(column=0, columnspan=3, row= 21)
    
def label_batton(windows):
    lab_m1 = Label(windows, text = 'Укажите год:')
    lab_m1.grid(column=0, row=6)
    lab_m2 = Label(windows, text = 'Укажите месяц:')
    lab_m2.grid(column=1, row=6)
    lab_m3 = Label(windows, text = 'Укажите день:')
    lab_m3.grid(column=2, row=6)
    titl1 = Entry(windows, bg='Light Blue', width=4,)
    titl1.grid(column=0, row=7)
    titl2 = Entry(windows, bg='Light Blue', width=2,)
    titl2.grid(column=1, row=7)
    titl3 = Entry(windows, bg='Light Blue', width=2,)
    titl3.grid(column=2, row=7)
    button1 = Button(windows, text='Ввести что бы получить день недели', 
                     command=partial(weekday, titl1, titl2, titl3, windows))
    button1.grid(column=0, columnspan=3, row= 8)
    lab_m4 = Label(windows, text = 'Укажите день недели:')
    lab_m4.grid(column=0, columnspan=2, row=9)
    week_list  = weekday_l(num=2)
    week_list_var = Variable(value=week_list)
    week_list_show = Listbox(windows, height=2, width=20, listvariable=week_list_var)
    week_list_show.grid(column=2,  row=9) 
    for elem in week_list:
        week_list_show.insert(END, elem)
    button2 = Button(windows, text='при нажатии получите года начинающиеся с этого дня', 
                     command=partial(year_weekday, week_list_show, windows))
    button2.grid(column=0, columnspan=3, row= 11)

def start_prog():
    windows = Tk()
    windows.title('Счетчик времени')
    windows.geometry('750x400')
    lab_n= Label(windows, text='До Нового Года осталось:')
    lab_n.grid(column=1, row=2)
    label_batton(windows)
    date_now(windows)
    date_new_yers(windows)
    windows.mainloop()

if __name__ == "__main__":
    start_prog()