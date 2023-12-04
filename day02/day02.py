def part1(game):
    control = {"red": 12, "green": 13, "blue": 14}
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

                
                
with open('day02\day02Input.txt') as f:
    lines = f.readlines()

value = 0
for game in lines:
    value += part1(game)
print(value)
