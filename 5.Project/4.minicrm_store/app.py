from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', '').strip()

    if name:
        stores = db.get_stores_by_name(name)
    else:
        stores = db.get_stores()

    return render_template('index.html', stores=stores, search=name)

# python 파일 로 실행할때만 불리는 코드임, flask run 으로 실행할때는 이 코드 안불림
if __name__ == '__main__':
    app.run(debug=True)