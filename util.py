
def merege_sort(moves, scores):
    return moves

def bubble_sort(moves, scores):

    for i in range(1, len(scores)):
        for j in range(0, len(scores)-1):
            if (scores[j+1] > scores[j]):
                scores[j+1], scores[j] = scores[j], scores[j+1]
                moves[j+1], moves[j] = moves[j], moves[j+1]
    return moves
        
