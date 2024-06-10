from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('modeloDrugs.pyl')
app.logger.debug('Modelo cargado correctamente.')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos enviados en el request
        bp = float(request.form['bp'])
        Na_to_K = float(request.form['Na_to_K'])
        Cholesterol_HIGH = float(request.form['Cholesterol_HIGH'])

        # Crear un DataFrame con los datos
        data_df = pd.DataFrame([[bp,Na_to_K,Cholesterol_HIGH]], columns=['BP', 'Na_to_K','Cholesterol_HIGH'])
        app.logger.debug(f'DataFrame creado: {data_df}')
        
        # Realizar predicciones
        prediction = model.predict(data_df)
        app.logger.debug(f'Predicción: {prediction[0]}')
        
        respuesta = ""
        if(prediction[0] == 0): respuesta = "DrugY" 
        if(prediction[0] == 1): respuesta = "drugA" 
        if(prediction[0] == 2): respuesta = "drugB" 
        if(prediction[0] == 3): respuesta = "drugC"
        if(prediction[0] == 4): respuesta = "drugX" 
        # Devolver las predicciones como respuesta JSON
        return jsonify({'categoria': respuesta})
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

