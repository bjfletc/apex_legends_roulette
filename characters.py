import random

characters_by_class = {
    'Assault': ['Ash', 'Fuse', 'Mad Maggie', 'Bangalore', 'Revenant'],
    'Skirmisher': ['Pathfinder', 'Horizon', 'Octane', 'Valkyrie', 'Wraith', 'Mirage'],
    'Recon': ['Bloodhound', 'Crypto', 'Seer', 'Vantage'],
    'Controller': ['Caustic', 'Wattson', 'Rampart', 'Catalyst'],
    'Support': ['Lifeline', 'Loba', 'Newcastle', 'Gibraltar']
}


def characters() -> list[str]:
    all_characters = []

    # get each list of characters by class from the dictionary
    for characters_for_class in characters_by_class.values():
        # add each character from current class to the list of all_characters
        for character in characters_for_class:
            all_characters.append(character)

    return all_characters


# used to choose character for player
def random_character() -> str:
    return random.choice(characters())
