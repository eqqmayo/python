# 231
# 에러

# 232
def make_url(str):
    return 'www.' + str + '.com'

# 233
def make_list(str):
    return list(str)

def make_list2(str):
    return [char for char in str]

# 234
def pickup_even(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result

print(pickup_even([3, 4, 5, 6, 7, 8]))

# 235
def convert_int(str):
    return int(''.join(str.split(',')))

def convert_int2(str):
    return int(str.replace(',', ''))

convert_int('123,234,234')

# 236
# 22

# 237
# 22

# 238
# 140

# 239
# 16

# 240
# 28