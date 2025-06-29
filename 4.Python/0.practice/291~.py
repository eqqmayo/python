# 291
file = open('/Users/caliapark/desktop/매수종목1.txt', mode = 'wt')
file.write('005930\n005380\n035420')
file.close()

# 292
file = open('/Users/caliapark/desktop/매수종목2.txt', mode = 'wt')
file.write('005930 삼성전자\n005380 현대차\n035420 NAVER')
file.close()

# 293
import csv
from decimal import DivisionByZero

file = open('/Users/caliapark/desktop/매수종목.csv', mode = 'wt', encoding = 'cp949', newline = '')
writer = csv.writer(file)
writer.writerows([['종목명', '종목코드', 'PER'], ['삼성전자', '005930', '15.79'], ['NAVER', '035420', '55.82']])
file.close()

# 294
file = open('/Users/caliapark/desktop/매수종목1.txt', encoding="utf-8")
lines = file.readlines()
file.close()

codes = []

for l in lines:
    codes.append(l.strip())

# 295
file = open('/Users/caliapark/desktop/매수종목2.txt', encoding="utf-8")
lines = file.readlines()
file.close()

stocks = {}

for l in lines:
    name, code = l.strip().split()
    stocks[name] = code

print(stocks)

# 296
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

# 297
per = ["10.31", "", "8.00"]
list = []

for i in per:
    try:
        list.append(float(i))
    except:
        pass

# 298
try:
    print(3 / 0)
except ZeroDivisionError:
    print('division by zero')

# 299
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

# 300
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print('not allowed to cast')
    else:
        print('what is this for')  # 예외가 없을 때 실행
    finally:
        print('print this anyway')