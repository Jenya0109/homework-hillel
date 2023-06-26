maps_size = 3
maps = [1,2,3,4,5,6,7,8,9]
def draw_maps():
	print (('_' * 4 * maps_size ))
	for i in range(maps_size):
		print ((' ' * 3 + '|') * 3)
		print ('',maps[i*3], '|', maps[1+i*3], '|', maps[2+i*3], '|')
		print (('_' * 3 + '|') * 3)

victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol

def get_result():
    win = ''
    for i in victories:
        if maps[i[0]] == 'X' and maps[i[1]] == 'X' and maps[i[2]] == 'X':
            win = 'You'
        if maps[i[0]] == 'O' and maps[i[1]] == 'O' and maps[i[2]] == 'O':
            win = 'Computer'
    return win

def check_line(sum_O, sum_X):
    step = ''
    for line in victories:
        o = 0
        x = 0
        for i in range(0, 3):
            if maps[line[i]] == 'O':
                o = o + 1
            if maps[line[i]] == 'X':
                x = x + 1
        if o == sum_O and x == sum_X:
            for i in range(0, 3):
                if maps[line[i]] != 'O' and maps[line[i]] != 'X':
                    step = maps[line[i]]
    return step

def VIRT():
    step = ''
    step = check_line(2, 0)
    if step == '':
        step = check_line(0, 2)
    if step == '':
        step = check_line(1, 0)
    if step == '':
        if maps[4] != 'X' and maps[4] != 'O':
            step = 5
    if step == '':
        if maps[0] != 'X' and maps[0] != 'O':
            step = 1
    return step

game_over = False
player = True

print('Welcome to the game\nYour game mode:\ngame  with virtual player')
(input('Press any key to start the game: '))

while game_over == False:
    draw_maps()
    if player == True:
        symbol = 'X'
        step = int(input('Your turn: '))
    else:
        print('Computer`s turn: ')
        symbol = 'O'
        step = VIRT()
    if step != '':
        step_maps(step, symbol)
        win = get_result()
        if win != '':
            game_over = True
        else:
            game_over = False
    else:
        game_over = True
        win = 'Draw'
    player = not (player)

draw_maps()
print(win, 'won!')
