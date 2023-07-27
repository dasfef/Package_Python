import time
import serial
import serial.tools.list_ports
import threading
import datetime

def send_naver_email(메일제목,메일내용):
    import smtplib
    from email.mime.text import MIMEText
    
    send_email = "네이버메일@naver.com"
    send_pwd = "네이버비밀번호"

    recv_email = "받는이메일주소@hanmail.net"

    smtp_name = "smtp.naver.com" 
    smtp_port = 587

    text = 메일내용
    msg = MIMEText(text)

    msg['Subject'] = 메일제목
    msg['From'] = send_email
    msg['To'] = recv_email
    print(msg.as_string())

    s=smtplib.SMTP( smtp_name , smtp_port )
    s.starttls()
    s.login( send_email , send_pwd )
    s.sendmail( send_email, recv_email, msg.as_string() )
    s.quit()

serial_receive_data = ""
def serial_read_thread():
    global serial_receive_data
    while True:
        read_data = my_serial.readline()
        serial_receive_data = read_data.decode()

def main():
    try:
        global serial_receive_data
        while True:
            if "BUTTON1=CLICK" in serial_receive_data:
                now = datetime.datetime.now()
                nowTime = now.strftime('버튼1이 %H시 %M분 %S초에 눌렸습니다.')
                send_naver_email("버튼1 눌림",nowTime)
                print(serial_receive_data)
                serial_receive_data = ""
            elif "BUTTON2=CLICK" in serial_receive_data:
                now = datetime.datetime.now()
                nowTime = now.strftime('버튼2가 %H시 %M분 %S초에 눌렸습니다.')
                send_naver_email("버튼2 눌림",nowTime)
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