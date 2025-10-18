import os, time, math, random

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def explode_ship(width=120, height=50, fps=8, score: int = 0):
    delay = 1.0 / fps

    # ==== человек (шагает) ====
    man_stand = [
        "   @@@   ",
        "  @@@@@  ",
        "   @@@   ",
        "   ###   ",
        "   ###   ",
        "   ###   ",
        "  ## ##  ",
        " ##   ## ",
    ]
    man_step_left = [
        "   @@@   ",
        "  @@@@@  ",
        "   @@@   ",
        "   ###   ",
        "   ###   ",
        "   ###   ",
        "  ##     ",
        " ##   ## ",
    ]
    man_step_right = [
        "   @@@   ",
        "  @@@@@  ",
        "   @@@   ",
        "   ###   ",
        "   ###   ",
        "   ###   ",
        "     ##  ",
        " ##   ## ",
    ]

    # ==== бомба ====
    bomb = [
        "     .:########:.     ",
        "   .:############:.   ",
        "  .:##############:.  ",
        "  :################:  ",
        "  :## ATOMIC BOMB ##: ",
        "  :################:  ",
        "   :##############:   ",
        "    :############:    ",
        "     `:########:'     ",
        "        ||||||        ",
        "        ||||||        ",
    ]
    bx, by = 15, height//2 - len(bomb)//2  # слева

    # ==== СЦЕНА 1: человек идёт к бомбе ====
    steps = 14
    for step in range(steps):
        canvas = [[" " for _ in range(width)] for _ in range(height)]
        # бомба
        for sy, row in enumerate(bomb):
            for sx, ch in enumerate(row):
                if ch != " " and 0 <= bx+sx < width and 0 <= by+sy < height:
                    canvas[by+sy][bx+sx] = ch
        # человек
        mx = width//2 + (steps-step)*3
        my = height//2 - len(man_stand)//2
        man = man_stand if step % 3 == 2 else (man_step_left if step % 3 == 0 else man_step_right)
        for sy, row in enumerate(man):
            for sx, ch in enumerate(row):
                if ch != " " and 0 <= mx+sx < width and 0 <= my+sy < height:
                    canvas[my+sy][mx+sx] = ch
        clear()
        print("\n".join("".join(r) for r in canvas))
        time.sleep(delay)

    # ==== СЦЕНА 2: касание бомбы ====
    frames_touch = int(1.5 * fps)
    for f in range(frames_touch):
        canvas = [[" " for _ in range(width)] for _ in range(height)]
        # бомба
        for sy, row in enumerate(bomb):
            for sx, ch in enumerate(row):
                if ch != " " and 0 <= bx+sx < width and 0 <= by+sy < height:
                    if f == frames_touch-1 and sy == len(bomb)//2 and 6 <= sx <= 12:
                        canvas[by+sy][bx+sx] = "@"
                    else:
                        canvas[by+sy][bx+sx] = ch
        # человек у бомбы
        mx = bx+25
        my = height//2 - len(man_stand)//2
        for sy, row in enumerate(man_stand):
            for sx, ch in enumerate(row):
                if ch != " " and 0 <= mx+sx < width and 0 <= my+sy < height:
                    canvas[my+sy][mx+sx] = ch
        # рука
        if f == frames_touch-1:
            canvas[my+3][mx-1] = "-"
            canvas[my+3][mx-2] = "-"
            canvas[my+3][mx-3] = "@"
        clear()
        print("\n".join("".join(r) for r in canvas))
        time.sleep(delay)

    # ==== СЦЕНА 3: корабль летит (4 сек) ====
    ship = [
        "    /^\\    ",
        "   /###\\   ",
        "  |#####|  ",
        "   \\###/   ",
        "    \\_/    ",
    ]
    ship_w, ship_h = len(ship[0]), len(ship)
    stars = [(random.randint(0, width-1), random.randint(0, height-1), random.uniform(0.3, 1.2))
             for _ in range(900)]
    frames_flight = int(4 * fps)
    for f in range(frames_flight):
        canvas = [[" " for _ in range(width)] for _ in range(height)]
        # звёзды
        for (sx, sy, sp) in stars:
            y = int((sy + f * sp) % height)
            if 0 <= y < height and 0 <= sx < width:
                canvas[y][sx] = "*" if random.random() < 0.85 else "."
        # корабль
        cx, cy = width//2, height//2
        x0, y0 = cx - ship_w//2, cy - ship_h//2 - f//5
        for sy, row in enumerate(ship):
            for sx, ch in enumerate(row):
                if ch != " " and 0 <= x0+sx < width and 0 <= y0+sy < height:
                    canvas[y0+sy][x0+sx] = ch
        clear()
        print("\n".join("".join(r) for r in canvas))
        time.sleep(delay)

    # ==== СЦЕНА 4: взрыв (6 сек, финал со SCORE) ====
    cx, cy = width//2, height//2
    frames_explosion = int(6 * fps)
    for step in range(frames_explosion):
        canvas = [[" " for _ in range(width)] for _ in range(height)]
        radius = step * 2 + 3
        for y in range(height):
            for x in range(width):
                dx, dy = x - cx, y - cy
                dist = math.sqrt(dx*dx + dy*dy)
                if dist < radius and random.random() < 0.7:
                    canvas[y][x] = random.choice([".", ":", "-", "=", "+", "*", "#", "%", "@"])
        # яркое ядро
        if step < frames_explosion - fps*2:
            core = max(1, 8 - step//2)
            for yy in range(cy-core, cy+core+1):
                for xx in range(cx-core*2, cx+core*2+1):
                    if 0 <= xx < width and 0 <= yy < height:
                        canvas[yy][xx] = "@"
        else:
            # тёмный круг
            dark_radius = min(12, step - (frames_explosion - fps*2) + 3)
            for y in range(height):
                for x in range(width):
                    dx, dy = x - cx, y - cy
                    if math.sqrt(dx*dx + dy*dy) < dark_radius*2:
                        canvas[y][x] = " "
            # SCORE
            text = f"SCORE: {score}"
            tx = cx - len(text)//2
            ty = cy
            for i, ch in enumerate(text):
                if 0 <= tx+i < width and 0 <= ty < height:
                    canvas[ty][tx+i] = ch
        clear()
        print("\n".join("".join(r) for r in canvas))
        time.sleep(delay)

    print(f"💥 Корабль уничтожен! SCORE: {score}")








import os, time, random, math

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def meteorite_destruction(score=0, width=120, height=50, fps=8):
    delay = 1.0 / fps

    # ASCII корабль
    ship = [
        "    /^\\    ",
        "   /###\\   ",
        "  |#####|  ",
        "   \\###/   ",
        "    \\_/    ",
    ]
    ship_w, ship_h = len(ship[0]), len(ship)

    # звёзды
    stars = [(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(400)]

    # === СЦЕНА 1: корабль летит ===
    frames_flight = int(3 * fps)
    for f in range(frames_flight):
        canvas = [[" " for _ in range(width)] for _ in range(height)]

        # звёзды
        for (sx, sy) in stars:
            if 0 <= sy < height and 0 <= sx < width:
                canvas[(sy + f) % height][sx] = "*" if random.random() < 0.8 else "."

        # корабль по центру
        cx, cy = width//2, height//2
        x0, y0 = cx - ship_w//2, cy - ship_h//2
        for sy, row in enumerate(ship):
            for sx, ch in enumerate(row):
                if ch != " ":
                    canvas[y0+sy][x0+sx] = ch

        # метеорит начинает появляться справа
        if f >= frames_flight-6:
            mx = width - (f - (frames_flight-6))*6
            my = cy
            if 0 <= mx < width:
                canvas[my][mx] = "O"
                canvas[my+1][mx] = "O"

        clear()
        print("\n".join("".join(r) for r in canvas))
        time.sleep(delay)

    # === СЦЕНА 2: столкновение, осколки ===
    cx, cy = width//2, height//2
    fragments = []
    for _ in range(60):  # осколки корабля
        angle = random.uniform(0, 2*math.pi)
        speed = random.uniform(0.5, 2.5)
        fragments.append({
            "x": cx,
            "y": cy,
            "dx": math.cos(angle)*speed,
            "dy": math.sin(angle)*speed,
            "ch": random.choice(["#", "+", "%", "*"])
        })

    frames_fragments = int(5 * fps)
    for f in range(frames_fragments):
        canvas = [[" " for _ in range(width)] for _ in range(height)]

        # звёзды
        for (sx, sy) in stars:
            if 0 <= sy < height and 0 <= sx < width:
                canvas[sy][sx] = "*" if random.random() < 0.8 else "."

        # двигаем осколки
        for frag in fragments:
            frag["x"] += frag["dx"]
            frag["y"] += frag["dy"]
            x, y = int(frag["x"]), int(frag["y"])
            if 0 <= x < width and 0 <= y < height:
                canvas[y][x] = frag["ch"]

        clear()
        print("\n".join("".join(r) for r in canvas))
        time.sleep(delay)

    # === СЦЕНА 3: финал — чёрный круг и SCORE ===
    frames_end = int(3 * fps)
    for f in range(frames_end):
        canvas = [[" " for _ in range(width)] for _ in range(height)]
        radius = (f+1) * 3
        for y in range(height):
            for x in range(width):
                dx, dy = x - cx, y - cy
                if math.sqrt(dx*dx + dy*dy) < radius:
                    canvas[y][x] = " "
                else:
                    if random.random() < 0.02:
                        canvas[y][x] = "."
        text = f"SCORE: {score}"
        tx = cx - len(text)//2
        ty = cy
        for i, ch in enumerate(text):
            if 0 <= tx+i < width and 0 <= ty < height:
                canvas[ty][tx+i] = ch
        clear()
        print("\n".join("".join(r) for r in canvas))
        time.sleep(delay)

    print(f"☄️ Метеорит уничтожил корабль! SCORE: {score}")


if __name__ == "__main__":
    meteorite_destruction(score=456, width=120, height=50, fps=8)














def oxygen_box_scene(score=0, width=120, height=50, fps=8, duration=12):
    delay = 1.0 / fps
    frames = int(duration * fps)

    cx, cy = width//2, height//2

    for f in range(frames):
        canvas = [[" " for _ in range(width)] for _ in range(height)]

        # === Панель кислорода ===
        box = "[ OXYGEN ]"
        bx = cx - len(box)//2
        for i, ch in enumerate(box):
            canvas[cy][bx+i] = ch

        # === Индикатор запаса ===
        full_len = 30
        left = max(0, full_len - (f * full_len // frames))
        bar = "[" + "█"*left + " "*(full_len-left) + "]"
        bx = cx - len(bar)//2
        for i, ch in enumerate(bar):
            canvas[cy+2][bx+i] = ch

        # === Пузыри воздуха ===
        bubble_count = max(0, 15 - f//3)  # всё меньше пузырей
        for _ in range(bubble_count):
            bx = cx + random.randint(-10, 10)
            by = cy - random.randint(3, 15)
            if 0 <= bx < width and 0 <= by < height:
                canvas[by][bx] = random.choice(["o", "O", "0"])

        # === Конец: кислород кончился ===
        if f > frames - fps*3:
            msg1 = "OXYGEN LOST"
            msg2 = f"SCORE: {score}"
            x1 = cx - len(msg1)//2
            x2 = cx - len(msg2)//2
            for i, ch in enumerate(msg1):
                canvas[cy-6][x1+i] = ch if (f//2) % 2 == 0 else " "
            for i, ch in enumerate(msg2):
                canvas[cy-4][x2+i] = ch

        clear()
        print("\n".join("".join(r) for r in canvas))
        time.sleep(delay)

    print(f"💀 OXYGEN LOST — FINAL SCORE: {score}")
