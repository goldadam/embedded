import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

from Player import Player
from Enemy import Enemy
from Enemies import Enemies




#해야 될 것 라즈베리에 연결해서 Image를 원하는 사이즈로 출력을 시켜보새ㅔ여  Pil resize 검색해서 해보고 Pil paste Image.paste 검색해서 붙여보고 paste 순서 신경 써서
# 240 x 240  8칸으로 나누면 F라는게 

# Create the display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)
BAUDRATE = 24000000

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

fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
fnt2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
background = Image.open('images/background1.jpg')
background = background.resize((240, 240))
#draw.text((40,120), "total score: ", font = fnt, fill = text_fill ) #total score 표시되게 해야됨
#draw.text((180, 120),"life: ", font = fnt, fill = text_fill ) #남은 life 표시되게 해야됨
#enemy = Enemy(0, 0, 25, 25)
enemy_index = [0, 1, 2, 3, 4, 5, 6, 7]
stage = 1
first = 0
life = 3
hit = 0
speed = 15
delete_enemy = []
up_down = 'None'
left_right = 'None'
enemies = Enemies(stage)
player = Player(life, speed)
button_a = 0
button_b = 0
while True:
    up_down = 'None'
    left_right = 'None'
    image.paste(background, (0,0))
    #image.paste(enemy.image, (enemy.left_top_x, enemy.left_top_y))
    if first == 0:
        delete_enemy = random.sample(enemy_index, 2)
        first = 1
    
    if not button_U.value:  # up pressed
        up_down = 'up'
    if not button_D.value:  # down pressed
        up_down = 'down'
    if not button_L.value:  # left pressed
        left_right = 'left'
    if not button_R.value:  # right pressed
        left_right = 'right'
    if not button_A.value:  # left pressed, fast player speed
        if button_a == 0:
            for enemy in enemies.enemy_list :
                enemy.speed_down()
            print('enemy speed down!')
            button_a += 1
    if not button_B.value:  # left pressed, slow enemy speed
        if button_b == 0:
            player.speed_up()
            print('speed up!')
            button_b += 1

    for i in range(len(enemies.enemy_list)) :
        if i in delete_enemy :
            continue
        else :
            image.paste(enemies.enemy_list[i].image, (enemies.enemy_list[i].left_top_x, enemies.enemy_list[i].left_top_y))
    image.paste(player.image, (player.x_position, player.y_position))
    player.move(up_down, left_right)

    for i in range(len(enemies.enemy_list)) :
        enemies.enemy_list[i].step()
        if i in delete_enemy :
            continue
        hit = hit or enemies.enemy_list[i].hit_check(player)
    
    if hit == 1:
        life -= 1
        print(life)

    if player.life == 0:
        while True:
                draw.rectangle((0, 0, width, height), outline=0, fill=0)

                rcolor = tuple(int (x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
            
                draw.text((52, 90), "YOU GOT F GRADE", font = fnt2, fill = rcolor)
            
                draw.text((52, 120), "YOU GOT F GRADE", font = fnt2, fill = rcolor)
            
                draw.text((52, 150), "YOU GOT F GRADE", font = fnt2, fill = rcolor)    #game clear 시..
                disp.image(image)
    if enemies.enemy_list[0].left_top_y >= 240 or hit :
        hit = 0
        first = 0
        stage += 1
        enemies = Enemies(stage)
        player = Player(life, speed)
        if stage > 20:
            while True:
                draw.rectangle((0, 0, width, height), outline=0, fill=0)

                rcolor = tuple(int (x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
            
                draw.text((65, 90), "Game Clear!!!", font = fnt2, fill = rcolor)
            
                draw.text((65, 120), "Game Clear!!!", font = fnt2, fill = rcolor)
            
                draw.text((65, 150), "Game Clear!!!", font = fnt2, fill = rcolor)    #game clear 시..
                disp.image(image)
    draw.text((10,10), "stage: " + str(stage), font = fnt, fill = (255, 0, 0) ) #total score 표시되게 해야됨
    draw.text((160, 10),"life: " + str(life), font = fnt, fill = (255, 0, 0) ) #남은 life 표시되게 해야됨
    # Display the Image
    disp.image(image)



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
