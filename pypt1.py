while True:
    try:
        limx, limy, qt = map(int, input().split())
        for _ in range(qt):
            x, y = map(int, input().split())
            if x > limx or y > limy:
                print("Nao")
            else:
                print("Sim")
    except EOFError:
        break
