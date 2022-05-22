from crypt import methods
from operator import truediv
from flask import *
from transformers import pipeline


app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('home.html', text="Akshar Betichod")

@app.route("/home", methods = ['GET'])
def home():
    return render_template('upload.html')

@app.route('/home', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template('summary.html', name = f.filename)

@app.route("/summary", methods = ['GET'])
def summary():
    return render_template('summary.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)