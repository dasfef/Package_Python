from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import time
import serial
import serial.tools.list_ports
import threading

serial_receive_data = ""
def serial_read_thread():
    global serial_receive_data
    while True:
        read_data = my_serial.readline()
        serial_receive_data = read_data.decode()

def send_vr():
    sendData = f"VR=?\n"
    my_serial.write( sendData.encode() )

def init():
    return line,

def animate(i):
    send_vr()
    global serial_receive_data
    if "VR=" in serial_receive_data:
        print("가변저항값:",serial_receive_data[3:])
        y = int(serial_receive_data[3:])
        serial_receive_data = ""
        y = float(y)

        old_y = line.get_ydata()
        new_y = np.r_[old_y[1:], y]
        line.set_ydata(new_y)
        return line,
    else:
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
    
    max_x_points = 200

    fig = plt.figure()
    ax = plt.axes(xlim=(0, max_x_points), ylim=(0, 1023))

    line, = ax.plot(np.arange(max_x_points), 
                    np.ones(max_x_points, dtype=np.float)*np.nan, lw=2)
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=False)

    plt.show()
    
    my_serial.close()