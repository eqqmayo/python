from flask import Flask, render_template, request
import database as db
from math import ceil

app = Flask(__name__)

@app.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    limit = 20
    # last_page = ceil(len(db.get_users()) / limit)
    last_page = db.get_user_count()

    users = db.get_users_per_page(page, limit)
    return render_template('index.html', 
                            users=users, 
                            last_page=last_page, 
                            current_page=page,
                            )

if __name__ == '__main__':
    app.run(debug=True)