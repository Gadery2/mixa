import random

money = 100
print(f"Вот твой стартовый капитал: {money}. Удачи!")

def ruletka():
    global money
    choice = input("Хотите сыграть в рулетку? (yes/no): ").strip().lower()
    if choice == "yes":
        print("Отлично. Начнем!")

        while money > 0:
            try:
                print(f"Баланс: {money}")
                bet = float(input("Сколько ставим?: "))
                if bet > money or bet <= 0:
                    print("Не можешь ты столько поставить, идиот.")
                    continue

                bet_input = input("На что ставим? (red/black/green или число 0-36): ").strip().lower()
                
                if bet_input in ["red", "black", "green"]:
                    bet_type = "color"
                elif bet_input.isdigit() and 0 <= int(bet_input) <= 36:
                    bet_type = "number"
                    bet_number = int(bet_input)
                else:
                    print("Ебанат, выбери норм ставку.")
                    continue

                winning_number = random.randint(0, 36)
                winning_color = "green" if winning_number == 0 else ("red" if winning_number % 2 == 0 else "black")

                print(f"Выпало: {winning_color} {winning_number}")

                if bet_type == "color" and bet_input == winning_color:
                    if winning_color == "green":
                        money -= bet
                        money += bet * 14
                    else:
                        money -= bet
                        money += bet * 2
                    print(f"Поздравляю, ты выиграл! Новый баланс: {money}")
                elif bet_type == "number" and bet_number == winning_number:
                    money -= bet
                    money += bet * 36
                    print(f"Поздравляю, ты угадал число! Новый баланс: {money}")
                else:
                    money -= bet
                    print(f"ЛОХ! Ты проиграл. Новый баланс: {money}")
            except ValueError:
                print("Пиши норм значение, уёбок.")

        print("Ты банкрот!")
        leave = input("Нажми Enter, чтобы выйти...")
        quit()

    elif choice == "no":
        print("Ну и иди нахуй")
        leave = input("Нажми Enter, чтобы выйти...")
        quit()
    else:
        print("Бля, по кнопкам не попадаешь? Давай ещё раз.")
        ruletka()
ruletka()
