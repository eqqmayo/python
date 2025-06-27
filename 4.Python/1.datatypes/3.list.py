my_list = [1, 2, 3, 4, 5]
print(my_list)

print(len(my_list))
print(my_list[0])
print(my_list[1])
# print(my_list[5]) # js 에서는 undifined, 그 외 다른 언어에서는 오류
print(my_list[-1]) # 거꾸로 갈 수 있음. 파이썬의 특징 ,대부분의 다른 언어는 허용하지 않음

# 리스트 슬라이싱
print(my_list[1:3]) # 1번째부터 3번째 포함하기 전까지
print(my_list[:3]) # 시작부터 3번째 포함하기 전까지
print(my_list[2:]) # 2번째부터 끝까지

print('-' * 10)

# 리스트에 멤버 추가하기
my_list.append(6)
print(my_list)
my_list.insert(2, 10) # 인덱스 2에 숫자 추가하겠음
print(my_list)

another_list = [7, 8, 9]
print(my_list)
print(another_list)

my_list.extend(another_list)
print(my_list)
print(another_list)

my_list.remove(10) # 리스트에서 10을 삭제할거야
my_list.pop(3)     # 인덱스3에 있는 요소를 삭제할거야

my_list.pop() # 인자 안주면 마지막 요소 삭제
print(my_list)

my_list.clear() # 리스트 비우기
print(my_list)

my_list = [1, 2, 3, 4, 5]

index_of_3 = my_list.index(1) # 숫자 1의 인덱스는 어디?
print(index_of_3)

count_2 = my_list.count(2) # 숫자 2는 몇개?
print(count_2)

sorted_list = sorted(my_list)
print(my_list)
print(sorted_list)

my_list.sort() # 오름차순 기본
print(my_list)

my_list.sort(reverse=True) # 내림차순
print(my_list)

my_list.reverse() # 현재 리스트를 역순으로 
print(my_list)

my_list2 = my_list.copy()
print(my_list2)

# 리스트 컴프리헨션 - 파이썬의 매우 큰 특징, 장점
# 리스트 안에 반복문, 조건문을 통해 리스트안에 채워질 요소를 정의
numbers = [n ** 2 for n in range(0, 10) if n % 2 == 0]
print(numbers)