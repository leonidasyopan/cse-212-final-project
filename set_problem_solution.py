# Board games in store
board_games = {"Ticket to Ride", "Catan",
               "7 Wonders", "Articulate!", "Azul"}

# Card Games in store
card_games = {"Monikers", "Scrimish", "Coup",
              "Death on the Cards", "Skyjo", "Duet"}


def add_board_game(game):
    if game in board_games:
        print("This game is already registered")
    else:
        board_games.add(game)
        print(game + " was added to the collection")


def add_card_game(game):
    if game in card_games:
        print("This game is already registered")
    else:
        card_games.add(game)
        print(game + " was added to the collection")


def list_all_games():
    all_games = board_games.union(card_games)
    for game in all_games:
        print(game)


new_board_game = input("Enter new board game name: ")
add_board_game(new_board_game)

new_card_game = input("Enter new card game name: ")
add_card_game(new_card_game)

list_all_games()
