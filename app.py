from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return f'<h1>Hello, I am Anbarasan</h1>'

if __name__ == "__main__":
    app.run()
