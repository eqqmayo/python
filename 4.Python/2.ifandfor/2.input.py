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

name = input('이름을 입력하시오')
score = int(input('점수를 입력하시오'))
grade = getGrade(score)

print(f'학생 {name}의 학점은 {grade}입니다')