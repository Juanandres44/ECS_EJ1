
import random
import esper
import pygame

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_enemyspawner import CEnemySpawner


def crear_cuadrado(ecs_world:esper.World, size: pygame.Vector2, pos:pygame.Vector2, vel:pygame.Vector2, col:pygame.Color):
    cuad_entity = ecs_world.create_entity()
    ecs_world.add_component(cuad_entity, 
                    CSurface(size, col))
        
    ecs_world.add_component(cuad_entity,
                    CTransform(pos))

    ecs_world.add_component(cuad_entity,
                    CVelocity(vel))
    
def crear_cuadrado_enemigo(ecs_world: esper.World, pos:pygame.Vector2, enemy:dict):
    tam = pygame.Vector2(enemy["size"]["x"], enemy["size"]["y"] )
    color = pygame.Vector3(enemy["color"]["r"], enemy["color"]["g"], enemy["color"]["b"])
    vel_min = enemy["velocity_min"]
    vel_max = enemy["velocity_max"]
    rango = random.randrange(vel_min, vel_max)
    vel = pygame.Vector2(random.choice([-rango, rango]), random.choice([-rango, rango]))
    crear_cuadrado(ecs_world, tam, pos, vel, color)
    
def crear_spawner(ecs_world:esper.World, level: dict):
    spawn_entity = ecs_world.create_entity()
    ecs_world.add_component(spawn_entity, CEnemySpawner(level["enemy_spawn_events"]))

