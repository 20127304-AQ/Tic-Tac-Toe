import pygame
import time
import datetime

# Choice of map
print("1. 3x3")
print("2. 5x5")
print("Enter your choice: ")
choice = int(input())

while(choice != 1 and choice != 2):
    print("Please input again: ")
    choice = int(input())

# Initializes pygame
pygame.init()

# Constant
if(choice == 1):
    WIDTH = 720
    HEIGHT = 720
    LINE_WIDTH = 10
    WIN_LINE_WIDTH = 10
    BOARD_ROWS = 3
    BOARD_COLS = 3
    SQUARE_SIZE = 240
    CIRCLE_RADIUS = 65
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 25
    SPACE = 55
    RED = (255, 0, 0)
    BG_COLOR = (224, 238, 238)
    LINE_COLOR = (131, 139, 139)
    CIRCLE_COLOR = (102, 205, 170)
    CROSS_COLOR = (255, 69, 0)
elif(choice == 2):
    WIDTH = 720
    HEIGHT = 720
    LINE_WIDTH = 10
    WIN_LINE_WIDTH = 10
    BOARD_ROWS = 5
    BOARD_COLS = 5
    SQUARE_SIZE = 144
    CIRCLE_RADIUS = 45
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 25
    SPACE = 45
    RED = (255, 0, 0)
    BG_COLOR = (224, 238, 238)
    LINE_COLOR = (131, 139, 139)
    CIRCLE_COLOR = (102, 205, 170)
    CROSS_COLOR = (255, 69, 0)

# Limit the search time of IDS
SEARCH_TIME = 20

# IDS variable best move and oppposit move at current state
BESTMOVE = [0, 0]
OPPOSITMOVE = [0, 0]
global time_check 

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
if choice == 1: pygame.display.set_caption('TIC TAC TOE 3x3')
if choice == 2: pygame.display.set_caption('TIC TAC TOE 5x5')
screen.fill(BG_COLOR)

# Initialize board
board = [[0 for i in range(BOARD_COLS)] for j in range(BOARD_ROWS)]

# variables
player = 1
game_over = False

