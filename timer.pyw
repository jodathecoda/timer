from tkinter import *
import time
from timeit import default_timer as timer
from datetime import timedelta
from datetime import datetime


root = Tk()
root.iconbitmap("icons\\timer_small.ico")

start = timer()

starting_stack = Entry(text="Starting Roll")
starting_stack.insert(0, "Start Roll")
end_stack = Entry()
end_stack.insert(0, "End Roll")

path_to_file = "C:\\Users\\mvelchev\\Timer\\report.txt"
raw_datetime = datetime.now()
rounded_down_datetime = raw_datetime.replace(microsecond=0)
date_time = str(rounded_down_datetime)

Options = [
"Cash 6",
"Headsup",
"MTT",
"Spin&Go"
] #etc

variable = StringVar(root)
variable.set(Options[0]) # default value
drop_down = OptionMenu(root, variable, *Options)

def stop_action():
    file = open(path_to_file, 'a+')
    file.write(date_time + "   " + starting_stack.get() + "   " + end_stack.get())

    ss = float(end_stack.get())
    es = float(starting_stack.get())

    file.write("  " + str(round(ss - es,2)))
    file.write("\n")

    file.write("\n")
    file.close()
    quit()

def timesnow():
    
    end = timer()

    timelabel.config (text=str(timedelta(seconds = round(end-start))))
    

    timelabel.after(1000, timesnow)

#creatng GUI's
timelabel = Label(root, font=("Courier", 20))
timelabel.grid(row=0, columnspan=10)
timesnow()

starting_stack.grid(row=1,column=0)
end_stack.grid(row=1,column=1)

setbutton = Button(text = "STOP", command = stop_action, bg='sienna')
setbutton.grid(row=2, columnspan=10,sticky=E+W)

root.mainloop()