def five_button_item():
    item1 = 1
    while(item1 > 0):
            player.spd +=10
            item1 -=1
            A_fill = 0
    if not button_A.value:  # left pressed, increase player speed
      pass
#처음에 아이템이라는 카테고리를 만들어 사용하려다 인식이 잘 되지 않아 지워버림
def six_button_item():
    item2 = 1
    while(item2 > 0):
        Enemy.spd -5
        item2 -=1
        B_fill = 0
    if not button_B.value:  # left pressed, slow enemy speed
        pass

#마찬가지 이유