# Function
# UI
def draw_lines(choice):
    if(choice == 1):
        # 1 horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        # 2 horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

        # 1 vertical
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        # 2 vertical
        pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    elif(choice == 2):
        # 1 horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        # 2 horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
        # 3 horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, 3 * SQUARE_SIZE), (WIDTH, 3 * SQUARE_SIZE), LINE_WIDTH)
        # 4 horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, 4 * SQUARE_SIZE), (WIDTH, 4 * SQUARE_SIZE), LINE_WIDTH)
        # 5 horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, 5 * SQUARE_SIZE), (WIDTH, 5 * SQUARE_SIZE), LINE_WIDTH)

        # 1 vertical
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        # 2 vertical
        pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        # 3 vertical
        pygame.draw.line(screen, LINE_COLOR, (3 * SQUARE_SIZE, 0), (3 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        # 4 vertical
        pygame.draw.line(screen, LINE_COLOR, (4 * SQUARE_SIZE, 0), (4 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        # 5 vertical
        pygame.draw.line(screen, LINE_COLOR, (5 * SQUARE_SIZE, 0), (5 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_XO():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + int(SQUARE_SIZE/2)), int(row * SQUARE_SIZE + int(SQUARE_SIZE/2))), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

# Set current square by current player
def set_square(row, col, player):
    board[row][col] = player

# Check if the current cell is available or not
def avai_square(row, col):
    return board[row][col] == 0

# Check if the board is full or not
def is_full(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

# Check all the board if human or computer win or not
def is_end(choice):
    # Vertical
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS):
            count = 0
            if(choice == 1):
                if board[row][col] == 1:
                    for temp_row in range(row, BOARD_ROWS):
                        if board[temp_row][col] == 1:
                            count+= 1
                        else: break
                        if count == 3:
                            return board[temp_row][col]
                if board[row][col] == 2:
                    for temp_row in range(row, BOARD_ROWS):
                        if board[temp_row][col] == 2:
                            count+= 1
                        else: break
                        if count == 3:
                            return board[temp_row][col]
                    
            if(choice == 2):
                if board[row][col] == 1:
                    for temp_row in range(row, BOARD_ROWS):
                        if board[temp_row][col] == 1:
                            count+= 1
                        else: break
                        if count == 4:
                            return board[temp_row][col]
                if board[row][col] == 2:
                    for temp_row in range(row, BOARD_ROWS):
                        if board[temp_row][col] == 2:
                            count+= 1
                        else: break
                        if count == 4:
                            return board[temp_row][col]
    # Horizontal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            count = 0
            if(choice == 1):
                if board[row][col] == 1:
                    for temp_c in range(col, BOARD_COLS):
                        if board[row][temp_c] == 1:
                            count += 1
                        else: break
                        if count == 3:
                            return board[row][temp_c]
                if board[row][col] == 2:
                    for temp_c in range(col, BOARD_COLS):
                        if board[row][temp_c] == 2:
                            count += 1
                        else: break
                        if count == 3:
                            return board[row][temp_c]
                    
            if(choice == 2):
                if board[row][col] == 1:
                    for temp_c in range(col, BOARD_COLS):
                        if board[row][temp_c] == 1:
                            count += 1
                        else: break
                        if count == 4:
                            return board[row][temp_c]
                if board[row][col] == 2:
                    for temp_c in range(col, BOARD_COLS):
                        if board[row][temp_c] == 2:
                            count += 1
                        else: break
                        if count == 4:
                            return board[row][temp_c]
    # Desc diagonal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            count = 0
            if(choice == 1):
                temp_r = row
                temp_c = col
                if(board[row][col] == 1):
                    while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS):
                        if(board[temp_r][temp_c] == 1):
                            count += 1
                        else: break
                        if(count == 3):
                            return board[temp_r][temp_c]
                        temp_r += 1
                        temp_c += 1
                if(board[row][col] == 2):
                    while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS):
                        if(board[temp_r][temp_c] == 2):
                            count += 1
                        else: break
                        if(count == 3):
                            return board[temp_r][temp_c]
                        temp_r += 1
                        temp_c += 1
            if(choice == 2):
                temp_r = row
                temp_c = col
                if(board[row][col] == 1):
                    while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS):
                        if(board[temp_r][temp_c] == 1):
                            count += 1
                        else: break
                        if(count == 4):
                            return board[temp_r][temp_c]
                        temp_r += 1
                        temp_c += 1
                if(board[row][col] == 2):
                    while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS):
                        if(board[temp_r][temp_c] == 2):
                            count += 1
                        else: break
                        if(count == 4):
                            return board[temp_r][temp_c]
                        temp_r += 1
                        temp_c += 1
    # Asc diagonal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            count = 0
            if(choice == 1):
                temp_r = row
                temp_c = col
                if(board[row][col] == 1):
                    while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS and temp_c >= 0):
                        if(board[temp_r][temp_c] == 1):
                            count += 1
                        else:
                            break
                        if(count == 3):
                            return board[temp_r][temp_c]
                        temp_r += 1
                        temp_c -= 1
                if(board[row][col] == 2):
                    while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS and temp_c >= 0):
                        if(board[temp_r][temp_c] == 2):
                            count += 1
                        else:
                            break
                        if(count == 3):
                            return board[temp_r][temp_c]
                        temp_r += 1
                        temp_c -= 1
            if(choice == 2):
                temp_r = row
                temp_c = col
                if(board[row][col] == 1):
                    while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS and temp_c >= 0):
                        if(board[temp_r][temp_c] == 1):
                            count += 1
                        else:
                            break
                        if(count == 4):
                            return board[temp_r][temp_c]
                        temp_r += 1
                        temp_c -= 1
                if(board[row][col] == 2):
                    while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS and temp_c >= 0):
                        if(board[temp_r][temp_c] == 2):
                            count += 1
                        else:
                            break
                        if(count == 4):
                            return board[temp_r][temp_c]
                        temp_r += 1
                        temp_c -= 1
    if(is_full(board) == False):
        return None
    return 0

