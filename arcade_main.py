# Python Platformer Maker
# By Playbounce35

import arcade

class ArcadeGame(arcade.Window):
    def __init__(self, PlatformerMaker):
        self.constants = PlatformerMaker.constants
        super().__init__(self.constants.WINDOW_WIDTH, self.constants.WINDOW_HEIGHT, self.constants.WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

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
        
        # Set up player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", scale=0.5)
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # --- HANDLE PHYSICS ---
        # Feed the engine the player, the walls, and the gravity setting
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls=self.wall_list, gravity_constant=0.5
        )

    def run(self):
        arcade.run()

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.player_list.draw()

    def on_fixed_update(self, delta_time):
        self.physics_engine.update()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        elif key == arcade.key.UP and self.physics_engine.can_jump():
            self.player_sprite.change_y = 10

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player_sprite.change_x = 0


if __name__ == "__main__": # Quickly test the code by running this file directly, instead of switching files every time.
    import init
    init.main()
