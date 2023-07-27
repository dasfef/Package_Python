import time
import serial
import serial.tools.list_ports
import threading
import tkinter
import tkinter.font

def send_object_temperature():
    sendData = f"OBJECT=?\n"
    my_serial.write( sendData.encode() )

def send_object_temperature_100mS():
    t2 = threading.Timer(0.1, send_object_temperature_100mS)
    t2.daemon = True
    t2.start()
    send_object_temperature()

def serial_read_thread():
    global object_temperature_value
    while True:
        read_data = my_serial.readline()
        serial_receive_data = read_data.decode()
        if "OBJECT=" in serial_receive_data:
            object_temperature_value = serial_receive_data[7:]
            print("물체온도:",object_temperature_value)
            serial_receive_data = ""

object_temperature_value = ""
def gui_object_temperature_view():
    global object_temperature_value
    label.config(text=object_temperature_value)
    window.after(100,gui_object_temperature_view)

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
    
    send_object_temperature_100mS()
    
    window = tkinter.Tk()
    window.title("비접촉 온도표시")
    window.geometry("300x200")
    window.resizable(False,False)

    font = tkinter.font.Font(size = 50)
    label=tkinter.Label(window, text="", font=font)
    label.pack()
    
    gui_object_temperature_view()
    
    window.mainloop()
    
    my_serial.close()