import sys
import time

name = sys.argv[1]

def  printToScreen(strng):
    for character in strng:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)


with open(name, 'r') as f:
    file = f.read()
    printToScreen(file)
