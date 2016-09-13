import sys
import os

def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

os.system('clear')
print_there(5,5,'@')
raw_input()
