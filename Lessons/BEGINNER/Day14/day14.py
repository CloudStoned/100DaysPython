import gamedata as gd
import random

def compare_game_entries():
    # Generate random indices within the range of available game data
    comp_a_num = random.randint(0, 50)
    comp_b_num = random.randint(0, 50)

    # Retrieve follower count for the randomly selected game data entries
    comp_a_follower = gd.data[comp_a_num]['follower_count']
    comp_b_follower = gd.data[comp_b_num]['follower_count']

    # Create dictionaries for comp_a and comp_b using selected game data attributes
    comp_a = {
        'name': gd.data[comp_a_num]['name'],
        'description': gd.data[comp_a_num]['description'],
        'country': gd.data[comp_a_num]['country']
    }

    comp_b = {
        'name': gd.data[comp_b_num]['name'],
        'description': gd.data[comp_b_num]['description'],
        'country': gd.data[comp_b_num]['country']
    }

    # Store comp_a and comp_b dictionaries in a list
    entries = [comp_a, comp_b]

    return entries

def print_entry(entry):
    print(f"Name: {entry['name']}")
    print(f"Description: {entry['description']}")
    print(f"Country: {entry['country']}")

# Call the function to compare two game entries and retrieve their dictionaries
entries = compare_game_entries()

# Print the entries in the list
for i, entry in enumerate(entries, start=1):
    print(f"Comparison {i}:")
    print_entry(entry)
    print()  # Print a blank line for separation
