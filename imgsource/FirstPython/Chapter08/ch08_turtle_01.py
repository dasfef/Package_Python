import turtle
import random


def getXYAS() :
    x, y, angle, size = 0, 0, 0, 0
    x  = random.randint(-250, 250)
    y = random.randint(-250, 250)
    size = random.randint(10, 50)
    return x, y, size

## 전역 변수 선언 부분 ##

koreanStr = """ 나랏말싸미 듕귁에 달아 문자와로 서르 사맛디 아니할쎄
이런 젼차로 어린 백셩이 니르고져 홀 배 이셔도
마참내 제 뜨들 시러펴디 몯 할 노미 하니라
내 이랄 위하야 어엿비 너겨 새로 스믈 여듧 짜랄 맹가노니
사람마다 해여 수비 니겨 날로 쑤메 뼌한킈 하고져 할따라미니라
"""
colorList = ["red", "green", "blue", "black", "magenta", "orange", "gray"]
tX, tY, txtSize = 0,0,0

## 메인 코드 부분 ##
turtle.shape('turtle')
turtle.setup(550, 550)
turtle.screensize(500, 500)
turtle.penup()

turtle.speed(5)


for  ch  in koreanStr :
    tX, tY, txtSize  = getXYAS() 
    color = random.choice(colorList)
    turtle.goto(tX,tY)
    turtle.pencolor(color)
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))

turtle.done()
