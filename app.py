from flask import Flask, render_template, request
app = Flask(__name__)


app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return render_template('index.html', title='LITHOGRAPH')

if __name__ == '__main__':
    app.run()
