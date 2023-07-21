'''
작성자: 최연웅
작성일: 23.07.21                파일명: day04_class(2).py
목적: 선의 길이 측정하는 클래스 실습
'''
class Line:
    length = 0
    
    def __init__(self, length):
        self.length = length
        print(f"{self.length}로 길이 설정")

    def __del__(self):
        print(f"{self.length}길이의 선이 삭제됩니다.")

    def __add__(self, other):
        return (self.length + other.length)

    def __lt__(self, other):
        return self.length < other.length
    
    def __eq__(self, other):
        return self.length == other.length
    
line1 = Line(10)
line2 = Line(5)

print(f"두 선의 길이의 합: {line1 + line2}")

if(line1 < line2):
    print("선 2가 더 깁니다.")
    del(line1)
elif(line1 == line2):
    print("두 선의 길이가 같습니다.")
else:
    print("선 1이 더 깁니다.")
    del(line2)