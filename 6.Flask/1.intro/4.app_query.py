from flask import Flask, request

app = Flask(__name__)  # 이름 짓기 귀찮을때 관행적으로

@app.route('/search')  # /search?q=apple&page=4
def search():
    query = request.args.get('q')
    page = request.args.get('page', default=1, type=int)

    print(query, page)

    return 'hello'

if __name__ == '__main__':
    app.run(debug=True) 
