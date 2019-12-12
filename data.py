from Bot import *
from library import *


class Data():
    """Data-class for MyAgent, more features to be added"""

    AGENTSTATE = {'STATE': 0, 'PURPOSE': 'OFFENCE', 'ROUTINE': 'UPKEEP', 'STRATEGY': 'BIOPRESSURE'}
    AGENT_WORKER = {'MINERS': [], 'GAS': [], 'BUILDER': [], 'REPAIR': [], 'ALL_WORKERS': []}
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

# class UnitData():
#     """
#     Har verkligen noll jävla aning om hur detta funkar!
#     Send Help
#     """
#
#     def __init__(self):
#         pass
#
#     TERRAN_MARINE = None
#     TERRAN_MARAUDER = None
#     TERRAN_REAPER = None
#     TERRAN_GHOST = None
#     TERRAN_SIEGETANK = None
#     TERRAN_SIEGETANKSIEGED = None
#     TERRAN_HELLION = None
#     TERRAN_WIDOWMINE = None
#     WIDOWMINEBURROWED = None
#     TERRAN_THOR = None
#     TERRAN_VIKINGASSAULT = None
#     TERRAN_VIKINGFIGHTER = None
#     TERRAN_MEDIVAC = None
#     TERRAN_LIBERATOR = None
#     TERRAN_LIBERATORAG = None
#     TERRAN_RAVEN = None
#     TERRAN_BANSHEE = None
#     TERRAN_BATTLECRUISER = None
#
#     __members__ = {
#
#         {'TERRAN_MARINE':
#              {'DPS': 9.8, 'TARGET': ['GROUND', 'AIR'], 'SPEED': 3.15,
#               'RANGE': 5, 'TYPE': 'LIGHT', 'BONUS': 'NONE'}},
#
#         {'TERRAN_MARAUDER':
#              {'DPS': 9.3, 'TARGET': ['GROUND'], 'SPEED': 3.15,
#               'RANGE': 6, 'TYPE': 'ARMORED', 'BONUS': {'ARMORED': 9.3}}},
#
#         {'TERRAN_REAPER':
#              {'DPS': 10.1, 'TARGET': ['GROUND'], 'SPEED': 5.25,
#               'RANGE': 5, 'TYPE': 'LIGHT', 'BONUS': 'NONE'}},
#
#         {'TERRAN_GHOST':
#              {'DPS': 9.3, 'TARGET': ['GROUND', 'AIR'], 'SPEED': 3.94,
#               'RANGE': 6, 'TYPE': 'LIGHT', 'BONUS': {'LIGHT': 9.3}}},
#
#         {'TERRAN_SIEGETANK':
#              {'DPS': 13.51, 'TARGET': ['GROUND'], 'SPEED': 3.15,
#               'RANGE': 7, 'TYPE': 'ARMORED', 'BONUS': {'LIGHT': 13.51}}},
#
#         {'TERRAN_SIEGETANKSIEGED':
#              {'DPS': 18.69, 'TARGET': ['GROUND'], 'SPEED': 0,
#               'RANGE': 12, 'TYPE': 'ARMORED', 'BONUS': {'LIGHT': 14.02}}},
#
#         {'TERRAN_HELLION':
#              {'DPS': 4.45, 'TARGET': ['GROUND'], 'SPEED': 5.95,
#               'RANGE': 5, 'TYPE': 'LIGHT', 'BONUS': {'LIGHT': 3.4}}},
#
#         {'TERRAN_WIDOWMINE':
#              {}},
#
#         {'WIDOWMINEBURROWED':
#              {'DPS': 125, 'TARGET': ['GROUND', 'AIR'], 'SPEED': 3.94,
#               'RANGE': 5, 'TYPE': 'LIGHT', 'BONUS': {'LIGHT': 160}}},
#
#         {'TERRAN_THOR':
#              {'DPS': 65.9, 'TARGET': ['GROUND'], 'SPEED': 2.62,
#               'RANGE': 7, 'TYPE': 'ARMORED', 'BONUS': {'LIGHT': 6.5}}},
#
#         {'TERRAN_VIKINGASSAULT':
#              {'DPS': 16.8, 'TARGET': ['GROUND'], 'SPEED': 3.15,
#               'RANGE': 6, 'TYPE': 'ARMORED', 'BONUS': {'MECHANICAL': 11.3}}},
#
#         {'TERRAN_VIKINGFIGHTER':
#              {'DPS': 14, 'TARGET': ['AIR'], 'SPEED': 3.85,
#               'RANGE': 9, 'TYPE': 'ARMORED', 'BONUS': {'ARMORED': 5.6}}},
#
#         {'TERRAN_MEDIVAC':
#              {'DPS': 0, 'TARGET': ['NONE'], 'SPEED': 3.5,
#               'RANGE': 'NONE', 'TYPE': 'ARMORED', 'BONUS': 'NONE'}},
#
#         {'TERRAN_LIBERATOR': {}},
#
#         {'TERRAN_LIBERATORAG':
#              {'DPS': 'NONE', 'TARGET': ['GROUND', 'AIR'], 'SPEED': 3.85,
#               'RANGE': 'NONE', 'TYPE': 'LIGHT', 'BONUS': 'NONE'}},
#
#         {'TERRAN_RAVEN':
#              {'DPS': 65.9, 'TARGET': ['GROUND'], 'SPEED': 2.62,
#               'RANGE': 7, 'TYPE': 'ARMORED', 'BONUS': {'LIGHT': 6.5}}},
#
#         {'TERRAN_BANSHEE':
#              {'DPS': 27, 'TARGET': ['GROUND'], 'SPEED': 3.85,
#               'RANGE': 6, 'TYPE': 'LIGHT', 'BONUS': 'NONE'}},
#
#         {'TERRAN_BATTLECRUISER':
#              {'DPS': 49.8, 'TARGET': ['GROUND', 'AIR'], 'SPEED': 2.62,
#               'RANGE': 6, 'TYPE': 'ARMORED', 'BONUS': 'NONE'}}
#
#     }
