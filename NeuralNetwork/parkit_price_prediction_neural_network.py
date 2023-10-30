import pandas as pd
import matplotlib.pyplot as plt
import math
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras.models import Sequential
import joblib

df = pd.read_csv('synthetic_parking_prices.csv')

#features and target variable
'''
Params:

1. Parking ID (Numeric)
2. Day of the week (1-7 for days of the week)
3. Time of day (in 4 digit hour format - 12pm = 1200 hours)
4. Amenity type (IDs given to different amenities - Mall': 1, 'Museum': 2, 'Garden': 3, 'Park': 4, 'Restaurant': 5, 'Bar': 6, 'Club': 7, 'Hotel': 8, 'Guesthouse': 9, 'Hospital': 10)
5. User rating of parking(0-5)
6. Handicap accessible (0 - No, 1 - Yes)
7. Distance to amenity (meters)
8. Price (INR)
'''

X = df[['Day of the week', 'Time of day', 'Amenity type', 'Distance to amenity', 'User rating of parking', 'Handicap accessible']]
y = df['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
joblib.dump(scaler, "scaler.pkl")

model = keras.Sequential([
    keras.layers.Input(shape=(X_train.shape[1],)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(1)  # Output layer with a single neuron (for regression)
])

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))
model.save("parking_price_prediction_model_neural_network.h5")
loss = model.evaluate(X_test, y_test)
print('Mean squared error:', loss)

# Plotting the actual vs. predicted prices
y_pred = model.predict(X_test)
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual Prices vs. Predicted Prices (Neural Network)')
plt.grid(True)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red', linewidth=2)
plt.tight_layout()
plt.show()