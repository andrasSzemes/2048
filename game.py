import random
import sys
import time
import os
import csv
from copy import deepcopy
from termcolor import colored
from playsound import playsound

width = os.get_terminal_size().columns

list_0 = [
'color_print(205, 193, 181, 205, 193, 181, "")',
'color_print(205, 193, 181, 205, 193, 181, "")',
'color_print(205, 193, 181, 205, 193, 181, "")',
'color_print(205, 193, 181, 205, 193, 181, "")',
'color_print(205, 193, 181, 205, 193, 181, "")',
'color_print(205, 193, 181, 205, 193, 181, "")',
'color_print(205, 193, 181, 205, 193, 181, "")',
'color_print(205, 193, 181, 205, 193, 181, "")',
'color_print(205, 193, 181, 205, 193, 181, "")',
'color_print(205, 193, 181, 205, 193, 181, "")',
]

list_2 = [
'color_print(119, 110, 101, 238, 228, 219, "")',
'color_print(119, 110, 101, 238, 228, 219, "")',
'color_print(119, 110, 101, 238, 228, 219, "  ___  ")',
'color_print(119, 110, 101, 238, 228, 219, " |__ \ ")',
'color_print(119, 110, 101, 238, 228, 219, "    ) |")',
'color_print(119, 110, 101, 238, 228, 219, "   / / ")',
'color_print(119, 110, 101, 238, 228, 219, "  / /_ ")',
'color_print(119, 110, 101, 238, 228, 219, " |____|")',
'color_print(119, 110, 101, 238, 228, 219, "")',
'color_print(119, 110, 101, 238, 228, 219, "")',
]

list_4 = [
'color_print(119, 110, 101, 237, 224, 201, "")',
'color_print(119, 110, 101, 237, 224, 201, "")',
'color_print(119, 110, 101, 237, 224, 201, "  _  _   ")',
'color_print(119, 110, 101, 237, 224, 201, " | || |  ")',
'color_print(119, 110, 101, 237, 224, 201, " | || |_ ")',
'color_print(119, 110, 101, 237, 224, 201, " |__   _|")',
'color_print(119, 110, 101, 237, 224, 201, "    | |  ")',
'color_print(119, 110, 101, 237, 224, 201, "    |_|  ")',
'color_print(119, 110, 101, 237, 224, 201, "")',
'color_print(119, 110, 101, 237, 224, 201, "")',
]

list_8 = [
'color_print(249, 246, 242, 241, 177, 125, "")',
'color_print(249, 246, 242, 241, 177, 125, "")',
'color_print(249, 246, 242, 241, 177, 125, "   ___  ")',
'color_print(249, 246, 242, 241, 177, 125, "  / _ \ ")',
'color_print(249, 246, 242, 241, 177, 125, " | (_) |")',
'color_print(249, 246, 242, 241, 177, 125, "  > _ < ")',
'color_print(249, 246, 242, 241, 177, 125, " | (_) |")',
'color_print(249, 246, 242, 241, 177, 125, "  \___/ ")',
'color_print(249, 246, 242, 241, 177, 125, "")',
'color_print(249, 246, 242, 241, 177, 125, "")',
]

list_16 = [
'color_print(249, 246, 242, 243, 149, 104, "")',
'color_print(249, 246, 242, 243, 149, 104, "")',
'color_print(249, 246, 242, 243, 149, 104, "  __   __  ")',
'color_print(249, 246, 242, 243, 149, 104, " /_ | / /  ")',
'color_print(249, 246, 242, 243, 149, 104, "  | |/ /_  ")',
'color_print(249, 246, 242, 243, 149, 104, "  | |  _ \ ")',
'color_print(249, 246, 242, 243, 149, 104, "  | | (_) |")',
'color_print(249, 246, 242, 243, 149, 104, "  |_|\___/ ")',
'color_print(249, 246, 242, 243, 149, 104, "")',
'color_print(249, 246, 242, 243, 149, 104, "")',
]

