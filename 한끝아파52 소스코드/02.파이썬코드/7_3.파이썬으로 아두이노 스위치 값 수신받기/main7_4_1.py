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

def send_servo(digree):
    sendData = f"SERVO={digree}\n"
    my_serial.write(sendData.encode())

serial_receive_data = ""
def serial_read_thread():
    global serial_receive_data
    while True:
        read_data = my_serial.readline()
        serial_receive_data = read_data.decode()

def data_split(data):
    numData = data.split("=")
    vrData = str(int(numData[1]) / 5.67)
    print(vrData)
    return vrData

def main():
    try:
        global serial_receive_data
        curr_time = 0
        prev_time = 0
        while True:
            if serial_receive_data != "":
                print(serial_receive_data)
                data = serial_receive_data.split("=")
                if (data[0] == "VR"):
                    servoData = data_split(serial_receive_data)
                    send_servo(servoData)
                    
                serial_receive_data = ""
            
            curr_time = time.time()
            if curr_time - prev_time >= 1.0:
                prev_time = curr_time
                send_vr()
                time.sleep(0.1)
                send_bright()

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