# Python Platformer Maker
# By Playbounce35

import arcade_main, constants


class PlatformerMaker:
    def __init__(self):
        self.constants = constants.Constants()
        self.game = arcade_main.ArcadeGame(self)
        self.run()

    def run(self):
        self.game.setup()
        self.game.run()


def main():
    platformer_maker = PlatformerMaker()
    platformer_maker.run()

if __name__ == "__main__":
    main()
