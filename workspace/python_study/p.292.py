from tkinter import*
window = Tk()

photo=PhotoImage(file="venv/gif/dog3.gif")
label1=Label(window,image = photo)

label1.pack()

window.mainloop()