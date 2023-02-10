import random
from prettytable import PrettyTable

table = PrettyTable()

player_names = ['Emma', 'Lewiz', 'Alex', 'Ike', 'Rita', 'Liam'
                'John', 'Chione', 'Demetria', 'Montezuma',
                'Olivia', 'Yuri', 'Yulian', 'Roma',
                ]
player_names.sort()
table.add_column("Participants", player_names)


print(table)
players_score = []
fixtures = []
fixed_list = []

is_game_started = False


def start_game():
    if not len(player_names) % 2 == 0:
        player_names.append('Computer')
        print(
            "\nComputer will join u guys since the total no of players isnt even")

    else:

        for players in player_names:
            # initialize every player zero point
            players_score.append((players, 0))
            players_score.sort()  # re-arrange the table

        global is_game_started
        is_game_started = True


def make_fixtures():
    is_game_started = False

    global fixtures
    global fixed_list
    while (len(fixtures) != len(player_names) / 2):

        random_selected_home_player = random.choice(player_names)
        random_selected_away_player = random.choice(player_names)

        if (random_selected_home_player != random_selected_away_player) and random_selected_home_player not in fixed_list and random_selected_away_player not in fixed_list:

            fixtures.append((random_selected_home_player,
                            random_selected_away_player))
            fixed_list.append(random_selected_home_player)
            fixed_list.append(random_selected_away_player)

        else:
            make_fixtures()


def get_fixtures():
    print("Here are the fixtures!!!")
    for home_play, away_player in fixtures:
        print(f"\n{home_play} will play {away_player}")
    print('\nSurvival of the fittest!!!\n May the best win.....')


while not is_game_started:
    start_game()

while len(player_names) != len(fixed_list):
    make_fixtures()
    get_fixtures()
