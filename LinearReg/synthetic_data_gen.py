import random
import csv

# Create a list of amenity types
amenity_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of days of the week
days_of_week = [1, 2, 3, 4, 5, 6, 7]

# Create a list of times of day in 24-hour format
times_of_day = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300]

# Create a list of distances to amenities
distances_to_amenities = [100, 200, 300, 400, 500]

# Create a list of user ratings of parking
user_ratings_of_parking = [1.0, 2.0, 3.0, 4.0, 5.0]

# Create a list of handicap accessible flags
handicap_accessible_flags = [True, False]

# Create a list of data points
data_points = []

for i in range(1000):
    # Generate a random amenity type
    amenity_type = random.choice(amenity_types)

    # Generate a random day of the week
    day_of_week = random.choice(days_of_week)

    # Generate a random time of day in 24-hour format
    time_of_day = random.choice(times_of_day)

    # Generate a random distance to the amenity
    distance_to_amenity = random.choice(distances_to_amenities)

    # Generate a random user rating of parking
    user_rating_of_parking = random.choice(user_ratings_of_parking)

    # Generate a random handicap accessible flag
    handicap_accessible_flag = random.choice(handicap_accessible_flags)

    # Generate a random price between 10 and 100 rupees as a multiple of 10
    price = random.randint(1, 10) * 10

    # Create a new data point
    data_point = {'Amenity type': amenity_type, 'Day of the week': day_of_week, 'Time of day': time_of_day, 'Distance to amenity': distance_to_amenity, 'User rating of parking': user_rating_of_parking, 'Handicap accessible': handicap_accessible_flag, 'Price': price}

    # Add the new data point to the list of data points
    data_points.append(data_point)

# Write the data points to a CSV file
with open('parking_prices.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data_points[0].keys())
    
    # Write the header row
    writer.writeheader()
    
    # Write the data points
    writer.writerows(data_points)