list_32 = [
'color_print(249, 246, 242, 244, 124, 99, "")',
'color_print(249, 246, 242, 244, 124, 99, "")',
'color_print(249, 246, 242, 244, 124, 99, "  ____ ___  ")',
'color_print(249, 246, 242, 244, 124, 99, " |___ \__ \ ")',
'color_print(249, 246, 242, 244, 124, 99, "   __) | ) |")',
'color_print(249, 246, 242, 244, 124, 99, "  |__ < / / ")',
'color_print(249, 246, 242, 244, 124, 99, "  ___) / /_ ")',
'color_print(249, 246, 242, 244, 124, 99, " |____/____|")',
'color_print(249, 246, 242, 244, 124, 99, "")',
'color_print(249, 246, 242, 244, 124, 99, "")',
]

list_64 = [
'color_print(249, 246, 242, 244, 95, 67, "")',
'color_print(249, 246, 242, 244, 95, 67, "")',
'color_print(249, 246, 242, 244, 95, 67, "    __ _  _   ")',
'color_print(249, 246, 242, 244, 95, 67, "   / /| || |  ")',
'color_print(249, 246, 242, 244, 95, 67, "  / /_| || |_ ")',
'color_print(249, 246, 242, 244, 95, 67, " |  _ \__   _|")',
'color_print(249, 246, 242, 244, 95, 67, " | (_) | | |  ")',
'color_print(249, 246, 242, 244, 95, 67, "  \___/  |_|  ")',
'color_print(249, 246, 242, 244, 95, 67, "")',
'color_print(249, 246, 242, 244, 95, 67, "")',
]

list_128 = [
'color_print(249, 246, 242, 236, 206, 120, "")',
'color_print(249, 246, 242, 236, 206, 120, "")',
'color_print(249, 246, 242, 236, 206, 120, "  __ ___   ___  ")',
'color_print(249, 246, 242, 236, 206, 120, " /_ |__ \ / _ \ ")',
'color_print(249, 246, 242, 236, 206, 120, "  | |  ) | (_) |")',
'color_print(249, 246, 242, 236, 206, 120, "  | | / / > _ < ")',
'color_print(249, 246, 242, 236, 206, 120, "  | |/ /_| (_) |")',
'color_print(249, 246, 242, 236, 206, 120, "  |_|____|\___/ ")',
'color_print(249, 246, 242, 236, 206, 120, "")',
'color_print(249, 246, 242, 236, 206, 120, "")',

]

list_256 = [
'color_print(249, 246, 242, 236, 203, 105, "")',
'color_print(249, 246, 242, 236, 203, 105, "")',
'color_print(249, 246, 242, 236, 203, 105, "  ___  _____  ___  ")',
'color_print(249, 246, 242, 236, 203, 105, " |__ \| ____|/ _ \ ")',
'color_print(249, 246, 242, 236, 203, 105, "    ) | |__ | (_) |")',
'color_print(249, 246, 242, 236, 203, 105, "   / /|___ \ > _ < ")',
'color_print(249, 246, 242, 236, 203, 105, "  / /_ ___) | (_) |")',
'color_print(249, 246, 242, 236, 203, 105, " |____|____/ \___/ ")',
'color_print(249, 246, 242, 236, 203, 105, "")',
'color_print(249, 246, 242, 236, 203, 105, "")',
]

list_512 = [
'color_print(249, 246, 242, 233, 198, 88, "")',
'color_print(249, 246, 242, 233, 198, 88, "")',
'color_print(249, 246, 242, 233, 198, 88, "  _____ __ ___  ")',
'color_print(249, 246, 242, 233, 198, 88, " | ____/_ |__ \ ")',
'color_print(249, 246, 242, 233, 198, 88, " | |__  | |  ) |")',
'color_print(249, 246, 242, 233, 198, 88, " |___ \ | | / / ")',
'color_print(249, 246, 242, 233, 198, 88, "  ___) || |/ /_ ")',
'color_print(249, 246, 242, 233, 198, 88, " |____/ |_|____|")',
'color_print(249, 246, 242, 233, 198, 88, "")',
'color_print(249, 246, 242, 233, 198, 88, "")',
]

