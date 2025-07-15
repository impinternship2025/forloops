#from statesandcities import world

def match_states_and_cities_with_target(world):
    target_states_cities = [{"name":"Tamil Nadu", "cities":[{"name":"Chennai"}]}, {"name":"West Bengal","cities":[{"name":"Calcutta"}]}]
    matched_states = []

    for country in world["country"]:
        if type(country) is not dict:
            continue

        country_name = country.get("name")

        for state in country.get("state", []):
            if type(state) is not dict:
                continue

            state_name = state.get("name")
            state_cities = state.get("cities", [])

            for target_state in target_states_cities:
                if target_state["name"] == state_name:

                    matched_cities = []
                    for city in target_state["cities"]:
                        if city in state_cities:
                            matched_cities.append(city)
                    
                    if matched_cities:
                        matched_states.append({
                            "country": country_name,
                            "state": state_name,
                            "cities": matched_cities
                        })
    
    print("Matched states and cities are:", matched_states)

#match_states_and_cities_with_target(world)

                            




            
                