import os
import random
import sys
import threading
import time
mainmenu = '''







                                                    1  =  play
                                                    2  =  credit
                                                    3  =  exit'''




crt = '''






                                            ________________________________X
                                            |                               |
                                            |     creator = @old_murtara    |
                                            |          telegram             |
                                            |                               |
                                            |_______________________________|

                                                press Enter for exit.
'''
print("starting...")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(mainmenu)
    print()
    mainchoise = input("|>  ")
    if mainchoise == '1':
        break
    elif mainchoise == '2':
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(crt)
        exitmen = input("|>  ")
        if exitmen == 'snake':
            print
        else:
            continue
    elif mainchoise == '3':
        exit("app closed")
    else:
        print("wrong input")
        time.sleep(1)
        continue

WIDTH, HEIGHT = 10, 20
EMPTY = ' .'
BLOCK = '[]'

SHAPES = {
    'I': [
        [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
        [[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]]
    ],
    'O': [
        [[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]]
    ],
    'T': [
        [[0,1,0,0],[1,1,1,0],[0,0,0,0],[0,0,0,0]],
        [[0,1,0,0],[0,1,1,0],[0,1,0,0],[0,0,0,0]],
        [[0,0,0,0],[1,1,1,0],[0,1,0,0],[0,0,0,0]],
        [[0,1,0,0],[1,1,0,0],[0,1,0,0],[0,0,0,0]]
    ],
    'L': [
        [[0,0,1,0],[1,1,1,0],[0,0,0,0],[0,0,0,0]],
        [[0,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,0,0]],
        [[0,0,0,0],[1,1,1,0],[1,0,0,0],[0,0,0,0]],
        [[1,1,0,0],[0,1,0,0],[0,1,0,0],[0,0,0,0]]
    ],
    'J': [
        [[1,0,0,0],[1,1,1,0],[0,0,0,0],[0,0,0,0]],
        [[0,1,1,0],[0,1,0,0],[0,1,0,0],[0,0,0,0]],
        [[0,0,0,0],[1,1,1,0],[0,0,1,0],[0,0,0,0]],
        [[0,1,0,0],[0,1,0,0],[1,1,0,0],[0,0,0,0]]
    ],
    'S': [
        [[0,1,1,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]],
        [[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,0]]
    ],
    'Z': [
        [[1,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]],
        [[0,0,1,0],[0,1,1,0],[0,1,0,0],[0,0,0,0]]
    ]
}

class Tetris:
    def __init__(self):
        self.board = [[0]*WIDTH for _ in range(HEIGHT)]
        self.score = 0
        self.gameover = False
        self.lock = threading.Lock()
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.current_rotation = 0
        self.spawn_piece()
    def spawn_piece(self):
        self.current_piece = random.choice(list(SHAPES.keys()))
        self.current_rotation = 0
        self.current_x = WIDTH // 2 - 2
        self.current_y = 0
        if not self.valid_position(self.current_x, self.current_y, self.current_rotation):
            self.gameover = True
    def rotate(self):
        new_rotation = (self.current_rotation + 1) % len(SHAPES[self.current_piece])
        if self.valid_position(self.current_x, self.current_y, new_rotation):
            self.current_rotation = new_rotation
    def valid_position(self, x, y, rotation):
        shape = SHAPES[self.current_piece][rotation]
        for row in range(4):
            for col in range(4):
                if shape[row][col]:
                    board_x = x + col
                    board_y = y + row
                    if board_x < 0 or board_x >= WIDTH or board_y < 0 or board_y >= HEIGHT:
                        return False
                    if self.board[board_y][board_x]:
                        return False
        return True
    def place_piece(self):
        shape = SHAPES[self.current_piece][self.current_rotation]
        for row in range(4):
            for col in range(4):
                if shape[row][col]:
                    self.board[self.current_y + row][self.current_x + col] = 1
        self.clear_lines()
        self.spawn_piece()
    def clear_lines(self):
        new_board = []
        lines_cleared = 0
        for row in self.board:
            if all(row):
                lines_cleared += 1
            else:
                new_board.append(row)
        for _ in range(lines_cleared):
            new_board.insert(0, [0]*WIDTH)
        self.board = new_board
        self.score += lines_cleared ** 2
    def move(self, dx):
        if self.valid_position(self.current_x + dx, self.current_y, self.current_rotation):
            self.current_x += dx
    def drop(self):
        if self.valid_position(self.current_x, self.current_y + 1, self.current_rotation):
            self.current_y += 1
        else:
            self.place_piece()
    def print_board(self):
        print('\033[2J\033[H', end='')  
        print(f'Score: {self.score}  | 1FPS')
        print("")
        board_copy = [row[:] for row in self.board]
        shape = SHAPES[self.current_piece][self.current_rotation]
        for row in range(4):
            for col in range(4):
                if shape[row][col]:
                    x = self.current_x + col
                    y = self.current_y + row
                    if 0 <= y < HEIGHT and 0 <= x < WIDTH:
                        board_copy[y][x] = 1
        lines = [''.join(BLOCK if cell else EMPTY for cell in row) for row in board_copy]
        print('\n'.join(lines))
    def input_thread_windows(self):
        import msvcrt
        while not self.gameover:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                with self.lock:
                    if key == b'\xe0':
                        key2 = msvcrt.getch()
                        if key2 == b'K': 
                            self.move(-1)
                        elif key2 == b'M':
                            self.move(1)
                        elif key2 == b'S':
                            self.drop()
                    elif key == b' ':
                        self.rotate()
                    elif key == b'q':
                        self.gameover = True
    def input_thread_unix(self):
        import sys
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setcbreak(fd)
        try:
            while not self.gameover:
                key = sys.stdin.read(1)
                with self.lock:
                    if key == '\x1b':
                        key2 = sys.stdin.read(1)
                        if key2 == '[':
                            key3 = sys.stdin.read(1)
                            if key3 == 'D':
                                self.move(-1)
                            elif key3 == 'C':
                                self.move(1)
                            elif key3 == 'B':
                                self.drop()
                    elif key == ' ':
                        self.rotate()
                    elif key == 'q':
                        self.gameover = True
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
def main():
    game = Tetris()
    if os.name == 'nt':
        input_t = threading.Thread(target=game.input_thread_windows, daemon=True)
    else:
        input_t = threading.Thread(target=game.input_thread_unix, daemon=True)
    input_t.start()
    while not game.gameover:
        with game.lock:
            game.drop()
            game.print_board()
            print()
            print("space = rotate")
            print("arrows = move")
        time.sleep(0.4)
    print("Game Over! Final score:", game.score)
    exitmmm = input()
    if exitmmm == "retry":
        exit()
    else:
        exit()
if __name__ == '__main__':
    main()
