def normalize(piece):
    min_x = min(x for x, y in piece)
    min_y = min(y for x, y in piece)
    return sorted((x - min_x, y - min_y) for x, y in piece)

def rotate_90(piece):
    return [(-y, x) for x, y in piece]

def check_overlap(piece1, piece2):
    if len(piece1) != len(piece2):
        return False
    target = normalize(piece2)
    rotated = piece1
    for _ in range(4):
        if normalize(rotated) == target:
            return True
        rotated = rotate_90(rotated)
    return False

def dfs_board(board, row, col, visited, empty):
    size = len(board)
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        empty.append((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited and board[nr][nc] == 0:
                stack.append((nr, nc))
                
def dfs_table(table, row, col, visited, piece):
    size = len(table)
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        piece.append((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited and table[nr][nc] == 1:
                stack.append((nr, nc))

def solution(game_board, table):
    answer = 0
    size = len(game_board)
    game_board_visited = set()
    table_visited = set()
    empties = []
    pieces = []

    for i in range(size):
        for j in range(size):
            if game_board[i][j] == 1:
                continue
            elif (i, j) not in game_board_visited:
                empty = []
                dfs_board(game_board, i, j, game_board_visited, empty)
                empties.append(empty)
        
    for i in range(size):
        for j in range(size):
            if table[i][j] == 0:
                continue
            elif (i, j) not in table_visited:
                piece = []
                dfs_table(table, i, j, table_visited, piece)
                pieces.append(piece)

    print(empties)
    print(pieces)
                
    used = set()
    for i in range(len(empties)):
        for j in range(len(pieces)):
            if check_overlap(empties[i], pieces[j]) and j not in used:
                print(i, j)
                used.add(j)
                answer += len(empties[i])
                break
                
    return answer
