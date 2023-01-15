from pygame import *

resolution = (700, 500)
window = display.set_mode(resolution)
display.set_caption('Догонялки')

background = transform.scale(
    image.load('PyGame/Catch Up/background.jpg'),
    (700, 500)
)

game = True
while game:
    window.blit(background, (0, 0))

    

    display.update()