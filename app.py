from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a sample web application!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
