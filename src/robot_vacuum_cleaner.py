from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Clean a room using a robot vacuum cleaner algorithm.
    
    Args:
    - grid (List[List[int]]): 2D grid representing the room layout
        0 represents an empty cell that can be cleaned
        1 represents an obstacle that cannot be cleaned
    - r (int): Starting row of the robot
    - c (int): Starting column of the robot
    - direction (int): Initial direction of the robot (0: North, 1: East, 2: South, 3: West)
    
    Returns:
    - int: Minimum number of steps required to clean the entire room, or -1 if impossible
    
    Raises:
    - ValueError: If the input grid is invalid or starting position is out of bounds
    """
    # Input validation
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        raise ValueError("Starting position is out of bounds")
    
    # Check if starting position is an obstacle
    if grid[r][c] == 1:
        raise ValueError("Starting position is an obstacle")
    
    # Directions: North, East, South, West
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Track total empty cells
    total_empty_cells = sum(row.count(0) for row in grid)
    
    # Special case for single-cell room
    if total_empty_cells == 1 and grid[r][c] == 0:
        return 0
    
    # If no empty cells, return -1
    if total_empty_cells == 0:
        return -1
    
    def is_connected_empty_cells() -> bool:
        """Check if empty cells form a connected component"""
        def dfs(x: int, y: int, visited: set) -> None:
            if (x, y) in visited or x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 1:
                return
            
            visited.add((x, y))
            
            for dx, dy in directions:
                dfs(x + dx, y + dy, visited)
        
        # Find first empty cell
        start = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    start = (i, j)
                    break
            if start:
                break
        
        if not start:
            return False
        
        visited = set()
        dfs(start[0], start[1], visited)
        
        return len(visited) == total_empty_cells
    
    # If empty cells are not connected, return -1
    if not is_connected_empty_cells():
        return -1
    
    def dfs(x: int, y: int, current_dir: int, steps: int, visited: set) -> int:
        """Depth-first search to clean the room"""
        # Mark current cell as visited if it's empty
        if grid[x][y] == 0:
            visited.add((x, y))
        
        # If all empty cells are cleaned, return steps
        if len(visited) == total_empty_cells:
            return steps
        
        # Try all 4 directions
        min_steps = float('inf')
        for i in range(4):
            # Calculate new direction and position
            new_dir = (current_dir + i) % 4
            dx, dy = directions[new_dir]
            new_x, new_y = x + dx, y + dy
            
            # Check if move is valid and not already visited
            if (0 <= new_x < len(grid) and 
                0 <= new_y < len(grid[0]) and 
                grid[new_x][new_y] == 0 and 
                (new_x, new_y) not in visited):
                # Recursively explore this path
                result = dfs(new_x, new_y, new_dir, steps + 1, visited.copy())
                min_steps = min(min_steps, result)
        
        return min_steps
    
    # Start cleaning from the initial position
    result = dfs(r, c, direction, 0, set())
    
    # If not all cells could be cleaned or no path found
    return result if result != float('inf') else -1