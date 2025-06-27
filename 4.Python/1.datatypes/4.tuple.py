my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])

# my_tuple[2] = 5 # 오류 발생. 튜플은 수정 불가능

my_list = list(my_tuple)
my_list[2] = 3

my_tuple2 = tuple(my_list)
# my_tuple2[2] = 10

# 튜플 안에 데이터를 여러개의 변수로 나누어 담을 수 있음
# 튜플 언패킹
a, b, _ = (1, 2, 3)
print(a)
print(b)
# print(c)