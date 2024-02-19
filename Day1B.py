import importer
input = importer.parseInput(0)
from word2number import w2n

solution = 0
first = last = 0

def getfirstdigit(line: str):
    global first
    for i in range(0,len(line)+1):
        try:
            first = w2n.word_to_num(line[0:i])
            if first < 10:
                return(first)
        except ValueError:
            continue
    return getfirstdigit(line[1:])

def getlastdigit(line: str):
    global last
    for i in range(len(line),-1,-1):
        try:
            last = w2n.word_to_num(line[i::])
            if last < 10:
                return(last)
        except ValueError:
            continue
    return getlastdigit(line[:-1])


for line in input:
    first = getfirstdigit(line)
    last = getlastdigit(line)
    solution = solution + first * 10 + last

print(solution)