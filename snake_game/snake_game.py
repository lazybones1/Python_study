import random
import curses

s = curses.initscr()  #화면을 나타내는 창 객체 반환 (초기화)
curses.curs_set(0) #커서가 필요 없는 경우 curs_set(0), 필요한 경우 curs_set(1)
sh, sw = s.getmaxyx() #s창의 y,x,값을 반환(최대값을 가짐)
w = curses.newwin(sh, sw, 0, 0) #높이 sh, 너비 sw, 시작 y 0, 시작 x 0인 새로운 창 생성
w.keypad(1) #커서키, 탐색키 등 특수키 사용
w.timeout(100) #100마다 화면 새로고침

#snake 시작 위치 설정
snk_x = sw/4
snk_y = sh/2
snake = [
  [snk_y, snk_x], #snake몸통 머리
  [snk_y, snk_x-1], #snake 몸통
  [snk_y, snk_x-2]  #snake 꼬리
]

food = [sh/2, sw/2] #food 초기 위치
w.addch(int(food[0]), int(food[1]), curses.ACS_PI) #π를 food로 사용 입력

key = curses.KEY_RIGHT #초기 snake의 이동 : KET_RIGHT가 입력되었을 경우로 설정

while True:
  next_key = w.getch() #키 입력
  key = key if next_key == -1 else next_key

  #게임 종료 조건 : snake가 벽에 부딪치는 경우
  if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
    curses.endwin() #창 죽이기
    quit() #종료

  new_head = [snake[0][0], snake[0][1]] #새로운 뱀의 머리

    #입력받은 키에 따라 새로운 뱀머리 정함
  if key == curses.KEY_DOWN:
    new_head[0] += 1
  if key == curses.KEY_UP:
    new_head[0] -= 1
  if key == curses.KEY_LEFT:
    new_head[1] -= 1
  if key == curses.KEY_RIGHT:
    new_head[1] += 1

  snake.insert(0, new_head) #뱀배열에 0번 위치에 새로운 머리 삽입

  #뱀이 음식을 먹은 경우
  if snake[0] == food:
    food = None
    while food is None:
      #랜덤으로 food위치 설정
      nf = [
        random.randint(1, sh-1),
        random.randint(1, sw-1)
      ]
      food = nf if nf not in snake else None
      w.addch(food[0], food[1], curses.ACS_PI) #음식 추가
  else:
    #뱀의 꼬리부분 제거(공백으로 표시)
    tail = snake.pop()
    w.addch(int(tail[0]), int(tail[1]), ' ')

  w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD) #뱀 머리를 화면에 표시
