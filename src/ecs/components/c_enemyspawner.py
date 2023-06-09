import pygame

class CEnemySpawner:
    def __init__(self, spawn_events:dict) -> None:
        self.time: float = 0
        self.spawn_event: list[SpawnEvent] = []
        for i in spawn_events:
            self.spawn_event.append(SpawnEvent(i))

class SpawnEvent:
    def __init__(self, event:dict) -> None:
        self.time:float = event["time"]
        self.enemy_type:str = event["enemy_type"]
        self.pos:pygame.Vector2 = pygame.Vector2(event["position"]["x"], event["position"]["y"])
        self.activate = False