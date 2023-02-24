import random

categorical_weapons = {'ARs': ['HAVOC', 'Flatline', 'Hemlock', 'R-301', 'Nemesis'],
                       'SMGs': ['Alternator', 'Prowler', 'R-99', 'Volt', 'C.A.R.'],
                       'LMGs': ['Devotion', 'L-STAR', 'Spitfire', 'Rampage'],
                       'Marksman': ['G7 Scout', 'Triple Take', '30-30 Repeater', 'Bocek Compound Bow'],
                       'Snipers': ['Charge Rifle', 'Longbow', 'Kraber', 'Sentinel'],
                       'Shotguns': ['EVA-8', 'Mastiff', 'Mozambique', 'Peacekeeper'],
                       'Pistols': ['RE-45', 'P2020', 'Wingman'],
                       'Season Supply Drop Weapons': ['Hemlock', 'RE-45', 'Bocek Compound Bow', 'Kraber'],
                       'Other': ['Ordnances', 'Fists', 'Supply Drop Weapons']}


def weapons() -> list[str]:
    all_weapons = []

    # get each list of weapons by category from the dictionary
    for weapons_category in categorical_weapons.values():
        # add each weapon from current category to the list of all_weapons
        for weapon in weapons_category:
            if weapon in categorical_weapons['Season Supply Drop Weapons']:
                continue
            else:
                all_weapons.append(weapon)

    return all_weapons


# used to choose weapons for player
def random_weapon() -> str:
    return random.choice(weapons())
