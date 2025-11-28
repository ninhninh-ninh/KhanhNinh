from collections import deque


def print_map(grid):
    print("Bản đồ địa hình:")
    for row in grid:
        print(" ".join(map(str, row)))
    print()


def bfs_find_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    visited = [[False] * cols for _ in range(rows)]

    parent = [[None] * cols for _ in range(rows)]

    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()

        if (x, y) == end:
            break

  
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
            
                if grid[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    parent[nx][ny] = (x, y)  
                    q.append((nx, ny))


    path = []
    step = end

    if not visited[end[0]][end[1]]:
        return None  

    while step:
        path.append(step)
        step = parent[step[0]][step[1]]

    path.reverse()
    return path


if __name__ == "__main__":
 
    grid = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]

    print_map(grid)

    start = (0, 0)   
    end = (4, 4)     

    print(f"Điểm bắt đầu: {start}")
    print(f"Điểm kết thúc: {end}\n")

    path = bfs_find_path(grid, start, end)

    if path:
        print("Đường đi ngắn nhất tìm được bằng BFS:")
        print(path)
        print(f"\nSố bước đi: {len(path)-1}")
    else:
        print("Không tìm được đường đi!")
