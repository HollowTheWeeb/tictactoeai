import random
from AI import RandAI
from aibase import baseAI

class moderateAI:
    def __init__(self, mark):
        self.mark = mark
        self.ai = RandAI(mark)
        self.aibase = BaseAI()

    def try_win_move(self, gameboard):

        return self.aibase.

    def make_move(self, gameboard):
        win = self.try_win_move(gameboard)
        if not win:
            self.ai.make_move(gameboard)