list_1024 = [
'color_print(249, 246, 242, 234, 195, 76, "")',
'color_print(249, 246, 242, 234, 195, 76, "")',
'color_print(249, 246, 242, 234, 195, 76, "  __  ___ ___  _  _   ")',
'color_print(249, 246, 242, 234, 195, 76, " /_ |/ _ \__ \| || |  ")',
'color_print(249, 246, 242, 234, 195, 76, "  | | | | | ) | || |_ ")',
'color_print(249, 246, 242, 234, 195, 76, "  | | | | |/ /|__   _|")',
'color_print(249, 246, 242, 234, 195, 76, "  | | |_| / /_   | |  ")',
'color_print(249, 246, 242, 234, 195, 76, "  |_|\___/____|  |_|  ")',
'color_print(249, 246, 242, 234, 195, 76, "")',
'color_print(249, 246, 242, 234, 195, 76, "")',
]

list_2048 = [
'color_print(249, 246, 242, 235, 194, 43, "")',
'color_print(249, 246, 242, 235, 194, 43, "")',
'color_print(249, 246, 242, 235, 194, 43, " ___   ___  _  _   ___  ")',
'color_print(249, 246, 242, 235, 194, 43, "|__ \ / _ \| || | / _ \ ")',
'color_print(249, 246, 242, 235, 194, 43, "   ) | | | | || || (_) |")',
'color_print(249, 246, 242, 235, 194, 43, "  / /| | | |__   _> _ < ")',
'color_print(249, 246, 242, 235, 194, 43, " / /_| |_| |  | || (_) |")',
'color_print(249, 246, 242, 235, 194, 43, "|____|\___/   |_| \___/ ")',
'color_print(249, 246, 242, 235, 194, 43, "")',
'color_print(249, 246, 242, 235, 194, 43, "")',
]

def header():
    s = '''        
      .--~*teu.        .n~~%x.             xeee       u+=~~~+u.    
     dF     988Nx    x88X   888.          d888R     z8F      `8N.  
    d888b   `8888>  X888X   8888L        d8888R    d88L       98E  
    ?8888>  98888F X8888X   88888       @ 8888R    98888bu.. .@*   
     "**"  x88888~ 88888X   88888X    .P  8888R    "88888888NNu.   
          d8888*`  88888X   88888X   :F   8888R     "*8888888888i  
        z8**"`   : 88888X   88888f  x"    8888R     .zf""*8888888L 
      :?.....  ..F 48888X   88888  d8eeeee88888eer d8F      ^%888E 
     <""888888888~  ?888X   8888"         8888R    88>        `88~ 
     8:  "888888*    "88X   88*`          8888R    '%N.       d*"  
     ""    "**"`       ^"==="`         "*%%%%%%**~    ^"====="`     '''
    print(colored(('\n'.join(l.center(width) for l in s.splitlines())), 'cyan'), '\n')

def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def color_print(r1, g1, b1, r2, g2, b2, s):
    RESET = '\033[0m'
    print(get_color_escape(r1, g1, b1), get_color_escape(r2, g2, b2, True)
        , s.center(24)
        , RESET, end=' ')

