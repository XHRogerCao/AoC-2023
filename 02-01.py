idSum = 0
redCube = 12
greenCube = 13
blueCube = 14
while True:
    inputval = input()
    if not inputval:
        break
    game_num, games = inputval.split(":")
    game_id = int(game_num.split(" ")[1])
    valid_game = True
    for one_game in games.split(";"):
        for cubes in one_game.split(","):
            cube_num, cube_color = cubes.strip().split(" ")
            cube_num = int(cube_num)
            if cube_color == "red" and cube_num > redCube:
                valid_game = False
            elif cube_color == "green" and cube_num > greenCube:
                valid_game = False
            elif cube_color == "blue" and cube_num > blueCube:
                valid_game = False
        if not valid_game:
            break
    if valid_game:
        idSum += game_id
print(idSum)
