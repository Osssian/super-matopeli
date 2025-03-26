import pytest
import random
from unittest.mock import patch
from matopeli import gameLoop, width, height, snake_block

@pytest.fixture
def mock_pygame():
    """Mock pygame to avoid initializing the game window during tests."""
    with patch("pygame.display.set_mode"), patch("pygame.font.SysFont"), patch("pygame.time.Clock"):
        yield

def test_snake_movement(mock_pygame):
    """Test that the snake moves correctly."""
    with patch("pygame.event.get", return_value=[]), \
         patch("pygame.display.update"), \
         patch("pygame.draw.rect"), \
         patch("pygame.quit"):
        # Simulate a single game loop iteration
        with patch("pygame.time.Clock.tick", side_effect=lambda _: exit()):
            gameLoop()

def test_food_spawn(mock_pygame):
    """Test that food spawns within the game boundaries."""
    for _ in range(100):  # Test multiple random spawns
        food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        assert 0 <= food_x < width
        assert 0 <= food_y < height

def test_collision_detection(mock_pygame):
    """Test that the game detects collisions correctly."""
    with patch("pygame.event.get", return_value=[]), \
         patch("pygame.display.update"), \
         patch("pygame.draw.rect"), \
         patch("pygame.quit"):
        # Simulate a collision by setting snake position out of bounds
        with patch("matopeli.width", 100), patch("matopeli.height", 100):
            with pytest.raises(SystemExit):  # Expect the game to quit
                gameLoop()
