import chess
import ai
import time
import requests

alphabeta_ai =  ai.AI_AlphaBeta()

def read_board_network():
    WEBSERVER = "http://127.0.0.1:5000"
    resp = requests.get(WEBSERVER)
    text = resp.content.decode("latin-1").strip().split("\n")
    board = [i.split() for i in text]
    return board

def read_board(filename):
    board_matrix = []
    with open(filename,'r') as f:
        for line in f:
            line_matrix = []
            for word in line.split():
                line_matrix.append(word)
            board_matrix.append(line_matrix)

    return board_matrix


def convert_to_fen(board):

    peice_conversion = {
        "BK": "k",
        "BQ": "q",
        "BB": "b",
        "BN": "n",
        "BR": "r",
        "BP": "p",
        "WK": "K",
        "WQ": "Q",
        "WB": "B",
        "WN": "N",
        "WR": "R",
        "WP": "P"
    }

    fen = ""
    for x in range(8):
        count = 0
        for y in range(8):
            if board[x][y] == "..":
                count += 1
            elif count > 0:
                fen += str(count)
                fen += peice_conversion.get(board[x][y])
                count = 0
            else:
                fen += peice_conversion.get(board[x][y])
        if count > 0:
            fen += str(count)
        if x != 7:
            fen += "/"

    fen += " b KQkq - 0 1"
    return fen

while True:

    #console input
    # move = input("enter move : ")
    # move = chess.Move.from_uci(move)
    # board.push(move)
    # print(board)

    #webserver input

    board = chess.Board(convert_to_fen(read_board_network()))
    #print(board)

    #ai move

    start_time = time.time()
    ai_move = alphabeta_ai.get_move(board, 3)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(ai_move)
    board.push(ai_move)
    print(board)
    print("================================")

    time.sleep(4)