def print_tableBIG():
    heigh = os.get_terminal_size().lines

    for emptylines in range(int(heigh/2) - 22):
        print()

    for rowsInTable in range(4):
        for rowsInASCIINumbers in range(10):
            print(''.rjust(int(width/2 - 57)), end='')
            for numbersInTableRow in range(4):
                if table[rowsInTable][numbersInTableRow] == 0:
                    exec(list_0[rowsInASCIINumbers])
                if table[rowsInTable][numbersInTableRow] == 2:
                    exec(list_2[rowsInASCIINumbers])
                if table[rowsInTable][numbersInTableRow] == 4:
                    exec(list_4[rowsInASCIINumbers])
                if table[rowsInTable][numbersInTableRow] == 8:
                    exec(list_8[rowsInASCIINumbers])
                if table[rowsInTable][numbersInTableRow] == 16:
                    exec(list_16[rowsInASCIINumbers])
                if table[rowsInTable][numbersInTableRow] == 32:
                    exec(list_32[rowsInASCIINumbers])
                if table[rowsInTable][numbersInTableRow] == 64:
                    exec(list_64[rowsInASCIINumbers])
                if table[rowsInTable][numbersInTableRow] == 128:
                    exec(list_128[rowsInASCIINumbers])
                if table[rowsInTable][numbersInTableRow] == 256:
                    exec(list_256[rowsInASCIINumbers])
                if table[rowsInTable][numbersInTableRow] == 512:
                    exec(list_512[rowsInASCIINumbers])
                if table[rowsInTable][numbersInTableRow] == 1024:
                    exec(list_1024[rowsInASCIINumbers])
                if table[rowsInTable][numbersInTableRow] == 2048:
                    exec(list_2048[rowsInASCIINumbers])
            print('')
        print()

def put_in_random_number():
    number=[2,4]
    if 0 in table[0]+table[1]+table[2]+table[3]:
        coordinate1=random.randint(0,3)
        coordinate2=random.randint(0,3)
        if table[coordinate1][coordinate2] == 0:
            table[coordinate1][coordinate2] = random.choice(number)
        else:
            put_in_random_number()

def lose(): #probably this will call a new file with an asci art
    os.system('clear')

    s = '''   
    ▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
    ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
    ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
    ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
    ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
    ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
    ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
    ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
    ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
    ░ ░                           ░                  ░          '''
    print(colored(('\n'.join(l.center(width) for l in s.splitlines())), 'red'), '\n')
    print("1 Main Menu".center(width))
    print("2 Exit".center(width))

    loseOption = 'x'
    loseOption = __call__(loseOption)
    if loseOption == '1':
        menu()
    if loseOption == '2':
        exit()
    else:
        lose()

def win():
    if 2048 in table[0]+table[1]+table[2]+table[3]:
        time.sleep(1.5)
        os.system('clear')
        s = '''
        ██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗     ██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗     ██████╗  ██████╗ ██████╗ ██╗  ██╗    ██╗     ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗
        ██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗    ██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝    ██║     ██║   ██║████╗  ██║██╔════╝██║  ██║
        ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝    ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝    ██████╔╝██║   ██║██████╔╝█████╔╝     ██║     ██║   ██║██╔██╗ ██║██║     ███████║
        ██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗    ██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗    ██╔═══╝ ██║   ██║██╔══██╗██╔═██╗     ██║     ██║   ██║██║╚██╗██║██║     ██╔══██║
        ╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║    ╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║    ██║     ╚██████╔╝██║  ██║██║  ██╗    ███████╗╚██████╔╝██║ ╚████║╚██████╗██║  ██║
        ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝
        '''
        print(colored(('\n'.join(l.center(width) for l in s.splitlines())), 'yellow'), '\n')
        print("1 Main Menu".center(width))
        print("2 Exit".center(width))
        
        winOption = 'x'
        winOption = __call__(winOption)
        if winOption == '1':
            menu()
        if winOption == '2':
            exit()
        else:
            win()

def transpose_table():                                          #have to be symetrical
    global table
    transposedTable = [[],[],[],[]]
    for row in range(4):                                          
        for coloumn in range(4):                                      
            transposedTable[row].append(table[coloumn][row])
    table = transposedTable

def is_lose():              #tries to move to the right, then saves the standing. Resets the table and tries to move to down.
    global table            #If both have the same results, the game is lost.

    temp = deepcopy(table)

    move_right()
    rightTemp = deepcopy(table)

    table = deepcopy(temp) #sets table back to the original position
    move_down()
    downTemp = deepcopy(table)

    table = deepcopy(temp) #sets table back to the original position

    if 0 not in table[0]+table[1]+table[2]+table[3] and rightTemp == downTemp:
        lose()

