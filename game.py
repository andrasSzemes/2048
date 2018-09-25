import random
import os #kell a kepernyo torleshez
from copy import deepcopy #kell a táblázatmásoláshoz
from termcolor import colored

def header(): #header lett a 2048-ból, hogy mindig ottmaradjon a tábla fölött képtörlés esetén is
    width = os.get_terminal_size().columns #középre igazításhoz megállapítja a terminál szélességét
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

def formatted_table(table): #meghatározza a tábla formátumát
    width = os.get_terminal_size().columns #középre igazításhoz megállapítja a terminál szélességét
    formatted = u'{:^4} {:^4} {:^4} {:^4}'.format(table[0], table[1], table[2], table[3])
    print(str(formatted).center(width))

def print_table():
    for i in range(4):
        formatted_table(table[i])

def print_tableBIG():
    

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
    import lose

def win():
    if 2048 in table[0]+table[1]+table[2]+table[3]:
        import win

def transpose_table():                                          #have to be symetrical
    global table
    transposedTable = [[],[],[],[]]
    for i in range(4):                                          #transzponaltban az egyes sorok
        for x in range(4):                                      #tablaban egyes elemek adott oszlopban
            transposedTable[i].append(table[x][i])
    table = transposedTable

def is_lose(): #elmozdíjta az aktuális állást jobbra, visszaállítja és elmozdítja le. Ha a kettő egyezik, és nincs bennük 0, az állás nem megnyerhető.
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
    for j in range(4):

            if table[1][j] is 0 and table[2][j] is 0 and table[3][j] == table[0][j]:
                table[3][j] = table[3][j]*2
                table[0][j] = 0 

            if table[3][j] == table[2][j]:
                table[3][j]=table[3][j]*2
                table[2][j] = 0
            elif table[2][j] == table[1][j]:
                table[2][j]=table[2][j]*2
                table[1][j] = 0
            elif table[1][j] == table[0][j]:
                table[1][j]=table[1][j]*2
                table[0][j] = 0

            elif table[1][j] is 0 and table[2][j] == table[0][j]:
                table[2][j] = table[2][j]*2
                table[0][j] = 0
            elif table[1][j] is 0 and table[3][j] == table[0][j]:
                table[3][j] = table[3][j]*2
                table[0][j] = 0
            elif table[2][j] is 0 and table[3][j] == table[1][j]:
                table[3][j] = table[3][j]*2
                table[1][j] = 0

            if table[1][j] is 0:
                table[1][j] = table[0][j]
                table[0][j] = 0

            if table[2][j] is 0:
                table[2][j] = table[1][j]
                table[1][j] = table[0][j]
                table[0][j] = 0

            if table[3][j] is 0:
                table[3][j] = table[2][j]
                table[2][j] = table[1][j]
                table[1][j] = table[0][j]
                table[0][j] = 0

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
        header()
        print_table()
        print_tableBIG()
        game()

    os.system('clear')
    put_in_random_number()
    header()
    print_table()
    print_tableBIG()
    win()
    is_lose()
    game()

table = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
put_in_random_number()
put_in_random_number()

#____________________________________________________________________________________________________
os.system('clear') #képernyő törlése

header()
print_table()
print_tableBIG()

game()