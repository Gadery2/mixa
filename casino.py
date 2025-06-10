import random

RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
BLACK_NUMBERS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}


def get_color(number: int) -> str:
    """Return the color for a given roulette number."""
    if number == 0:
        return "green"
    return "red" if number in RED_NUMBERS else "black"


def roulette() -> None:
    """Simple roulette game."""
    money = 100
    print(f"Ваш стартовый капитал: {money}. Удачи!")
    while money > 0:
        try:
            print(f"Баланс: {money}")
            bet = float(input("Сколько ставим? "))
            if bet > money or bet <= 0:
                print("Некорректная сумма ставки.")
                continue
            bet_input = input("На что ставим? (red/black или число 0-36): ").strip().lower()
            if bet_input in ("red", "black"):
                bet_type = "color"
            elif bet_input.isdigit() and 0 <= int(bet_input) <= 36:
                bet_type = "number"
                bet_number = int(bet_input)
            else:
                print("Некорректная ставка.")
                continue
            winning_number = random.randint(0, 36)
            winning_color = get_color(winning_number)
            print(f"Выпало: {winning_number} ({winning_color})")
            if bet_type == "color" and bet_input == winning_color:
                money += bet
                print(f"Вы выиграли! Баланс: {money}")
            elif bet_type == "number" and bet_number == winning_number:
                money += bet * 35
                print(f"Поздравляем, вы угадали число! Баланс: {money}")
            else:
                money -= bet
                print(f"Вы проиграли. Баланс: {money}")
        except ValueError:
            print("Введите корректное значение.")
    print("Вы банкрот.")


if __name__ == "__main__":
    roulette()
