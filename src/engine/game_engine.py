import pygame
import esper
import json

from src.create.prefab_creator import crear_spawner

from src.ecs.systems.s_enemy_spawner import system_enemyspawner
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering


from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

fileE = open('assets/cfg/enemies.json')
rectangles = json.load(fileE)

fileW = open('assets/cfg/window.json', encoding="utf-8")
window = json.load(fileW)

fileL = open('assets/cfg/level_01.json')
level = json.load(fileL)

class GameEngine:

    def __init__(self) -> None:
        
        pygame.init()
        pygame.display.set_caption(window["window"]["title"])
        self.screen = pygame.display.set_mode(((window["window"]['size']['w']),(window["window"]['size']['h'])), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.framerate = window["window"]["framerate"]
        self.bg_color = pygame.Color(window["window"]["bg_color"]["r"], window["window"]["bg_color"]["g"], window["window"]["bg_color"]["b"])
        self.delta_time = 0

        self.ecs_world = esper.World()   

    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):
        crear_spawner(self.ecs_world, level)
        pass

    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        system_enemyspawner(self.ecs_world, rectangles, self.delta_time)
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)

    def _draw(self):

        self.screen.fill(self.bg_color)

        system_rendering(self.ecs_world, self.screen)
 
        pygame.display.flip()


    def _clean(self):
        pygame.quit()
