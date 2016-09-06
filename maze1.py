import random

w, h = 70 , 20
walls = [[[1,1] for x in range(w)] for y in range(h)] # represents right and down directions.
cells = [[0 for x in range(w)] for y in range(h)]
dirs = [[[] for x in range(w)] for y in range(h)];

for j in range(h):
    for i in range(w):
        dirs[j][i] = [0,1,2,3]
        random.shuffle(dirs[j][i])

def breakWall(x,y,d):
    if d == 0: #right
        walls[y][x][0] = 0
        return (x+1,y)
    elif d == 1: #up
        walls[y - 1][x][1] = 0
        return (x,y-1)
    elif d == 2: #left
        walls[y][x-1][0] = 0
        return (x-1,y)
    elif d == 3: #down
        walls[y][x][1] = 0
        return (x,y+1)

def probe(x,y,d):
    if d == 0: # right
        if (x == w - 1) or (cells[y][x+1] == 1):
            return 1
    elif d == 1: #up
        if (y == 0) or (cells[y-1][x] == 1):
            return 1
    elif d == 2: #left
        if (x == 0) or (cells[y][x-1] == 1):
            return 1
    elif d == 3: #down
        if (y == h - 1) or (cells[y + 1][x] == 1):
            return 1
    return 0

def iterate(x,y):
    cells[y][x] = 1
    for i in dirs[y][x]:
        if (probe(x,y,i) == 0):
            a, b = breakWall(x,y,i)
            iterate(a, b)

def printMaze():
    print "#"*(w*2+1)
    for j in range(h):
        a = "#"
        b = "#"
        for i in range(w):
            a += " "
            if (walls[j][i][0] == 1):
                a += "#"
            else:
                a += " "
            if (walls[j][i][1] == 1):
                b += "##"
            else:
                b += " #"
        print a
        print b


iterate(0,0)

printMaze()
