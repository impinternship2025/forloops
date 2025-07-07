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


def add_thane_to_maharashtra(world):
    for country in world["country"]:
        if type(country) is not dict:
            continue

        if country.get("name") == "India":
            for state in country.get("state", []):
                if type(state) is not dict:
                    continue

                if state.get("name") == "Maharashtra":
                    state.get("cities", []).append({"name": "Thane"})
                    print("Thane added to Maharashtra successfully!")

                    print("Cities in Maharashtra after addition:")
                    for city in state.get("cities", []):
                        print(f"{city['name']}")


add_thane_to_maharashtra(world)
