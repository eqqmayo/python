from flask import Flask, jsonify, url_for, render_template
import random

app = Flask(__name__)  

cat_images = [
    'cat1.jpeg',
    'cat2.jpeg',
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random-dog')  
def random_dog():
    random_img = random.choice(cat_images)
    image_url = url_for('static', filename=f'img/{random_img}', _external=True)  # 절대경로 만들기
    return jsonify({'url': image_url})
    
if __name__ == '__main__':
    app.run(debug=True) 
