from flask import Flask, render_template

app = Flask(__name__)  

@app.route('/')  
def home():
    users = [
    {'name': 'Alice', 'age': 25, 'mobile': '010-1234-5678'},
    {'name': 'Bob', 'age': 22, 'mobile': '010-1111-1111'},
    {'name': 'Charlie', 'age': 30, 'mobile': '010-2222-2222'},
    ]
    return render_template('index3.html', users=users)  # 우리의 Html 파일안에 이 users
    
if __name__ == '__main__':
    app.run(debug=True) 
