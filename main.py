import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import Player.py as Player
import Enemy.py as Enemy
import item.py as item

import Player
from Player import Player1
player = Player1()

import Enemy
from Enemy import Enemy1
Enemy = Enemy1()




#해야 될 것 라즈베리에 연결해서 Image를 원하는 사이즈로 출력을 시켜보새ㅔ여  Pil resize 검색해서 해보고 Pil paste Image.paste 검색해서 붙여보고 paste 순서 신경 써서
# 240 x 240  8칸으로 나누면 F라는게 

# Create the display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)
BAUDRATE = 24000000
player_life = 3

spi = board.SPI()
disp = st7789.ST7789(
    spi,
    height=240,
    width = 240,
    y_offset=80,
    rotation=180,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

# Input pins:
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

# Turn on the Backlight
backlight = DigitalInOut(board.D26)
backlight.switch_to_output()
backlight.value = True

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for color.
width = disp.width
height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Clear display.
draw.rectangle((0, 0, width, height), outline=0, fill=(255, 0, 0))
disp.image(image)

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
black_fill = "#000000"
udlr_fill = "#00FF00"
udlr_outline = "#00FFFF"
button_fill = "#FF00FF"
button_outline = "#FFFFFF"
black_outline = "#000000"
text_fill = "#1FDA11"


total_score = 0
Life = 3
goal_score = 20
stage = 1

fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
background = image.open(background.jpg)
draw.text((40,120), "total score: ", font = fnt, fill = text_fill ) #total score 표시되게 해야됨
draw.text((180, 120),"life: ", font = fnt, fill = text_fill ) #남은 life 표시되게 해야됨
Player1 = image.open(player.jpg)
Enemy1 = image.open(enemy.jpg)
#background
#image.open(파일경로)
#background = image.paste() background 이산수학 시험지로
#player
# image.open(파일 경로)
#player = image.paste() pass 이미지 활용하기
#playerWidth = CharacterSize[0]
#playerHeight = CharacterSize[1]
#Enemy = image.paste() F떨어지는거
#EnemyWidth = CharacterSize[0]
#EnemyHeight = CharacterSize[1]


#score 위치 print : 왼쪽 위 life = (Player.life)    오른쪽 위 total_score = 써놓기
#class Player:
    #def __init__(self):
        #self.Life = Life
        #self.x_position = self.width/2
        #self.y_position = self.height - 180
        #self.image = player.image #이미지 파일 pass 임
        #self.spd = 5
        #self.max_spd
        #if life <= 0 print("game end you got F grade") break
        #움직일수 있는 위치 0<=x<=240 0<=y<=70
        #if total_score == 20 print("you Win!!! you got A grade!") break
        #조이스틱 방향을 direction 으로 구현할지 아니면 그냥 x, y좌표 변경으로 구할지 -> x,y 변경 방식으로 하자.
        



#class Enemy:
    #def __init__(self):
        #여기 구현이 좀 힘듦 구역 240을 8로 쪼개어 x좌표방향으로 10부터 시작 
        #
        #image = 이미지 파일 F임
        #height = 50 , width = 22(조절 가능) 
        #1번 position부터 8번 position까지 만들어놓고 randomint 2개 뽑아서 두칸 비우기
        #position은 x좌표 기준으로 하고 각각의 y1, y2..가 한번에 움직이고 만약 <=0이면 다시 처음으로 돌아가기
        #루프문 끝난 다음에는 total_count +=1
        #if Enemy.xposition = player.xposition || yposition(곂칠때) life -=1
        #if Enemy.yposition < 170 Enemy.spd = 10(속도 계산)
        #else Enemy.spd = 15(# 10단계까지)
        #if total_score >= 5 spd = spd+5
        #if spd = mx_spd: spd = mx_spd

circle_center_x = width/2
circle_center_y = height/2 + 15

while True:
    up_fill = 0
    Player.x_position = circle_center_x
    Player.y_position = circle_center_y
    if not button_U.value:  # up pressed
        up_fill = udlr_fill
        button_check = 1
        circle_center_y -= player.spd

  
    down_fill = 0
    
    if not button_D.value:  # down pressed
        down_fill = udlr_fill
        button_check = 1
        circle_center_y += player.spd

 
    left_fill = 0
    if not button_L.value:  # left pressed
        left_fill = udlr_fill
        button_check = 1
        circle_center_x -= player.spd

   

    if not button_R.value:  # right pressed
        right_fill = udlr_fill
        button_check = 1
        circle_center_x += player.spd




 
      # B button
    
    
     #epplipse position = 
    #draw.rectangle((0, 0, width, height), outline=0, fill=0)







    

    # Display the Image
    disp.image(image)

    time.sleep(0.01)
