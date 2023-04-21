def mine_sweeper(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [['_' for _ in range(cols)] for _ in range(rows)]


    print("Lets play minesweeper!")

    while True:
        print("Current board:")
        for row in result:
            print(" ".join(row))
        print("Enter the coordinates of a cell to reveal(row, cols):")
        try:
            row, col = map(int, input().split())
        except ValueError:
            print("Invalid input.")
            continue
        if not (0 <= row < rows and 0 <= col < cols):
            print("Invalid coordinated make sure its on the board")
            continue
        if grid[row][col] == '#':
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] =='#':
                        result[i][j] = '#'
            print("Game over! You hit a mine")
            break
        else:
            count = 0
            for x, y in [(row-1, col- 1), (row-1, col),(row-1, col+1), (row, col-1),(row, col+1), (row+1, col-1),(row+1, col), (row+1, col+1)]:
                try:
                    if x >= 0 and y >= 0 and grid[x][y] == '#':
                        count += 1
                except IndexError:
                    pass
            result[row][col] = str(count)
            if all(result[i][j] != '_' for i in range(rows) for j in range(cols)):
                print("Congratulations you won!")
                break

    return result


grid = [["-", "-", "-", "#", "-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "#", "-", "-", "-", "-"],
        ["-", "#", "-", "-", "-", "-", "-", "-", "#"],
        ["-", "-", "-", "-", "#", "-", "-", "-", "-"],
        ["-", "-", "#", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        ]
result = mine_sweeper(grid)










           