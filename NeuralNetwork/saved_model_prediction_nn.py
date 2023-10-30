import pandas as pd
import math
import tensorflow as tf
from tensorflow import keras
import joblib

loaded_model = keras.models.load_model("parking_price_prediction_model_neural_network.h5")

scaler = joblib.load("scaler.pkl")

new_data = pd.DataFrame({
    'Day of the week': [3],
    'Time of day': [12],
    'Amenity type': [2],
    'Distance to amenity': [1000],
    'User rating of parking': [4],
    'Handicap accessible': [1]
})

new_data_scaled = scaler.transform(new_data)

predictions = loaded_model.predict(new_data_scaled)

print('Predicted Price:', math.ceil(predictions[0][0]))
