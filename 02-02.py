idSum = 0
while True:
    inputval = input()
    if not inputval:
        break
    game_num, games = inputval.split(":")
    game_id = int(game_num.split(" ")[1])
    redCube = 0
    greenCube = 0
    blueCube = 0
    for one_game in games.split(";"):
        for cubes in one_game.split(","):
            cube_num, cube_color = cubes.strip().split(" ")
            cube_num = int(cube_num)
            if cube_color == "red":
                redCube = max(cube_num, redCube)
            elif cube_color == "green":
                greenCube = max(cube_num, greenCube)
            elif cube_color == "blue":
                blueCube = max(cube_num, blueCube)
    idSum += redCube * greenCube * blueCube
print(idSum)
