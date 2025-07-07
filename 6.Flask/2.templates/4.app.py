from flask import Flask, render_template, request

app = Flask(__name__)  

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '010-1234-5678'},
    {'name': 'Bob', 'age': 22, 'mobile': '010-1111-1111'},
    {'name': 'Charlie', 'age': 30, 'mobile': '010-2222-2222'},
]

# http://localhost:5000/?name=ccc <-- url 은 / 에서 끝 나머지는 ? GET 파라미터
# http://localhost:5000/name/ccc <-- url 리소스를 통해 입력 = 라우트 경로로 파싱

@app.route('/')  
def home(): 
    name = request.args.get('name')
    print(name)
    filtered_users = users

    # for u in users:
    #     if u['name'].lower() == name.lower():
    #         filtered_users = [u]
    #         break

    if name:
        filtered_users = [u for u in users if u['name'].lower() == name.lower()]

    return render_template('index4.html', users=filtered_users) 
    
if __name__ == '__main__':
    app.run(debug=True) 
