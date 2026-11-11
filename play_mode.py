from pico2d import SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE, clear_canvas, get_events, load_image, update_canvas

import game_framework
import game_world
from bird import Flock
from boy import Boy
from grass import Grass


boy = None


def init():
    global boy
    game_world.add_oject(Grass(), 0)
    image = load_image('bird_animation.png')
    game_world.add_oject(Flock(image))
    boy = Boy()
    game_world.add_oject(boy)


def finish():
    global boy
    game_world.clear()
    boy = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT or (
            event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
        ):
            game_framework.quit()
            return
        boy.handle_event(event)


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()
