from flask import Flask, url_for, render_template, request, redirect
import secrets

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def homepage():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)