from Bot import *
from library import *


class Data():
    """Data-class for MyAgent, more features to be added"""

    AGENTSTATE = {'STATE': 0, 'PURPOSE': 'OFFENCE',
                  'ROUTINE': 'UPKEEP', 'STRATEGY': 'BIOPRESSURE'}
    AGENT_WORKER = {'MINERS': [], 'GAS': [], 'BUILDER': [],
                    'REPAIR': [], 'ALL_WORKERS': []}
    AGENT_COMBATUNITS = {'DEFENCE': {}, 'OFFENCE': {}}
    AGENTUNITS = {}
    BASE_HANDLER = {}
    NEUTRALUNITS = {}
    ENEMYUNITS = {}

    QUEUED_BUILDINGS = []
    BUILDQ = {}

    AGENT_COMBAT_UNITS = {}

    AGENT_ECONOMY = [0, 0]
    AGENT_LOST = [0, 0]

    ENEMY_ECONOMY = [0, 0]
    ENEMY_LOST = [0, 0]
    BUILDER = []

    SCOUT = []
    enemies_in_base = []
    AGENTUPGRADES = []
    WALLPOSITION = []

    NE_BASE = (26.5, 137.5)
    SE_BASE = (125.5, 30.5)


    def __init__(self):
        pass

    def start_base(self):
        """Determines PLAYER_SELF starting base"""

        start_location = (self.start_location.x, self.start_location.y)

        if start_location == (26.5, 137.5):
            return 'NE'
        elif start_location == (125.5, 30.5):
            return 'SE'


    def total_value(self):
        """Determines the total value of all Agent Units"""

        types = len(list(Data.AGENTUNITS))
        mineral_spent = 0
        gas_spent = 0

        for units in range(types):
            current = list(Data.AGENTUNITS)[units]
            amount = len(Data.AGENTUNITS[current])
            unit_cost = UnitType(current, self)
            mineral_spent += unit_cost.mineral_price * amount
            gas_spent += unit_cost.gas_price * amount

        return [mineral_spent, gas_spent]


    def enemy_total_value(self):
        """Determines the total value of all Enemy Units"""

        types = len(list(Data.ENEMYUNITS))
        enemy_mineral_spent = 0
        enemy_gas_spent = 0

        for units in range(types):
            current = list(Data.ENEMYUNITS)[units]
            amount = len(Data.ENEMYUNITS[current])
            unit_cost = UnitType(current, self)
            enemy_mineral_spent += unit_cost.mineral_price * amount
            enemy_gas_spent += unit_cost.gas_price * amount

        return [enemy_mineral_spent, enemy_gas_spent]


    def wall_positions(self, step):

        start = Data.start_base(self)

        if start == 'NE':
            WALLPOSITION = [(37.0, 122.0), (34.0, 125.0), (32.5, 120.5)]
        if start == 'SE':
            WALLPOSITION = [(118.0, 43.0), (115.0, 46.0), (117.5, 46.5)]

        return WALLPOSITION[step][0], WALLPOSITION[step][1]
