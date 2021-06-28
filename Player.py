from PIL import Image, ImageDraw, ImageFont
class Player:
    def __init__(self, life, speed):
        self.life = life
        self.x_position = 120
        self.y_position = 210
        self.image = Image.open("images/player1.jpg") #이미지 파일 pass 임
        self.spd = speed
        self.max_spd = 30
        #if life <= 0 print("game end you got F grade") break
        #움직일수 있는 위치 0<=x<=240 0<=y<=70
        
        #맨 위에 total score 랑 stage 구현 해야됨
        
    
    
    
    def move(self, up_down, left_right):
        if up_down == 'up':
            if self.y_position - self.spd < 0:
                pass
            else :
                self.y_position -= self.spd
        elif up_down == 'down':
            if self.y_position + self.spd > 215:
                pass
            else :
                self.y_position += self.spd
        if left_right == 'left':
            if self.x_position - self.spd < 0:
                pass
            else :
                self.x_position -= self.spd
        elif left_right == 'right':
            if self.x_position + self.spd > 215:
                pass
            else :
                self.x_position += self.spd

        #움직이는 코드 ~
       
    def speed_up(self):
        self.spd += 10