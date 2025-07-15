def repeating_states(data):
    state_count = {}
    for country, state, city in data:
        if state not in state_count:
            state_count[state] = 1
        else:
            state_count[state] += 1
    return state_count

