#สร้างฟังก์ชันนับปลา
def get_fish_money(fish_count):
    return fish_count * 20

total_fish = 0
#สร้างวนลูปเพื่อให้มันวนถาม4รอบ
for day in range(1, 5):
    to_day = int(input(f"Day {day} How many fish did you catch?:"))
    total_fish += to_day 
    
    #เอาตัวเเปลtotal_fish มาบวกกับตัวเเปร to_day เพื่อให้ลูปนับคะเเนนทั้ง4รอบ
    print(f"You caught {to_day} fish")
total_money = get_fish_money(total_fish)
print("-------------------------------")
print(f"total fish caught: {total_fish}") #เเสดงผลรวมปลา
print(f"You get money: {total_money}$") #เเสดงผลรวมเงินที่ได้รับ

#สร้างเงื่อนไขว่าถ้าเราได้ผลรวมปลาเท่าไรคุณจะได้เป็นอะไร เพื่อเพิ่มความสนุกของเกมนี้โดยใช้ if, elif, else
if total_fish >= 100:
    print("You is the emperor of the sea congratulations")
elif total_fish >= 50:
    print("You are the king")
else:
    print("You're Fish")
