"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


"""
    定义player函数，传入参数为board
    判断当前轮到哪个玩家。
    在初始状态下，X 先行动。随后，玩家交替进行。
    如果棋盘已满且没有获胜者，则返回 None。
 """
# 把你的代码写在下面
def player(board):
    """
    定义player函数，传入参数为board
    判断当前轮到哪个玩家。
    在初始状态下，X 先行动。随后，玩家交替进行。
    如果棋盘已满且没有获胜者，则返回 None。
    """
    count_x = 0
    count_o = 0
    for row in board:
        count_x += row.count(X)
        count_o += row.count(O)
    if count_x == count_o:
        return X
    elif count_x - count_o == 1:
        return O
    else:
        return None



def actions(board):
    """
    返回当前棋盘上所有可能的行动。
    每个行动都表示为一个元组 (i, j)，其中 i 是行索引，j 是列索引。
    如果棋盘已满，则返回一个空列表。
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return possible_actions


def result(board, action):
    """
    返回执行某个行动后的新棋盘状态。
    如果行动无效（例如，选择的单元格已被占用），则抛出异常。
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    判断当前棋盘上是否有玩家获胜。
    如果 X 获胜，则返回 X；如果 O 获胜，则返回 O；如果没有获胜者，则返回 None。
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]!= EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]!= EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]!= EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]!= EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    判断游戏是否结束。
    如果游戏结束（即有获胜者或棋盘已满），则返回 True；否则，返回 False。
    """
    return winner(board) is not None or all(EMPTY not in row for row in board)


def utility(board):
    """
    返回游戏结束时的得分。
    如果 X 获胜，则返回 1；如果 O 获胜，则返回 -1；如果是平局，则返回 0。
    """
    w = winner(board)
    return 1 if w == X else -1 if w == O else 0


def minimax(board):
    """
    使用 minimax 算法找到当前玩家的最佳行动。
    如果棋盘已满或游戏结束，则返回 None。
    """
    if terminal(board):
        return None
    current_player = player(board)
    best_action = None
    if current_player == X:
        max_eval = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            eval = minimax_value(new_board, O)
            if eval > max_eval:
                max_eval = eval
                best_action = action
    else:
        min_eval = math.inf
        for action in actions(board):
            new_board = result(board, action)
            eval = minimax_value(new_board, X)
            if eval < min_eval:
                min_eval = eval
                best_action = action
    return best_action


def minimax_value(board, player):
    """
    计算 minimax 算法中的评估值。
    如果玩家是 X，则返回最大值；如果玩家是 O，则返回最小值。
    """
    if terminal(board):
        return utility(board)
    if player == X:
        return max(minimax_value(result(board, action), O) for action in actions(board))
    else:
        return min(minimax_value(result(board, action), X) for action in actions(board))
