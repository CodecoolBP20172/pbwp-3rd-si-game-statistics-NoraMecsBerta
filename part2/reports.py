
# Report functions
#What is the title of the most played game (i.e. sold the most copies)?, output: string
def get_most_played(file_name):
    with open(file_name, "r") as txt:
        sold_copies_max = 0
        all_info_per_games = [] #a nagy listához
        for game_info in txt.readlines():
            info_per_game = game_info.split('\t')
            all_info_per_games.append(info_per_game) # a nagy listához
        #print(all_info_per_games) # a nagy listához
        for info_per_game in all_info_per_games:
            copies_sold = int(float(info_per_game[1]))
            if copies_sold > sold_copies_max:
                sold_copies_max = copies_sold
                print(sold_copies_max)
        for info_per_game in all_info_per_games:
            s_sold_copies_max = str(int(sold_copies_max))
            if info_per_game[1] == s_sold_copies_max: #== info_per_game[1]:
                print(info_per_game[0])
                return info_per_game[0]
get_most_played('game_stat.txt')


#how many copies have been sold total? output:number
def sum_sold(file_name):
    all_info_per_games = []
    all_sold_copies = 0.0
    with open(file_name, "r") as txt:
        for game_info in txt.readlines():
            info_per_game = game_info.split('\t')
            all_info_per_games.append(info_per_game) # a nagy listához
        for info_per_game in all_info_per_games:
            sold_copies_pergame = float(info_per_game[1])
            all_sold_copies += sold_copies_pergame
            print(sold_copies_pergame)
        print(all_sold_copies)
        return all_sold_copies
sum_sold('game_stat.txt')

#What is the average selling? output: number
def get_selling_avg(file_name):
    all_info_per_games = [] #a nagy listához
    all_sold_copies = 0.0
    number_of_games = 0
    selling_avg = 0.0
    with open(file_name, "r") as txt:
        for game_info in txt.readlines():
            info_per_game = game_info.split('\t')
            all_info_per_games.append(info_per_game) # a nagy listához
        for info_per_game in all_info_per_games:
            sold_copies_pergame = float(info_per_game[1])
            all_sold_copies += sold_copies_pergame
            number_of_games += 1
        selling_avg = all_sold_copies/number_of_games
        print(number_of_games)
        print(all_sold_copies)
        print(selling_avg)
        return selling_avg

get_selling_avg('game_stat.txt')

def count_longest_title(file_name):
    all_info_per_games = [] #a nagy listához
    len_of_title = 0
    with open(file_name, "r") as txt:
        for game_info in txt.readlines():
            info_per_game = game_info.split('\t')
            all_info_per_games.append(info_per_game) # a nagy listához
        for info_per_game in all_info_per_games:
            if len(info_per_game[0]) > len_of_title:
                len_of_title = len(info_per_game[0])
                print(info_per_game[0])
        print(len_of_title)
        print(len(all_info_per_games[23][0]))
        return len_of_title
count_longest_title('game_stat.txt')

# the average of the release dates, average year, number, rounded up
def get_date_avg(file_name):
    all_info_per_games = [] #a nagy listához
    release_date_sums = 0
    number_of_games = 0
    with open(file_name, "r") as txt:
        for game_info in txt.readlines():
            info_per_game = game_info.split('\t')
            all_info_per_games.append(info_per_game) # a nagy listához
        for info_per_game in all_info_per_games:
            release_pergame = int(info_per_game[2])
            release_date_sums += release_pergame
            number_of_games += 1
            print(release_date_sums)
        release_date_avg = round(release_date_sums/number_of_games)
        return release_date_avg
print(get_date_avg('game_stat.txt'))

#properties per game, output: list of various types, output: list of various type
def get_game(file_name, title):
    all_info_per_games = [] #a nagy listához
    number_of_games = -1
    with open(file_name, "r") as txt:
        for game_info in txt.readlines():
            info_per_game = game_info.replace('\n', '').split('\t')
            all_info_per_games.append(info_per_game) # a nagy listához
        for info_per_game in all_info_per_games:
            number_of_games += 1
            if info_per_game[0] == title:
                info_per_game[1] = float(info_per_game[1])
                info_per_game[2] = int(info_per_game[2])
                return all_info_per_games[number_of_games]

print(get_game('game_stat.txt', 'Populous'))