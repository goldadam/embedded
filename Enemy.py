from PIL import Image, ImageDraw, ImageFont

class Enemy:
    
    def __init__(self, x1, y1, x2, y2, total_stage):
        
        
        self.image = Image.open("images/enemy1.jpg") #이미지 파일 pass 임
        self.left_top_x = x1
        self.left_top_y = y1
        self.right_bottom_x = x2
        self.right_bottom_y = y2
        self.Enemy_spd = 5 #enemy 파일 이미지(F학점) 받아서 객체 생성후 필요한 값들 저장 및 초기화
        #5단계씩 마다 난이도 조절을 위해 스피드를 증가시킴
        if(total_stage //5 == 4):
            self.Enemy_spd = 30    #final 단계는 속도 증가폭 증가
            print('stage : 20')
        elif (total_stage //5 == 3):
            self.Enemy_spd = 20
            print('stage : 15')
        elif (total_stage //5 == 2):
            self.Enemy_spd = 15
            print('stage : 10')
        elif (total_stage //5 == 1):
            self.Enemy_spd = 10
            print('stage : 5')
    
    def step(self):
        #y만 self.speed 만큼 + 하면서 내려오게 하면 됨
        if self.left_top_y < 240 :
            self.left_top_y = self.left_top_y + self.Enemy_spd
            self.right_bottom_y = self.right_bottom_y + self.Enemy_spd
        #enemy 떨어지는 속도를 이용해 top_y와 bottom_y 를 이용해 찌그러지지 않게 이미지 파일 구현
    
    def hit_check(self, player):
        if((player.x_position > self.left_top_x and player.x_position < self.right_bottom_x ) and \
            (player.y_position < self.right_bottom_y and player.y_position > self.left_top_y)) or \
            ((player.x_position + 25> self.left_top_x and player.x_position + 25 < self.right_bottom_x) and \
                (player.y_position < self.right_bottom_y and player.y_position > self.left_top_y)):
            print("collision!!!")
            #뒤로 갈수록 점점 속도가 빨라져 앞에 부딪히는 것만 인식하기 때문에, 각 변의 길이와 좌표를 이용하여 부딪히는지 안부딪히는지 체크함 직사각형으로 따지면 밑의 부분
            return 1

        else:
            return 0
            
    def speed_down(self):
        self.Enemy_spd -= 4
        #아이템 2 구현, 적의 속도를 4만큼 늦출 수 있음 한번만 사용 가능, 아이템 사용은 main.py 에 구현해놓음