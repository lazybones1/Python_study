import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx();
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

pacman = [[sh/2, sw/4]]

for i in range(1, sw-1):
  for j in range(1, sh):
    w.addch(int(j), int(i), curses.ACS_PI)

key = curses.KEY_RIGHT
pac_man_shape = '⊂'

while True:
  next_key = w.getch()
  key = key if next_key == -1 else next_key

  if pacman in [0, sh] or pacman in [0, sw]:
    curses.endwin()
    quit()

  pacmanMove = [pacman[0][0], pacman[0][1]]

  if key == curses.KEY_DOWN:
    pacmanMove[0] += 1
    pac_man_shape = '∩'
  if key == curses.KEY_UP:
    pacmanMove[0] -= 1
    pac_man_shape = '∪'
  if key == curses.KEY_LEFT:
    pacmanMove[1] -= 1
    pac_man_shape = '⊃'
  if key == curses.KEY_RIGHT:
    pacmanMove[1] += 1
    pac_man_shape = '⊂'

  pacman.insert(0, pacmanMove)

  removes = pacman.pop()
  w.addch(int(removes[0]), int(removes[1]), ' ')

  w.addch(int(pacman[0][0]), int(pacman[0][1]), pac_man_shape)
