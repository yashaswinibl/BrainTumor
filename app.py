from flask import Flask, request,render_template, redirect,session
from flask_sqlalchemy import SQLAlchemy
from tensorflow.keras.models import load_model
from flask import Flask, request, url_for, render_template, redirect, session, Response
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import file_required, file_allowed
from werkzeug.utils import secure_filename
from tensorflow.keras.applications import EfficientNetB1
from tensorflow.keras.layers import GlobalAveragePooling2D, Dropout, Dense,Input
from tensorflow.keras.models import Model
import cv2
import numpy as np
import os
import bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'
app.config['SECRET_KEY']='jaykumar'


model = load_model('brain_tumor.h5')


class BrainForm(FlaskForm):
    style={'class': 'form-control', 'style':'width:25%;'}
    image = FileField("",validators=[file_required(),file_allowed(['jpg','png','jpeg'],'Images Only!')],render_kw=style)
    submit = SubmitField("Analyze",render_kw={'class':'btn btn-outline-primary'})
    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('main.html')
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')


@app.route('/main.html')
def main():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('main.html',user=user)
    
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')


@app.route('/empty_page')
def empty_page():
    filename = session.get('filename', None)
    os.remove(os.path.join(UPLOAD_FOLDER, filename))
    return redirect(url_for('index'))

def predict(model,sample):
    img = cv2.imread(sample)
    img = cv2.resize(img,(150,150))
    img = np.reshape(img,(1,150,150,3))
    return np.argmax(model.predict(img))


def tumor_name(value):
    if value==0:
        return 'Glioma Tumor'
    elif value==1:
        return 'Meningioma Tumor'
    elif value==2:
        return 'No Tumor Found'
    elif value==3:
        return 'Pituitary Tumor'
x=0

@app.route('/result', methods=['POST', 'GET'])
def prediction():
    pred_val = predict(model,x)
    result = tumor_name(pred_val)
    os.remove(x)
     # Assuming you have a user object stored in the session
    user = User.query.filter_by(email=session.get('email')).first()

    return render_template('prediction.html',result=result,user=user)

@app.route('/')
def index2():
    return render_template('index2.html')

@app.route('/pred', methods=['POST', 'GET'])
def index():
    form = BrainForm()

    # Assuming you have a user object stored in the session
    user = User.query.filter_by(email=session.get('email')).first()

    if form.validate_on_submit():
        assets_dir = './static'
        img = form.image.data
        img_name = secure_filename(img.filename)

        img.save(os.path.join(assets_dir, img_name))
        global x
        x = os.path.join(assets_dir, img_name)

        return redirect(url_for('prediction'))

    return render_template('index.html', form=form, user=user)


@app.route('/home',methods=['POST', 'GET'])
def home():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('home.html', user=user)
    else:
        return redirect('/login')

@app.route('/create_model', methods=['POST', 'GET'])
def model_architecture():
    effnet = EfficientNetB1(weights="imagenet", include_top=False, input_shape=(224,224, 3))
    model = effnet.output
    model = GlobalAveragePooling2D()(model)
    model = Dropout(0.5)(model)
    model = Dense(4, activation="softmax")(model)
    model = Model(inputs=effnet.input, outputs=model)
    
    # Generate model summary as a string
    model_summary_str = []
    model.summary(print_fn=lambda x: model_summary_str.append(x))

    return render_template('create_model.html', model_summary=model_summary_str)


@app.route('/evaluation_matrix', methods=['POST', 'GET'])
def evaluation_matrix():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
    else:
        user = None
    return render_template('evaluation_matrix.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)