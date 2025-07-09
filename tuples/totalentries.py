#Find the total entries

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

def count_total_entries(geographical_data):
    if type(geographical_data) is list:                     
        total = len(geographical_data)                      
        print(f"Total number of entries: {total}")
    else:
        print("Input is not a valid list.")    

count_total_entries(geographical_data)
