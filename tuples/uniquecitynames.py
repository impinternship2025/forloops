#Find all unique city names that doesn’t have duplicates

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

def find_unique_city_names(geographical_data):
    city_count = {}

    for places in geographical_data:
        if type(places) is tuple and len(places):
            city = places[2]
            if city not in city_count:
                city_count[city] = 1
            else:
                city_count[city] += 1

    unique_cities = []
    for city in city_count:
        if city_count[city] == 1:
            unique_cities.append(city)

    return unique_cities


result = find_unique_city_names(geographical_data)     
print("The unique city names are:",result)   