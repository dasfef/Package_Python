'''
작성자: 최연웅
작성일: 23.07.21                파일명: day04_turtle.py
목적: 바다거북과 모래거북(슈퍼클래스 / 서브클래스) 실습
'''
import turtle

class SeaTurtle(turtle.Turtle):
    name = ""
    body = None

    def __init__(self):
        self.body = turtle.Turtle('triangle')           # 모양을 삼각형으로 지정
        self.body.color("blue")
        self.name = "바다거북"
    
    def swim(self, x, y):
        self.body.goto(x, y)

class SandTurtle(turtle.Turtle):
    name = ""
    body = None

    def __init__(self):
        self.body = turtle.Turtle('circle')           # 모양을 삼각형으로 지정
        self.body.color("red")
        self.name = "모래거북"
    
    def walk(self, x, y):
        self.body.goto(x, y)

SeaTut = SeaTurtle()
SandTut = SandTurtle()

SeaTut.swim(100, 100)
SeaTut.body.write(SeaTut.name, font=("Arial", 20))

SandTut.walk(-100, 100)
SandTut.body.write(SandTut.name, font=("Arial", 20))