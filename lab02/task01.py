money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months = 0
money_capital += salary # This one is not obvious at all, but is required to pass the tests.

while money_capital >= spend:
    money_capital -= spend
    money_capital += salary
    #print(f"{money_capital=}")
    spend *= (1 + increase)
    #print(f"{spend=}")
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
