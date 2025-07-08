from flask import Flask, request

app = Flask(__name__)  

@app.route('/')  
def home():
    return '''
<html>
<head>
</head>
<body>
    <h1>hello, Flask!</h1>
    <h2>안녕하세요</h2>
    <p>상품목록</p>
    <div>
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
        </ul>
    <div>
</body>
<html>
'''

if __name__ == '__main__':
    app.run(debug=True) 
