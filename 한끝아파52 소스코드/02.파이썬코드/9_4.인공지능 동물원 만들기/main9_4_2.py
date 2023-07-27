import tensorflow.keras
import numpy as np
import cv2
import time
import serial
import serial.tools.list_ports

def send_servo(digree):
    sendData = f"SERVO={digree}\n"
    my_serial.write( sendData.encode() )

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3,640)
    camera.set(4,480)
    
    model_path = r"9_4.인공지능 동물원 만들기\keras_model.h5"
    model = tensorflow.keras.models.load_model(model_path)
    labels_path = r"9_4.인공지능 동물원 만들기\labels.txt"
    
    while( camera.isOpened() ):
        _, image = camera.read()
        
        size = (224, 224)
        image_resized = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
        
        image_normalized = (image_resized.astype(np.float32) / 127.0) - 1
        
        image_reshaped = image_normalized.reshape((1, 224, 224, 3))

        prediction = model.predict(image_reshaped)
        result = np.argmax(prediction[0])
        
        with open(labels_path, 'rt', encoding='UTF8') as f : 
            readLines = f.readlines()
        
        print(readLines[result])
        
        if "기린" in readLines[result]:
            print("문열림")
            send_servo(180)
            time.sleep(1.0)
        else:
            send_servo(0)
        
        cv2.imshow('camera out',image)
        
        if cv2.waitKey(100) == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'Arduino Uno' in p.description:
            print(f"{p} 포트에 연결하였습니다.")
            my_serial = serial.Serial(p.device, baudrate=9600, timeout=1.0)
            time.sleep(2.0)
    
    main()
    
    my_serial.close()