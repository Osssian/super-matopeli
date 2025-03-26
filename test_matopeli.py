import pytest
import random
from matopeli import width, height, snake_block

def test_food_spawn():
    """Test that food spawns within the game boundaries."""
    for _ in range(100):  # Test multiple random spawns
        food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        assert 0 <= food_x < width
        assert 0 <= food_y < height

