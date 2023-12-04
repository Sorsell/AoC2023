def part1(game,control):
    game = game.split(":")
    id = int(game[0].split(" ")[1])
    sets = game[1].split(";")
    for set in sets:
        parts = set.split(",")
        for part in parts:
            cube = part.strip().split(" ")
            value = int(cube[0])
            color = cube[1]
            if value > control[color]:
                return 0
    return id

def part2(game):
    min = {"red": 0, "green": 0, "blue": 0}
    game = game.split(":")
    id = int(game[0].split(" ")[1])
    sets = game[1].split(";")
    for set in sets:
        parts = set.split(",")
        for part in parts:
            cube = part.strip().split(" ")
            value = int(cube[0])
            color = cube[1]
            if value > min[color]:
                min[color] = value
    sum = min["red"] * min["green"] * min["blue"]
    return sum
                
                
with open('day02\day02Input.txt') as f:
    lines = f.readlines()

control = {"red": 12, "green": 13, "blue": 14}
value = 0
for game in lines:
    value += part1(game,control)
print(value)

sum = 0
for game in lines:
    sum += part2(game)
print(sum)

