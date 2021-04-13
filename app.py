from flask import Flask, render_template

app = Flask(__name__, template_folder="./templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True, port=3333)
