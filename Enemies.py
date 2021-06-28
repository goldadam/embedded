from Enemy import Enemy

class Enemies:
    def __init__(self, total_stage):
        self.enemy_list = []
        self.x1 = 0
        self.x2 = 25
        self.y1 = 0
        self.y2 = 25
        for i in range(0, 8):
            self.enemy_list.append(Enemy(self.x1, self.y1, self.x2, self.y2, total_stage))
            self.x1 += 30
            self.x2 += 30
            



