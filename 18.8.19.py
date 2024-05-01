ticket = int(input("Введите нужное количество билетов: "))
age_ = []

for i in range(1, ticket + 1):
    input_value = int(input(f'Введите возраст посетителя № {i}:'))
    age_.append(input_value)


def price_ticket(age):
    if age < 18:
        return 0
    elif 18 <= age < 25:
        return 990
    elif age >= 25:
        return 1360


total_sum = sum(map(price_ticket, age_))
discount = int(total_sum * 0.1)
discount_prise = (total_sum - discount)
if ticket > 3:
    print("Общая стоимость билетов:", total_sum, "руб.")
    print("Сумма скидки, при регистрации более 3 посетителей:", discount, "руб.")
    print("Общая стоймость билетов со скидкой:", discount_prise, "руб.")
else:
    print("Общая стоимость билетов:", total_sum, "руб.")
