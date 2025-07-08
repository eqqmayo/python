from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # methods 안넣으면 GET이 기본값
def index():
    return render_template('form.html') 

@app.route('/submit', methods=['POST']) 
def submit():
    # name = request.args.get('name')  # 없음
    name = request.form.get('name')  # POST로 form이 전달된 것 안에서 name 이 키인 것을 주시옹
    age = request.form.get('age')  # POST로 form이 전달된 것 안에서 키가 age인 것을 주시옹
    return f'안녕하세요 {age}세 {name}님' 

if __name__ == '__main__':
    app.run(debug=True) 
