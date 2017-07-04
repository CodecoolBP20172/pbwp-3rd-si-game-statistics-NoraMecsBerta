import reports

# Printing functions


def count_games_print(file_name):
    print(reports.count_games(file_name))


def decide_print(file_name, year):
    print(reports.decide(file_name, year))


def get_latest_print(file_name):
    print(reports.get_latest(file_name))


def count_by_genre_print(file_name, genre):
    print(reports.count_by_genre(file_name, genre))


def get_line_number_by_title_print(file_name, title):
    print(reports.get_line_number_by_title(file_name, title))


count_games_print('game_stat.txt')
decide_print('game_stat.txt', 1950)
get_latest_print('game_stat.txt')
count_by_genre_print('game_stat.txt', 'Simulation')
get_line_number_by_title_print('game_stat.txt', 'Populous')

