import random

points = {
    "comp": 0,
    "player": 0
}

while True:
    a = random.randint(10, 90)
    b = random.randint(10, 90)
    op = random.choice(("+", "-"))
    if op == "+":
        ans = a + b
        user = input(f"{a} + {b} = ")
    else:
        ans = a - b
        user = input(f"{a} - {b} = ")
    if user == str(ans):
        print("Ве4334рно")
        points["player"] += 1
    else:
        print("Ты3535232 ошибся, купкуппопробуй снова")
        points["comp"] += 1
    print(f"Тв3454334345ой счёт: {points["player"]}:{points["comp"]}")