def move_left():
    for i in range(4):                                          
        virtualRow = []                                         #workingplace
        for x in range(4):                                      
            if table[i][x] != 0:                                 
                virtualRow.append(table[i][x])             
        for y in range(len(virtualRow) - 1):                    # -1 is needed because using virtualRow[y + 1] in next line
            if virtualRow[y] == virtualRow[y + 1]:              
                virtualRow[y] = virtualRow[y] * 2               
                del virtualRow[y + 1]                          
                virtualRow.append(0)                            #len(virtualRow) would give error without this
        if len(virtualRow) != 4:                                #at this point the numbers are merged/shifted
            for z in range(4 - len(virtualRow)):                #the empty spaces are filled up with 0
                virtualRow.append(0)
        table[i] = virtualRow                                   #the original row is assigned to the workingplace

def move_up():
    transpose_table()
    move_left()
    transpose_table()

def move_right():
    for i in range(4):      #every possible move...

            if table[i][0] > 0 and table[i][0] == table[i][1] == table[i][2] == table[i][3]:
                table[i][3] = table[i][3]*2
                table[i][2] = table[i][1]*2
                table[i][1] = 0
                table[i][0] = 0
                return

            if table[i][0] == table[i][1] and table[i][2] == table[i][3]:
                table[i][3] = table[i][3]*2
                table[i][2] = table[i][1]*2
                table[i][1] = 0
                table[i][0] = 0
            
            if table[i][1] is 0 and table[i][2] is 0 and table[i][3] == table[i][0]:
                table[i][3] = table[i][3]*2
                table[i][0] = 0 
            
            if table[i][3] == table[i][2]:
                table[i][3]=table[i][3]*2
                table[i][2] = 0
            elif table[i][2] == table[i][1]:
                table[i][2]=table[i][2]*2
                table[i][1] = 0
            elif table[i][1] == table[i][0]:
                table[i][1]=table[i][1]*2
                table[i][0] = 0
            
            elif table[i][1] is 0 and table[i][2] == table[i][0]:
                table[i][2] = table[i][2]*2
                table[i][0] = 0
            elif table[i][2] is 0 and table[i][3] == table[i][1]:
                table[i][3] = table[i][3]*2
                table[i][1] = 0        

            if table[i][1] is 0:
                table[i][1] = table[i][0]
                table[i][0] = 0
            
            if table[i][2] is 0:
                table[i][2] = table[i][1]
                table[i][1] = table[i][0]
                table[i][0] = 0

            if table[i][3] is 0:
                table[i][3] = table[i][2]
                table[i][2] = table[i][1]
                table[i][1] = table[i][0]
                table[i][0] = 0

def move_down():
    transpose_table()
    move_right()
    transpose_table()

def __call__(self): #read keystroke without hitting enter
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./80)

def slowprintX(s):
    spacing = ''
    for i in range(int(width/2 - len(s)/2)):
        spacing = spacing + ' '
    for c in spacing:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./1000)
    for f in s + '\n':
        sys.stdout.write(f)
        sys.stdout.flush()
        time.sleep(1./1)

def game():
    temp = deepcopy(table)
    os.system('clear')
    print_tableBIG()

    ASDW = 1
    ASDW = __call__(ASDW)
    if ASDW == 'a':
        move_left()
        ASDW = 1
    if ASDW == 's':
        move_down()
        ASDW = 1
    if ASDW == 'd':
        move_right()
        ASDW = 1
    if ASDW == 'w':
        move_up()
        ASDW = 1
    if ASDW == 'x':
        ASDW = 1
        exit()
    if ASDW == 'p':
        ASDW = 1
        save_game()
        exit()

    if temp == table:
        os.system('clear')
        print_tableBIG()
        game()

    os.system('clear')
    put_in_random_number()
    print_tableBIG()
    win()
    is_lose()
    game()

