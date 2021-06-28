import Player
from Player import Player1
Enemy_spd = 10
fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
class Enemy1:
    
    def __init__(self, x1, y1, x2, y2):
        
        #image = 이미지 파일 F임
        
        #1번 position부터 8번 position까지 만들어놓고 randomint 2개 뽑아서 두칸 비우기 random randomint((1, 8), 2)
        #position은 x좌표 기준으로 하고 각각의 y1, y2..가 한번에 움직이고 만약 <=0이면 다시 처음으로 돌아가기
        #루프문 끝난 다음에는 total_count +=1
        #if Enemy.xposition = player.xposition || yposition(곂칠때) life -=1
        #if Enemy.yposition < 170 Enemy.spd = 10(속도 계산)
        self.image = Image.open("images/enemy.jpg") #이미지 파일 pass 임
        self.left_top_x = 
        self.left_top_y =
        self.right_top_x = 
        self.right_top_y = 
        self.right_bottom_x =
        self.right_bottom_y = 
        self.Enemy_spd = 0
    if (self.right_bottom_y == 240):
        score +=1
        #delete Enemy/Enemies 구현 필요
    #total stage 가 20이고 5단계마다 적 속도 증가함
    
    
    
    rcolor = tuple(int (x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
    if (total_stage > 20):
        
        draw.text((120, 90), "Game Clear!!!", font = fnt, fill = rcolor)
        
        draw.text((120, 120), "Game Clear!!!", font = fnt, fill = rcolor)
        
        draw.text((120, 150), "Game Clear!!!", font = fnt, fill = rcolor)    #game clear 시..
    elif(total_stage //5 == 4):
        Enemy_spd = 30    #final 단계는 속도 증가폭 증가
    elif (total_stage //5 == 3):
        Enemy_spd = 20
    elif (total_stage //5 == 2):
        Enemy_spd = 15
    else:
        Enemy_spd = 10
    
    def step(self):
        #y만 self.speed 만큼 + 하면서 내려오게 하면 됨
        while(left_top_y < 240)
            self.left_top_y = left_top_y + Enemy_spd

    
    def hit_check(self, Player):
        #hit_check 어떻게 할까...
        while Player.Life != 0:
            #####부딛혔을때..
            Player.life -=1
        if Player.Life == 0:
            draw.text((120, 120), "you got F Grade", font = fnt, fill = rcolor)
            
            




    #def update(self):
        #self.speed += 5