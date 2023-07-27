import tkinter
import tkinter.font

window = tkinter.Tk()
window.title("비접촉 온도표시")
window.geometry("300x200")
window.resizable(False,False)

font = tkinter.font.Font(size = 50)
label=tkinter.Label(window, text="hello", font=font)
label.pack()

window.mainloop()