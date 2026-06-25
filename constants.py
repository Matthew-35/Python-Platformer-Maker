# Python Platformer Maker
# By Playbounce35

class Constants:
    # Game dimensions
    # GAME_WIDTH = 1024
    # GAME_HEIGHT = 1024

    # Window dimensions
    WINDOW_WIDTH = 1024
    WINDOW_HEIGHT = 1024
    
    TILE_SIZE = 64
    WINDOW_TITLE = "Python Platformer Maker"

    # Temporary grid map for testing purposes; this will eventually be created by the user in the level editor (currently 16 rows x 16 columns)
    GRID_MAP = [
        "WWWWWWWWWWWWWWWW",
        "W______________W",
        "W______________W",
        "W______________W",
        "W______________W",
        "W______________W",
        "W______________W",
        "W______________W",
        "W______________W",
        "W____WWW_______W",
        "W___W__________W",
        "W_______W______W",
        "W_WW___________W",
        "W____W_________W",
        "W_P_WW_W_______W",
        "WWWWWWWWWWWWWWWW",
    ]

    MAX_JUMP_COUNT = 2  # Maximum number of jumps allowed (for double jump)
