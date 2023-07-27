import time
import serial
import serial.tools.list_ports
import requests
import re

def send_fnd(data):
    sendData = f"FND={data}\n"
    my_serial.write( sendData.encode() )

def send_rgb_led(red,green,blue):
    sendData = f"RGB={red},{green},{blue}\n"
    my_serial.write( sendData.encode() )

def main():
    try:
        while True:
            url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=fFWLxGIoKo8cQCIuS5Is1fVoiKXkdls%2FU5DSGRwzmbiwIBI0nlz5V6jllexlrGLKR9y8wV3E3i0SMPTLtAhyvw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"
            response = requests.get(url)
            
            pm10 = re.findall(r'<pm10Value>(.+)</pm10Value>',response.text)
            pm25 = re.findall(r'<pm25Value>(.+)</pm25Value>',response.text)
            stationName = re.findall(r'<stationName>(.+)</stationName>',response.text)

            findNum = stationName.index('강남구')
            print("pm10:",pm10[findNum])
            print("pm25:",pm25[findNum])
            print("station:",stationName[findNum])
            
            pm25 = int(pm25[findNum])
            send_fnd(pm25)
            time.sleep(0.2)
            
            if pm25 <= 30:
                send_rgb_led(0,255,0)
            elif pm25 >= 31 and pm25 <= 80:
                send_rgb_led(0,0,255)
            elif pm25 >= 81:
                send_rgb_led(255,0,0)

            for i in range(60):
                time.sleep(60.0)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'Arduino Uno' in p.description:
            print(f"{p} 포트에 연결하였습니다.")
            my_serial = serial.Serial(p.device, baudrate=9600, timeout=1.0)
            time.sleep(2.0)
    
    main()
    
    my_serial.close()