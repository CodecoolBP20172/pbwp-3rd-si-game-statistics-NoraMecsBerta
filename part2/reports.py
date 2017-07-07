# Report functions


def read_file(file_name):
    all_info_per_games = []
    with open(file_name, "r") as txt:
        for game_info in txt:
            info_per_game = game_info.strip().split('\t')
            all_info_per_games.append(info_per_game)
        print(all_info_per_games)
        return all_info_per_games


#What is the title of the most played game (i.e. sold the most copies)?, output: string
def get_most_played(file_name):
    sold_copies_max = 0.0
    all_info_per_games = read_file(file_name)
    for info_per_game in all_info_per_games:
        copies_sold = float(info_per_game[1])
        if copies_sold > sold_copies_max:
            sold_copies_max = copies_sold
    if sold_copies_max % 1 == 0:
        sold_copies_max = int(sold_copies_max)
    for info_per_game in all_info_per_games:
        s_sold_copies_max = str(sold_copies_max)
        if info_per_game[1] == s_sold_copies_max:
            return info_per_game[0]

print(get_most_played('game_stat.txt'))


#how many copies have been sold total? output:number
def sum_sold(file_name):
    all_sold_copies = 0.0
    all_info_per_games = read_file(file_name)
    for info_per_game in all_info_per_games:
        sold_copies_pergame = float(info_per_game[1])
        all_sold_copies += sold_copies_pergame
    return all_sold_copies

print(sum_sold('game_stat.txt'))


#What is the average selling? output: number
def get_selling_avg(file_name):
    all_sold_copies = 0.0
    number_of_games = 0
    selling_avg = 0.0
    all_info_per_games = read_file(file_name)
    for info_per_game in all_info_per_games:
        sold_copies_pergame = float(info_per_game[1])
        all_sold_copies += sold_copies_pergame
        number_of_games += 1
    selling_avg = all_sold_copies/number_of_games
    return selling_avg

print(get_selling_avg('game_stat.txt'))


def count_longest_title(file_name):
    len_of_title = 0
    all_info_per_games = read_file(file_name)
    for info_per_game in all_info_per_games:
        if len(info_per_game[0]) > len_of_title:
            len_of_title = len(info_per_game[0])
    return len_of_title

print(count_longest_title('game_stat.txt'))


# the average of the release dates, average year, number, rounded up
def get_date_avg(file_name):
    release_date_sums = 0
    number_of_games = 0
    all_info_per_games = read_file(file_name)
    for info_per_game in all_info_per_games:
        release_pergame = int(info_per_game[2])
        release_date_sums += release_pergame
        number_of_games += 1
    release_date_avg = round(release_date_sums/number_of_games)
    return release_date_avg

print(get_date_avg('game_stat.txt'))


#properties per game, output: list of various types, output: list of various type
def get_game(file_name, title):
    number_of_games = -1
    all_info_per_games = read_file(file_name)
    for info_per_game in all_info_per_games:
        number_of_games += 1
        if info_per_game[0] == title:
            info_per_game[1] = float(info_per_game[1])
            info_per_game[2] = int(info_per_game[2])
            return all_info_per_games[number_of_games]

print(get_game('game_stat.txt', 'Age of Empires'))

#games are there grouped by genre? dictionary {[genre]: [count]}
def count_grouped_by_genre(file_name):
    grouped_bygenre = {}
    genre_keys = []
    genre_values = []
    count_bygenre = 0
    all_info_per_games = read_file(file_name)
    for info_per_game in all_info_per_games:
        if info_per_game[3] not in genre_keys:
            genre_keys.append(info_per_game[3])
    for genre_index in range(len(genre_keys)):
        for info_per_game in all_info_per_games:
            if info_per_game[3] == genre_keys[genre_index]:
                count_bygenre += 1
        genre_values.append(count_bygenre)
        count_bygenre = 0
    grouped_bygenre.update(zip(genre_keys, genre_values))
    return grouped_bygenre

print(count_grouped_by_genre('game_stat.txt'))



#date ordered list of the games, output list, desc, strings of list, secondary -alphabetical, asc
def get_date_ordered(file_name):
    list_of_dates = []
    desc_dates = []
    games_list = []
    games_list_for_sort = []
    all_info_per_games = read_file('game_stat.txt')
    for info_per_game in all_info_per_games:
        if info_per_game[2] not in list_of_dates:
            list_of_dates.append(info_per_game[2])
            list_of_dates.sort()
            desc_dates = list_of_dates[::-1]
    for desc_index in range(len(desc_dates)):
        for info_per_game in all_info_per_games:
            if info_per_game[2] == desc_dates[desc_index]:
                games_list_for_sort.append(info_per_game[0])
        if len(games_list_for_sort) > 1:
            games_list_for_sort.sort()
            games_list.extend(games_list_for_sort)
            games_list_for_sort = []
        else:
            games_list.extend(games_list_for_sort)
            games_list_for_sort = []
    return games_list
print(get_date_ordered('game_stat.txt'))
