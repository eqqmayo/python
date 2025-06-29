# 221
def print_reverse(str):
    print(str[::-1])

# 222
def print_score(scores):
    print(sum(scores) / len(scores))

# 223
def print_even(nums):
    for n in nums:
        if n % 2 == 0:
            print(n)

# 224
def print_keys(dict):
    for key in dict:
        print(key)

# 225
def print_value_by_key(dict, date): 
    print(dict[date])

my_dict = {"10/26": [100, 130, 100, 100], "10/27": [10, 12, 10, 11]}

print_value_by_key(my_dict, "10/26")

# 226
def print_5xn(str):
    i = 0
    while i < len(str):
        print(str[i:i+5])
        i += 5

print_5xn('안녕안녕나는파이썬이야')

# 227
def print_mxn(str, n):
    i = 0
    while i < len(str):
        print(str[i:i+n])
        i += n
 
print_mxn('안녕안녕나는파이썬이야', 3)

# 228
def calc_monthly_salary(annual_salary):
    print(annual_salary // 12)

# 229
# 왼쪽: 100
# 오른쪽: 200

# 230
# 왼쪽: 200
# 오른쪽: 100