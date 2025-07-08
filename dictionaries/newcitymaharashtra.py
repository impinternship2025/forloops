#Add a new City in Mahatrashtra called “Thane”
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
                    "cities": [{"name": "Mumbai"}, {"name": "Pune"}, {"name": "Nagpur"}]
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


def add_thane_to_maharashtra(world, target_country, target_state, city_to_be_added):
    for country in world.get("country", []):
        if type(country) is not dict:
            continue

        if country.get("name") == target_country:
            for state in country.get("state", []):
                if type(state) is not dict:
                    continue

                if state.get("name") == target_state:
                    state.get("cities", []).append(city_to_be_added)
                    print(f"{city_to_be_added['name']} added to {target_state} ")

                    print(f"Cities in {target_state} after addition:")
                    for city in state.get("cities", []):
                        print(f"{city['name']}")
                    return  



target_country = "India"
target_state = "Maharashtra"
city_to_be_added = {"name": "Thane"}

add_thane_to_maharashtra(world, target_country, target_state, city_to_be_added)
