'''
작성자: 최연웅
작성일: 23.07.21                파일명: day04_library.py
목적: PIL 패키지를 사용한 이미지 라이브러리 실습
'''
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

img = Image.open("C:/Users/user/Desktop/WORK/Python/imgsource/photo/picture01.jpg")

img = img.crop((100, 100, 600, 600))
img.show()