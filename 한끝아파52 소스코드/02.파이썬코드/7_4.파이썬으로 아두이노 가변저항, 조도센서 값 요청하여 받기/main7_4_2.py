import time
import serial
import serial.tools.list_ports
import threading

def send_vr():
    sendData = f"VR=?\n"
    my_serial.write( sendData.encode() )

def send_bright():
    sendData = f"BRIGHT=?\n"
    my_serial.write( sendData.encode() )

serial_receive_data = ""
def serial_read_thread():
    global serial_receive_data
    while True:
        read_data = my_serial.readline()
        serial_receive_data = read_data.decode()

def send_vr_bright_1sec():
    t2 = threading.Timer(1, send_vr_bright_1sec)
    t2.daemon = True
    t2.start()
    send_vr()
    time.sleep(0.1)
    send_bright()

def main():
    try:
        send_vr_bright_1sec()
        global serial_receive_data
        while True:
            if serial_receive_data != "":
                print(serial_receive_data)
                serial_receive_data = ""

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