import game.map as map
import game.player as player
import time

map.init_map(50,25)
player.init_player()
map.display_map()

while(True):
    player.player_move()