import Bot


class gamestate:
    """Data-class for MyAgent, more features to be added"""

    AGENTUNITS = {}
    AGENTUPGRADES = {}
    NEUTRALUNITS = {}

    MINERAL_WORKER = []
    GAS_WORKER = []
    BUILDER = []
    ATTACKER = []

    BASE = []
    WALLPOSITION = []


    def __init__(self):
        pass

    def start_base(self):

        start_location = (self.start_location.x, self.start_location.y)

        if start_location == (26.5, 137.5):
            return 'NE'
        elif start_location == (125.5, 30.5):
            return 'SE'

    def total_value(self):
        """Determines the total value of all Agent Units"""

        types = len(list(gamestate.AGENTUNITS))
        mineral_spent = 0
        gas_spent = 0

        for units in range(types):
            current = list(gamestate.AGENTUNITS)[units]
            amount = len(gamestate.AGENTUNITS[current])
            unit_cost = Bot.UnitType(current, self)
            mineral_spent += unit_cost.mineral_price * amount
            gas_spent += unit_cost.gas_price * amount

        return [mineral_spent, gas_spent]

    def total_lost(self):
        """Determines the total lost value of perished Agent Units"""

        lost_minerals = 0
        lost_gas = 0

        for unit in list(gamestate.AGENTUNITS):
            for individual in gamestate.AGENTUNITS[unit]:
                if individual.is_alive == False:
                    lost_minerals += individual.unit_type.mineral_price
                    lost_gas += individual.unit_type.gas_price

        return [lost_minerals, lost_gas]

    def wall_positions(self, step):

        start = gamestate.start_base(self)

        if start == 'NE':
            WALLPOSITION = [(37.0, 122.0), (34.0, 125.0), (36.5, 124.5)]
        if start == 'SE':
            WALLPOSITION = [(118.0, 43.0), (115.0, 46.0), (113.5, 43.5)]

        return WALLPOSITION[step][0], WALLPOSITION[step][1]




