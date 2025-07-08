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

def match_states_with_target(world):
    target_states = ["Tamil Nadu", "West Bengal", "California"]
    matched_states = []

    for country in world["country"]:
        if type(country) is not dict:
            continue

        country_name = country.get("name")

        for state in country.get("state", []):
            if type(state) is not dict:
                continue

            state_name = state.get("name")

            if state_name in target_states:
                print(f"Match found: {state_name} (Country: {country_name})")
                matched_states.append(state_name)

    print(f"Matched states are: {matched_states}")

match_states_with_target(world)
