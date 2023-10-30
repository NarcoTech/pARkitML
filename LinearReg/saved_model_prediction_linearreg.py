import pandas as pd
import joblib
import math

model_filename = 'LinearReg/linear_regression_model.pkl'
model = joblib.load(model_filename)

current_user_data = {
    'Day of the week': 3,
    'Time of day': 12,
    'Amenity type': 2,
    'Distance to amenity': 1500,
    'User rating of parking': 4.5,
    'Handicap accessible': 1
}


current_user_data_df = pd.DataFrame([current_user_data])

predicted_price = model.predict(current_user_data_df)

print('Predicted Price:', math.ceil(predicted_price[0]))
