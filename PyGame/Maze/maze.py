from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, _image, speed, x, y):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(_image), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def clear(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

width, height = 700, 500
window = display.set_mode((width, height))
display.set_caption('Maze | Лабиринт')

background = transform.scale(image.load('background.jpg'), (width, height))
hero = GameSprite('hero.png', 1, 100, 100)
enemy = GameSprite('cyborg.png', 1, 400, 100)
treasure = GameSprite('treasure.png', 0, 500, 500)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

clock = time.Clock()
FPS = 60

game = True
while game:
    window.blit(background, (0, 0))
    hero.clear()
    enemy.clear()
    treasure.clear()

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()