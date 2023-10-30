# import pandas as pd
# import numpy as np
# import math

# # Define the number of synthetic data points you want to create
# num_synthetic_data = 25000

# # Define the range and distribution for each feature
# # You can customize these based on the characteristics of your actual data
# day_of_week_range = [1, 7]  # Days of the week
# time_of_day_range = [800, 2000]  # Time of day (in 4 digit hour format)
# amenity_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Amenity types
# distance_range = [50, 5000]  # Distance to amenity (in meters)
# user_rating_range = [1.0, 5.0]  # User rating of parking
# handicap_values = [0, 1]  # Handicap accessible

# # Create synthetic data for each feature
# day_of_week = np.random.randint(day_of_week_range[0], day_of_week_range[1] + 1, num_synthetic_data)
# time_of_day = np.random.randint(time_of_day_range[0], time_of_day_range[1] + 1, num_synthetic_data)
# amenity_type = np.random.choice(amenity_types, num_synthetic_data)
# distance_to_amenity = np.random.randint(distance_range[0], distance_range[1] + 1, num_synthetic_data)
# user_rating = np.random.uniform(user_rating_range[0], user_rating_range[1], num_synthetic_data)
# handicap_accessible = np.random.choice(handicap_values, num_synthetic_data)

# # Calculate the 'Price' based on user rating and distance
# # You can adjust the coefficients as needed to control the impact of each factor on price
# price = np.ceil(user_rating * 10 + (1 / (distance_to_amenity / 1000 + 1)) * 10)
# price = np.clip(price, 1, 200)  # Clip the values to the desired range (1-200)


# # Create a DataFrame for the synthetic data
# synthetic_data = pd.DataFrame({
#     'Day of the week': day_of_week,
#     'Time of day': time_of_day,
#     'Amenity type': amenity_type,
#     'Distance to amenity': distance_to_amenity,
#     'User rating of parking': user_rating,
#     'Handicap accessible': handicap_accessible,
#     'Price': price
# })

# # Save the synthetic data to a CSV file
# synthetic_data.to_csv('synthetic_parking_prices.csv', index=False)
import pandas as pd
import numpy as np
import math

# Define the number of synthetic data points you want to create
num_synthetic_data = 50000

# Define the range and distribution for each feature
# You can customize these based on the characteristics of your actual data
day_of_week_range = [1, 7]  # Days of the week
time_of_day_range = [800, 2000]  # Time of day (in 4 digit hour format)
amenity_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Amenity types
distance_range = [50, 5000]  # Distance to amenity (in meters)
user_rating_range = [1.0, 5.0]  # User rating of parking
handicap_values = [0, 1]  # Handicap accessible

# Create synthetic data for each feature
day_of_week = np.random.randint(day_of_week_range[0], day_of_week_range[1] + 1, num_synthetic_data)
time_of_day = np.random.randint(time_of_day_range[0], time_of_day_range[1] + 1, num_synthetic_data)
amenity_type = np.random.choice(amenity_types, num_synthetic_data)
distance_to_amenity = np.random.randint(distance_range[0], distance_range[1] + 1, num_synthetic_data)
user_rating = np.random.uniform(user_rating_range[0], user_rating_range[1], num_synthetic_data)
handicap_accessible = np.random.choice(handicap_values, num_synthetic_data)

# Calculate the 'Price' based on user rating and distance with adjusted coefficients
# You can adjust the coefficients to control the impact of each factor on price
price = np.ceil(user_rating * 5 + (1 / (distance_to_amenity / 1000 + 1)) * 20)
price = np.clip(price, 1, 200)  # Clip the values to the desired range (1-200)

# Create a DataFrame for the synthetic data
synthetic_data = pd.DataFrame({
    'Day of the week': day_of_week,
    'Time of day': time_of_day,
    'Amenity type': amenity_type,
    'Distance to amenity': distance_to_amenity,
    'User rating of parking': user_rating,
    'Handicap accessible': handicap_accessible,
    'Price': price
})

# Save the synthetic data to a CSV file
synthetic_data.to_csv('synthetic_parking_prices.csv', index=False)
