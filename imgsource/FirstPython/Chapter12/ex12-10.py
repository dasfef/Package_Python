from tkinter import *
root = Tk()

button1 = Button(root, text="버튼1")
button2 = Button(root, text="버튼2")
button3 = Button(root, text="버튼3")

button1.pack(side=BOTTOM) 
button2.pack(side=BOTTOM) 
button3.pack(side=BOTTOM) 

root.mainloop()
