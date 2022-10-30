money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = -1  # количество месяцев, которое можно прожит

while money_capital > 0:
    delta = salary-spend
    money_capital += delta
    month += 1
    spend *= (1+increase)

print(month)
