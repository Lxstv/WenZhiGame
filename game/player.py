#导入库
import game.map as map
import keyboard
import time
#定义公共变量
global player_x
global player_y
#定义初始化玩家函数
def init_player():
    global player_x
    global player_y
    player_x = map.map_long // 2
    player_y = map.map_wide // 2
    print(player_x,player_y)
    map.map[player_y][player_x] = '我'
#定义碰撞检测函数
def Collision_Detection(xy,fu):
    #导入公共变量
    global player_x
    global player_y
    if xy == 'x':
        if fu == '+':
            if map.map[player_y][player_x+1] == '边':
                return False
            else:
                return True
        elif fu == '-':
            if map.map[player_y][player_x-1] == '边':
                return False
            else:
                return True
    if xy == 'y':
        if fu == '+':
            if map.map[player_y+1][player_x] == '边':
                return False
            else:
                return True
        elif fu == '-':
            if map.map[player_y-1][player_x] == '边':
                return False
            else:
                return True
#定义玩家控制函数
def player_move():
    #导入公共变量
    global player_x
    global player_y
    map.map[player_y][player_x] = '  '
    if keyboard.is_pressed('w') and Collision_Detection('y','-'):
        player_y -= 1
    elif keyboard.is_pressed('s') and Collision_Detection('y','+'):
        player_y += 1
    elif keyboard.is_pressed('a') and Collision_Detection('x','-'):
        player_x -= 1
    elif keyboard.is_pressed('d') and Collision_Detection('x','+'):
        player_x += 1
    else:
        return 0
    time.sleep(0.1)
    map.map[player_y][player_x] = '我'
    map.display_map()