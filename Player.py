from PIL import Image, ImageDraw, ImageFont

class Player1:
    def __init__(self):
        self.Life = Life
        self.x_position = self.width/2
        self.y_position = self.height - 180
        self.image = Image.open("images/player.jpg") #이미지 파일 pass 임
        self.spd = 5
        self.max_spd = 10
        #if life <= 0 print("game end you got F grade") break
        #움직일수 있는 위치 0<=x<=240 0<=y<=70
        #if total_score == 20 print("you Win!!! you got A grade!") break
        #조이스틱 방향을 direction 으로 구현할지 아니면 그냥 x, y좌표 변경으로 구할지 -> x,y 변경 방식으로 하자.
        
    def move(self, direction):
        #움직이는 코드 ~