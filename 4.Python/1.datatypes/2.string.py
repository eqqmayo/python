str = 'hello, world'
str2 = '  how are you doing python  '

print(str)

# 라이브러리 함수들로 만들어놨음 이걸 잘 알아야함
print(str.lower())
print(str.upper())
print(str.capitalize()) # 문장 시작만 대문자로
print(str.title()) # 문장 단어 시작마다 대문자로
print(str2.strip()) # 앞뒤 불필요한 공백 없애기
print(str2.lstrip()) 
print(str2.rstrip()) 
print(str2.split()) # 문장을 단어 단위로 자름

words = str.split() # 배열로 리턴
print(words) 
