from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('land.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/home')
def land():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)