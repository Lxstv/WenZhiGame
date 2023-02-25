def goto(x,y):
    print('\033[' + str(y) + ';' + str(x) + 'H',end='')