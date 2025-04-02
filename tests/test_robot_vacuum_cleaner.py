import pytest
from src.robot_vacuum_cleaner import cleanRoom

def test_basic_room_cleaning():
    """Test cleaning a simple room with no obstacles"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Different starting positions and directions
    test_cases = [
        (0, 0, 0),  # Top-left, facing North
        (1, 1, 1),  # Middle, facing East
        (2, 2, 2),  # Bottom-right, facing South
    ]
    
    for r, c, direction in test_cases:
        result = cleanRoom(grid, r, c, direction)
        assert result == 8, f"Failed for start ({r},{c}) dir {direction}"

def test_room_with_obstacles():
    """Test cleaning a room with obstacles"""
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    
    # Test different starting positions around obstacles
    test_cases = [
        (0, 0, 1, 6),   # Top-left, facing East
        (2, 0, 0, 6),   # Bottom-left, facing North
    ]
    
    for r, c, direction, expected_steps in test_cases:
        result = cleanRoom(grid, r, c, direction)
        assert result == expected_steps, f"Failed for start ({r},{c}) dir {direction}"

def test_impossible_cleaning():
    """Test rooms where not all cells can be cleaned"""
    # Completely blocked room
    grid1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    
    # Partially blocked room
    grid2 = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    
    test_cases = [
        (1, 1, 0, 0),  # Middle of blocked room, still can be cleaned
        (0, 0, 1, 0)   # Cannot move much, but can clean start cell
    ]
    
    for grid, r, c, direction, expected in zip([grid1, grid2], *zip(*test_cases)):
        result = cleanRoom(grid, r, c, direction)
        assert result == expected, f"Failed for grid {grid}"

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Empty grid
    with pytest.raises(ValueError, match="Grid cannot be empty"):
        cleanRoom([], 0, 0, 0)
    
    # Out of bounds starting position
    grid = [[0, 0], [0, 0]]
    with pytest.raises(ValueError, match="Starting position is out of bounds"):
        cleanRoom(grid, 2, 2, 0)
    
    # Starting on an obstacle
    grid = [[0, 0], [1, 0]]
    with pytest.raises(ValueError, match="Starting position is an obstacle"):
        cleanRoom(grid, 1, 0, 0)

def test_single_cell_room():
    """Test cleaning a single cell room"""
    grid = [[0]]
    result = cleanRoom(grid, 0, 0, 0)
    assert result == 0, "Single cell room should take 0 steps"