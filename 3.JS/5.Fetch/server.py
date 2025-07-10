from flask import Flask, jsonify, send_file, render_template
# from flask_cors import CORS
# 여기다가 cors 라이브러리를 추가해서 해결하거나 프런트엔드를 내가 서빙하거나

app = Flask(__name__)
# CORS(app)

@app.route('/')
def index():
    return send_file('5.getimage_by_breed.html')

@app.route('/data')
def data():
    return jsonify({'result': 'Hi'})

if __name__ == '__main__':
    app.run(debug=True)