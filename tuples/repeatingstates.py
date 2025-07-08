#Find the number of times each state has repeated

geographical_data = [
    ("India", "Tamil Nadu", "Chennai"),
    ("India", "Tamil Nadu", "Trichy"),
    ("India", "Tamil Nadu", "Coimbatore"),
    ("India", "Maharashtra", "Mumbai"),
    ("India", "Maharashtra", "Pune"),
    ("India", "Maharashtra", "Nagpur"),
    ("India", "Maharashtra", "Thane"),
    ("India", "Karnataka", "Bengaluru"),
    ("India", "Karnataka", "Mysuru"),
    ("USA", "California", "Los Angeles"),
    ("USA", "California", "San Francisco"),
    ("USA", "California", "San Diego"),
    ("USA", "New York", "New York City"),
    ("USA", "New York", "Buffalo"),
    ("Canada", "Ontario", "Toronto"),
    ("Canada", "Ontario", "Ottawa"),
    ("Canada", "British Columbia", "Vancouver"),
    ("Canada", "British Columbia", "Victoria"),
    ("India", "Maharashtra", "Mumbai"), # Deliberate duplicate
    ("USA", "California", "Los Angeles") # Another deliberate duplicate
]

def repeating_states(geographical_data):
    repeating_states = {}

    for places in geographical_data:
        if type(places) is tuple and len(places) == 3:
            state = places[1]  

            if state not in repeating_states:
                repeating_states[state] = 1
            else:
                repeating_states[state] += 1

    return repeating_states

result = repeating_states(geographical_data)
print("The repeating states are:", result)

