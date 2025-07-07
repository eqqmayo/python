from math import ceil
from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'id': i, 'name': f'User{i}', 'age': 20+i % 10, 'phone': f'010-0000-{str(i).zfill(4)}'} for i in range(1, 101)
]

@app.route('/pages/<int:page>')
def index(page):
    limit = 20
    current_users = users[(page - 1) * limit:page * limit]

    last_page = ceil(len(users) / limit)
    pre_page = max(page - 1, 1)
    next_page = min(page + 1, last_page)

    return render_template('users2.html', 
                            users=current_users, 
                            page=page,
                            last_page=last_page,
                            pre_page=pre_page,
                            next_page=next_page)


if __name__ == '__main__':
    app.run(debug=True)