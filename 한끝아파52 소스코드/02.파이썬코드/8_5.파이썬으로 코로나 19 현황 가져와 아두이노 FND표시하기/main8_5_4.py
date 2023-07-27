import time
import serial
import serial.tools.list_ports
import requests
import re
import datetime

def send_fnd(data):
    sendData = f"FND={data}\n"
    my_serial.write( sendData.encode() )

def get_today_covid19():
    now = datetime.datetime.now()
    yyyymmdd = now.strftime('%Y%m%d')
    print(yyyymmdd)

    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey="
    apiKey = "fFWLxGIoKo8cQCIuS5Is1fVoiKXkdls%2FU5DSGRwzmbiwIBI0nlz5V6jllexlrGLKR9y8wV3E3i0SMPTLtAhyvw%3D%3D"
    pageNo =  "&pageNo=1&numOfRows=30&"
    today = "startCreateDt=" + yyyymmdd + "&endCreateDt=" + yyyymmdd

    response = requests.get(url + apiKey + pageNo + today)

    gubun = re.findall(r'<gubun>(.+?)</gubun>',response.text)
    incDec = re.findall(r'<incDec>(.+?)</incDec>',response.text)

    findHab = gubun.index('합계')
    return incDec[findHab]

def main():
    try:
        while True:
            전국확진자수 = get_today_covid19()
            print(전국확진자수)
            send_fnd(int(전국확진자수))
            
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
    
    main()
    
    my_serial.close()