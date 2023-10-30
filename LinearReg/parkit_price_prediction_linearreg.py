import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math
import joblib
from sklearn.metrics import mean_squared_error

"""**Dataset Loading**

*Params:*
* Parking ID (Numeric)
* Day of the week (1-7 for days of the week)
* Time of day (in 4 digit hour format - 12pm = 1200 hours)
* Amenity type	(IDs given to different amenities - Mall': 1, 'Museum': 2, 'Garden': 3, 'Park': 4, 'Restaurant': 5, 'Bar': 6, 'Club': 7, 'Hotel': 8, 'Guesthouse': 9, 'Hospital': 10)
* User rating of parking(0-5)
* Handicap accessible	(0 - No, 1 - Yes)
* Distance to amenity	(meters)
* Price (INR)


"""

df = pd.read_csv('parking_prices.csv')

from sklearn.model_selection import train_test_split

X = df[['Day of the week', 'Time of day', 'Amenity type', 'Distance to amenity', 'User rating of parking', 'Handicap accessible']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

model_filename = 'linear_regression_model.pkl'
joblib.dump(model, model_filename)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print('Mean squared error:', mse)

# Plotting the actual vs. predicted prices
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual Prices vs. Predicted Prices (Linear Regression)')
plt.grid(True)

plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red', linewidth=2)
plt.tight_layout()

plt.show()
