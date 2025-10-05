#..... waiting for something to happen?

import os , subprocess , random , sys , threading , time
os.system('cls' if os.name == 'nt' else 'clear')
warn = '''
This software does not work well on Windows 11 
(cls refresh rate is known as jumpdown & make dots blink)      '''
time.sleep(0.8)
print(warn)
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)
def press_f11(delay: float = 0.05):
    platform = sys.platform
    if platform.startswith("win"):
        import ctypes
        from ctypes import wintypes

        INPUT_KEYBOARD = 1
        KEYEVENTF_KEYUP = 0x0002
        VK_F11 = 0x7A
        class KEYBDINPUT(ctypes.Structure):
            _fields_ = [
                ("wVk", wintypes.WORD),
                ("wScan", wintypes.WORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
            ]
        class INPUT_union(ctypes.Union):
            _fields_ = [("ki", KEYBDINPUT)]
        class INPUT(ctypes.Structure):
            _fields_ = [("type", wintypes.DWORD),
                        ("union", INPUT_union)]
        SendInput = ctypes.windll.user32.SendInput
        ki = KEYBDINPUT(wVk=VK_F11, wScan=0, dwFlags=0, time=0, dwExtraInfo=None)
        inp = INPUT(type=INPUT_KEYBOARD, union=INPUT_union(ki=ki))
        SendInput(1, ctypes.byref(inp), ctypes.sizeof(inp))
        time.sleep(delay)
        ki_up = KEYBDINPUT(wVk=VK_F11, wScan=0, dwFlags=KEYEVENTF_KEYUP, time=0, dwExtraInfo=None)
        inp_up = INPUT(type=INPUT_KEYBOARD, union=INPUT_union(ki=ki_up))
        SendInput(1, ctypes.byref(inp_up), ctypes.sizeof(inp_up))
    elif platform == "darwin":
        apple_script = 'tell application "System Events" to keystroke "f" using {control down, command down}'
        subprocess.run(["osascript", "-e", apple_script], check=True)
    elif platform.startswith("linux"):
        try:
            subprocess.run(["xdotool", "key", "F11"], check=True)
        except FileNotFoundError:
            raise RuntimeError("xdotool not found. Install it via your package manager (e.g., apt, yum).")
    else:
        raise NotImplementedError(f"Platform '{platform}' not supported. by the way yo can go ahead.")
    print("done.")
    time.sleep(0.4)   
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
if os.name == "nt":
    import msvcrt
else:
    import termios
    import tty
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_key():
    if os.name == "nt":
        key = msvcrt.getch()
        if key == b'\xe0':
            key = msvcrt.getch()
            if key == b'H':
                return "UP"
            elif key == b'P':
                return "DOWN"
        elif key == b'\r':
            return "ENTER"
    else:
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

        if key == '\x1b[A':
            return "UP"
        elif key == '\x1b[B':
            return "DOWN"
        elif key == '\n':
            return "ENTER"
    return None
options = ["Windows", "Linux"]
current = 0
while True:
    clear()
    print("\n" * 5)
    for i, opt in enumerate(options):
        if i == current:
            print(f"\t\t\033[100m {opt} \033[0m")  # هایلایت خاکستری
        else:
            print(f"\t\t {opt}")
    key = get_key()
    if key == "UP":
        current = (current - 1) % len(options)
    elif key == "DOWN":
        current = (current + 1) % len(options)
    elif key == "ENTER":
        clear()
        if options[current] == "Linux":
            print("sucess!")
            time.sleep(1)
        elif options[current] == "Windows":
            print("success!")
            time.sleep(1)
            press_f11()
        break
def dess(duration=2.0, lines=8, speed=0.06):
    clear_screen()
    print("PYTHON BOOT / CHECKING ...\n")
    start = time.time()
    status_options = [
        "VERIFYING MODULE", "AUTH TOKEN", "IO CHECK", "MEMSCAN",
        "GRAPHICS", "INPUT", "SOUND", "LEVELS", "SPEED PROFILE",
        "USER PREFS", "DRIVER LOAD", "NET CHECK"
    ]
    while time.time() - start < duration:
        for _ in range(lines):
            hexcode = ''.join(random.choice('0123456789ABCDEF') for _ in range(12))
            status = random.choice(status_options)
            ok = random.choice(["OK", "OK", "OK", "ACCEPT", "PASS"])
            print(f"[{hexcode}] {status} ... {ok}")
            time.sleep(speed)
            if time.time() - start >= duration:
                break
        elapsed = time.time() - start
        pct = min(1.0, elapsed / duration)
        bar_len = 30
        filled = int(bar_len * pct)
        bar = '[' + '#' * filled + '-' * (bar_len - filled) + ']'
        print("\nProgress:", bar, f"{int(pct*100):3d}%")
        time.sleep(0.12)
        up_lines = lines + 3
        print('\033[F' * up_lines, end='')
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print("FINAL STATUS: ALL MODULES OK")
    time.sleep(0.6)
    clear_screen()
dess()
time.sleep(0.5)
print("no error reported.")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
mainmenu = '''
                                                     T E T R I S

                                                     1  =  Play
                                                     2  =  Credit
                                                     3  =  Options
                                                     4  =  Exit
'''

crt = '''
                                            ________________________________X
                                            |                               |
                                            |     creator = @old_murtara    |
                                            |          telegram             |
                                            |                               |
                                            |_______________________________|

                                                Press Enter to exit.
'''

fpsfast = 0.1
fpsfasttext = 'Fast'
fpsmid = 0.4
fpsmidtext = "Medium"
fpsslow = 1
fpsslowtext = "Slow"
supslowfps = 2
supslowfpstext = "Super Slow"
fpssec = fpsmid
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    clear_screen()
    print(mainmenu)

def show_credit():
    clear_screen()
    print(crt)
    input("|>  ")

def show_options():
    clear_screen()
    print(f'''
                                            Select FPS :

                                            1  =  {fpsfasttext} > 0.1 refresh rate
                                            2  =  {fpsmidtext}  > 0.4 refresh rate     (Default)
                                            3  =  {fpsslowtext} > 1.0 refresh rate
                                            4  =  {supslowfpstext} > 2.0 refresh rate

                                            ''')
def select_fps():
    global fpssec
    show_options()
    selectfps = input("|>  ").strip()
    if selectfps == '1':
        fpssec = fpsfast
        print("\nSelected Fast")
    elif selectfps == '2':
        fpssec = fpsmid
        print("\nSelected Medium")
    elif selectfps == '3':
        fpssec = fpsslow
        print("\nSelected Slow")
    elif selectfps == '4':
        fpssec = supslowfps
        print("\nSelected Super Slow")
    else:
        print("\nWrong input, FPS unchanged.")
    time.sleep(1)
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
        print(f'Score: {self.score}  |  FPS: {fpssec}')
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
def play_game():
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
            print("Space = rotate | Arrows = move | Q = quit")
        time.sleep(fpssec)
    print("Game Over! Final score:", game.score)
    while True:
        retry = input("Type '1' to play again or any other key to exit: ").strip().lower()
        if retry == "1":
            return True
        else:
            return False
def main():
    while True:
        show_main_menu()
        mainchoice = input("|>  ").strip()
        if mainchoice == '1':
            play_again = play_game()
            if not play_again:
                break
        elif mainchoice == '2':
            show_credit()
        elif mainchoice == '3':
            select_fps()
        elif mainchoice == '4':
            print("App closed.")
            sys.exit()
        else:
            print("Wrong input")
            time.sleep(1)
            continue
if __name__ == '__main__':
    main()
