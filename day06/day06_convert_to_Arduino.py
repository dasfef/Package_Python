import time
import serial
import serial.tools.list_ports
from currency_converter import CurrencyConverter

cc = CurrencyConverter()

def send_fnd(data):
    sendData = f"FND={data}\n"
    my_serial.write(sendData.encode())

def main():
    try:
        while True:
            usd_to_krw_rate = round(cc.convert(1, 'USD', 'KRW'))
            print(usd_to_krw_rate)
            send_fnd(usd_to_krw_rate)
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