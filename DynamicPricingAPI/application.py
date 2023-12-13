from flask import Flask, request, jsonify
import pandas as pd
import tensorflow as tf
import joblib
import math

application = Flask(__name__)

# Load the trained model and scaler
model = tf.keras.models.load_model("parking_price_prediction_model_neural_network.h5")
scaler = joblib.load("scaler.pkl")

@application.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data
        data = request.json
        input_df = pd.DataFrame([data])

        # Preprocess and make predictions
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)
        predicted_price = math.ceil(float(prediction[0][0]))

        # Return the prediction
        return jsonify(predicted_price)

    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    application.run(debug=True)