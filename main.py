import chess
import ai
import time

board = chess.Board("7r/pQp2kp1/3r1n1p/4n3/3q1B2/7P/PPP3P1/3R1R1K b - - 0 1")
alphabeta_ai =  ai.AI_AlphaBeta()

print(board)

while True:
    move = input("enter move : ")
    move = chess.Move.from_uci(move)
    board.push(move)
    print(board)
    start_time = time.time()
    ai_move = alphabeta_ai.get_move(board, 4)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(ai_move)
    board.push(ai_move)
    print(board)
