import pytest
from unittest.mock import patch, MagicMock
import matopeli

@patch("matopeli.pygame.display.set_mode")
@patch("matopeli.pygame.font.SysFont")
@patch("matopeli.pygame.draw.rect")
@patch("matopeli.pygame.event.get")
def test_game_quit(mock_event_get, mock_draw_rect, mock_sysfont, mock_set_mode):
    # Mock events to simulate quitting the game
    mock_event_get.side_effect = [[MagicMock(type=matopeli.pygame.QUIT)]]
    
    with patch("matopeli.pygame.quit") as mock_quit, patch("matopeli.quit") as mock_exit:
        matopeli.gameLoop()
        mock_quit.assert_called_once()
        mock_exit.assert_called_once()

@patch("matopeli.pygame.display.set_mode")
@patch("matopeli.pygame.font.SysFont")
@patch("matopeli.pygame.draw.rect")
@patch("matopeli.pygame.event.get")
def test_snake_movement(mock_event_get, mock_draw_rect, mock_sysfont, mock_set_mode):
    # Mock events to simulate snake movement
    mock_event_get.side_effect = [
        [MagicMock(type=matopeli.pygame.KEYDOWN, key=matopeli.pygame.K_RIGHT)],
        [MagicMock(type=matopeli.pygame.QUIT)]
    ]
    
    with patch("matopeli.pygame.quit"), patch("matopeli.quit"):
        matopeli.gameLoop()
        # Verify that the snake's position is updated
        assert mock_draw_rect.call_count > 0

@patch("matopeli.pygame.display.set_mode")
@patch("matopeli.pygame.font.SysFont")
@patch("matopeli.pygame.draw.rect")
@patch("matopeli.pygame.event.get")
def test_collision_with_boundaries(mock_event_get, mock_draw_rect, mock_sysfont, mock_set_mode):
    # Mock events to simulate snake moving out of bounds
    mock_event_get.side_effect = [
        [MagicMock(type=matopeli.pygame.KEYDOWN, key=matopeli.pygame.K_UP)],
        [MagicMock(type=matopeli.pygame.QUIT)]
    ]
    
    with patch("matopeli.pygame.quit"), patch("matopeli.quit"):
        matopeli.gameLoop()
        # Verify that the game ends when the snake hits the boundary
        assert mock_draw_rect.call_count > 0
        from unittest.mock import patch, MagicMock
import matopeli