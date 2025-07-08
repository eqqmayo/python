from flask import Flask, render_template, request

app = Flask(__name__)  

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '010-1234-5678'},
    {'name': 'Bob', 'age': 22, 'mobile': '010-1111-1111'},
    {'name': 'Charlie', 'age': 30, 'mobile': '010-2222-2222'},
]

@app.route('/')  
def home(): 
    name = request.args.get('name')
    age = request.args.get('age')
    mobile = request.args.get('mobile')

    filtered_users = users

    if name:
        filtered_users = [u for u in users if u['name'].lower() == name.lower()]
    
    if age:
        filtered_users = [u for u in filtered_users if u['age'] == int(age)]

    if mobile:
        filtered_users = [u for u in filtered_users if mobile in u['mobile']]

    return render_template('index9.html', users=filtered_users) 
    
if __name__ == '__main__':
    app.run(debug=True) 
