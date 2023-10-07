from engine import Engine
from AI import RandAI
from moderateAI import moderateAI

class AdvancedAI:

    def __init__(self, mark):
        self.mark = mark
        self.rand_ai = RandAI(mark)
        self.moderateAI = moderateAI



    def make_move(self, gameboard):
        if not self.moderateAI(gameboard):
            pass

