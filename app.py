from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_frozen import Freezer

app = Flask(__name__)

Bootstrap(app)
freezer = Freezer(app)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/bio.html')
def bio():
	return render_template('bio.html')

if __name__ == '__main__':
    freezer.freeze();
    app.run()
