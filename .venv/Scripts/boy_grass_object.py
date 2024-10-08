from operator import truediv

from pico2d import *
from random import randint
# Game object class here

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')

    def update(self):
        pass
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y=randint(0, 600), 90
        self.frame=randint(0, 8)
        self.image=load_image('run_animation.png')
    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def reset_world():
    global running, grass, team, world
    running= True
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for _ in range(11)]

    world+=team

def update_world():
    for obj in world:
        obj.update()


def render_world():
    clear_canvas()
    for obj in world:
        obj.draw()
    update_canvas()


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

# initialization code
reset_world()


# game main loop code
running = True
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()