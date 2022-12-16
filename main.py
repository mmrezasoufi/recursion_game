# please install these libraries
import time
from tk import *
from colorama import Fore, Back, Style
import winsound

# sounds
heart = 'heartbeat.wav'
gameover = 'gameover.wav'
winn = 'win.wav'

# primary board
grid = [
    [9, 1, 2, 3, 9],
    [4, 0, 0, 0, 0],
    [5, 0, 0, 0, 0],
    [6, 0, 0, 0, 0],
    [9, 0, 0, 0, 9]
]

# publish our boardgame
def print_board(grid: list):
    grid_temp = [grid[0].copy(), grid[1].copy(), grid[2].copy(), grid[3].copy(), grid[4].copy()]
    for i in range(len(grid_temp)):
        for j in range(len(grid_temp[i])):
            if grid_temp[i][j] == 9:
                grid_temp[i][j] = "!◙!"
            if grid_temp[i][j] == 1 or grid_temp[i][j] == 2 or grid_temp[i][j] == 3:
                grid_temp[i][j] = " ▼ "
            if grid_temp[i][j] == 4 or grid_temp[i][j] == 5 or grid_temp[i][j] == 6:
                grid_temp[i][j] = " ► "
            if grid_temp[i][j] == 0:
                grid_temp[i][j] = "..."
    Style.BRIGHT
    for i in grid_temp:
        print(Fore.LIGHTGREEN_EX, *i, sep=" ")
    print()

# return our beads coordinates
def position(grid: list, num: int):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == num:
                x = i
                y = j
                break
    return x, y

# check win
def win(grid: list, player: str) -> bool:
    if (grid[1][-1] != 0 and grid[2][-1] != 0 and grid[3][-1] != 0) and player == 'player2':
        return True
    if (grid[-1][1] != 0 and grid[-1][2] != 0 and grid[-1][3] != 0) and player == 'player1':
        return True
    return False

# check lock : when three beads can't move
def lock(grid: list, player: str) -> bool:
    count1 = 0
    if player == 'player1':
        for i in range(1, 4):
            if not valid_move(grid, i, 'player1'):
                count1 += 1
        if count1 == 3:
            return True
        return False

    count2 = 0
    if player == 'player2':
        for i in range(4, 7):
            if not valid_move(grid, i, 'player2'):
                count2 += 1
        if count2 == 3:
            return True
        return False

# to check how beads are moved
def valid_move(grid: list, num: int, player: str) -> bool:
    if player == "player1":
        x, y = position(grid, num)
        if x > 3:
            return 0
        if grid[x + 1][y] != 0 and grid[x + 2][y] != 0:
            return 0
        if grid[x + 1][y] != 0:
            return 2
        return 1

    if player == "player2":
        x, y = position(grid, num)
        if y > 3:
            return 0
        if grid[x][y + 1] != 0 and grid[x][y + 2] != 0:
            return 0
        if grid[x][y + 1] != 0:
            return 2
        return 1

# a function to move a bead of player1
def move_player1(grid: list, num: int) -> list:
    n = valid_move(grid, num, 'player1')
    x, y = position(grid, num)
    grid[x + n][y] = num
    grid[x][y] = 0
    return grid
# a function to move a bead of player2
def move_player2(grid: list, num: int) -> list:
    m = valid_move(grid, num, 'player2')
    x, y = position(grid, num)
    grid[x][y + m] = num
    grid[x][y] = 0
    return grid

#best moves for player2 which leads to victory
def evaluation(grid: list, player:str) -> bool:
    if player == 'player2':
        opponent = 'player1'
    else:
        opponent = 'player2'

    # base case
    if win(grid, player):
        return True
    if win(grid, opponent):
        return False

    #check lock
    if lock(grid, player):
        return not evaluation(grid, opponent)

    # Backtrack(recursion)
    if player == 'player2':
        for i in range(4, 7):
            if valid_move(grid, i, player):
                grid_temp = [grid[0].copy(), grid[1].copy(), grid[2].copy(), grid[3].copy(), grid[4].copy()]
                move_player2(grid_temp, i)
                if not evaluation(grid_temp, opponent):
                    return True
        return False
    if player == 'player1':
        for i in range(1, 4):
            if valid_move(grid, i, player):
                grid_temp = [grid[0].copy(), grid[1].copy(), grid[2].copy(), grid[3].copy(), grid[4].copy()]
                move_player1(grid_temp, i)
                if not evaluation(grid_temp, opponent):
                    return True
        return False

# Check out each of the ways to achieve victory using the evaluation function
def moves(grid : list, player : str) -> int:
    for i in range(4, 7):
        if valid_move(grid, i, player):
            grid_temp = [grid[0].copy(), grid[1].copy(), grid[2].copy(), grid[3].copy(), grid[4].copy()]
            move_player2(grid_temp, i)
            if not evaluation(grid_temp, 'player1'):
                return i
    for i in range(4, 7):
        if valid_move(grid, i, 'player2'):
            return i


print(Fore.LIGHTMAGENTA_EX, '--------------> Hello , Welcome to the Game <----------------')
print()
def game(grid: list):
    from tk import turn
    print_board(grid)
    while not win(grid, 'player1') and not win(grid, 'player2'): # loop game until one player wins
        Style.RESET_ALL
        if turn == 1:
            if not lock(grid, 'player1'):
                print('Your turn ...')
                while True: # check correct value of the input
                    num = int(input())
                    if 0 < int(num) < 4 and valid_move(grid, num, 'player1') != 0: # checks the input is correct or not
                        break
                    print('please choose another bead ☻ - [1,3]')
                if valid_move(grid, num, 'player1'):
                    move_player1(grid, num)
            if win(grid, 'player1'): # check win : if player1 wins, game will end
                print_board(grid)
                print(Fore.BLUE, '¯\_( ͡° ͜ʖ ͡°)_/¯    you win ...   ¯\_( ͡° ͜ʖ ͡°)_/¯')
                winsound.PlaySound(winn, winsound.SND_FILENAME)
                break
            turn = 2

        print_board(grid)
        if turn == 2:
            if not lock(grid, 'player2'):
                t = time.time()
                print('Oponent is thinking !')
                num = moves(grid, 'player2')
                while True: # fun : time which opponent takes to think
                    if time.time() - t > 2:
                        winsound.PlaySound(heart, winsound.SND_FILENAME)
                        print(num)
                        break
                if valid_move(grid, num, 'player2'):
                    move_player2(grid, num)
                    print_board(grid)
            if win(grid, 'player2'):# check win : if player2 wins, game will end
                print_board(grid)
                print(Fore.RED, 'O_O ... You lost ... O_O')
                winsound.PlaySound(gameover, winsound.SND_FILENAME)
            turn = 1

game(grid)
