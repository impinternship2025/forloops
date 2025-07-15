from tuples.geographicaldata import get_data
from tuples.totalentries1 import count_total_entries
from tuples.uniquecities import find_unique_city_names, find_unique_us_cities
from tuples.repeatingstates import repeating_states

def run_all():
    data = get_data()

    total = count_total_entries(data)
    print(f"Total entries: {total}")

    states = repeating_states(data)
    print("Repeating states and counts:", states)

    unique = find_unique_city_names(data)
    print("Unique cities (no duplicates):", unique)

    us_unique = find_unique_us_cities(data)
    print("Unique US cities:", us_unique)

run_all()
