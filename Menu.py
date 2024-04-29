import pygame as pg 
from button import Button

class Menu():
    def __init__(self, surface):
        self.surface = surface
        self.play_with_bot = Button(30, 30, 100, 30, "Play with Bot", (180, 0, 0), (14, 0, 0), (100, 0, 0), (255, 255, 255)) 
        self.play_with_friend = Button(30, 80, 100, 30, "Play with Friend", (180, 0, 0), (14, 0, 0), (100, 0, 0), (255, 255, 255))
        self.settings = Button(30, 130, 100, 30, "Settings", (180, 0, 0), (14, 0, 0), (100, 0, 0), (255, 255, 255))
        self.exit = Button(30, 180, 100, 30, "Exit", (180, 0, 0), (14, 0, 0), (100, 0, 0), (255, 255, 255))
        self.clock = pg.time.Clock()
        self.FPS = 30



    def update(self):
        events = pg.event.get()
        self.play_with_bot.update(events)
        self.play_with_friend.update(events)
        self.settings.update(events)
        self.exit.update(events)

        self.play_with_bot.draw(self.surface)
        self.play_with_friend.draw(self.surface)
        self.settings.draw(self.surface)
        self.exit.draw(self.surface)


if __name__ == '__main__':
    pg.init()

    mw = pg.display.set_mode((700, 500))
    menu = Menu(mw)
    game = True 
    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
        menu.update()

        pg.display.flip()
        pg.time.Clock().tick(30)
