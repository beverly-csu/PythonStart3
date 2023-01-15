from pygame import *

resolution = (700, 500)
window = display.set_mode(resolution)
display.set_caption('Догонялки')

background = transform.scale(image.load('PyGame/Catch Up/background.jpg'), (700, 500))

x1, y1 = 100, 100
x2, y2 = 500, 100

sprite1 = transform.scale(image.load('PyGame/Catch Up/sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('PyGame/Catch Up/sprite2.png'), (100, 100))

game = True
while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()