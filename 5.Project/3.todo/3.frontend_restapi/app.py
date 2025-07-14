from flask import Flask, request, url_for, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__)  
CORS(app)  # 나의 서버에 누구든지 와서 정보를 요청할 수 있음

images = [
    {'filename': 'cat1.jpeg', 'keywords': ['cat', 'animal', 'cute']},
    {'filename': 'cat2.jpeg', 'keywords': ['cat', 'pet', 'cute']},
    {'filename': 'cat3.jpeg', 'keywords': ['cat', 'kitty', 'cute']},
    {'filename': 'cat4.jpeg', 'keywords': ['cat', 'dog']},
    {'filename': 'cat5.jpeg', 'keywords': ['animal', 'meow']},
]

@app.route('/')  
def index():
    if app.static_folder is None:
        return "Static folder not configured", 500
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/search')  
def search():
    query = request.args.get('q', '').lower()
    results = []

    for item in images:
        if any(query in keyword for keyword in item['keywords']):
            image_url = url_for('static', filename=f'img/{item['filename']}')
            results.append(image_url)

    return jsonify({"url": results})
    
if __name__ == '__main__':
    app.run(debug=True) 
