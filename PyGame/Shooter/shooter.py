from pygame import *
mixer.init()

WIDTH, HEIGHT = 700, 500
FPS = 60

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Shooter | шутер')

background = transform.scale(image.load('bg.jpg'), (WIDTH, HEIGHT))

mixer.music.load('bg_music.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')

clock = time.Clock()

game = True
while game:
    mw.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)
