#Write a search function that search by name and return the path.
# For example, if I give Ottawa, it should print Canada --> Ontario --> Ottawa
# If I give British Columbia , then it should print Canada --> British Columbia

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

def search_path_of_location(world):
    target_name = "Tamil Nadu"  
    
    for country in world["country"]:
        if type(country) is not dict:
            continue

        country_name = country.get("name")

        for state in country.get("state", []):
            if type(state) is not dict:
                continue

            state_name = state.get("name")

            if state_name == target_name:
                print(f" Found: {country_name} --> {state_name}")
                return

            for city in state.get("cities", []):
                if type(city) is not dict:
                    continue

                city_name = city.get("name")

                if city_name == target_name:
                    print(f"Found: {country_name} --> {state_name} --> {city_name}")
                    return

    print(f"'{target_name}' not found in the given dictionary")

search_path_of_location(world)