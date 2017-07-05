import reports
# Export functions


def export_answers(file_name='export_judy.txt'):
    with open(file_name, "w") as txt:
        lines_of_text = [reports.get_most_played('game_stat.txt'), \
                         str(reports.sum_sold('game_stat.txt')),\
                         str(reports.get_selling_avg('game_stat.txt')), \
                         str(reports.count_longest_title('game_stat.txt')), \
                         str(reports.get_date_avg('game_stat.txt')),
                         str(reports.get_game('game_stat.txt', 'Age of Empires'))]
        for item in lines_of_text:
            txt.write('%s\n' % item)

export_answers()
