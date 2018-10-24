from tkinter import*

window = Tk()
window.title("윈도창 연습")
window.geometry("400x100")
window.resizable(width=FALSE, height=FALSE)
label1 = Label(window, text="글자")
label2 = Label(window, text="글자1", font=("궁서체", 30), fg="blue", bg="yellow")
label3 = Label(window, text="글자2", width=20, height=5, anchor=SE, bg="green")

label1.pack()
label2.pack()
label3.pack()




window.mainloop()