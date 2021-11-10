# 2

# 3. написать программу "Личный счет"
# Описание работы программы:
# Пользователь запускает программу у него на счету 0 руб
# Программа предлагает следующие варианты действий (основное меню):
# - пополнить счет (при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет,
# /после того как пользователь вводит сумму она добавляется к счету, снова попадаем в основное меню)
# - совершить покупку (при выборе этого пункта пользователю предлагается ввести сумму покупки,
# /если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню,
# /если денег достаточно предлагаем пользователю ввести название покупки, например (еда), снимаем деньги со счета,
# /сохраняем покупку в историю, выходим в основное меню)
# - история покупок (выводим историю покупок пользователя (название и сумму),возвращаемся в основное меню)
# - выход (завершение цикла, выход из меню)

import json
class User:
    def __init__(self,balance,history):
        self.balance = balance
        self.history = history

def proga(some_user='new'):
    if some_user == 'new':
        user = User(0,{})
        history = {}
    else:
        user = some_user
        history = user.history

    StartPage = True
    while StartPage:
        step1 = input('Запустить программу? Для запуска ответьте "да" (без кавычек, пробелов) ')
        if step1 == 'да':
            StartPage = False
            continue
        else:
            print('Возврат на начальную страницу')
    exit_proga = False
    while not exit_proga:
        action = input(f'Ваш баланс равен {user.balance},выберите действие: пополнить баланс/совершить покупку/выйти/история покупок) ')
        if action == 'выйти':
            exit_proga = True
        elif action == 'пополнить баланс':
            add_sum = input('Введите сумму пополнения баланса: ')
            try:
                user.balance = int(user.balance) + int(add_sum)
            except:
                print('Баланс не был пополнен, в следующий раз введите число')
        elif action == 'совершить покупку':
            try:
                purchase_sum = int(input('Введите сумму покупки: '))
                if user.balance >= purchase_sum:
                    good_name = input('Введите название товара: ')
                    if good_name in history:
                        user.balance -= purchase_sum
                        history[good_name] = purchase_sum + int(history[good_name])
                    else:
                        user.balance -= purchase_sum
                        history[good_name] = purchase_sum
                    user.history = history
                else:
                    print(f'Вашего баланса ({user.balance}) недостаточно. Пополните баланс')
            except:
                print('Введённое значение не является числом, в следующий раз введите целое число')
        elif action == 'история покупок':
            print(history)
    return user


user = proga(some_user='new')
print(user.balance,user.history)

balance = user.balance
balance = {'balance':balance}
history = user.history

with open('balance.json','w') as f:
    json.dump(balance,f)
with open('history.json','w') as f:
    json.dump(history,f)

with open('balance.json') as f:
    balance = json.load(f)
with open('history.json') as f:
    history = json.load(f)

user.balance = balance['balance']
user.history = history

user = proga(some_user=user)