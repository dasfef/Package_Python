from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageTk

## 함수 선언 부분 ##
def displayPhoto() :   
    pass

def func_open() :     
    pass

def func_save() :      
    pass

def func_exit() :
    exit()

def func_zoomin() :      
    pass

def func_zoomout() :    
    pass

def func_mirror1() :    
    pass

def func_mirror2() :      
    pass

def func_rotate() :      
    pass

def func_bright() :      
    pass

def func_embos() :       
    pass

def func_blur() :        
    pass

def func_sketch() :  
    pass

def func_contour() :        
    pass

## 전역 변수 선언 부분 ##
root, canvas = None, None
inPhoto, outPhoto = None, None
inX, inY = 0, 0

## 메인 코드 부분 ##
root = Tk()
root.geometry("500x500")
root.title("포토 에디터")

mainMenu = Menu(root)
root.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_command(label = "파일 저장", command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

effect1Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(1)", menu = effect1Menu)
effect1Menu.add_command(label = "확대", command = func_zoomin)
effect1Menu.add_command(label = "축소", command=func_zoomout)
effect1Menu.add_separator()
effect1Menu.add_command(label = "상하 반전", command = func_mirror1)
effect1Menu.add_command(label = "좌우 반전", command = func_mirror2)
effect1Menu.add_command(label = "회전", command = func_rotate)

effect2Menu = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지 처리(2)", menu = effect2Menu)
effect2Menu.add_command(label = "밝게/어둡게", command = func_bright)
effect2Menu.add_separator()
effect2Menu.add_command(label = "엠보싱", command = func_embos)
effect2Menu.add_command(label="블러링", command=func_blur)
effect2Menu.add_separator()
effect2Menu.add_command(label="연필스케치", command=func_sketch)
effect2Menu.add_command(label = "경계선추출", command = func_contour)
root.mainloop()
