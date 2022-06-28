import random

def createBoard():
    All_Board = list(range(0, 9)), list(range(0, 9)), list(range(0, 9))
    return All_Board

def Alpha_row_num(A_End = 1, B_End =1, Time = 0):
    if len(All_Board[0]) != 0 and len(All_Board[1]) == 0 and len(All_Board[2]) == 0:
        A_End= 0
    if len(All_Board[0]) == 0 and len(All_Board[1]) != 0 and len(All_Board[2]) == 0:
        B_End = 0
    if len(All_Board[0]) != 0 and len(All_Board[1]) != 0 and len(All_Board[2]) == 0:
        B_End = 0 
    for num in range(0, 3):
        if len(All_Board[num]) == 0:
            continue
        else:
            Time += 1
    return A_End, B_End, Time

def printBoard(All_Board):
    A_End, B_End, Time = Alpha_row_num()
    if len(All_Board[0]) != 0:
        print("A", end = "      " * A_End)
    if len(All_Board[1]) != 0:
        print("B", end = "      " * B_End)
    if len(All_Board[2]) != 0:
        print("C", end = "")
    print("")
    n, sep = 0, 1
    for num in range(0, 3):
        if len(All_Board[num]) == 0:
            continue
        else:
            n += 1
            if n == Time:
                sep = 0
            print(*All_Board[num][0:3], sep = " ", end = "  " * sep)
    print("")
    n, sep = 0, 1
    for num in range(0, 3): 
        if len(All_Board[num]) == 0:
            continue
        else:
            n += 1
            if n == Time:
                sep = 0
            print(*All_Board[num][3:6], sep = " ", end = "  " * sep)
    print("")
    n, sep = 0, 1
    for num in range(0, 3): 
        if len(All_Board[num]) == 0:
            continue
        else:
            n += 1
            if n == Time:
                sep = 0
            print(*All_Board[num][6:9], sep = " ", end = "  " * sep)
    print("")

def makeMove(All_Board, board, index, Player):
    if All_Board[board][index] != "X":
        All_Board[board][index] = "X"

def Elimate_Winner(index, All_Board,  Player):
    global Remain_Board 
    Remain_Board = 3  
    for board in range(0, 3):
        for Compare in Answer:
            if Record[board] >= Compare:
                 All_Board[board].clear()
                 Remain_Board -= 1
                 if Remain_Board == 0:
                    if Player == "1":
                        Player = "2"
                    else:
                        Player = 1
                    print(f'Player {Player} wins game')
                    return True
                 break

def count_board():
    board_num = 0
    for num in range(0, 3):
        if len(All_Board[num]) != 0:
            board_num += 1
    return board_num

def record_system(Record):
    Record[board].add(index)
    if Player == "2":
        Follow  = []
        Follow.append(board)
        Follow.append(index)
        return Follow
    
def input_system():
    global board, index
    move = input("Player "+Player+": ")
    decyo = {"A": 0, "B": 1, "C": 2}
    if len(move) != 0 and (move[0] == "A" or move[0] == "B" or move[0] == "C") and len(move) == 2 and move[1] in "012345678":
        board = move[0]
        board = decyo[board]
        index = int(move[1])  
    else:
        print("Invalid move, please input again")
        input_system()
    if len(All_Board[board]) == 0:
        print("Invalid move, please input again")
        input_system()
    elif All_Board[board][index] == "X":
        print("Invalid move, please input again")
        input_system()
    return board, index

def Player_1_AI(Case_Type, Remain_Board):
    global Reference
    global Case_type
    global n
    if n == 0:
        board, index = random.randint(0, 2), 4
        n += 1
        return Case_Type,board, index, Reference
    AI = {0: [5, 7], 2: [3, 7] , 6: [1, 5], 8: [1, 3], 1: [6, 8], 3: [2, 8], 5: [0, 6], 7: [0, 2], 4:[0, 1, 2, 3, 4, 5, 6, 7, 8]}
    Player_2_board = Player_2_Choice[0]
    Player_2_index = Player_2_Choice[1]
    if board_num == 1:
        Ex = None
        board = Player_2_board
        for index in AI[Player_2_index]:
            if All_Board[board][index] != "X":
                for elimate in Answer:
                    Record_X = set()
                    Record_Tem = list(Record[board])
                    for element in Record_Tem:
                        Record_X.add(element)
                    Record_X. add(index)
                    if Record_X >= elimate :
                        Ex = True
                        break
                    else:
                        index = index
                        board = board
                        Ex = False
                if Ex == False:
                    return Case_Type, board, index, Reference
        if Ex == True:
            for index in range(0, 9):
                Record_X = Record
                if All_Board[Player_2_board][index] == "X":
                    continue
                else:
                    Record_X[Player_2_board].add(index)
                for Compare in Answer:
                    if Record_X[Player_2_board] <= Compare:                  
                        return Case_Type, board, index, Reference
    for board in range(0, 3): #board_killing
        if len(All_Board[board]) == 0:
            continue
        for elimate in Answer:
            index = elimate & set(Record[Player_2_board])
            if len(index) == 2:
                index = elimate - index
                index = list(index)
                index = index[0]
                board = Player_2_board
                return Case_Type, board, index, Reference          
        for board in range(0, 3): #Seeking for empty board middle
            if len(All_Board[board]) == 0:
                continue
            if All_Board[board][4] != "X" and len(Record[board]) == 0:
                Case_Type, board, index = 1, board, 4
                if All_Board[Player_2_board][4] != "X":
                    Reference = [Player_2_board, Player_2_index]
                return Case_Type, board, index, Reference
        for index in AI[Player_2_index]: #little mind game 
            if All_Board[Player_2_board][index] != "X":
                return Case_Type, Player_2_board, index, Reference

Answer = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
Answer = list(map(set, Answer))
Record = [ [] for i in range(0,3)]
Record = list(map(set, Record))
All_Board = createBoard()
printBoard(All_Board)
Player, n, Case_Type, Reference  = "1", 0, None, None
Remain_Board = 3
while True:
    board_num = count_board()    
    if Player == "1":
        Case_Type, board, index, Reference = Player_1_AI(Case_Type, Remain_Board)
        decyo = {0: "A", 1: "B", 2: "C"}
        print(f"Player 1: {decyo[board]}{index}")
    else:
        board, index = input_system()
    Player_2_Choice = record_system(Record)
    makeMove(All_Board, board, index, Player)
    if Elimate_Winner(index, All_Board,Player) == True:
        break
    printBoard(All_Board)
    if Player == "1":
        Player = "2"
    else:
        Player = "1"