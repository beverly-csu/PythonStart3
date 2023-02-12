from pygame import *
mixer.init()

WIDTH, HEIGHT = 700, 500

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Shooter | шутер')

background = transform.scale(image.load('bg.jpg'), (WIDTH, HEIGHT))

mixer.music.load('bg_music.ogg')
mixer.music.play()

fire = mixer.Sound('fire.ogg')
