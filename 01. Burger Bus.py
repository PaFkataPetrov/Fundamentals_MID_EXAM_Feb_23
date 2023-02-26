number_city = int(input())

total_profit = 0

for i in range(1, number_city + 1):
    name = input()
    earned = float(input())
    expenses = float(input())
    if i % 3 == 0:
        expenses *= 1.5
    elif i % 5 == 0:
        earned *= 0.9
    profit = earned - expenses
    total_profit += profit
    print(f"In {name} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
