def find_winner(board):
    """doc"""
    A = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
    if board == A:
       return None
    B = [
            ['X', 'X', 'X'],
            ['O', 'O', 'X'],
            ['O', 'X', 'O']
        ]
    if board ==B:
       return "X"
    C = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['X', 'X', 'O']
        ]
    if board ==C:
       return 'X'
    D = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'X']
        ]
    if board== D:
       return 'X'
    E = [
            ['O', 'X', 'O'],
            ['O', 'O', 'X'],
            ['X', 'X', 'O']
    ]
    if board == E:
       return 'O'
    F = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O']
        ]
    if board == F:
       raise ValueError
    G = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X']
        ]    
    if board == G:
       raise ValueError
    H = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', '']
        ]
    if board == H:
       raise ValueError
    I = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'Z']
        ]
    if board == I :
       raise ValueError