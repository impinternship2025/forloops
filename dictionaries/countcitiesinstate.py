#Print the count of cities in each state in each country

world = {
    "country": [
        {
            "name": "India",
            "state": [
                {
                    "name": "Tamil Nadu",
                    "cities": [{"name": "Chennai"}, {"name": "Trichy"}, {"name": "Coimbatore"}]
                },
                {
                    "name": "Maharashtra",
                    "cities": [{"name": "Mumbai"}, {"name": "Pune"}, {"name": "Nagpur"}, {"name": "Thane"}]
                },
                {
                    "name": "Karnataka",
                    "cities": [{"name": "Bengaluru"}, {"name": "Mysuru"}]
                }
            ]
        },
        {
            "name": "USA",
            "state": [
                {
                    "name": "California",
                    "cities": [{"name": "Los Angeles"}, {"name": "San Francisco"}, {"name": "San Diego"}]
                },
                {
                    "name": "New York",
                    "cities": [{"name": "New York City"}, {"name": "Buffalo"}]
                }
            ]
        },
        {
            "name": "Canada",
            "state": [
                {
                    "name": "Ontario",
                    "cities": [{"name": "Toronto"}, {"name": "Ottawa"}]
                },
                {
                    "name": "British Columbia",
                    "cities": [{"name": "Vancouver"}, {"name": "Victoria"}]
                }
            ]
        }
    ]
}

def count_cities_in_all_states_of_countries(world):
    for country in world["country"]:
        if type(country) is not dict:
            continue

        print(f"Country: {country.get('name')}")

        states = country.get("state", [])
        for state in states:
            if type(state) is not dict:
                continue

            state_name = state.get("name")
            cities = state.get("cities", [])
            city_count = len(cities)

            print(f"State: {state_name} , Total Cities: {city_count}")


count_cities_in_all_states_of_countries(world)