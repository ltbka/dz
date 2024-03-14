import random
from decouple import config

INITIAL_CAPITAL = float(config('MY_MONEY', default=1000))

def play_game():
    money = INITIAL_CAPITAL
    while True:
        bet = float(input(f'Введите сумму ставки (ваш текущий баланс: ${money}): '))
        if bet > money:
            print('У вас недостаточно денег для этой ставки. ')
            continue
        slot = int(input('Выберите число от 1 до 10: '))
        winning_slot = random.randint(1, 10)
        if slot == winning_slot:
            money += bet
            print(f'Поздравляем! Вы выиграли ${bet * 2}!')
        else:
            money -= bet
            print(f'Вы проиграли ${bet}. Правильное число было: {winning_slot}.')
        print(f'У вас осталось ${money}.')
        play_again = input('Сыграть еще? (да/нет): ').lower()
        if play_again != 'да':
            break
    print(f'Игра окончена. Ваш итоговый баланс: ${money}')

if __name__ == "__main__":
    play_game()

