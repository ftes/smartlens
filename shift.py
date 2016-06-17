# python shift.py <inputFile> <outputFile> <x-offset-1> <y-offset-1> ... <x-offset-n> <y-offset-n>

import re
import sys


def shift(data, x, y):
    # https://docs.python.org/2/library/re.html#re.sub
    data = re.sub('X([^\s]+)', lambda o: 'X' + str(float(o.group(1)) + x), data)
    data = re.sub('Y([^\s]+)', lambda o: 'Y' + str(float(o.group(1)) + y), data)
    return data


def shift_multiple(data, *args, callback=lambda c: print(c)):
    x_offsets = args[0::2] # every other (starting at 0)
    y_offsets = args[1::2] # every odd other (starting at 1)
    for x_offset, y_offset in zip(x_offsets, y_offsets):
        copy = shift(data, x_offset, y_offset)
        callback(copy)


# run as script
if __name__ == '__main__':
    inFileName = sys.argv[1]
    outFileName = sys.argv[2]
    offsets = map(lambda i: float(i), sys.argv[3:])

    # 'r' for read, 'a' for append
    with open(inFileName, 'r') as inFile, open(outFileName, 'a') as outFile:
        original = inFile.read()
        shift_multiple(original, callback=lambda c: outFile.write(c), *offsets)

#data = """G1 Z0.200 F7200.000
#G1 X75.572 Y93.157 F7200.000
#"""
#shift_multiple(data, 0, 0, 1, 1, 4.5, 4.5) # <x-offset-1> <y-offset-1> ... <x-offset-n> <y-offset-n>