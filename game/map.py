import PublicFunction

global map
global map_long
global map_wide
map = []

def init_map(f_map_long , f_map_wide):
    global map
    global map_long
    global map_wide
    map_long = f_map_long
    map_wide = f_map_wide
    for i_0 in range(map_wide):
        map.append([])
    
    map[0].append('边')
    for i_1 in range(map_long-2):
        map[0].append('边')
    map[0].append('边')

    for i_0 in range(1,map_wide-1):
        map[i_0].append('边')
        for i_1 in range(map_long-2):
            map[i_0].append('  ')
        map[i_0].append('边')

    map[map_wide-1].append('边')
    for i_1 in range(map_long-2):
        map[map_wide-1].append('边')
    map[map_wide-1].append('边')

def display_map():
    global map
    global map_long
    global map_wide
    show_string = ''
    print('\033[2J',end='')
    PublicFunction.goto(0,0)
    for i_0 in range(map_wide):
        for i_1 in range(map_long):
            show_string += map[i_0][i_1]
        show_string += '\n'
    print(show_string,end='')