def menu():

    global table                    
    
    table = [                           #this new table reference is neccessary when the menu is accessed from game()
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
    put_in_random_number()
    put_in_random_number()

    os.system('clear')
    header()
    print("1. New Game".center(width))
    print("2. Load Game".center(width))
    print("3. Rules".center(width))
    print("4. Credits".center(width))
    print("5. Exit Game".center(width))
    print("\n")
    choice = print("Choose an option!".center(width))

    menuOption = 'x'
    menuOption = __call__(menuOption)
    if menuOption == '1':
        game()
        menuOption = 'x'
    if menuOption == '2':
        load_game()
        menuOption = 'x'
    if menuOption == '3':
        rules()
        menuOption = 'x'
    if menuOption == '4':
        credits()
        menuOption = 'x'
    if menuOption == '5':
        exit()

def rules():
    os.system('clear')
    print("Use your W, A, S and D keys to move the tiles. When two tiles with the same number touch, they merge into one!".center(width))
    print("During game press P to save and quit, or X to quit without saving.".center(width))
    print("Try to get to 2048!".center(width))
    print("Press 1 to go back to the Main Menu.".center(width))

    menuOption = 'x'
    menuOption = __call__(menuOption)
    if menuOption == '1':
        menu()

def credits():
    os.system('clear')

    s = '''        
    ██████╗  ██████╗ ██╗  ██╗ █████╗ 
    ╚════██╗██╔═████╗██║  ██║██╔══██╗
    █████╔╝██║██╔██║███████║╚█████╔╝
    ██╔═══╝ ████╔╝██║╚════██║██╔══██╗
    ███████╗╚██████╔╝     ██║╚█████╔╝
    ╚══════╝ ╚═════╝      ╚═╝ ╚════╝ '''
    print(colored (('\n'.join(l.center(width) for l in s.splitlines())), 'green'), '\n')

    time.sleep(1.5)
    slowprint("Directed by: Michael Bay".center(width))
    slowprint("Music: Hans Zimmer".center(width))
    print()
    slowprint("STARRING:".center(width))
    print()
    slowprint("Christian Bale - 2048".center(width))
    slowprint("Helen Mirren - 1024".center(width))
    slowprint("Lupita Nyong'o - 512".center(width))
    slowprint("Steven Seagal - 256".center(width))
    slowprint("Scarlett Johansson - 128".center(width))
    slowprint("Jack Nicholson - 64".center(width))
    slowprint("Kevin Costner - 32".center(width))
    slowprint("David Hasselhoff - 16".center(width))
    slowprint("Andy Serkis - 8 (motion capture)".center(width))
    slowprint("Emma Stone - 4".center(width))
    print()
    slowprint("WITH".center(width))
    print()
    time.sleep(1)
    slowprint("Samuel L Jackson as 2".center(width))
    time.sleep(3)
    os.system('clear')
    print('\n\n\n')
    slowprintX("....")
    slowprint("Incoming transmission".center(width))
    time.sleep(1)
    slowprint("Decoding".center(width))
    slowprintX("....")
    os.system('clear')
    time.sleep(1)
    slowprint(colored ('''██╗  ██╗ ██████╗  █████╗  ██████╗ ''', 'green').center(width))
    slowprint(colored ('''██║  ██║██╔═████╗██╔══██╗██╔════╝ ''', 'green').center(width))
    slowprint(colored ('''███████║██║██╔██║╚██████║███████╗ ''', 'green').center(width))
    slowprint(colored ('''╚════██║████╔╝██║ ╚═══██║██╔═══██╗''', 'green').center(width))
    slowprint(colored ('''     ██║╚██████╔╝ █████╔╝╚██████╔╝''', 'green').center(width))
    slowprint(colored ('''     ╚═╝ ╚═════╝  ╚════╝  ╚═════╝ ''', 'green').center(width))
    print()
    print("The numbers will return...".center(width))
    time.sleep(3)
    menu()

def save_game():
    global table
       
    with open("saved_game.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(table)

def load_game():
    global table

    with open("saved_game.csv", "r") as f:
        reader = csv.reader(f)
        temp=[]
        for row in reader:
            temp.append([int(val) for val in row])
    
    table = temp
    game()

table = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]

#____________________________________________________________________________________________________
os.system('clear')

print_tableBIG()

menu()