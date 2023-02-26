from pygame import *
from random import randint
mixer.init()
mixer.music.set_volume(0.2)
import time as Timer

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    prev_time = Timer.time()
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < (WIDTH - self.rect.width - 5):
            self.rect.x += self.speed
        if keys[K_SPACE]:
            self.fire()

    def fire(self):
        if Timer.time() - 0.3 > self.prev_time:
            fire_sound.play()
            x = self.rect.centerx
            y = self.rect.top
            bullet = Bullet('bullet.png', x, y, 10, 20, 5)
            bullet.rect.x -= bullet.rect.width // 2
            bullets.add(bullet)
            self.prev_time = Timer.time()

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = -60
            self.speed = randint(1, 8)
            global lost
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


WIDTH, HEIGHT = 700, 500
FPS = 60
lost = 0

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Shooter | шутер')

background = transform.scale(image.load('bg.jpg'), (WIDTH, HEIGHT))
player = Player('player.png', WIDTH // 2, HEIGHT - 70, 65, 65, 10)

monsters = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png', randint(0, WIDTH), -100, 100, 100, randint(1, 8))
    monsters.add(enemy)

bullets = sprite.Group()

mixer.music.load('bg_music.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.wav')

font.init()
my_font = font.Font('my_font.otf', 30)

clock = time.Clock()

game = True
while game:
    mw.blit(background, (0, 0))
    player.update()
    player.reset()
    monsters.update()
    monsters.draw(mw)
    bullets.update()
    bullets.draw(mw)
    missed_text = my_font.render('Пропущено: ' + str(lost), True, (225, 225, 225))
    mw.blit(missed_text, (10, 10))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)
