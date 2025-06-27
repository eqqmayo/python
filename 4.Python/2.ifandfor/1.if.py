score = 90

if (score) >= 90:
    print('A')
elif (score) >= 80:  # 다른 많은 언어는 else if
    print('B')
elif (score) >= 70:
    print('C')
else:
    print('F')

grade = ''

def getGrade(score):
    if (score) >= 90:
        grade = 'A'
    elif (score) >= 80: 
        grade = 'B'
    elif (score) >= 70:
        grade = 'C'
    else:
        grade = 'F'
    
    return grade

user = int(input('점수를 입력하시오: ')) # 내장 함수
print(getGrade(user))


