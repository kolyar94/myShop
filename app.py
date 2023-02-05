from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os
from cloudipsp import Api, Checkout

UPLOAD_FOLDER = 'static/image/'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'gif'])
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///myshop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

class Mac(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # номер
    title = db.Column(db.String(100), nullable=False)  # название
    file = db.Column(db.Text, nullable=False)  # картинка
    price = db.Column(db.Integer, nullable=False)  # цена
    descr = db.Column(db.String(100), nullable=False)  # краткое описание товара
    text = db.Column(db.Text, nullable=False) # полное описание

    def __repr__(self):
        return self.id


class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # номер
    title = db.Column(db.String(100), nullable=False)  # название
    file = db.Column(db.Text, nullable=False)  # картинка
    price = db.Column(db.Integer, nullable=False)  # цена
    descr = db.Column(db.String(100), nullable=False)  # краткое описание товара
    text = db.Column(db.Text, nullable=False)  # полное описание

    def __repr__(self):
        return self.id


class Watch(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # номер
    title = db.Column(db.String(100), nullable=False)  # название
    file = db.Column(db.Text, nullable=False)  # картинка
    price = db.Column(db.Integer, nullable=False)  # цена
    descr = db.Column(db.String(100), nullable=False)  # краткое описание товара
    text = db.Column(db.Text, nullable=False)  # полное описание

    def __repr__(self):
        return self.id


class AirPods(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # номер
    title = db.Column(db.String(100), nullable=False)  # название
    file = db.Column(db.Text, nullable=False)  # картинка
    price = db.Column(db.Integer, nullable=False)  # цена
    descr = db.Column(db.String(100), nullable=False)  # краткое описание товара
    text = db.Column(db.Text, nullable=False)  # полное описание

    def __repr__(self):
        return self.id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/phone')
def phone():
    phones = Phone.query.order_by(Phone.id).all()
    return render_template('phone.html',phones=phones)

@app.route('/buy_phone/<int:id>')
def buy_phone(id):
    phone=Phone.query.get(id)
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        'currency': 'RUB',
        'amount': str(phone.price) + '00'
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


@app.route('/create_phone', methods=['POST','GET'])
def create_phone():
    if request.method =='POST':
        title=request.form['title']
        price=request.form['price']
        descr=request.form['descr']
        text=request.form['text']
        file=request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        dirname = os.path.dirname(app.config['UPLOAD_FOLDER'])
        file=os.path.join(dirname+'/'+filename)

        phone=Phone(title=title,price=price,descr=descr,text=text,file=file)

        try:
            db.session.add(phone)
            db.session.commit()
            return redirect('/phone')

        except:

            return 'Произошла ошибка'
    else:
        return render_template('create_phone.html')




@app.route('/airpods')
def airpods():
    airpodss = AirPods.query.order_by(AirPods.id).all()
    return render_template('airpods.html',airpodss=airpodss)

@app.route('/buy_airpods/<int:id>')
def buy_airpods(id):
    airpods = AirPods.query.get(id)
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        'currency': 'RUB',
        'amount': str(airpods.price) + '00'

    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)

@app.route('/create_airpods', methods=['POST','GET'])
def create_airpods():
    if request.method =='POST':
        title=request.form['title']
        price=request.form['price']
        descr=request.form['descr']
        text=request.form['text']
        file=request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        dirname = os.path.dirname(app.config['UPLOAD_FOLDER'])
        file=os.path.join(dirname+'/'+filename)

        airpods=AirPods(title=title,price=price,descr=descr,text=text,file=file)

        try:
            db.session.add(airpods)
            db.session.commit()
            return redirect('/airpods')

        except:

            return 'Произошла ошибка'
    else:
        return render_template('create_airpods.html')



@app.route('/macbook')
def macbook():
    macbooks = Mac.query.order_by(Mac.id).all()
    return render_template('macbook.html',macbooks=macbooks)


@app.route('/buy_mac/<int:id>')
def buy_mac(id):
    mac = Mac.query.get(id)
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        'currency': 'RUB',
        'amount': str(mac.price) + '00'

    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


@app.route('/create_macbook', methods=['POST','GET'])
def create_macbook():
    if request.method =='POST':
        title=request.form['title']
        price=request.form['price']
        descr=request.form['descr']
        text=request.form['text']
        file=request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        dirname = os.path.dirname(app.config['UPLOAD_FOLDER'])
        file=os.path.join(dirname+'/'+filename)

        mac=Mac(title=title,price=price,descr=descr,text=text,file=file)

        try:
            db.session.add(mac)
            db.session.commit()
            return redirect('/macbook')

        except:

            return 'Произошла ошибка'
    else:
        return render_template('create_macbook.html')


@app.route('/watch')
def watch():
    watchs = Watch.query.order_by(Watch.id).all()
    return render_template('watch.html',watchs=watchs)


@app.route('/buy_watch/<int:id>')
def buy_watch(id):
    watch = Watch.query.get(id)
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        'currency': 'RUB',
        'amount': str(watch.price) + '00'

    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)

@app.route('/create_watch', methods=['POST','GET'])
def create_watch():
    if request.method =='POST':
        title=request.form['title']
        price=request.form['price']
        descr=request.form['descr']
        text=request.form['text']
        file=request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        dirname = os.path.dirname(app.config['UPLOAD_FOLDER'])
        file=os.path.join(dirname+'/'+filename)

        watch=Watch(title=title,price=price,descr=descr,text=text,file=file)

        try:
            db.session.add(watch)
            db.session.commit()
            return redirect('/watch')

        except:

            return 'Произошла ошибка'
    else:
        return render_template('create_watch.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__=='__main__':
    app.run(debug=True)