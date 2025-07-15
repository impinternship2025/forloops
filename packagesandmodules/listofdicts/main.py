# from  statesandcities import world
# from countcities import count_cities_in_all_states_of_countries
# from matchtargetcities import match_states_and_cities_with_target

from .statesandcities import world
from .countcities import count_cities_in_all_states_of_countries
from .matchtargetcities import match_states_and_cities_with_target

def start_list_of_dicts():
    count_cities_in_all_states_of_countries(world)
    match_states_and_cities_with_target(world)

