def find_unique_city_names(data):
    city_count = {}
    for country, state, city in data:
        if city not in city_count:
            city_count[city] = 1
        else:
            city_count[city] += 1

    return [city for city in city_count if city_count[city] == 1]


def find_unique_us_cities(data):
    unique_us_cities = []
    for country, state, city in data:
        if country == "USA" and city not in unique_us_cities:
            unique_us_cities.append(city)
    return unique_us_cities
