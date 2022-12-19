tickets=int (input ("Введите желаемое количество билетов: "))
total_price = 0
for ticket_age in range (1, tickets+1):
        ticket_age=int (input (f"Введите возраст посетителя {ticket_age} :"))
        if ticket_age < 18:
            total_price += 0
        elif 18 <= ticket_age <25:
            total_price += 990
        elif ticket_age >=25:
            total_price += 1390

print(f"Стоимость билетов: {total_price} руб.")

if tickets >=3 :
    total_price=0.9*total_price
    print(f"Стоимость билетов с учетом скидки при покупке от 3 билетов: {total_price} руб.")