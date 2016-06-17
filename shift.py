import re

def shift(input, x, y):
    # https://docs.python.org/2/library/re.html#re.sub
    input = re.sub('X([^\s]+)', lambda o: 'X' + str(float(o.group(1)) + x), input)
    input = re.sub('Y([^\s]+)', lambda o: 'Y' + str(float(o.group(1)) + y), input)
    return input

# run as script
if __name__ == '__main__':
    with open('test/small.gcode', 'r') as inFile, open('out.gcode', 'w') as outFile:
        input = inFile.read()
        output = shift(input, 5.3, 4.87)
        outFile.write(output)