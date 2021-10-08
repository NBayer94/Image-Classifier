import model
import os
from flask import Flask, render_template, request, flash, redirect

UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    # check if the post request has the file part
    if 'imagefile' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['imagefile']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if not allowed_file(file.filename):
        flash('invalid file')
        return redirect(request.url)

    if file:
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        prediction = model.predict_image(path)
        return render_template('index.html', prediction=prediction, image=file.filename)

    return


if __name__ == '__main__':
    app.run(port=3000, debug=True)