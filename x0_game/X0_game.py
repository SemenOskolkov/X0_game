print('Привет!')

'''Ввод игроков'''
player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')

players = [player_1, player_2]
for i in range(len(players)):
    print(f'Игрок {i + 1}: \n{players[i].title()}')

game_symbols = ['X', '0']

'''Значение для каждой ячейки хранится в списке'''
numbers_game = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def playground(numbers_game):
    '''Функция, отрисовывает поле'''
    print('-' * 13)
    print(f'| {numbers_game[0]} | {numbers_game[1]} | {numbers_game[2]} |')
    print('-' * 13)
    print(f'| {numbers_game[3]} | {numbers_game[4]} | {numbers_game[5]} |')
    print('-' * 13)
    print(f'| {numbers_game[6]} | {numbers_game[7]} | {numbers_game[8]} |')
    print('-' * 13)


def player_1_move(player_symbol):
    '''Функцию, которая проверяет возможность поставить значение в клетке'''
    '''В данной функции проверяется, что клетка пуста и что пользователь ввел число'''
    condition = False
    while not condition:
        player_answer = input(f'Ходит {player_1.title()} \nКуда ставить X? ')
        if player_answer.isdigit():
            player_answer = int(player_answer)
            if 1 <= player_answer <= 9:
                if numbers_game[(player_answer) - 1] not in game_symbols[0:]:
                    numbers_game[(player_answer) - 1] = player_symbol
                    condition = True
        else:
            print(f'Некорректный ввод. Введите число')


def player_2_move(player_symbol):
    condition = False
    while not condition:
        player_answer = input(f'Ходит {player_2.title()} \nКуда ставить 0? ')
        if player_answer.isdigit():
            player_answer = int(player_answer)
            if 1 <= player_answer <= 9:
                if numbers_game[player_answer - 1] not in game_symbols[0:]:
                    numbers_game[player_answer - 1] = player_symbol
                    condition = True
        else:
            print(f'Некорректный ввод. Введите число')


def check_win(numbers_game):
    '''Функция, которая проверяет, есть ли выигрышная комбинация на поле'''
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for comb in win_comb:
        if numbers_game[comb[0]] == numbers_game[comb[1]] == numbers_game[comb[2]]:
            return numbers_game[comb[0]]
    return False


def main_func(numbers_game):
    '''Описать в главной функции с помощью цикла все вышеописанные функции'''
    '''Добавить в главной функции ввод имени пользователя и вывод имени победившего игрока'''
    game_step = 0  # Взял за основу счетчик ходов
    win = False
    while not win:
        playground(numbers_game)
        if game_step % 2 == 0:
            player_1_move('X')
        else:
            player_2_move('0')
        game_step += 1
        if game_step == 5 or game_step == 7:
            win_win = check_win(numbers_game)
            if win_win:
                print(f'Победил(а) {player_1.title()}.')
                break
        if game_step == 6 or game_step == 8:
            win_win = check_win(numbers_game)
            if win_win:
                print(f'Победил(а) {player_2.title()}.')
                break
        if game_step == 9:
            win_win = check_win(numbers_game)
            if win_win:
                print(f'Победил(а) {player_1.title()}.')
            else:
                print(f'Ничья')
            break
    playground(numbers_game)


main_func(numbers_game)


if __name__ == '__main__':
    main()
