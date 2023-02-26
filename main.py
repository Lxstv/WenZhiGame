#导入库
import game.map as map
import game.player as player
#初始化
map.init_map(50,25)
player.init_player()
map.display_map()
#开始游戏循环
while(True):
    player.player_move()