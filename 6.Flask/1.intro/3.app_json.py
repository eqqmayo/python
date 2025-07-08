from numbers import Number
from flask import Flask, jsonify
# from flask import jsonify

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '010-1234-5678'},
    {'name': 'Bob', 'age': 22, 'mobile': '010-1111-1111'},
    {'name': 'Charlie', 'age': 30, 'mobile': '010-2222-2222'},
]

@app.route('/')
def index():
    # return users
    return jsonify(users)

@app.route('/user/<name>')
def get_user_by_name(name):
    # u = next((user for user in users if user['name'] == name), None)
    output = None

    for user in users:
        try:
            age = int(name)
            if user['age'] == age:
                output = user
                break
        except:
            if user['name'].lower() == name.lower():
                output = user
                break
    return jsonify(output) if output else jsonify({'error': 'User not found'})
    
if __name__ == '__main__':
    app.run(debug=True) 
