import turtle

turtle.shape("turtle")
turtle.penup()

while True :
    x = int(input("X 위치 ==>"))
    y = int(input("Y 위치 ==>"))
    text= input("쓰고 싶은 글자 ==>")
    
    turtle.goto(x,y)
    turtle.write(text, font=("Arial", 30))

turtle.done()