# Check if current 
def check_win(player, choice):
    # Vertical
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS):
            count = 0
            if(choice == 1):
                for temp_r in range(row, BOARD_ROWS):
                    if(board[temp_r][col] == player):
                        count += 1
                    else:
                        break
                    if(count == 3):
                        draw_vertical_winning_line(temp_r + 1, temp_r - 3, col, player)
                        return True
            if(choice == 2):
                for temp_r in range(row, BOARD_ROWS):
                    if(board[temp_r][col] == player):
                        count += 1
                    else:
                        break
                    if(count == 4):
                        draw_vertical_winning_line(temp_r, temp_r - 3, col, player)
                        return True
    # Horizontal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            count = 0
            if(choice == 1):
                for temp_c in range(col, BOARD_COLS):
                    if(board[row][temp_c] == player):
                        count += 1
                    else:
                        break
                    if(count == 3):
                        draw_horizontal_winning_line(temp_c + 1, temp_c - 3, row, player)
                        return True
            if(choice == 2):
                for temp_c in range(col, BOARD_COLS):
                    if(board[row][temp_c] == player):
                        count += 1
                    else:
                        break
                    if(count == 4):
                        draw_horizontal_winning_line(temp_c, temp_c - 3, row, player)
                        return True
    # Desc diagonal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            count = 0
            if(choice == 1):
                temp_r = row
                temp_c = col
                while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS):
                    if(board[temp_r][temp_c] == player):
                        count += 1
                    else:
                        break
                    if(count == 3):
                        draw_desc_diagonal(temp_c - 2, temp_r - 2, temp_c, temp_r, player)
                        return True
                    temp_r += 1
                    temp_c += 1
            if(choice == 2):
                temp_r = row
                temp_c = col
                while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS):
                    if(board[temp_r][temp_c] == player):
                        count += 1
                    else:
                        break
                    if(count == 4):
                        draw_desc_diagonal(temp_c - 3, temp_r - 3, temp_c, temp_r, player)
                        return True
                    temp_r += 1
                    temp_c += 1
    # Asc diagonal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            count = 0
            if(choice == 1):
                temp_r = row
                temp_c = col
                while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS and temp_c >= 0):
                    if(board[temp_r][temp_c] == player):
                        count += 1
                    else:
                        break
                    if(count == 3):
                        draw_asc_diagonal(temp_c, temp_r, temp_c + 2, temp_r - 2, player)
                        return True
                    temp_r += 1
                    temp_c -= 1
            if(choice == 2):
                temp_r = row
                temp_c = col
                while(temp_r < BOARD_ROWS and temp_c < BOARD_COLS and temp_c >= 0):
                    if(board[temp_r][temp_c] == player):
                        count += 1
                    else:
                        break
                    if(count == 4):
                        draw_asc_diagonal(temp_c, temp_r, temp_c + 3, temp_r - 3, player)
                        return True
                    temp_r += 1
                    temp_c -= 1

# UI CARO
def draw_vertical_winning_line(start, end, col, player):
    posX = col * SQUARE_SIZE + int(SQUARE_SIZE/2)
    pos_startY = start * SQUARE_SIZE + int(SQUARE_SIZE/2)
    pos_endY = end * SQUARE_SIZE + int(SQUARE_SIZE/2)

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, pos_startY), (posX, pos_endY), LINE_WIDTH)

def draw_horizontal_winning_line(start, end, row, player):
    posY = row * SQUARE_SIZE + int(SQUARE_SIZE/2)
    pos_startX = start * SQUARE_SIZE + int(SQUARE_SIZE/2)
    pos_endX = end * SQUARE_SIZE + int(SQUARE_SIZE/2)

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (pos_startX, posY), (pos_endX, posY), WIN_LINE_WIDTH)

def draw_asc_diagonal(startX, startY, endX, endY, player):
    pos_startX = startX * SQUARE_SIZE + int(SQUARE_SIZE/2)
    pos_endX = endX * SQUARE_SIZE + int(SQUARE_SIZE/2)
    pos_startY = startY * SQUARE_SIZE + int(SQUARE_SIZE/2)
    pos_endY = endY * SQUARE_SIZE + int(SQUARE_SIZE/2)

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (pos_startX, pos_startY), (pos_endX, pos_endY), WIN_LINE_WIDTH)

