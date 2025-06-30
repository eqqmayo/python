import module_a as ma

def start_program():
    print('main으로 부터 호출된 start_program 함수')
    local_function_a()

def local_function_a():
    print('main으로 부터 호출된 local_function_a 함수')
    ma.function_a1()

if __name__ == '__main__':  # 파이썬이 나를 직접 호출했을때 실행되는 것 = 메인 함수
    start_program()