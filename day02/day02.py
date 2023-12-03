def part1(line):
    line = line.split(":")
    parts = line[1].split(";")
    print(parts)
    for part in parts:
        parts2 = part.split(",")
        print(parts2)
                
with open('day02\day02Input.txt') as f:
    lines = f.readlines()

value = 0
for line in lines:
    value += part1(line)
print(value)
