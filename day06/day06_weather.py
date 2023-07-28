'''
날짜: 2023.07.27
목표: 기상청 홈페이지 html 사용하여 청주 오창읍 온도 FND 출력 / pm10에 따른 RGB 출력
작성자: 최연웅
'''
import requests
import re
import time
import serial
import serial.tools.list_ports

def send_fnd(data):
    sendData = f"FND={data}\n"
    my_serial.write(sendData.encode())

def send_RGB(red, green, blue):
    sendData = f"RGB={red},{green},{blue}\n"
    my_serial.write(sendData.encode())

def main():
    try:
        while True:
            # url = "https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4311425300"         # 오창읍의 동네예보
            link = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey="
            serviceKey = "74c5ZdkDfPARwepbwip9XOy3B2OYJkUBxj12RhzlgPLU34nfU9FiPmprQPybkilNGZS10zlDq1jRt9PG6HH0uQ%3D%3D"
            afterLink = "&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%B6%A9%EB%B6%81&ver=1.0"
            url = link + serviceKey + afterLink
            response = requests.get(url)

            temp = re.findall(r"<temp>(.+)</temp>", response.text)                      # 온도데이터
            humi = re.findall(r"<reh>(.+)</reh>", response.text)                        # 습도데이터
            weather = re.findall(r"<wfKor>(.+)</wfKor>", response.text)                 # 날씨: 맑음, 흐림, 비, 소나기 등...
            pm10 = re.findall(r"<pm10Value>(.+)</pm10Value>", response.text)            # pm10 미세먼지 농도
            pm25 = re.findall(r"<pm25Value>(.+)</pm25Value>", response.text)            # pm2.5 미세먼지 농도
            station = re.findall(r"<stationName>(.+)</stationName>", response.text)     # 각 기기가 위치한 역 이름

            # print(f"기온={temp[0]}, 습도={humi[0]}, 날씨={weather[0]}")
            findStation = station.index("오창읍")
            print(f"찾는 지역의 인덱스: {findStation}")
            print(f"{station[findStation]}의 pm10={pm10[findStation]}, pm25={pm25[findStation]}")

            pm10 = int(pm10[findStation])
            # pm25 = int(pm25[findStation])
            send_fnd(pm10)

            if pm10<=30:
                send_RGB(0,255,0)
            elif pm10 >= 31 and pm10 <= 80:
                send_RGB(0,0,255)
            elif pm10 >= 81:
                send_RGB(255,0,0)

            for i in range(60):
                time.sleep(60.0)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "Arduino Uno" in p.description:
            print(f"{p} 포트에 연결되었습니다.")
            my_serial = serial.Serial(p.device, baudrate=9600, timeout=1.0)
            time.sleep(2.0)

    main()

    my_serial.close()