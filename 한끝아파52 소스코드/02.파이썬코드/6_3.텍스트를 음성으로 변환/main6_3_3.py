from gtts import gTTS
from playsound import playsound

file_path = r'6_3.텍스트를 음성으로 변환\나의텍스트.txt'
with open(file_path, 'rt', encoding='UTF8') as f : 
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save(r"6_3.텍스트를 음성으로 변환\나의텍스트.mp3")

playsound(r"6_3.텍스트를 음성으로 변환\나의텍스트.mp3")