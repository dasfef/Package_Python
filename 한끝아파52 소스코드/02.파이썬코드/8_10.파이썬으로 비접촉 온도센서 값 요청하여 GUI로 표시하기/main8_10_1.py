import tkinter

window = tkinter.Tk()
window.title("비접촉 온도표시")
window.geometry("300x200")
window.resizable(False,False)

label=tkinter.Label(window, text="hello")
label.pack()

window.mainloop()