def draw_desc_diagonal(startX, startY, endX, endY, player):
    pos_startX = startX * SQUARE_SIZE + int(SQUARE_SIZE/2)
    pos_endX = endX * SQUARE_SIZE + int(SQUARE_SIZE/2)
    pos_startY = startY * SQUARE_SIZE + int(SQUARE_SIZE/2)
    pos_endY = endY * SQUARE_SIZE + int(SQUARE_SIZE/2)

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (pos_startX, pos_startY), (pos_endX, pos_endY), WIN_LINE_WIDTH)

# Restart the game after ending
def restart():
    screen.fill(BG_COLOR)
    draw_lines(choice)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

# Rotate current player
def change_Player(player):
    if(player == 1):
        return 2
    if(player == 2):
        return 1

# 3x3
# Minimax alpha-beta pruning
def max_alphabeta(alpha, beta):
    max = -5

    px = None
    py = None

    result = is_end(choice)
    if result == 1:
        return (-1, 0, 0)
    elif result == 2:
        return (1, 0, 0)
    elif result == 0:
        return (0, 0, 0)

    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] == 0:
                board[i][j] = 2
                (m, min_i, min_j) = min_alphabeta(alpha, beta)
                if(m > max):
                    max = m
                    px = i
                    py = j

                board[i][j] = 0

                if max >= beta:
                    return (max, px, py)

                if max > alpha:
                    alpha = max
    return (max, px, py)

def min_alphabeta(alpha, beta):
    min = 5

    qx = None
    qy = None

    result = is_end(choice)

    if result == 1:
        return (-1, 0, 0)
    elif result == 2:
        return (1, 0, 0)
    elif result == 0:
        return (0, 0, 0)

    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] == 0:
                board[i][j] = 1
                (m, max_i, max_j) = max_alphabeta(alpha, beta)
                if m < min:
                    min = m
                    qx = i
                    qy = j

                board[i][j] = 0

                if min <= alpha:
                    return (min, qx, qy)

                if min < beta:
                    beta = min
    return (min, qx, qy)

# 5x5
# Calculate number of X and O in the line
def calculateXO(line):
    TotalX = 0
    TotalO = 0
    TotalEmpty = 0
    for i in range(len(line)):
        if line[i] == 1: TotalO += 1
        if line[i] == 2: TotalX += 1
        if line[i] == 0: TotalEmpty += 1
    return TotalO, TotalX, TotalEmpty

# Calculate the score of current line
def scoreLine(line):
    score = 0
    totalO, totalX, totalEmpty = calculateXO(line)
    if totalO == 0 and totalX != 0:
        score += pow(10, (totalX - 1))
    if totalX == 0 and totalO != 0:
        score -= pow(10, (totalO - 1))
    return score

# Find all empty cells in the board      
def possible_move():
    res = []
    for i in range (BOARD_ROWS):
        for j in range (BOARD_COLS):
            if board[i][j] == 0:
                res.append([i,j])
    return res

# Get 4 elements in the row of the board
def getRow(number):
    res1 = []
    res2 = []
    for i in range(BOARD_COLS - 1):
        res1.append(board[number][i])
    for i in range(1, BOARD_COLS):
        res2.append(board[number][i])
    return res1, res2

# Get 4 elements in the col of the board
def getCol(number):
    res1 = []
    res2 = []
    for i in range(BOARD_ROWS - 1):
        res1.append(board[i][number])
    for i in range(1, BOARD_ROWS):
        res2.append(board[i][number])
    return res1,  res2

# Get 4 elements in all diagonals of the board which size more than  or equal to 4
def getDiagonal():
    diagonal1 = [board[i][i] for i in range(4)]

    diagonal2 = [board[i][i] for i in range(1, 5)]

    j = 0
    diagonal3 = []
    for i in reversed(range(1, 5)):
        diagonal3.append(board[j][i])
        j += 1

    j = 1
    diagonal4 = []
    for i in reversed(range(0, 4)):
        diagonal4.append(board[j][i])
        j += 1

    diagonal5 = [board[i][i + 1] for i in range(4)]
    
    diagonal6 = [board[i + 1][i] for i in range(4)]

    j = 0
    diagonal7 = []
    for i in reversed(range(4)):
        diagonal7.append(board[j][i])
        j += 1

    j = 1
    diagonal8 = []
    for i in reversed(range(1, 5)):
        diagonal8.append(board[j][i])
        j += 1

    return diagonal1, diagonal2, diagonal3, diagonal4, diagonal5, diagonal6, diagonal7, diagonal8

