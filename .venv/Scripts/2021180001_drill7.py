from operator import truediv

from pico2d import *
from random import randint
# Game object class here

class Ball:
    def __init__(self):
        self.x, self.y = randint(0, 800), 599
        self.typeofball = randint(0, 1)
        if (self.typeofball == 0):
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

        self.dy = randint(5, 10)

    def update(self):
        if (self.typeofball == 0 and self.y > 55):
            self.y -= self.dy
        elif(self.typeofball != 0 and self.y > 60):
            self.y -= self.dy
    def draw(self):
        self.image.draw(self.x, self.y)

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
    balls = [Ball() for _ in range(20)]
    world += balls

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