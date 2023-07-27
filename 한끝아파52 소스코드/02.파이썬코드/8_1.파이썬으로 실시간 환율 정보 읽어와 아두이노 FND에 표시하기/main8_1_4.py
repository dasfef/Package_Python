import time
import serial
import serial.tools.list_ports
import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'id': 'last_last'})
    return containers.text

def send_fnd(data):
    sendData = f"FND={data}\n"
    my_serial.write( sendData.encode() )

def main():
    try:
        while True:
            usd_to_krw_rate = get_exchange_rate('usd', 'krw')
            usd_to_krw_rate = usd_to_krw_rate.replace(",","")
            usd_to_krw_rate = float(usd_to_krw_rate)
            usd_to_krw_rate = int(usd_to_krw_rate)
            print(usd_to_krw_rate)
            send_fnd(usd_to_krw_rate)
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