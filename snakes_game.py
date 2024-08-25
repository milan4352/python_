import random
import curses

stdscr = curses.initscr()
curses.curs_set(0)  
sh, sw = stdscr.getmaxyx()  
w = curses.newwin(sh, sw, 0, 0)  
w.keypad(1)  
w.timeout(100)  

snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

food = [sh // 2, sw // 2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT
score = 0

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if (
        new_head[0] in [0, sh] or
        new_head[1] in [0, sw] or
        new_head in snake
    ):
        curses.endwin()
        quit()

    snake.insert(0, new_head)

    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
