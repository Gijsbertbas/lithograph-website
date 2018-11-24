import os
from flask import Flask, render_template, flash, request, redirect, url_for, session

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/gijs/Projects/lithograph-website/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'las']) #'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'verysecret'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html', title='LITHOGRAPH')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'myfile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['myfile']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print('filename = {}'.format(filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(request.url)
#            return redirect(url_for('uploaded_file',filename=filename))
    return render_template('index.html', title='LITHOGRAPH')

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(debug = True)
