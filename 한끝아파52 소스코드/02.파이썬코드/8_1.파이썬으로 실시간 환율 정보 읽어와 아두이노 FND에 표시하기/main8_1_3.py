import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'id': 'last_last'})
    return containers.text

usd_to_krw_rate = get_exchange_rate('usd', 'krw')
usd_to_krw_rate = usd_to_krw_rate.replace(",","")
usd_to_krw_rate = float(usd_to_krw_rate)
usd_to_krw_rate = int(usd_to_krw_rate)
print(usd_to_krw_rate)