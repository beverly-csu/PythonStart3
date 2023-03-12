from pygame import *
from random import randint
mixer.init()
mixer.music.set_volume(0.05)
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
    health = 5
    num_fire = 0
    rel_flag = False
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
        if Timer.time() - self.prev_time < 2 and self.rel_flag:
            return
        if Timer.time() - 0.1 > self.prev_time:
            fire_sound.play()
            x = self.rect.centerx
            y = self.rect.top
            bullet = Bullet('bullet.png', x, y, 10, 20, 5)
            bullet.rect.x -= bullet.rect.width // 2
            bullets.add(bullet)
            self.prev_time = Timer.time()
            self.num_fire += 1
            if self.num_fire >= 5:
                self.rel_flag = True

    def reset(self):
        super().reset()
        if Timer.time() - self.prev_time > 2 and self.rel_flag:
            self.rel_flag = False
            self.num_fire = 0
        if self.rel_flag:
            reload_time = round(2 - (Timer.time() - self.prev_time), 1)
            reload_text = 'Перезарядка ещё ' + str(reload_time) + 'с'
            reload = my_font.render(reload_text, True, (225, 225, 225))
            reload_rect = reload.get_rect()
            reload_rect.centerx = WIDTH // 2
            reload_rect.centery = HEIGHT // 2
            mw.blit(reload, (reload_rect.x, reload_rect.y))


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


class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = -self.rect.height
            self.rect.x = randint(0, WIDTH - self.rect.width)
            self.speed = randint(1, 5)


WIDTH, HEIGHT = 1280, 720
FPS = 60
lost = 0
score = 0

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Shooter | шутер')

background = transform.scale(image.load('galaxy.jpg'), (WIDTH, HEIGHT))
player = Player('rocket.png', WIDTH // 2, HEIGHT - 70, 65, 65, 10)

monsters = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png', randint(0, WIDTH), -100, 100, 50, randint(1, 8))
    monsters.add(enemy)

asteroids = sprite.Group()
for i in range(3):
    asteroid = Asteroid('asteroid.png', randint(0, WIDTH), -100, 50, 50, randint(1, 5))
    asteroids.add(asteroid)

bullets = sprite.Group()

mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
fire_sound.set_volume(0.02)

font.init()
my_font = font.Font(None, 30)

clock = time.Clock()

game = True
finish = False
while game:
    if not finish:
        mw.blit(background, (0, 0))
        player.update()
        player.reset()
        monsters.update()
        monsters.draw(mw)
        bullets.update()
        bullets.draw(mw)
        asteroids.update()
        asteroids.draw(mw)
        missed_text = my_font.render('Пропущено: ' + str(lost), True, (225, 225, 225))
        killed_text = my_font.render('Уничтожено: ' + str(score), True, (225, 225, 225))
        mw.blit(missed_text, (10, 50))
        mw.blit(killed_text, (10, 10))

        collided = sprite.groupcollide(monsters, bullets, True, True)
        if len(collided) > 0:
            for i in range(len(collided)):
                enemy = Enemy('ufo.png', randint(0, WIDTH), -100, 100, 50, randint(1, 8))
                monsters.add(enemy)
                score += 1

        if lost >= 10:
            finish = True
            result_text = my_font.render('Вы проиграли!', True, (255, 30, 30))
        if score >= 10:
            finish = True
            result_text = my_font.render('Вы выиграли!', True, (30, 255, 30))
        last_tick_time = Timer.time()
    else:
        mw.blit(background, (0, 0))
        text_rect = result_text.get_rect()
        bg_rect = background.get_rect()
        text_rect.center = bg_rect.center
        mw.blit(result_text, (text_rect.x, text_rect.y))
        if Timer.time() - last_tick_time > 3:
            score = 0
            lost = 0
            finish = False
            monsters.empty()
            for i in range(5):
                enemy = Enemy('ufo.png', randint(0, WIDTH), -100, 100, 50, randint(1, 8))
                monsters.add(enemy)
            player.rect.x = bg_rect.centerx



    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)
