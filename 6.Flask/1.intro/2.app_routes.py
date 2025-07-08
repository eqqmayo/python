from flask import Flask

app = Flask(__name__)  # 이름 짓기 귀찮을때 관행적으로

@app.route('/')  # 사용자가 / 에 접속하면 이 아래 함수 호출해줘
def home():
    return '<h1>Hiii Flask!</h1>'  

@app.route('/user')  
def user():
    return '<h1>Hiii User!</h1>'  

@app.route('/user/<username>')  # 위에 flask 데코레이터에서 정한 <변수명> 으로 함수 인자로 전달
def username(username):
    print(username)  
    return f'<h1>Hiii {username}님!</h1>'  # 서버사이드 렌더링(서버에서 필요한 html을 만들어줌)

@app.route('/product/<int:num>')  # 내가 따로 정의하지 않으면 문자열임. 바꾸고 싶으면 타입 선언
def product(num):
    return f'<h1>This is Product{num}!</h1>'  

@app.route('/user/<name>/<int:num>/<float:weight>')
def greet_user_with_detail(name, num, weight):
    if weight > 100:
        info = '무거운'
    else: 
        info = '가벼운'
    return f'<h1>Hiii {name}님! This is {info} Product{num}!</h1>'  

if __name__ == '__main__':
    print('여기가 메인 함수')
    app.run(debug=True, port=7000)  # 절대 디버그 켜진 채로 배포 xxx
 
