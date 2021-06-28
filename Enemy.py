from PIL import Image, ImageDraw, ImageFont

class Enemy:
    
    def __init__(self, x1, y1, x2, y2, total_stage):
        
        #image = 이미지 파일 F임
        
        #1번 position부터 8번 position까지 만들어놓고 randomint 2개 뽑아서 두칸 비우기 random randomint((1, 8), 2)
        #position은 x좌표 기준으로 하고 각각의 y1, y2..가 한번에 움직이고 만약 <=0이면 다시 처음으로 돌아가기
        #루프문 끝난 다음에는 total_count +=1
        #if Enemy.xposition = player.xposition || yposition(곂칠때) life -=1
        #if Enemy.yposition < 170 Enemy.spd = 10(속도 계산)
        self.image = Image.open("images/enemy1.jpg") #이미지 파일 pass 임
        self.left_top_x = x1
        self.left_top_y = y1
        self.right_bottom_x = x2
        self.right_bottom_y = y2
        self.Enemy_spd = 5
    #------------------------------------------------------------------
    #if (self.right_bottom_y == 240):
    #    score +=1
        #delete Enemy/Enemies 구현 필요
    #total stage 가 20이고 5단계마다 적 속도 증가함
    
    #rcolor = tuple(int (x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
    #if (total_stage > 20):
        
    #    draw.text((120, 90), "Game Clear!!!", font = fnt, fill = rcolor)
        
    #    draw.text((120, 120), "Game Clear!!!", font = fnt, fill = rcolor)
        
    #    draw.text((120, 150), "Game Clear!!!", font = fnt, fill = rcolor)    #game clear 시..
    #------------------------------------------------------------------

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

    
    def hit_check(self, player):
        if((player.x_position > self.left_top_x and player.x_position < self.right_bottom_x ) and \
            (player.y_position < self.right_bottom_y and player.y_position > self.left_top_y)) or \
            ((player.x_position + 25> self.left_top_x and player.x_position + 25 < self.right_bottom_x) and \
                (player.y_position < self.right_bottom_y and player.y_position > self.left_top_y)):
            print("collision!!!")
            #그 스테이지 종료 후 목숨 >= 1일경우 다음 스테이지로 넘어가고 아니면 계속 진행함, 뒤로 갈수록 속도가 매우 빨라지기 때문에 맨 위에가 닿았을 경우에만 구현
            return 1

        else:
            return 0
            
    def speed_down(self):
        self.Enemy_spd -= 4