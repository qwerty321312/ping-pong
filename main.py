from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, filename, size, coords):
        super().__init__()
        self.image = transform.scale(image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]
    
    def reset(self):
        mw.blit(self.image, self.rect) 

class Player(GameSprite):
    def __init__(self, filename, size, coords, speed=5, keys=[K_w, K_s]):
        super().__init__(filename, size, coords)
        self.speed = speed
        self.keys = keys

    def update(self):
        keys = key.get_pressed()
        if keys[self.keys[0]] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.keys[1]] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, coords):
        super().__init__('pngegg.png', (100, 50), coords)
        self.dx, self.dy = 5, 5
    
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.y <= 0:
            self.dy *= -1

        if self.rect.y >= HEIGHT - self.rect.height:
            self.dy *= -1
        
        if self.rect.colliderect(player1.rect):
            self.dx *= -1

        if self.rect.colliderect(player2.rect):
            self.dx *= -1   

class Score(object):
    _font = font.Font(None, 50)
    left_score = 0
    right_score = 0

    @staticmethod
    def draw():
        text = f"{Score.left_score} : {Score.right_score}"
        _image = Score._font.redner(text, True, (40, 40, 40)) 
        _rect = _image.ger_rect()
        _rect.centerx = mw.get_rect().centerx
        _rect.y = 10
        mw.blit(_image, _rect)

    @staticmethod
    def add(left=0, right=0):
        if left: Score.left_score += 1
        elif right: Score.right_score += 1


WIDTH, HEIGHT = 700, 500
FPS = 60

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Ping-Pong")
clock = time.Clock()

player1 = Player('ww.png', (20, 500), (10, 0), 5, [K_w, K_s])
player2 = Player('ww.png', (20, 500), (WIDTH-30, 0), 5, [K_UP, K_DOWN])
ball = Ball((WIDTH // 2, HEIGHT // 2))

game = True
finish = False


while game:
    if not finish:
        mw.fill((200, 200, 200))
        player1.update()
        player2.update()
        player1.reset()
        player2.reset()
        ball.update()
        ball.reset()
        Score.draw()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)



