def find_path(maze, y, x, path):
    if y < 0 or y >= len(maze) or x < 0 or x >= len(maze[0]) or maze[y][x] == '#':
        return False
    
    if maze[y][x] == 'E':
        path.append((y, x))
        return True
    
    if maze[y][x] == '*':
        return False
    
    if maze[y][x] != 'S':
        maze[y][x] = '*'
    path.append((y, x))

    if (find_path(maze, y+1, x, path) or
        find_path(maze, y-1, x, path) or
        find_path(maze, y, x+1, path) or
        find_path(maze, y, x-1, path)):
        return True

    path.pop()
    if maze[y][x] != 'S':
        maze[y][x] = '.'
    return False

def calc_maze(maze):
    start_x = start_y = None
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 'S':
                start_x, start_y = x, y
                break
        if start_x is not None:
            break

    path = []
    if find_path(maze, start_x, start_y, path):
        print("Solution found:")
        for row in maze:
            print(''.join(row))
    else:
        print("No solution found")

print("Enter the entire maze in one line. Use '.' for open cells, '#' for walls, 'S' for start, and 'E' for end.")
print("Separate each row with a comma (,).")

input_maze = input("Enter the maze: ")
maze = [list(row) for row in input_maze.split(',')]

print("Your maze:")

for row in maze:
    print(''.join(row))

calc_maze(maze)