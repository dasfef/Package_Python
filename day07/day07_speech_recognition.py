import speech_recognition as sr
try:
    while True:
        r = sr.Recognizer()
        audio_file = sr.AudioFile('C:/Users/user/Desktop/WORK/Python/day07/drama_test.wav')
        # with sr.Microphone() as source:/
        with audio_file as source:
            print("음성 입력")
            audio = r.record(source)

            try:
                print("음성변환: " + r.recognize_google(audio, language='ko-KR'))
            except sr.UnknownValueError:
                print("오디오를 이해할 수 없습니다.")
            except sr.RequestError as e:
                print(f"에러 발생: {e}")
except KeyboardInterrupt:
    pass