def part1(line):
    for i in range(len(line)):
        if line[i].isdigit():
            value = line[i]
            for i in reversed(range(len(line))):
                if line[i].isdigit():
                    value = value + line[i]
                    return int(value)
                

with open('day1Input.txt') as f:
    lines = f.readlines()
value = 0
for line in lines:
    value += part1(line)
print(value)

