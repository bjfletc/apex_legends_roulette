import players


def main():
    players_playing = players.players()
    chosen_characters = players.select_characters()
    chosen_weapons = players.select_weapons()

    # for style above program output to console
    program_header()

    for index, player in enumerate(players_playing):
        # multiply the index # by 2 to get every two pairs of weapons
        index *= 2
        print(f'{player:10}: {chosen_characters[player]:20} | Weapon 1: {chosen_weapons[index]:20}'
              f' Weapon 2: {chosen_weapons[index + 1]}')

    # for style below program output to console
    program_footer()


def program_header():
    print()
    print('-' * 35, end='')
    print(' Apex Legends Roulette ', end='')
    print('-' * 35)
    print()


def program_footer():
    print()
    print('-' * 94)


if __name__ == '__main__':
    main()
