import esper


from src.create.prefab_creator import crear_cuadrado_enemigo
from src.ecs.components.c_enemyspawner import CEnemySpawner, SpawnEvent

def system_enemyspawner(ecs_world:esper.World, enemies:dict, delta:float):
    components = ecs_world.get_component(CEnemySpawner)
    c_es:CEnemySpawner
    for _, c_es in components:
        c_es.time += delta
        c_evt: SpawnEvent
        for c_evt in c_es.spawn_event:
            if c_es.time >= c_evt.time and not c_evt.activate:
                c_evt.activate = True
                crear_cuadrado_enemigo(ecs_world, c_evt.pos, enemies[c_evt.enemy_type])