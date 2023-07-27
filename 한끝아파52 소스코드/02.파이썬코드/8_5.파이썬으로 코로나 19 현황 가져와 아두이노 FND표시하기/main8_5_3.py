import requests
import re
import datetime

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

print(incDec[findHab])