from Bot import *

class combat(MyAgent):

    def select_all(self):

        combat_units = []

        for unittype in Data.AGENTUNITS:
            for unit in Data.AGENTUNITS[unittype]:
                if not unit.unit_type.is_combat_unit:
                    continue
                else:
                    if unit.is_alive:
                        combat_units.append(unit)
                    elif not unit.is_alive:
                        Data.AGENTUNITS[unittype].remove(unit)
        return combat_units

    def get_enemy_near(self, unit, distance):

        try:
            from_x = Unit1.position.x
            from_y = Unit1.position.y

            units_near = []

            for unittypes in Data.ENEMYUNITS:
                for unit in Data.ENEMYUNITS[unittypes]:
                    to_x = unit.position.x
                    to_y = unit.position.y
                    if math.sqrt((from_x - to_x) ** 2 + (from_y - to_y) ** 2) < distance:
                        if len(units_near) > 3:
                            break
                        units_near.append(unit)
                else:
                    continue
            return units_near
        except:
            return []

    def select_type(self, unit_typeid):

        combat_units = []

        for unit in Data.AGENTUNITS[unit_typeid]:
            if unit.is_alive:
                combat_units.append(unit)
            elif not unit.is_alive:
                Data.AGENTUNITS[unit_typeid].remove(unit)

    def unit_data(self, unit):

        if unit.unit_type.name == 'TERRAN_MARINE':
            return {'DPS': 9.8, 'TARGET': ['GROUND', 'AIR'], 'SPEED': 3.15, 'RANGE': 5, 'TYPE': 'LIGHT','BONUS': 'NONE'}
        if unit.unit_type.name == 'TERRAN_MARAUDER':
            return {'DPS': 9.3, 'TARGET': ['GROUND'], 'SPEED': 3.15, 'RANGE': 6, 'TYPE': 'ARMORED','BONUS': {'ARMORED': 9.3}}
        if unit.unit_type.name == 'TERRAN_REAPER':
            return {'DPS': 10.1, 'TARGET': ['GROUND'], 'SPEED': 5.25, 'RANGE': 5, 'TYPE': 'LIGHT', 'BONUS': 'NONE'}
        if unit.unit_type.name == 'TERRAN_GHOST':
            return {'DPS': 9.3, 'TARGET': ['GROUND', 'AIR'], 'SPEED': 3.94, 'RANGE': 6, 'TYPE': 'LIGHT','BONUS': {'LIGHT': 9.3}}
        if unit.unit_type.name == 'TERRAN_SIEGETANK':
            return {'DPS': 13.51, 'TARGET': ['GROUND'], 'SPEED': 3.15, 'RANGE': 7, 'TYPE': 'ARMORED','BONUS': {'LIGHT': 13.51}}
        if unit.unit_type.name == 'TERRAN_SIEGETANKSIEGED':
            return {'DPS': 18.69, 'TARGET': ['GROUND'], 'SPEED': 0, 'RANGE': 12, 'TYPE': 'ARMORED','BONUS': {'LIGHT': 14.02}}
        if unit.unit_type.name == 'TERRAN_HELLION':
            return {'DPS': 4.45, 'TARGET': ['GROUND'], 'SPEED': 5.95, 'RANGE': 5, 'TYPE': 'LIGHT','BONUS': {'LIGHT': 3.4}}
        if unit.unit_type.name == 'TERRAN_WIDOWMINE':
            return None
        if unit.unit_type.name == 'WIDOWMINEBURROWED':
            return {'DPS': 125, 'TARGET': ['GROUND', 'AIR'], 'SPEED': 3.94, 'RANGE': 5, 'TYPE': 'LIGHT','BONUS': {'LIGHT': 160}}
        if unit.unit_type.name == 'TERRAN_THOR':
            return {'DPS': 65.9, 'TARGET': ['GROUND'], 'SPEED': 2.62, 'RANGE': 7, 'TYPE': 'ARMORED','BONUS': {'LIGHT': 6.5}}
        if unit.unit_type.name == 'TERRAN_VIKINGASSAULT':
            return {'DPS': 16.8, 'TARGET': ['GROUND'], 'SPEED': 3.15, 'RANGE': 6, 'TYPE': 'ARMORED','BONUS': {'MECHANICAL': 11.3}}
        if unit.unit_type.name == 'TERRAN_VIKINGFIGHTER':
            return {'DPS': 14, 'TARGET': ['AIR'], 'SPEED': 3.85, 'RANGE': 9, 'TYPE': 'ARMORED','BONUS': {'ARMORED': 5.6}}
        if unit.unit_type.name == 'TERRAN_MEDIVAC':
            return {'DPS': 0, 'TARGET': ['NONE'], 'SPEED': 3.5, 'RANGE': 'NONE', 'TYPE': 'ARMORED', 'BONUS': 'NONE'}
        if unit.unit_type.name == 'TERRAN_LIBERATOR':
            return None
        if unit.unit_type.name == 'TERRAN_LIBERATORAG':
            return {'DPS': 'NONE', 'TARGET': ['GROUND', 'AIR'], 'SPEED': 3.85, 'RANGE': 'NONE','TYPE': 'LIGHT', 'BONUS': 'NONE'}
        if unit.unit_type.name == 'TERRAN_RAVEN':
            return {'DPS': 65.9, 'TARGET': ['GROUND'], 'SPEED': 2.62, 'RANGE': 7, 'TYPE': 'ARMORED', 'BONUS': {'LIGHT': 6.5}}
        if unit.unit_type.name == 'TERRAN_BANSHEE':
            return {'DPS': 27, 'TARGET': ['GROUND'], 'SPEED': 3.85, 'RANGE': 6, 'TYPE': 'LIGHT', 'BONUS': 'NONE'}
        if unit.unit_type.name == 'TERRAN_BATTLECRUISER':
            return {'DPS': 49.8, 'TARGET': ['GROUND', 'AIR'], 'SPEED': 2.62, 'RANGE': 6, 'TYPE': 'ARMORED','BONUS': 'NONE'}

        else:
            return None

