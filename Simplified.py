from Bot import *
import library
from main import *


class Ez():
    """Simplified methods from Bot"""

    def __init__(self, *args, **kwargs):
        self.args = args

    def build(self, building: UnitType, near: Unit):
        """build(self: Bot, building: library.UnityType, near: library.Unit) -> None"""

        if self.build_queue_open() and self.econ_check(self, building):
            x = near.position.x,
            y = near.position.y
            pos = self.find_build_target(Point2D(x, y), building, 2, 10)
            if library.building_placer.can_build_here(pos.x, pos.y, building):
                builder = Bot.get_worker(self)
                builder.build(building, pos)
