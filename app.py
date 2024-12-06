from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to the Flask app."

if __name__ == '__main__':
    app.run(debug=True)
