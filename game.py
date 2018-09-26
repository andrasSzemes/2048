import random
import sys
import time
import os #needed to clear screen
from copy import deepcopy #needed for table copy
from termcolor import colored

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

def header(): #2048 set as header so that it can be diplayed even if the screen is cleared
    width = os.get_terminal_size().columns #gets the width of the terminal size, so that displayed parts can be centered
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

def formatted_table(table): #sets the format of the table
    width = os.get_terminal_size().columns #gets the width of the terminal size, so that displayed parts can be centered
    formatted = u'{:^4} {:^4} {:^4} {:^4}'.format(table[0], table[1], table[2], table[3])
    print(str(formatted).center(width))

def print_table():
    for i in range(4):
        formatted_table(table[i])

def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def color_print(r1, g1, b1, r2, g2, b2, s):
    RESET = '\033[0m'
    print(get_color_escape(r1, g1, b1), get_color_escape(r2, g2, b2, True)
        , s.center(24)
        , RESET, end=' ')

def print_tableBIG():
    width = os.get_terminal_size().columns
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
        random1=random.randint(0,3)
        random2=random.randint(0,3)
        if table[random1][random2] == 0:
            table[random1][random2] = random.choice(number)
        else:
            put_in_random_number()

def lose(): #probably this will call a new file with an asci art
    os.system('clear')
    width = os.get_terminal_size().columns

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

    loseOption = 1
    loseOption = __call__(loseOption)
    if loseOption == '1':
        menu()
    if loseOption == '2':
        exit()

def win():
    if 2048 in table[0]+table[1]+table[2]+table[3]:
        time.sleep(1.5)
        os.system('clear')
        width = os.get_terminal_size().columns
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
        
        winOption = 1
        winOption = __call__(winOption)
        if winOption == '1':
            menu()
        if winOption == '2':
            exit()

def transpose_table():                                          #have to be symetrical
    global table
    transposedTable = [[],[],[],[]]
    for i in range(4):                                          #transzponaltban az egyes sorok
        for x in range(4):                                      #tablaban egyes elemek adott oszlopban
            transposedTable[i].append(table[x][i])
    table = transposedTable

def transpose_down():
    global table
    downTable = [[],[],[],[]]
    for i in range(4):
        for j in range(4):
            downTable[i].append(table[j][i])
    table=downTable

def is_lose(): #tries to move to the right, then saves the standing. Resets the table and tries to move to down. If both have the same results, the game is lost.
    global table

    temp=deepcopy(table) #table bekerül a tempbe

    move_right()
    rt=deepcopy(table)

    table=deepcopy(temp) #visszaállítom a table-t az elmozdítás előtti (eredeti) pozícióba
    move_down()
    dt=deepcopy(table)

    table=deepcopy(temp) #visszállítom a table-t, hogy a következő lépés már a játékos előző állásából történjen

    if 0 not in table[0]+table[1]+table[2]+table[3] and rt == dt: #ha nincs a táblában 0 és minden elmozdítás után ugyanazt adja vissza
        lose()

def move_left():
    for i in range(4):                                          #sorok sorszama
        virtualRow = []                                         #workingplace
        for x in range(4):                                      #szamok sorszama
            if table[i][x] != 0:                                #vegig megy a szamokon, ha nem 0 a workingplace-hez adja 
                virtualRow.append(table[i][x])             
        for y in range(len(virtualRow) - 1):                    #vegig megy a szamokon workingplace-ben
            if virtualRow[y] == virtualRow[y + 1]:              #jobbra levo elemmel megegyezik akkor
                virtualRow[y] = virtualRow[y] * 2               #ketszerese lesz
                del virtualRow[y + 1]                           #mellette levo elem kitorlodik!!!
                virtualRow.append(0)                            #len miatt egy 0-at rak a sor vegere
        if len(virtualRow) != 4:                                #ha rovidebb a workplace
            for z in range(4 - len(virtualRow)):                #amennyivel rovidebb annyi 0-at rak hozza
                virtualRow.append(0)
        table[i] = virtualRow                                   #kezdeti sort megfelelteti workingplace-nek

def move_up():
    transpose_table()
    move_left()
    transpose_table()

def move_right():
    for i in range(4):

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
            elif table[i][1] is 0 and table[i][3] == table[i][0]:
                table[i][3] = table[i][3]*2
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
    transpose_down()
    move_right()
    transpose_down()

def __call__(self):
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
    #spaces = 
    for i in range(int(width/2 - len(s)/2)):
        spacing = spacing + ' '
    for c in spacing:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./1000)
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./1)

def game():
    doesItChange = deepcopy(table)

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

    if doesItChange == table:
        os.system('clear')
        #header()
        #print_table()
        print_tableBIG()
        game()

    os.system('clear')
    put_in_random_number()
    #header()
    #print_table()
    print_tableBIG()
    win()
    is_lose()
    game()

def menu():

    global table
    
    table = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
    put_in_random_number()
    put_in_random_number()

    os.system('clear')
    width = os.get_terminal_size().columns
    header()
    print("1. New Game".center(width))
    print("2. Rules".center(width))
    print("3. Credits".center(width))
    print("4. Exit Game".center(width))
    print("\n")
    choice = print("Choose an option!".center(width))

    menuOption = 1
    menuOption = __call__(menuOption)
    if menuOption == '1':
        game()
        menuOption = 1
    if menuOption == '2':
        rules()
        menuOption = 1
    if menuOption == '3':
        credits()
        menuOption = 1
    if menuOption == '4':
        exit()

def rules():
    os.system('clear')
    width = os.get_terminal_size().columns
    print("Use your W, A, S and D keys to move the tiles. When two tiles with the same number touch, they merge into one!".center(width))
    print("Try to get to 2048!".center(width))
    print("Press 1 to go back to the Main Menu.".center(width))

    menuOption = 1
    menuOption = __call__(menuOption)
    if menuOption == '1':
        menu()

def credits():
    width = os.get_terminal_size().columns

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
    #os.system('clear')
    slowprint("Directed by: Michael Bay".center(width))
    slowprint("Music: Hans Zimmer".center(width))
    print()
    slowprint("STARRING:".center(width))
    #os.system('clear')
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
    #os.system('clear')
    print()
    slowprint("WITH".center(width))
    print()
    time.sleep(1)
    #os.system('clear')
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

table = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
put_in_random_number()
put_in_random_number()

#____________________________________________________________________________________________________
os.system('clear') #clear screen

#header()
#print_table()
print_tableBIG()

menu()