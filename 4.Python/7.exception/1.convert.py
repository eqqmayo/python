# 레거시 언어는 if 문으로 다 비교하는 등의 방식

# 모던 언어의 방식은
# try-catch, try-except 형태로 변경해서 오류 처리

# 이때 try 안에 오는 범위를 최소화 할수록 좋은 것
# except 내에서 퉁쳐서 잡지말고 구체적으로 잡아서 핸들링
# try:
#     result = 10 / 0 # crash .. 프로그램 종료되고 다음줄 실행 불가능
#     print(result)
# except ZeroDivisionError:
#     print('0으로 나눌 수 없음')

# 문자를 숫자로 바꾸기
# 다른 모든 언어는 함수의 설명을 함수 위에 쓰는데, 파이썬은 아래에 씀"
def convert_to_int(num_Str):
    """글자를 숫자로 바꾸는 함수임 <-- docstring 이라고 부름
    Args:
        num_str (String): 사용자 입력을 문자열 형태의 숫자로 받음
    Returns:
        result: 변환된 숫자값, 변환에 실패한 경우 none qksghks
    """
    try:
        result = int(num_Str)
    except:
        print('숫자 변환 실패')
        result = None
    return result

def double_number(num):
    return num * 2

user_input = 'A'
result = double_number(convert_to_int(user_input))
print(result)
