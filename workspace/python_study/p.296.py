from tkinter import*
window = Tk()

def myFunc() :
    if var.get() == 1 :
       lb1.configure(text="파이썬")
    elif var.get() == 2 :
       lb1.configure(text="C++")
    else :
       lb1.configure(text="Java")

var = IntVar()
rb1 = Radiobutton(window, text="파이썬", variable=var, value=1, command=myFunc)
rb2 = Radiobutton(window, text="C++", variable=var, value=2, command=myFunc)
rb3 = Radiobutton(window, text="Java", variable=var, value=3, command=myFunc)
lb1 = Label(window, text="선택한 언어:", fg="red")

rb1.pack(side=TOP)
rb2.pack(side=TOP)
rb3.pack(side=TOP)
lb1.pack()

window.mainloop()