import importer
input = importer.parseInput()

solution = 0
first = last = 0
    
for line in input:
    for f in line:
        if f.isdigit():
            first = int(f)
            break
    for l in line[::-1]:
        if l.isdigit():
            last = int(l)
            break
    solution = solution + first * 10 + last

print(solution)