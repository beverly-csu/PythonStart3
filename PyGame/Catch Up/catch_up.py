from pygame import *

resolution = (700, 500)
window = display.set_mode(resolution)
display.set_caption('Догонялки')

background = transform.scale(
    image.load('PyGame/Catch Up/background.jpg'),
    (700, 500)
)

x1, y1 = 100, 100
x2, y2 = 500, 100

game = True
while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()