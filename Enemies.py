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
            
#enemy를 여러개를 담을 수 있는 클래스를 만듦..(한번에 내려가야 하기 때문)


