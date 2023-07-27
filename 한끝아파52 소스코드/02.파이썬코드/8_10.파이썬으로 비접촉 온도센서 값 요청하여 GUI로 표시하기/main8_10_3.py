import tkinter
import tkinter.font
import random

def gui_object_temperature_view():
    randData = random.randint(1, 100)
    label.config(text=str(randData))
    window.after(1000,gui_object_temperature_view)

if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("비접촉 온도표시")
    window.geometry("300x200")
    window.resizable(False,False)

    font = tkinter.font.Font(size = 50)
    label=tkinter.Label(window, text="", font=font)
    label.pack()
    
    gui_object_temperature_view()
    
    window.mainloop()