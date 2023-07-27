import time
import serial
import serial.tools.list_ports
import requests
import re

def send_fnd(data):
    sendData = f"FND={data}\n"
    my_serial.write( sendData.encode() )

def main():
    try:
        while True:
            url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4139054000"
            response = requests.get(url)

            temp = re.findall(r'<temp>(.+)</temp>',response.text)
            humi = re.findall(r'<reh>(.+)</reh>',response.text)

            print(temp)
            print(humi)
            send_fnd(temp[0])
            time.sleep(60.0 * 5)
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