'''
날짜: 2023.07.27
목표: 기상청 홈페이지 html 사용하여 청주 오창읍 온도 FND 출력
'''
import requests
import re
import time
import serial
import serial.tools.list_ports

def send_fnd(data):
    sendData = f"FND={data}\n"
    my_serial.write(sendData.encode())

def main():
    try:
        while True:
            url = "https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4311425300"
            response = requests.get(url)

            temp = re.findall(r"<temp>(.+)</temp>", response.text)
            humi = re.findall(r"<reh>(.+)</reh>", response.text)
            weather = re.findall(r"<wfKor>(.+)</wfKor>", response.text)

            print(f"기온={temp[0]}, 습도={humi[0]}, 날씨={weather[0]}")

            send_fnd(temp[0])
            time.sleep(60.0 * 5)
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