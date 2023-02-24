import characters
import weapons

locked_characters_for_player = {'Brandon': [],
                                'Dakota': ["Horizon", "Seer", "Mad Maggie", "Newcastle", "Catalyst"],
                                'Ryan': ["Rampart", "Horizon", "Ash", "Mad Maggie", "Newcastle", "Catalyst"],
                                'Tanner': []}


def players() -> list[str]:
    all_players = []

    for player in locked_characters_for_player.keys():
        all_players.append(player)

    return all_players


def random_character_for_player(player: str) -> str:
    rand_character = characters.random_character()

    while rand_character in locked_characters_for_player[player]:
        rand_character = characters.random_character()

    return rand_character


def select_characters() -> dict:
    chosen_characters = {}
    players_to_choose_for = players()

    for player in players_to_choose_for:
        players_character = random_character_for_player(player)

        while players_character in chosen_characters.values():
            players_character = random_character_for_player(player)

        chosen_characters[player] = players_character

    return chosen_characters


def select_weapons() -> list[str]:
    chosen_weapons = []

    # choosing weapons based off of how many players there are
    # multiply by 2 times the length of players due to each player
    # getting 2 weapons in this game
    for i in range(len(players()) * 2):
        rand_weapon = weapons.random_weapon()
        while rand_weapon in chosen_weapons:
            rand_weapon = weapons.random_weapon()
        chosen_weapons.append(rand_weapon)

    return chosen_weapons
