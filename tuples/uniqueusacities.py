geographical_data = [
    ("India", "Tamil Nadu", "Chennai"),
    ("India", "Tamil Nadu", "Trichy"),
    ("India", "Tamil Nadu", "Coimbatore"),
    ("India", "Maharashtra", "Mumbai"),
    ("India", "Maharashtra", "Pune"),
    ("India", "Maharashtra", "Nagpur"),
    ("India", "Maharashtra", "Thane"),
    ("India", "Karnataka", "Bengaluru"),
    ("India", "Karnataka", "Mysuru"),
    ("USA", "California", "Los Angeles"),
    ("USA", "California", "San Francisco"),
    ("USA", "California", "San Diego"),
    ("USA", "New York", "New York City"),
    ("USA", "New York", "Buffalo"),
    ("Canada", "Ontario", "Toronto"),
    ("Canada", "Ontario", "Ottawa"),
    ("Canada", "British Columbia", "Vancouver"),
    ("Canada", "British Columbia", "Victoria"),
    ("India", "Maharashtra", "Mumbai"), # Deliberate duplicate
    ("USA", "California", "Los Angeles") # Another deliberate duplicate
]

def find_unique_us_cities(geographical_data):
    unique_us_cities = []

    for places in geographical_data:
        if type(places) is tuple and len(places) == 3:
            country = places[0]
            city = places[2]

            if country == "USA" and city not in unique_us_cities:
                unique_us_cities.append(city)

    return unique_us_cities


result = find_unique_us_cities(geographical_data)
print("The unique US cities are:",result)


