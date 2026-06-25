# Python Platformer Maker
# By Playbounce35

import arcade

class ArcadeGame(arcade.Window):
    def __init__(self, PlatformerMaker):
        self.constants = PlatformerMaker.constants
        super().__init__(self.constants.WINDOW_WIDTH, self.constants.WINDOW_HEIGHT, self.constants.WINDOW_TITLE)
        #arcade.set_background_color(arcade.color.AMAZON)

        self.wall_list = None
        self.player_list = None
        self.player_sprite = None
        
        # Physics Engine
        self.physics_engine = None

    def setup(self):
        # Enforce spatial hashing for extreme physics performance on walls
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.player_list = arcade.SpriteList()

        # --- GENERATE TILEMAP FROM CODE ---
        # Loop through the grid array (top to bottom, left to right)
        # Note: PyGame/Arcade 0,0 is bottom-left, so we reverse rows to read top-down
        for row_idx, row in enumerate(reversed(self.constants.GRID_MAP)):
            for col_idx, cell in enumerate(row):
                if cell == "W":
                    # Use a built-in default resource asset from Arcade
                    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", scale=0.5)
                    # Position based on index * tile dimension
                    wall.left = col_idx * self.constants.TILE_SIZE
                    wall.bottom = row_idx * self.constants.TILE_SIZE
                    self.wall_list.append(wall)

    def run(self):
        arcade.run()

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        # Update your game logic here
        pass


if __name__ == "__main__": # Quickly test the code by running this file directly, instead of switching files every time.
    import init
    init.main()
