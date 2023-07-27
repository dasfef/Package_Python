import time
import serial
import serial.tools.list_ports
import threading
import requests
import json

slack_webhook_url = "https://hooks.slack.com/services/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"

def sendSlackWebhook(strText):
    headers = {
    "Content-type": "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200:
        return "ok"
    else:
        return "error"

def send_bright():
    sendData = f"BRIGHT=?\n"
    my_serial.write( sendData.encode() )

serial_receive_data = ""
def serial_read_thread():
    global serial_receive_data
    while True:
        read_data = my_serial.readline()
        serial_receive_data = read_data.decode()

def send_bright_1sec():
    t2 = threading.Timer(1, send_bright_1sec)
    t2.daemon = True
    t2.start()
    send_bright()

def main():
    try:
        send_bright_1sec()
        global serial_receive_data
        while True:
            if "BRIGHT=" in serial_receive_data:
                bright = int(serial_receive_data[7:])
                print("밝기값:",bright)
                serial_receive_data = ""
                
                if bright < 500:
                    sendSlackWebhook("어둡습니다.")
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

    t1 = threading.Thread(target=serial_read_thread)
    t1.daemon = True
    t1.start()
    
    main()
    
    my_serial.close()