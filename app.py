from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form.get('nombre')
    return f"¡Formulario enviado! ¡Hola, {nombre}!"

if __name__ == '__main__':
    app.run(debug=True)