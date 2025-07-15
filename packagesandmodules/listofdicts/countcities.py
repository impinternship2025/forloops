# from statesandcities import world

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


# count_cities_in_all_states_of_countries(world)