from flask import Flask, render_template

app = Flask(__name__)  

@app.route('/')  
def home():
    return render_template('index.html')  # 이 파일은 무조건 templates 폴더에 있어야함
    
if __name__ == '__main__':
    app.run(debug=True) 
