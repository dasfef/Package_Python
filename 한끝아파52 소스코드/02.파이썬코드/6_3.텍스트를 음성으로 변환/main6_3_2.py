from gtts import gTTS
from playsound import playsound

text = "안녕하세요. 오늘은 날씨가 좋네요. 행복한 하루되세요"

tts = gTTS(text=text, lang='ko')
tts.save(r"6_3.텍스트를 음성으로 변환\hi.mp3")

playsound(r"6_3.텍스트를 음성으로 변환\hi.mp3")