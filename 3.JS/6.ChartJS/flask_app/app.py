from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    data = {
        'labels': ['1월', '2월', '3월', '4월'],
        'values': [12, 24, 30, 10]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)