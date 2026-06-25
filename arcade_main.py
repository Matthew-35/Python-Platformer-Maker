# Python Platformer Maker
# By Playbounce35

import arcade

class ArcadeGame(arcade.Window):
    def __init__(self, PlatformerMaker):
        super().__init__(PlatformerMaker.constants.WINDOW_WIDTH, PlatformerMaker.constants.WINDOW_HEIGHT, PlatformerMaker.constants.WINDOW_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        pass

    def run(self):
        arcade.run()

    def on_draw(self):
        self.clear()
        # Draw your game here
        arcade.draw_text("Welcome to Python Platformer Maker!", self.width / 2, self.height / 2,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def update(self, delta_time):
        # Update your game logic here
        pass
