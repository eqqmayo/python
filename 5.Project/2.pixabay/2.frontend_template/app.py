from flask import Flask, render_template, request, url_for

app = Flask(__name__)  

images = [
    {'filename': 'cat1.jpeg', 'keywords': ['cat', 'animal', 'cute']},
    {'filename': 'cat2.jpeg', 'keywords': ['cat', 'pet', 'cute']},
    {'filename': 'cat3.jpeg', 'keywords': ['cat', 'kitty', 'cute']},
    {'filename': 'cat4.jpeg', 'keywords': ['cat', 'dog']},
    {'filename': 'cat5.jpeg', 'keywords': ['animal', 'meow']},
]

@app.route('/')  
def index():
    return render_template('index.html')

@app.route('/search')  
def search():
    query = request.args.get('q', '').lower()
    results = []

    for item in images:
        found = False
        for keyword in item['keywords']:
            if query in keyword:
                found = True
        if found:
            image_url = url_for('static', filename=f'img/{item['filename']}')
            results.append(image_url)
            break


        # if any(query in keyword for keyword in item['keywords']):
        #     image_url = url_for('static', filename=f'img/{item['filename']}')
        #     results.append(image_url)

    # return jsonify({'url': results})  # 순수 백엔드 개발자는 여기까지
    return render_template('results.html', query=query, results=results)
    
if __name__ == '__main__':
    app.run(debug=True) 
