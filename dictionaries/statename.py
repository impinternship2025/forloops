#Find the state of the city “Ottawa”

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

target_city = "Ottawa"

def state_in_which_ottawa_is_present(world):
    for country in world["country"]:
        if type(country) is not dict:
            continue

        for key1 in country:
            value1 = country[key1]

            if key1 == "state" and isinstance(value1, list):
                for state in value1:
                    if type(state) is not dict:
                        continue

                    for city in state.get("cities", []):
                        if type(city) is not dict:
                            continue

                        if city.get("name") == target_city:
                            print(f" The city '{target_city}' is in state: '{state['name']}', country: '{country['name']}'")
                            return

    print(f"The city '{target_city}' was not found.")

state_in_which_ottawa_is_present(world)