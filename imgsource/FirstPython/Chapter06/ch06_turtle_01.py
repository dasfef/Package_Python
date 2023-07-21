import turtle 
import random 

turtle.shape("turtle") 
colors = ['red','green','magenta', 'blue', 'black'] 
turtle.penup() 
turtle.screensize(300,300) 
turtle.setup(330,330) 

for i in range(7) : 
    for k in range(7) : 
        x = i*50 - 150 
        y = k*50 - 150 
        turtle.goto( x, y ) 
        turtle.color(random.choice(colors)) # 색상을 랜덤하게 고름 
        turtle.stamp()                            # 현재 위치에서 도장 찍음 

turtle.done() 
