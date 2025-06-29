import datetime
import time
import os
import numpy

# 241
print(datetime.datetime.now())

# 242
print(type(datetime.datetime.now()))


# 243
now = datetime.datetime.now()

for day in range(5, 0, -1):
    print(now - datetime.timedelta(days = day))

# 244
print(datetime.datetime.now().strftime('%H:%M:%S'))

# 245
print(datetime.datetime.strptime('2020-05-04', '%Y-%m-%d'))

# 246
while True: 
    print(datetime.datetime.now())
    time.sleep(1)

# 247
# import module - 모듈명.함수명 형태로 사용
# import module as alias
# from module import function
# from module import * - 함수명 직접 사용

# 248
print(os.getcwd())

# 249
# os.rename("/Users/caliapark/Desktop/new.txt", "/Users/caliapark/Desktop/changed.txt")

# 250
for i in numpy.arange(0.0, 5.0, 0.1):
    print(i)
