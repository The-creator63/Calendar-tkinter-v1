#importing the libraries
from tkinter import*
import calendar

#Functions for showing the calendar
def show_cal():
    new_root = Tk()
    new_root.config(background = "white")
    new_root.title("calendar")
    new_root.geometry("550x600")

    get_year = int(year.get())
    cal_content = calendar.calendar(get_year)
    cal_year = Label(new_root,text = cal_content,font = ("Arial", 10, "bold"))
    cal_year.grid(row = 5,column = 1,padx = 20)
    new_root.mainloop()

#create the main window
if __name__ == "__main__":
    root = Tk()
    root.config(background = "white")
    root.title("CALENDAR")
    root.geometry("250x150")
    cl = Label(root,text = "CALENDAR",bg = "yellow", fg = "black", font = ("Times", 25, "bold"))
    