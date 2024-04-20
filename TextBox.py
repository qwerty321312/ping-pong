import pygame as pg

class Textbox():
    def __init__(self, x, y, width, height, color_base=(0,0,0), color_active=(0,0,0), color_used=(0,0,0), text_color=(0,0,0), font=None):
        self.rect = Rect(0, 0, 200, 300)
        self.color_base = color_base
        self.color_active = color_active
        self.color_used = color_used
        font = pg.font.Font(font, height)
        self.status = 'base'
        self.text = ''
#8 32 127
    def update(self, events):
        x, y = pg.mouse.get_pos()
        if not self.rect.collidepoint(x, y):
            return
        for event in events:
            if event.type == pg.KEYDOWN:
                key = event.dict['key']
                if key >= 48 and key <= 57:
                    self.text += chr(key)
                elif key >= 65 and key <= 90:
                    self.text += chr(key)
                elif key >= 97 and key <= 122:
                    self.text += chr(event.key)
                elif key >= 224 and key <= 240:
                    self.text += chr(key)
                elif key == 8:
                    self.text = self.text[:-1]
                elif key == 13:
                    self.text += chr(32)

    def draw(self, surface):
        x, y = pg.mouse.get_pos()
        is_hovered = False
        if self.rect.collidepoint(x, y):
            if_hovered = True

        image = self.font.render(self.text, True, self.text_color)
        pg.draw.rect(surface, self.color_base, self.rect)
        image_rect = image.get_rect()
        image_rect.center = self.rect.center
        if is_hovered:
            pg.draw.rect(surface, self.color_used, self.rect, 5)
        surface.blit(image, image_rect)
        


                
