# Check if “New York” belongs to country “India”

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

def check_if_newyork_in_india(world):
    target_country = "India"
    target_state = "New York"
    
    for country in world["country"]:
        if type(country) is not dict:
            continue

        if country.get("name") == target_country:
            for state in country.get("state", []):
                if type(state) is not dict:
                    continue

                if state.get("name") == target_state:
                    print(f"Yes, '{target_state}' belongs to '{target_country}'.")
                    return

            print(f"No, '{target_state}' does NOT belong to '{target_country}'.")
            return

    print(f"Country '{target_country}' not found.")

    check_if_newyork_in_india(world)