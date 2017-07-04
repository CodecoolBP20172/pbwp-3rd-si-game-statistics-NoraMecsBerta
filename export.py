

import reports

# Export functions


def export_answers(file_name='new_file.txt'):
    with open(file_name, "w") as txt:
        lines_of_text = [str(reports.count_games('game_stat.txt')), \
                         str(reports.decide('game_stat.txt', '2000')),\
                         reports.get_latest('game_stat.txt'), \
                         str(reports.count_by_genre('game_stat.txt', 'RPG')), \
                         str(reports.get_line_number_by_title('game_stat.txt', 'Doom 3'))]
        for item in lines_of_text:
            txt.write('%s\n' % item)

export_answers()
