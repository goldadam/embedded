import main as if __name__ == '__main__':
    main()
    


from PIL import Image, ImageDraw, ImageFont
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT
class Player1:
    def __init__(self):
        self.Life =Life
        self.x_position = self.width/2
        self.y_position = self.height - 180
        self.image = Image.open("images/player.jpg") #이미지 파일 pass 임
        self.spd = 15
        self.max_spd = 30
        
        #if life <= 0 print("game end you got F grade") break
        #움직일수 있는 위치 0<=x<=240 0<=y<=70
        
        #맨 위에 total score 랑 stage 구현 해야됨
        
    
    
    
    def move(self, direction):
        #움직이는 코드 ~
       
    while True:
        
        Player.x_position = circle_center_x
        Player.y_position = circle_center_y
    
    if (y_position < 40):
        y_position = 40             #player 가 갈수 있는 위치 정해주기...


    if not button_U.value:  # up pressed
        circle_center_y -= Player1.spd

  
    if not button_D.value:  # down pressed
        circle_center_y += Player1.spd

 
    
    if not button_L.value:  # left pressed
        circle_center_x -= Player1.spd

   

    if not button_R.value:  # right pressed
        circle_center_x += Player1.spd

