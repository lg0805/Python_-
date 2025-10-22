import random
import board


class Player(object):
    """玩家类"""

    def __init__(self, name):
        self.name = name  # 姓名
        self.score = 0  # 成绩
        self.chess = None  # 棋子

    def move(self, chess_board):
        """在棋盘上落子

        :param chess_board:
        """
        # 1. 由用户输入要落子索引
        index = -1
        while index not in chess_board.movable_list:
            try:
                index = int(input("请 “%s” 输入落子位置 %s：" %
                                  (self.name, chess_board.movable_list)))
            except ValueError:
                pass

        # 2. 在指定位置落子
        chess_board.move_down(index, self.chess)


class AIPlayer(Player):
    """智能玩家"""

    def move(self, chess_board):
        """在棋盘上落子

        :param chess_board:
        """
        print("%s 正在思考落子位置..." % self.name)

        # 1. 查找我方必胜落子位置
        for index in chess_board.movable_list:
            if chess_board.is_win(self.chess, index):
                print("走在 %d 位置必胜！！！" % index)
                chess_board.move_down(index, self.chess)

                return

        # 2. 查找地方必胜落子位置-我方必救位置
        other_chess = "O" if self.chess == "X" else "X"

        for index in chess_board.movable_list:
            if chess_board.is_win(other_chess, index):
                print("敌人走在 %d 位置必输，火速堵上！" % index)
                chess_board.move_down(index, self.chess)

                return

        # 3. 根据子力价值选择落子位置
        index = -1
        # 没有落子的角位置列表
        corners = list(set([0, 2, 6, 8]).intersection(chess_board.movable_list))
        # 没有落子的边位置列表
        edges = list(set([1, 3, 5, 7]).intersection(chess_board.movable_list))

        if 4 in chess_board.movable_list:
            index = 4
        elif corners:
            index = random.choice(corners)
        elif edges:
            index = random.choice(edges)

        # 在指定位置落子
        chess_board.move_down(index, self.chess)


if __name__ == '__main__':
    # 1. 创建棋盘对象
    chess_board = board.Board()

    # 2. 创建玩家对象
    human = Player("玩家")
    human.chess = "X"

    # 3. 玩家在棋盘上循环落子，直到玩家胜利
    while not chess_board.is_win(human.chess):
        human.move(chess_board)

        # 显示棋盘
        chess_board.show_board()
