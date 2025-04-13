from flask import Flask, render_template
from flask import Flask 


app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/tests')
def tests():
    return render_template('tests.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/test_1')
def test_1():
    return render_template('test_1.html')


@app.route('/test_2')
def test_2():
    return render_template('test_2.html')


@app.route('/test_3')
def test_3():
    return render_template('test_3.html')

 
if __name__ == '__main__':
    app.run(debug=True)
