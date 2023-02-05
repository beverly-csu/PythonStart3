from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, _image, speed, x, y):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(_image), (65, 65))
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

class Enemy(GameSprite):
    direction = 'left'
    
    def update(self):
        if self.rect.x >= 620:
            self.direction = 'left'
        if self.rect.x <= 520:
            self.direction = 'right'
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed  

class Wall(sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


width, height = 700, 500
window = display.set_mode((width, height))
display.set_caption('Maze | Лабиринт')

background = transform.scale(image.load('background.jpg'), (width, height))
hero = Player('hero.png', 10, 10, 10)
enemy = Enemy('cyborg.png', 1, 620, 300)
treasure = GameSprite('treasure.png', 0, 500, 500)

w1 = Wall(300, 10, 100, 20, (255, 0, 0))
w2 = Wall(10, 200, 100, 20, (255, 0, 0))
w3 = Wall(10, 300, 500, 150, (255, 0, 0))

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
    enemy.update()
    enemy.clear()
    treasure.clear()
    w1.draw()
    w2.draw()
    w3.draw()

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()