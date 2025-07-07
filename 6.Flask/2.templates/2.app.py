from flask import Flask, render_template

app = Flask(__name__)  

@app.route('/')  
def home():
    users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    return render_template('index2.html', users=users)  # 우리의 Html 파일안에 이 users
    
if __name__ == '__main__':
    app.run(debug=True) 
