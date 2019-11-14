from Bot import *
import library
from main import *


class Ez():
    """Simplified methods from Bot"""

    def __init__(self, *args, **kwargs):
        pass

    def build(self, building: UnitType, near: Unit, range):
        """build(self: Bot, building: library.UnityType, near: library.Unit) -> None"""

        if Bot.build_queue_open() and Bot.econ_check(self, building):
            x = near.position.x,
            y = near.position.y
            pos = self.find_build_target(x, y, building, range, 10)
            if library.building_placer.can_build_here(pos.x, pos.y, building):
                builder = Bot.get_worker(self)
                builder.build(building, pos)
