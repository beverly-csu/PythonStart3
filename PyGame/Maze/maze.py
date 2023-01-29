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

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < (height - self.rect.height - 5):
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < (width - self.rect.width - 5):
            self.rect.x += self.speed

width, height = 700, 500
window = display.set_mode((width, height))
display.set_caption('Maze | Лабиринт')

background = transform.scale(image.load('background.jpg'), (width, height))
hero = Player('hero.png', 10, 100, 100)
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
    hero.update()
    hero.clear()
    enemy.clear()
    treasure.clear()

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()