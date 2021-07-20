class GameStats:
    """
    跟踪游戏的统计消息
    """

    def __init__(self, ai_game):
        """
        初始化统计消息
        :param ai_game:火箭
        """

        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏启动处于活动状态
        self.game_active = False

        # 任何适合都不应该重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """
        初始化游戏运行期间的可能变化的统计消息
        """

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
