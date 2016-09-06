# Random Mountain Generator.
# inputs: width, height, horizontal and vertical variation parameters, depth of recursion.
# by Pedro Ciambra

from __future__ import print_function
import random

w, h = 110,20

mountain = [0 for i in range(w)]

# choose heights for peak, left and right

# horizontal and vertical variation. the smaller the number, the most variation. minimum is 1
# bigger numbers tend to form triangles.

hvar, vvar = 2, 5

# number of iterations. bigger numbers mean more chaotic mountains.

iterations = 10

def getMiddlePoint(a, b, var):
    variationRange = abs(a - b) / var
    base = (a + b - variationRange) / 2
    middle = base + random.uniform(0,variationRange)
    return int(round(middle))

mountain[0] = 0
mountain[-1] = 0
middlePoint = 0

if w > 5:
    middlePoint = getMiddlePoint(0,w-1,hvar)
else:
    middlePoint = int(round((w-1)/2))

mountain[middlePoint] = h-1
    
def iterateRange(l,r,hv,vv,n, m):
    if r <= l + 1:
        return
    elif r == l + 2:
        m[l+1] = int(round((m[l] + m[r])/2))
    else:
        if n == 0:
            numberOfSteps = abs(r - l)
            totalHeight = m[r] - m[l]
            stepHeight = totalHeight / numberOfSteps
            for i in range(1,numberOfSteps):
                m[l+i] = int(round(m[l] + i * stepHeight))
        else:
            midpoint = getMiddlePoint(l,r,hv)
            m[midpoint] = getMiddlePoint(m[l],m[r],vv)
            iterateRange(l,midpoint,hv,vv,n-1,m)
            iterateRange(midpoint,r,hv,vv,n-1,m)


iterateRange(0,middlePoint,hvar,vvar,iterations,mountain)
iterateRange(middlePoint,w-1,hvar,vvar,iterations,mountain)

def printMountain(h,w,m):
    for j in range(h):
        for i in range(w):
            print(' ' if (h-j > m[i]) else '#',end='')
        print('')
                
printMountain(h,w,mountain)
        
print(mountain)


