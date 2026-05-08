def get_fish_money(fish_count):
    return fish_count * 20

total_fish = 0

for day in range(1, 5):
    to_day = int(input(f"Day {day} How many fish did you catch?:"))
    total_fish += to_day
    print(f"You caught {to_day} fish")
total_money = get_fish_money(total_fish)
print("-------------------------------")
print(f"total fish caught: {total_fish}")
print(f"You get money: {total_money}$")

if total_fish >= 100:
    print("You is the imperor of the sea congratulations")
elif total_fish >= 50:
    print("You are the king")
else:
    print("You're still gay")