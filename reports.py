
# Report functions


def count_games(file_name='game_stat.txt'):
    number_of_games = 0
    all_info_per_games = []
    with open(file_name, "r") as txt:
        for game_info in txt.readlines():
            info_per_game = game_info.split('\t')
            all_info_per_games.append(info_per_game)
            number_of_games += 1
        return number_of_games


def decide(file_name, year):
    all_info_per_games = []
    given_year = str(year)
    with open(file_name, "r") as txt:
        for game_info in txt.readlines():
            info_per_game = game_info.split('\t')
            all_info_per_games.append(info_per_game)
        for info_per_game in all_info_per_games:
            if info_per_game[2] == given_year:
                return True
        for info_per_game in all_info_per_games:
            if info_per_game[2] != given_year:
                return False


def get_latest(file_name):
    latest_game_year = 0
    with open(file_name, "r") as txt:
        all_info_per_games = []
        for game_info in txt.readlines():
            info_per_game = game_info.split('\t')
            all_info_per_games.append(info_per_game)
        for info_per_game in all_info_per_games:
            game_year = int(info_per_game[2])
            if game_year > latest_game_year:
                latest_game_year = game_year
        for info_per_game in all_info_per_games:
            if info_per_game[2] == str(latest_game_year):
                return info_per_game[0]


def count_by_genre(file_name, genre):
    count_game_bygenre = 0
    with open(file_name, "r") as txt:
        all_info_per_games = []
        for game_info in txt.readlines():
            info_per_game = game_info.split('\t')
            all_info_per_games.append(info_per_game)
        for info_per_game in all_info_per_games:
            if info_per_game[3] == genre:
                count_game_bygenre += 1
        return count_game_bygenre


def get_line_number_by_title(file_name, title):
    with open(file_name, "r") as txt:
        line_number = 0
        number_of_games = 0
        all_info_per_games = []
        for game_info in txt.readlines():
            info_per_game = game_info.split('\t')
            all_info_per_games.append(info_per_game)
        for info_per_game in all_info_per_games:
            line_number += 1
            number_of_games += 1
            if title == info_per_game[0]:
                return line_number
        if line_number == number_of_games:
            raise ValueError('This game is not in the list.')
