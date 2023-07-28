import tensorflow.keras
import numpy as np
import serial
import serial.tools.list_ports
import time
import cv2

def send_buzzer(freq):
    sendData = f"BUZZER={freq}\n"
    my_serial.write(sendData.encode())

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3,640)
    camera.set(4,480)
    
    model_path = r"C:/Users/user/Desktop/WORK/Python/converted_keras/keras_model.h5"
    model = tensorflow.keras.models.load_model(model_path)
    labels_path = r"C:/Users/user/Desktop/WORK/Python/converted_keras/labels.txt"

    class_labels = {
        0: 'On Mask',
        1: 'Not on Mask',
        2: 'BackGround'
    }
        
    while( camera.isOpened() ):
        _, image = camera.read()
        if not _:
            print("Failed to Connect")
            continue
        
        size = (224, 224)
        image_resized = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
        
        image_normalized = (image_resized.astype(np.float32) / 127.0) - 1
        
        image_reshaped = image_normalized.reshape((1, 224, 224, 3))

        prediction = model.predict(image_reshaped)
        result = np.argmax(prediction[0])
        print(prediction)

        with open(labels_path, 'rt', encoding='UTF-8') as f :
            readLines = f.readlines()
        print(readLines[result])

        if "1 마스크 미착용" in readLines[result]:
            send_buzzer(1000)
        else:
            send_buzzer(0)

        confidences = prediction[0]  
        max_conf_idx = np.argmax(confidences)  
        max_conf = confidences[max_conf_idx]

        if max_conf > 0.5:  
            label = class_labels.get(max_conf_idx, "Unknown")
            color = (0, 0, 255) 
            cv2.putText(image, f"{label}: {max_conf:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        cv2.imshow('camera out',image)
        if cv2.waitKey(1) == ord('q'):
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