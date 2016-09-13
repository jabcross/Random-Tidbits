# Pedro Ciambra
# pedrociambra@gmail.com
#
# Random Tidbit #1
# Maze generator
#
# usage:
#
# maze1.py [-animate] [-freq <number>] [x [y]]
# -animate: animates creation of maze
# -freq number: changes speed of animation in hertz
# x, y : dimensions of maze. if only x is inserted,
# creates square maze of size x.

import sys
import random
import time
import os

args = sys.argv[1:]

if "-animate" in args:
    animate = 1
    args.remove("-animate")
else:
    animate = 0

if "-freq" in args:
    i = args.index("-freq")
    freq = int(args[i+1])
    del args[i + 1]
    del args[i]
else:
    freq = 10
    
if len(args) == 1:
    w = h = int(args[0])
elif len(args) == 2:
    w, h = [int(i) for i in args[0:2]]
else:
    w, h = 10 , 10



    
walls = [[[1,1] for x in range(w)] for y in range(h)] # represents right and down directions.
cells = [[0 for x in range(w)] for y in range(h)]
dirs = [[[] for x in range(w)] for y in range(h)];
begin = [random.randint(0,x) for x in (w-1,h-1)] 

for j in range(h):
    for i in range(w):
        dirs[j][i] = [0,1,2,3]
        random.shuffle(dirs[j][i])

def print_there(y, x, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()
        
def breakWall(x,y,d):
    a,b = x*2 + 2,y*2 + 2
    if d == 0: #right
        walls[y][x][0] = 0
        a += 1
        r = (x+1,y)
    elif d == 1: #up
        walls[y - 1][x][1] = 0
        b -= 1
        r = (x,y-1)
    elif d == 2: #left
        walls[y][x-1][0] = 0
        a -= 1
        r = (x-1,y)
    elif d == 3: #down
        walls[y][x][1] = 0
        b += 1
        r = (x,y+1)
    if animate == 1:
        print_there(a,b,' ')
    return r

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

stack = []
            
def iter():
    stack.append(tuple(begin))
    if animate == 1:
        os.system('clear')
        printMaze()
    while len(stack) > 0:
        cont = 0
        x,y = stack[-1]
        cells[y][x] = 1
        for i in dirs[y][x]:
            if (probe(x,y,i))== 0:
                if animate == 1:
                    time.sleep(1/float(freq))
                stack.append(breakWall(x,y,i))
                cont = 1
                break
        if cont == 1:
            continue
        stack.pop()
                

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


iter()

if animate == 0:
    printMaze()
