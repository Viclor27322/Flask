from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo, Victor Fernando Rivera Hernandez 9 B"

if __name__ == '__main__':
    app.run(debug=True)