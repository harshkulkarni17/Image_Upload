from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import io
import base64
from PIL import Image
from predict import predictCaption

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/imageupload'
# db = SQLAlchemy(app)

# class images(db.Model):
#      sno = db.Column(db.Integer, primary_key=True)
#      name = db.Column(db.String(100), index=True, nullable=False)
#      img = db.Column(db.LargeBinary, nullable=False)
#      datetime = db.Column(db.String(), nullable=False)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        img = request.files['my_image']
        if img:
            # name = request.form.get('my_image')
            image = Image.open(img.stream)

            imagePath = "static/images/" + img.filename
            f = open("static/imageExt.txt", "w")
            f.write(imagePath)
            f.close()

            image.save(imagePath)
            # newfile = images(name=image.filename, img=image.read(), datetime = datetime.now())
            # db.session.add(newfile)
            # db.session.commit()
            caption = predictCaption()
        else:
            return "Select the File"
    return render_template('output.html', path= imagePath, cap=caption)


app.run(debug=True)
