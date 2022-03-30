import chess
import chess.polyglot
import tables
import util
import sys

class AI_AlphaBeta:

    INFINITE = 10000000
    PIECE_VALUES = [0, 100, 300, 330, 500, 900, INFINITE]
    boards_evaluated = 0

    def __init__(self):
        pass  

    def get_move(self, board, depth):

        #self.test_openings(board)

        best_eval = -self.INFINITE
        self.boards_evaluated = 0

        moves = list(board.legal_moves)
        # print(moves)
        # moves = self.order_moves(board, moves)

        for move in board.legal_moves:
            board.push(move)

            eval = -self.alphabeta(board, depth-1, -self.INFINITE, self.INFINITE)
            
            if (eval > best_eval):
                best_eval = eval
                best_move = move

            board.pop()
        #print(self.boards_evaluated)
        return best_move

    def alphabeta(self, board, depth, alpha, beta):
        if (depth == 0):
                self.boards_evaluated += 1
                return self.evaluate(board)

        moves = list(board.legal_moves)
        moves = self.order_moves(board, moves)

        if (len(moves) == 0):
            return 0

        for move in moves:
            board.push(move)
            eval = -self.alphabeta(board, depth-1, -beta, -alpha)
            board.pop()
            
            if (eval >= beta):
                return beta
            if (eval > alpha):
                alpha = eval

        return eval


    def evaluate(self, board):

        eval = 0

        for i in range(64):
            piece = board.piece_at(i)
            if (piece != None):
                if (piece.color == board.turn):
                    eval += self.PIECE_VALUES[piece.piece_type]
                    eval += tables.PIECE_TABLE[piece.piece_type][int(i/8)][i%8]
                else:
                    eval -= self.PIECE_VALUES[piece.piece_type]
                    eval -= tables.PIECE_TABLE[piece.piece_type][int(i/8)][i%8]

        return eval

    def test_openings(self, board):
        with chess.polyglot.open_reader("data/polyglot/performance.bin") as reader:
            for entry in reader.find_all(board):
                print(entry.move, entry.weight, entry.learn)

    def order_moves(self, board, moves):

        move_scores = []

        for move in moves:

            score = 0

            if (board.is_capture(move) and board.piece_at(move.to_square) != None):
                score += 10 * self.PIECE_VALUES[board.piece_at(move.to_square).piece_type] - self.PIECE_VALUES[board.piece_at(move.from_square).piece_type]    

            move_scores.append(score)      

        return util.bubble_sort(moves, move_scores)

# #main
# try:
#     fen = sys.argv[1]
#     depth = sys.argv[2]
#     board = chess.Board(fen)
#     ai = AI_AlphaBeta()
#     print(ai.get_move())

# except:
#     print("Invalid argumants")
