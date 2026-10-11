import pgzrun
import random
HEIGHT = 450
WIDTH = 800
amongus = Actor("amongus.png",(150,290))
def draw():
    screen.blit("mariobackground.png",(0,0))
    amongus.draw()
def on_mouse_down(pos):
    if amongus.collidepoint(pos):
        amongus.pos = (random.randint(0,750),(random.randint(0,400)))
pgzrun.go()