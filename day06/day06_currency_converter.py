from currency_converter import CurrencyConverter

cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/')
print(cc.currencies)

print(round(cc.convert(1, 'USD', 'KRW')), "원")