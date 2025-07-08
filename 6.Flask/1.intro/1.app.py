from flask import Flask

app = Flask(__name__)  # 이름 짓기 귀찮을때 관행적으로

if __name__ == '__main__':
    print('여기가 메인 함수')
    app.run()  # 문열고 요청올 때까지 대기: 데몬(daemon)

