from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask import session

app = Flask(__name__)
app.secret_key = 'sesac'

users = [
    {'name': 'SeSAC', 'id': 'sesac', 'pw': 'sesac'},
    {'name': 'HI', 'id': 'hi', 'pw': 'hi'},
    ]

items = [
    {'id': 'prod-001', 'name': '사과', 'price': '1000'},
    {'id': 'prod-002', 'name': '딸기', 'price': '2000'},
    {'id': 'prod-003', 'name': '바나나', 'price': '1500'},
    ]

@app.route('/product')
def product():
    user = session.get('user')
    return render_template('product.html', user=user, items=items)

@app.route('/add-to-cart')
def add_to_cart():
    itemid = request.args.get('id')

    id = next((item['id'] for item in items if item['id'] == itemid), None)

    if 'cart' not in session:
        session['cart'] = {}

    if id in session['cart']:
        session['cart'][id] += 1
    else:
        session['cart'][id] = 1
        
    return render_template('product.html')

@app.route('/cart')
def cart():
    user = session.get('user')
    cart_items = session.get('cart')
    
    item_details = []

    if cart_items:
        item_details = [{
            'id': item['id'],
            'name': item['name'], 
            'price': item['price'], 
            'count': cart_items[item['id']]
            } 
            for item in items 
            if item['id'] in cart_items
        ]

    return render_template('cart.html', user=user, items=item_details)

@app.route('/')
def home():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/user')
def user():
    user = session.get('user')
    if user:
        return render_template('user.html', user=user)
    return redirect(url_for('login'))

@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    user = session.get('user')

    if request.method == 'POST':
        new_id = request.form.get('id')
        new_pw = request.form.get('pw')
        
        current_id = session['user']['id']
        is_edited = False

        for user in users:
            if user['id'] == current_id:
                if new_id:
                    user['id'] = new_id
                    session['user']['id'] = new_id
                    is_edited = True
                if new_pw:
                    user['pw'] = new_pw
                    session['user']['pw'] = new_pw
                    is_edited = True
                break

        if is_edited:
            session.modified = True
            flash('프로필 변경 완료')
        else:
            flash('변경 사항 없음')

        return render_template('profile.html', user=user)

    return render_template('profile.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('id')
        pw = request.form.get('pw')

        user = next((user for user in users if user['id'] == id and user['pw'] == pw), None)

        if user:
            session['user'] = user
            return redirect(url_for('user'))
        else:
            return render_template('login.html', error='로그인 실패')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)  # 유저가 없을 때(로그아웃 두 번 이상 하는 등) 발생하는 키 에러 방지
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


