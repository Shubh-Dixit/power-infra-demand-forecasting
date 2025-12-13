from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
try:
    model = joblib.load('demand_forecasting_model.pkl')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Material Demand Forecasting API is Running."})

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({"error": "Model not loaded."}), 500

    try:
        data = request.get_json()
        
        # Expected features
        # 'Region', 'Terrain', 'Infrastructure_Type', 'Project_Category', 'Voltage_Level_kV', 'Weather_Condition', 'Route_Length_km'
        
        input_data = {
            'Region': [data.get('Region')],
            'Terrain': [data.get('Terrain')],
            'Infrastructure_Type': [data.get('Infrastructure_Type')],
            'Project_Category': [data.get('Project_Category')],
            'Voltage_Level_kV': [float(data.get('Voltage_Level_kV'))],
            'Weather_Condition': [data.get('Weather_Condition')],
            'Route_Length_km': [float(data.get('Route_Length_km'))]
        }
        
        input_df = pd.DataFrame(input_data)
        
        # Predict
        prediction = model.predict(input_df)
        
        # Target cols: ['ACSR_Conductor_m', 'Towers_Steel_Count', 'Insulators_Count', 'Power_Transformers_Count', 'Circuit_Breakers_Count', 'Concrete_m3']
        # Rounding for better display
        result = {
            'ACSR_Conductor_m':  round(prediction[0][0], 2),
            'Towers_Steel_Count': round(prediction[0][1], 0), # Count should be integer-ish
            'Insulators_Count': round(prediction[0][2], 0),
            'Power_Transformers_Count': round(prediction[0][3], 0),
            'Circuit_Breakers_Count': round(prediction[0][4], 0),
            'Concrete_m3': round(prediction[0][5], 2)
        }
        
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
