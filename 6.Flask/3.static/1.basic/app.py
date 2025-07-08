from flask import Flask, render_template

# app = Flask(__name__, static_folder='my_static')  # static 폴더 이름 변경
app = Flask(__name__)  

# 1. static 폴더는 바꿀 수는 있지만 굳이 바꿀 필요는 없음
# 2. static 이라고 폴더명을 정해주며 그곳은 자동으로 외부에 노출된다
# 3. 그래서 index 안에서 static을 전달할때는 하드코딩해도 동작은 하지만 진자 문법 url_for('static', ..)을 통해 전달하는 것이 좋음

@app.route('/')  
def home():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True) 
