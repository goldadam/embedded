from PIL import Image, ImageDraw, ImageFont
class Player:
    def __init__(self, life, speed):
        self.life = life
        self.x_position = 120
        self.y_position = 210
        self.image = Image.open("images/player1.jpg") #이미지 파일 pass 임
        self.spd = speed
        self.max_spd = 30
      
    
    #spd 만큼 x, y 좌표 조정, 방향별로 따르게 구현 
    def move(self, up_down, left_right):
        if up_down == 'up':
            if self.y_position - self.spd < 0:
                pass #밖으로 안나가게 처리함
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
                self.x_position += self.spd #안나가면 움직임

        
       
    def speed_up(self):
        self.spd += 10
    #아이템 구현 player 속도 up, 실제 사용은 main.py 에서 사용함