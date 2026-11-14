
# Alpha-Beta Pruning

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, -1]
}

def alphabeta(node, alpha, beta, maxi):
    if isinstance(node, int):
        return node

    if maxi:
        best = -999
        for child in tree[node]:
            best = max(best, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 999
        for child in tree[node]:
            best = min(best, alphabeta(child, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

print("Best Value:", alphabeta('A', -999, 999, True))
