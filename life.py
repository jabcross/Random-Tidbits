from __future__ import print_function

w = 10
h = 10

m = [[0 for i in range(w)] for j in range(h)]
n = [[0 for i in range(w)] for j in range(h)]

c = [[0 for i in range(w)] for j in range(h)]

f = 0

def getDot((x, y)):
    return m[y][x]

def setDot(x,y,k):
    m[y][x] = k

conv = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

def convolution():
    for j in range(h):
        for i in range(w):
            k = 0;
            for n in conv:
                x = (i + n[0] + w) % w
                y = (j + n[1] + h) % h
                k += m[y][x]
            c[j][i] = k

def iteration():
    convolution()
    global m, n
    for j in range(h):
        for i in range(w):
            n[j][i] = 0
            if m[j][i] == 1 and c[j][i] > 1 and c[j][i] < 4:
                n[j][i] = 1
            elif m[j][i] == 0 and c[j][i] == 3:
                n[j][i] = 1
    t = m
    m = n
    n = t
    printMatrix()

def printMatrix():
    print(' ' + "_" * w)
    for j in range(h):
        print('|',end='')
        for i in range(w):
            if m[j][i] == 1:
                print("#", end='')
            else:
                print(" ", end='')
        print('|')
    print("+" + "-" * w + "+")

m[1][2] = 1
m[2][3] = 1
m[3][1] = 1
m[3][2] = 1
m[3][3] = 1

while(True):
    l = raw_input()
    iteration()