# Evaluate the score of current board
def evaluate():
    score = 0
    for i in range(5):
        for j in range(2):
            score += scoreLine(getRow(i)[j])
            score += scoreLine(getCol(i)[j])
    for i in range(8):
        score += scoreLine(getDiagonal()[i])
    
    return score

# New minimax alpha beta pruning apply for 5x5 caro
def minimax_alphabeta_heuristic(depth, isMax, alpha, beta, startTime, timeLimit, time_check):
    moves = possible_move()
    score = evaluate()
    position = None

    if  datetime.datetime.now() - startTime >= timeLimit:
        time_check = True

    if not moves or depth == 0 or time_check:
        gameResult = is_end(choice)
        if gameResult == 1:
            return pow(-10, (4 + 1)), position
        elif gameResult == 2:
            return pow(10, (4 + 1)), position
        elif gameResult == 0:
            return 0, position
        return score, position

    if isMax:
        for curmove in moves:
            board[curmove[0]][curmove[1]] = 2
            score, pos = minimax_alphabeta_heuristic(depth-1, not isMax, alpha, beta, startTime, timeLimit, time_check)
            if score > alpha:
                alpha = score
                position = curmove
                BESTMOVE = curmove

            board[curmove[0]][curmove[1]] = 0
            if beta <= alpha:
                break
        return alpha, position

    else:
        for curmove in moves:
            board[curmove[0]][curmove[1]] = 1
            score, pos = minimax_alphabeta_heuristic(depth-1, not isMax, alpha, beta, startTime, timeLimit, time_check)
            if score < beta:
                beta = score
                position = curmove
                OPPOSITMOVE = curmove
            board[curmove[0]][curmove[1]] = 0
            if alpha >= beta:
                break
        return beta, position

# Iterative Deepening Search
def IDS():
    startTime = datetime.datetime.now()
    endTime = startTime + datetime.timedelta(0, SEARCH_TIME)
    depth = 1
    position = None
    while True:
        currentTime = datetime.datetime.now()
        if currentTime >= endTime:
            break
        best, position = minimax_alphabeta_heuristic(depth, True, -10000000, 10000000, currentTime, endTime-currentTime, time_check)
        depth += 1

    if position is None:
        position = BESTMOVE
    return position

# MAINLOOP
draw_lines(choice)
check_accept = False

while True:
    # HUMAN = 1 --> O, AI = 2 --> X
    # HUMAN first turn always
    startTime = datetime.datetime.now()
    endTime = startTime + datetime.timedelta(0, SEARCH_TIME)
    time_check = False
    for event in pygame.event.get():
        # HUMAN TURN
        if event.type == pygame.QUIT:
            pygame.sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and player == 1 and game_over == False:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            click_row = int(mouseY / SQUARE_SIZE)
            click_col = int(mouseX / SQUARE_SIZE)
            
            if avai_square(click_row, click_col):
                set_square(click_row, click_col, player)
                check_accept = True
                if check_win(player, choice) or is_full(board):
                    game_over = True
                draw_XO() 
            player = change_Player(player)

        # COMPUTER TURN
        elif player == 2 and game_over == False:
            start = time.time()
            if choice == 1:
                (m, px, py) = max_alphabeta(-5, 5)
            elif choice == 2:
                (px, py) = IDS()
            end = time.time()
            # Check time of the algorithm
            print('Evaluation time: {}s'.format(round(end - start, 7)))
            if avai_square(px, py) and check_accept == True:
                set_square(px, py, player)
                if check_win(player, choice) or is_full(board):
                    game_over = True
                draw_XO()
            check_accept = False
            player = change_Player(player)

        # Press T to restart the game
        if(game_over == True):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    restart()
                    player = 1
                    game_over = False
    pygame.display.update()
