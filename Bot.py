from library import *
from data import *
from extra import *
from main import *
from Simplified import *
import math
from contextlib import *


# from Simplified import *


class Bot(MyAgent):
    """ Main method handler for bot features. Inherits MyAgent """

    def __init__(self):
        pass

    """///////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                      ~COMMANDS~
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

    """---  Make Buildings  ---"""

    def make_refinery(self):
        """Builds refineries at nearby vespene geysers"""

        if UNIT_TYPEID.TERRAN_SUPPLYDEPOT not in Data.AGENTUNITS:
            return

        if UNIT_TYPEID.TERRAN_REFINERY in Data.AGENTUNITS:
            if Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY][-1].is_being_constructed:
                return

        for base in Data.BASE_HANDLER:

            gas = Data.BASE_HANDLER[base]['GAS']
            base_unit = Data.BASE_HANDLER[base]['BASE']
            geysers = Data.BASE_HANDLER[base]['GEYSERS']

            if len(gas) == 2:
                continue

            TERRAN_REFINERY = UnitType(UNIT_TYPEID.TERRAN_REFINERY, self)
            builder = Bot.get_worker(self)

            for geyser in geysers:
                if Bot.near(self, base_unit.position, geyser.position, 14):
                    if UNIT_TYPEID.TERRAN_REFINERY in Data.AGENTUNITS:
                        if len(Bot.get_agentunits_near(self, base_unit, UNIT_TYPEID.TERRAN_REFINERY, 13)) == 0 \
                                and len(Bot.build_queue(self)) < 2:
                            builder.build_target(TERRAN_REFINERY, geyser)
                            return
                        for refinery in Bot.get_agentunits_near(self, base_unit, UNIT_TYPEID.TERRAN_REFINERY, 13):
                            if refinery.id not in gas:
                                Data.BASE_HANDLER[base]['GAS'].update({refinery.id: []})
                            elif refinery.position.x != geyser.position.x and refinery.position.y != geyser.position.y \
                                    and len(Bot.build_queue(self)) < 1:
                                builder.build_target(TERRAN_REFINERY, geyser)
                                return
                    else:
                        builder.build_target(TERRAN_REFINERY, geyser)
                        return
            else:
                continue

    def make_barracks(self):
        """Builds barracks"""

        if UNIT_TYPEID.TERRAN_SUPPLYDEPOT in Data.AGENTUNITS and UNIT_TYPEID.TERRAN_BARRACKS not in Data.AGENTUNITS:
            TERRAN_BARRACKS = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)
            base = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0]

            Bot.build(self, TERRAN_BARRACKS, base, 2)


        if UNIT_TYPEID.TERRAN_FACTORY in Data.AGENTUNITS and UNIT_TYPEID.TERRAN_BARRACKS in Data.AGENTUNITS and \
                len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]) < 2:
            TERRAN_BARRACKS = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)
            base = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0]

            Bot.build(self, TERRAN_BARRACKS, base, 2)
            return

        if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]) > 2\
                and UNIT_TYPEID.TERRAN_BARRACKS in Data.AGENTUNITS and \
                len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]) < 3\
                and UNIT_TYPEID.TERRAN_FACTORY in Data.AGENTUNITS:
            TERRAN_BARRACKS = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)
            base = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0]

            Bot.build(self, TERRAN_BARRACKS, base, 2)
            return

    def make_supply_depot(self):
        """Creates supply depots"""

        if Bot.supply_check(self) and len(Bot.build_queue(self)) < 3:

            if UNIT_TYPEID.TERRAN_SUPPLYDEPOT in Data.AGENTUNITS:
                if Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SUPPLYDEPOT][-1].is_being_constructed and \
                        self.minerals < 400:
                    return

            TERRAN_SUPPLYDEPOT = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)
            base = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0]

            Bot.build(self, TERRAN_SUPPLYDEPOT, base, 0)
            return

    def make_factory(self):
        """Builds factories"""

        if len(Data.BUILDER) > 1:
            return False

        if UNIT_TYPEID.TERRAN_BUNKER in Data.AGENTUNITS and \
                UNIT_TYPEID.TERRAN_FACTORY not in Data.AGENTUNITS and len(Bot.build_queue(self)) < 2:
            TERRAN_FACTORY = UnitType(UNIT_TYPEID.TERRAN_FACTORY, self)
            base = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0]
            Bot.build(self, TERRAN_FACTORY, base, 2)

    def make_expansion(self):
        """Expands the base when requirements are met"""

        if not Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][-1].is_completed:
            with suppress(Exception):
                near_neutral = Bot.get_neutralunits_near
                ID = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][-1].id
                mineral_deposits = near_neutral(self, Data.BASE_HANDLER[ID]['BASE'], UNIT_TYPEID.NEUTRAL_MINERALFIELD,
                                                6)
                Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][-1].right_click(mineral_deposits[0])
                return

        if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SUPPLYDEPOT]) >= 2 and \
                len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]) >= 22 * \
                len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]) and \
                UNIT_TYPEID.TERRAN_MARINE in Data.AGENTUNITS and \
                len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE]) >= 2:

            TERRAN_COMMANDCENTER = UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER, self)
            builder = Bot.get_worker(self)
            with suppress(Exception):
                if Bot.econ_check(self, TERRAN_COMMANDCENTER) and len(Bot.build_queue(self)) < 1:
                    if Data.start_base(self) == 'NE':
                        x = 25
                        y = 111
                    else:
                        x = 126
                        y = 56
                    builder.build(TERRAN_COMMANDCENTER, Point2DI(x, y))

        if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]) > 1 and \
                len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]) and UNIT_TYPEID.TERRAN_MARAUDER in Data.AGENTUNITS:
            TERRAN_COMMANDCENTER = UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER, self)
            builder = Bot.get_worker(self)
            with suppress(Exception):
                if Bot.econ_check(self, TERRAN_COMMANDCENTER) and len(Bot.build_queue(self)) < 1:
                    if Data.start_base(self) == 'NE':
                        x = 59
                        y = 128
                    else:
                        x = 91
                        y = 40
                    builder.build(TERRAN_COMMANDCENTER, Point2DI(x, y))

    def make_bunker(self):
        """Builds bunkers, OBS: den hoppar över try av nån anledning"""

        TERRAN_BUNKER = UnitType(UNIT_TYPEID.TERRAN_BUNKER, self)
        builder = Bot.get_worker(self)

        marines_in_bunker = []

        if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]) < 2:
            return False

        with suppress(Exception):
            if Bot.econ_check(self, TERRAN_BUNKER) and len(Bot.build_queue(self)) < 1:
                if Data.start_base(self) == 'NE':
                    x = 45
                    y = 102
                else:
                    x = 107
                    y = 67
                builder.build(TERRAN_BUNKER, Point2DI(x, y))

        with suppress(Exception):
            if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BUNKER]) >= 1:
                marines = Data.AGENT_COMBATUNITS['DEFENCE']['CHOKE']
                for marine in marines:
                    if Bot.near(self, Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BUNKER][0].position, marine.position, 4):
                        marines_in_bunker.append(marine)
                    elif marine in marines_in_bunker \
                            and not Bot.near(self, Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BUNKER][0].position,
                                             marine.position, 4):
                        marines_in_bunker.remove(marine)
                    elif not Bot.near(self, Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BUNKER][0].position, marine.position, 4):
                        marine.right_click(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BUNKER][0])
                    continue


    """---  Upgrade Units  ---"""

    def barracks_upgrade(self):
        """Upgrades barracks with reactors or techlabs"""

        if UNIT_TYPEID.TERRAN_BARRACKS not in Data.AGENTUNITS:
            return False

        REACTOR = UnitType(UNIT_TYPEID.TERRAN_BARRACKSREACTOR, self)
        TECHLAB = UnitType(UNIT_TYPEID.TERRAN_BARRACKSTECHLAB, self)

        if UNIT_TYPEID.TERRAN_BARRACKSREACTOR in Data.AGENTUNITS and Bot.econ_check(self, TECHLAB):
            for barrack in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]:
                if barrack.build_percentage == 1 and UNIT_TYPEID.TERRAN_BARRACKSTECHLAB not in Data.AGENTUNITS \
                        and not barrack.is_training:
                    barrack.train(TECHLAB)
                elif TECHLAB in Data.AGENTUNITS:
                    pass

        if Bot.econ_check(self, REACTOR):
            for barrack in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]:
                if barrack.build_percentage == 1 and not barrack.is_training:
                    barrack.train(REACTOR)

    def factory_upgrade(self):
        """Upgrades factories with reactors or techlabs"""

        if UNIT_TYPEID.TERRAN_FACTORY not in Data.AGENTUNITS:
            return False

        REACTOR = UnitType(UNIT_TYPEID.TERRAN_FACTORYREACTOR, self)
        TECHLAB = UnitType(UNIT_TYPEID.TERRAN_FACTORYTECHLAB, self)

        if UNIT_TYPEID.TERRAN_FACTORYTECHLAB in Data.AGENTUNITS and Bot.econ_check(self, TECHLAB):
            for barrack in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_FACTORY]:
                if barrack.build_percentage == 1 and UNIT_TYPEID.TERRAN_FACTORYREACTOR not in Data.AGENTUNITS \
                        and not barrack.is_training:
                    barrack.train(REACTOR)
                elif TECHLAB in Data.AGENTUNITS:
                    pass

        if Bot.econ_check(self, TECHLAB):
            for barrack in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_FACTORY]:
                if barrack.build_percentage == 1 and not barrack.is_training:
                    barrack.train(TECHLAB)

    def upgrade_orbital_command(self):
        """Upgrades bases to orbital commands"""

        with suppress(Exception):
            for base in Data.BASE_HANDLER:
                base = Data.BASE_HANDLER[base]['BASE']

                if base.unit_type.unit_typeid != UNIT_TYPEID.TERRAN_COMMANDCENTER:
                    if self.minerals > 300:
                        base.ability(ABILITY_ID.MORPH_ORBITALCOMMAND)


    """---  Make Units  ---"""

    def make_workers(self):
        """Creates workers"""

        for base in Data.BASE_HANDLER:
            if len(Data.BASE_HANDLER[base]['WORKERS']) < 22:
                BASE = Data.BASE_HANDLER[base]['BASE']
                TERRAN_SCV = UnitType(UNIT_TYPEID.TERRAN_SCV, self)

                if not Bot.econ_check(self, TERRAN_SCV):
                    return False
                if not BASE.is_training:
                    BASE.train(TERRAN_SCV)
            else:
                continue

    def make_marines(self):
        """Makes Marines, Pewpew"""

        TERRAN_MARINE = UnitType(UNIT_TYPEID.TERRAN_MARINE, self)
        REACTOR = UnitType(UNIT_TYPEID.TERRAN_BARRACKSREACTOR, self)

        if UNIT_TYPEID.TERRAN_MARINE in Data.AGENTUNITS:
            if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE]) > 7:
                for barrack in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]:
                    if UNIT_TYPEID.TERRAN_COMMANDCENTER in Data.AGENTUNITS and \
                            len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE]) < 16 and \
                            len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]) > 1:
                        barrack.train(TERRAN_MARINE)
                        barrack.train(TERRAN_MARINE)
                    else:
                        pass

        if UNIT_TYPEID.TERRAN_BARRACKSREACTOR not in Data.AGENTUNITS:
            return False


        elif Bot.econ_check(self, TERRAN_MARINE) and self.minerals > 200:
            for barrack in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]:
                if barrack.build_percentage == 1 and UNIT_TYPEID.TERRAN_BARRACKSREACTOR in Data.AGENTUNITS \
                        and not barrack.is_training and Bot.has_addon(self, barrack, REACTOR):
                    barrack.train(TERRAN_MARINE)
                    barrack.train(TERRAN_MARINE)

        elif UNIT_TYPEID.TERRAN_MARAUDER in Data.AGENTUNITS:
            for barrack in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]:
                if Bot.econ_check(self, TERRAN_MARINE) and Bot.has_addon(self, barrack, REACTOR) \
                        and len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE]) < 37:
                    barrack.train(TERRAN_MARINE)
                    barrack.train(TERRAN_MARINE)

    def make_siege_tanks(self):
        """Creates siege tanks"""

        if UNIT_TYPEID.TERRAN_SIEGETANK in Data.AGENTUNITS:
            if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SIEGETANK]) > 6:
                return False

        if UNIT_TYPEID.TERRAN_FACTORYTECHLAB not in Data.AGENTUNITS:
            return False

        TERRAN_SIEGETANK = UnitType(UNIT_TYPEID.TERRAN_SIEGETANK, self)
        TECHLAB = UnitType(UNIT_TYPEID.TERRAN_FACTORYTECHLAB, self)

        if Bot.econ_check(self, TERRAN_SIEGETANK):
            for factory in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_FACTORY]:
                if factory.build_percentage == 1 and UNIT_TYPEID.TERRAN_FACTORYTECHLAB in Data.AGENTUNITS \
                        and not factory.is_training and Bot.has_addon(self, factory, TECHLAB):
                    factory.train(TERRAN_SIEGETANK)

        if UNIT_TYPEID.TERRAN_COMMANDCENTER in Data.AGENTUNITS and \
                len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]) >=2:
            if Bot.econ_check(self, TERRAN_SIEGETANK) and \
                 UNIT_TYPEID.TERRAN_MARAUDER in Data.AGENTUNITS:
                for factory in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_FACTORY]:
                    if not factory.is_training and Bot.has_addon(self, factory, TECHLAB):
                        if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SIEGETANK]) < 8:
                            factory.train(TERRAN_SIEGETANK)
                        else:
                            return False

    def make_marauders(self):
        """"Makes marauders"""

        TERRAN_MARAUDER = UnitType(UNIT_TYPEID.TERRAN_MARAUDER, self)
        TECHLAB = UnitType(UNIT_TYPEID.TERRAN_BARRACKSTECHLAB, self)

        if UNIT_TYPEID.TERRAN_MARAUDER in Data.AGENTUNITS and len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARAUDER]) > 17:
            return False

        if UNIT_TYPEID.TERRAN_BARRACKS in Data.AGENTUNITS and UNIT_TYPEID.TERRAN_BARRACKSTECHLAB in Data.AGENTUNITS and \
                UNIT_TYPEID.TERRAN_FACTORY in Data.AGENTUNITS:
            for barrack in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]:
                if Bot.econ_check(self, TERRAN_MARAUDER) and Bot.has_addon(self, barrack, TECHLAB):
                    barrack.train(TERRAN_MARAUDER)

    """---  Control Units  ---"""

    def move_marines_to_ramp(self):
        """Moves marines to defence-positions"""

        if UNIT_TYPEID.TERRAN_MARINE in Data.AGENTUNITS:

            ramp = Data.wall_positions(self, 2)

            if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]) == 2:

                if Data.start_base(self) == 'NE':
                    x = 45
                    y = 102
                else:
                    x = 107
                    y = 67

                if 'CHOKE' not in Data.AGENT_COMBATUNITS['DEFENCE']:
                    Data.AGENT_COMBATUNITS['DEFENCE'].update({'CHOKE': []})
                for marine in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE][8:16]:
                    if not Bot.near(self, marine.position, Point2D(x, y), 5):
                        marine.move(Point2D(x, y))
                    elif Bot.near(self, marine.position, Point2D(x, y), 5) and \
                            marine not in Data.AGENT_COMBATUNITS['DEFENCE']['CHOKE']:
                        Data.AGENT_COMBATUNITS['DEFENCE']['CHOKE'].append(marine)
                    else:
                        pass

            with suppress(IndexError):
                if 'RAMP' not in Data.AGENT_COMBATUNITS['DEFENCE']:
                    Data.AGENT_COMBATUNITS['DEFENCE'].update({'RAMP': []})
                for marine in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE][0:8]:
                    if not Bot.near(self, marine.position, Point2D(ramp[0], ramp[1]), 5):
                        marine.move(Point2D(ramp[0], ramp[1]))
                    elif Bot.near(self, marine.position, Point2D(ramp[0], ramp[1]), 5) and \
                            marine not in Data.AGENT_COMBATUNITS['DEFENCE']['RAMP']:
                        Data.AGENT_COMBATUNITS['DEFENCE']['RAMP'].append(marine)
                    else:
                        continue

    def move_siege_to_defend(self):
        """Moves siege tanks to defend-positions"""

        if UNIT_TYPEID.TERRAN_SIEGETANK in Data.AGENTUNITS:

            army = Data.AGENT_COMBATUNITS['DEFENCE']
            ramp = Data.wall_positions(self, 2)

            if Data.start_base(self) == 'NE':

                x = 45
                y = 102
            else:

                x = 107
                y = 67

            if len(army['CHOKE']) >= 4 and len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SIEGETANK]) >= 2:
                for siegetank in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SIEGETANK][:2]:  # [2:4]:
                    if not Bot.near(self, siegetank.position, Point2D(x, y), 5):
                        siegetank.move(Point2D(x, y))
                    elif Bot.near(self, siegetank.position, Point2D(x, y), 5) and \
                            siegetank not in army['CHOKE']:
                        army['CHOKE'].append(siegetank)
                    elif Bot.near(self, siegetank.position, Point2D(x, y), 5):
                        siegetank.ability(ABILITY_ID.MORPH_SIEGEMODE)
                    else:
                        pass

            if len(army['RAMP']) >= 8 and UNIT_TYPEID.TERRAN_SIEGETANK in Data.AGENTUNITS \
                    and len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SIEGETANK]) >= 2:
                for siegetank in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SIEGETANK][2:4]:  # [0:2]:
                    if not Bot.near(self, siegetank.position, Point2D(ramp[0], ramp[1]), 5):
                        siegetank.move(Point2D(ramp[0], ramp[1]))
                    elif Bot.near(self, siegetank.position, Point2D(ramp[0], ramp[1]), 5) and \
                            siegetank not in Data.AGENT_COMBATUNITS['DEFENCE']['RAMP']:
                        Data.AGENT_COMBATUNITS['DEFENCE']['RAMP'].append(siegetank)
                    elif Bot.near(self, siegetank.position, Point2D(ramp[0], ramp[1]), 5):
                        siegetank.ability(ABILITY_ID.MORPH_SIEGEMODE)

                    else:
                        continue

    def send_scout(self) -> None:
        """Sends a scout to gather intel"""

        if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]) > 15 and len(Data.SCOUT) < 1:
            for SCV in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
                if not Bot.is_building(self, SCV) and SCV.is_alive and SCV in Bot.all_miners(self):
                    scout = SCV
                    Data.SCOUT.append(scout)
                    continue

            if Data.start_base(self) == 'NE':
                opponent_base_x = Data.SE_BASE[0]
                opponent_base_y = Data.SE_BASE[1]
            elif Data.start_base(self) == 'SE':
                opponent_base_x = Data.NE_BASE[0]
                opponent_base_y = Data.NE_BASE[1]
            with suppress(Exception):
                scout.move(Point2D(opponent_base_x, opponent_base_y))

        with suppress(Exception):
            for i in range(2):
                pos_x = int(Data.ENEMYUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.x)
                pos_y = int(Data.ENEMYUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.y)

                next_tile = self.building_placer.get_build_location_near \
                    (Point2DI(pos_x, pos_y), UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self), 0, 100)

                scout.move(next_tile)

                if scout.tile_position == next_tile:
                    continue

            scout.move(Point2D(self.start_location_x, self.start_location_y))
            Data.SCOUT.clear()
            return

    def unit_attack_handler(self):
        """Denna ska lägga in units i AGENT_COMBATUNITS så att vi kan attackera m.h.a den."""

        if UNIT_TYPEID.TERRAN_MARINE in Data.AGENTUNITS:
            if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE]) > 16:
                for marine in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE][16:]:
                    if 'MARINE' not in Data.AGENT_COMBATUNITS['OFFENCE']:
                        Data.AGENT_COMBATUNITS['OFFENCE'].update({'MARINE': []})
                    elif marine not in Data.AGENT_COMBATUNITS['OFFENCE']['MARINE']:
                        Data.AGENT_COMBATUNITS['OFFENCE']['MARINE'].append(marine)

        elif UNIT_TYPEID.TERRAN_SIEGETANK in Data.AGENTUNITS:
            if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SIEGETANK]) > 4:
                for siegetank in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SIEGETANK][4:]:
                    if 'SIEGE' not in Data.AGENT_COMBATUNITS['OFFENCE']:
                        Data.AGENT_COMBATUNITS['OFFENCE'].update({'SIEGE': []})
                    elif siegetank not in Data.AGENT_COMBATUNITS['OFFENCE']['SIEGE']:
                        Data.AGENT_COMBATUNITS['OFFENCE']['SIEGE'].append(siegetank)

        elif UNIT_TYPEID.TERRAN_MARAUDER in Data.AGENTUNITS:
            for marauder in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARAUDER]:
                if 'MARAUDER' not in Data.AGENT_COMBATUNITS['OFFENCE']:
                    Data.AGENT_COMBATUNITS['OFFENCE'].update({'MARAUDER': []})
                elif marauder not in Data.AGENT_COMBATUNITS['OFFENCE']['MARAUDER']:
                    Data.AGENT_COMBATUNITS['OFFENCE']['MARAUDER'].append(marauder)

        with suppress(Exception):
            if UNIT_TYPEID.TERRAN_SIEGETANK in Data.AGENTUNITS and UNIT_TYPEID.TERRAN_MARINE in Data.AGENTUNITS and \
                    'MARINE' in Data.AGENT_COMBATUNITS['OFFENCE'] and len(Data.AGENT_COMBATUNITS['OFFENCE']['MARINE']) >= 24:

                if 'ATTACKERS' not in Data.AGENT_COMBATUNITS:
                    Data.AGENT_COMBATUNITS.update({'ATTACKERS': []})

                for marine in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE]:
                    if marine.is_alive and marine.is_idle and marine not in Data.AGENT_COMBATUNITS[
                        'ATTACKERS']:
                        Data.AGENT_COMBATUNITS['ATTACKERS'].append(marine)
                    if not marine.is_alive and marine in Data.AGENT_COMBATUNITS['ATTACKERS']:
                        Data.AGENT_COMBATUNITS['ATTACKERS'].remove(marine)

                for siegetank in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SIEGETANK]:
                    if siegetank.is_alive and siegetank.is_idle and siegetank not in \
                            Data.AGENT_COMBATUNITS['ATTACKERS']:
                        siegetank.ability(ABILITY_ID.MORPH_UNSIEGE)
                        Data.AGENT_COMBATUNITS['ATTACKERS'].append(siegetank)
                        Data.AGENT_COMBATUNITS['RAMP'].remove(siegetank)
                        Data.AGENT_COMBATUNITS['CHOKE'].remove(siegetank)
                    if not siegetank.is_alive and siegetank in Data.AGENT_COMBATUNITS['ATTACKERS']:
                        Data.AGENT_COMBATUNITS['ATTACKERS'].remove(siegetank)

                for marauder in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARAUDER]:
                    if marauder.is_alive and marauder.is_idle and marauder not in \
                            Data.AGENT_COMBATUNITS['ATTACKERS']:
                        Data.AGENT_COMBATUNITS['ATTACKERS'].append(marauder)
                    if not marauder.is_alive and marauder in Data.AGENT_COMBATUNITS['ATTACKERS']:
                        Data.AGENT_COMBATUNITS['ATTACKERS'].remove(marauder)


                for attacker in Data.AGENT_COMBATUNITS['ATTACKERS']:
                    if len(Data.AGENT_COMBATUNITS['ATTACKERS']) > 35:
                        if Data.start_base(self) == 'NE':
                            opponent_base_x = 125.5
                            opponent_base_y = 30.5
                        else:
                            opponent_base_x = 26.5
                            opponent_base_y = 137.5
                        attacker.attack_move(Point2D(opponent_base_x, opponent_base_y))

    def lower_supply(self) -> None:
        """Lowers every supply depot"""

        if UNIT_TYPEID.TERRAN_SUPPLYDEPOT in Data.AGENTUNITS:
            for supply in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SUPPLYDEPOT]:
                if supply.build_percentage == 1:
                    supply.ability(ABILITY_ID.MORPH_SUPPLYDEPOT_LOWER)
                else:
                    continue

    """---  Combat Specific  ---"""

    def defend_base(self):
        """Defends Base (poorly) if attacked"""

        for enemy in Data.enemies_in_base:
             if not enemy.is_alive:
                 Data.enemies_in_base.remove(enemy)
             for i in range(2):
                 for type in Data.AGENT_COMBATUNITS['ALL']:
                     for defender in Data.AGENT_COMBATUNITS['ALL'][type]:
                         if defender.is_alive and defender.is_completed:
                             defender.attack_unit(enemy)

        if len(Data.enemies_in_base) < 2 and Data.AGENTSTATE['PURPOSE'] != 'OFFENCE':
             Bot.state_setter('PURPOSE', 'OFFENCE')

    """///////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                   ~DATA-HANDLING~
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

    """---  Worker Unit Handling  ---"""

    def mineral_worker_handler(self) -> None:
        """Assigns workers to mineral nodes"""

        if UNIT_TYPEID.NEUTRAL_MINERALFIELD not in Data.NEUTRALUNITS:
            return

        for base in Data.BASE_HANDLER:

            mineral_workers = Data.BASE_HANDLER[base]['MINERS']
            base_workers = Data.BASE_HANDLER[base]['WORKERS']
            mineral_deposits = Data.BASE_HANDLER[base]['MINERALS']

            if len(mineral_workers) > 16:
                continue

            for minerals in mineral_deposits:
                next = 0
                for worker in base_workers:
                    if next >= 3:
                        break
                    if worker.is_idle:
                        worker.right_click(minerals)
                        next += 1
                    continue
                continue

    def gas_worker_handler(self) -> None:
        """Assigns workers to refineries"""

        if UNIT_TYPEID.TERRAN_REFINERY in Data.AGENTUNITS:

            for base in Data.BASE_HANDLER:

                for refinery in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]:
                    if refinery.id not in Data.BASE_HANDLER[base]['GAS'] and refinery.is_completed and \
                            Bot.near(self, refinery.position, Data.BASE_HANDLER[base]['BASE'].position, 14):
                        Data.BASE_HANDLER[base]['GAS'].update({refinery.id: []})
                        continue

                mineral_workers = Data.BASE_HANDLER[base]['MINERS']
                base_workers = Data.BASE_HANDLER[base]['WORKERS']
                base_unit = Data.BASE_HANDLER[base]['BASE']  # UNIT

                if len(mineral_workers) < 14:
                    return

                base_refineries = \
                    Bot.get_agentunits_near(self, base_unit, UNIT_TYPEID.TERRAN_REFINERY, 13)

                workers = []
                for refinery in Data.BASE_HANDLER[base]['GAS']:
                    workers.extend(Data.BASE_HANDLER[base]['GAS'][refinery])

                """CLEAR ROGUES"""
                for worker in base_workers:
                    if workers.count(worker) > 1:
                        for i in Data.BASE_HANDLER[base]['GAS']:
                            if worker in Data.BASE_HANDLER[base]['GAS'][i]:
                                Data.BASE_HANDLER[base]['GAS'][i].remove(worker)
                                break
                    if worker.has_target:
                        if worker.target not in base_refineries:
                            continue
                        if worker not in Data.BASE_HANDLER[base]['GAS'][worker.target.id]:
                            worker.move(base_unit.position)
                            break

                """MAIN REFINERY HANDLER"""
                with suppress(Exception):
                    for refinery in base_refineries:
                        if not refinery.is_completed:
                            break
                        if len(Data.BASE_HANDLER[base]['GAS'][refinery.id]) >= 3:
                            continue
                        for worker in base_workers:
                            if worker not in workers:
                                worker.right_click(refinery)
                                return

    def worker_task_handler(self) -> None:
        """Handles all workers and related data"""

        if UNIT_TYPEID.NEUTRAL_MINERALFIELD not in Data.NEUTRALUNITS:
            return

        for base in Data.BASE_HANDLER:

            nearagent = Bot.get_agentunits_near

            refineries = nearagent(self, Data.BASE_HANDLER[base]['BASE'], UNIT_TYPEID.TERRAN_REFINERY, 13)

            gas_workers = []
            if len(Data.BASE_HANDLER[base]['GAS']) > 0:
                for i in Data.BASE_HANDLER[base]['GAS']:
                    gas_workers.extend(Data.BASE_HANDLER[base]['GAS'][i])
            base_workers = Data.BASE_HANDLER[base]['WORKERS']
            base_builders = Data.BASE_HANDLER[base]['BUILDERS']
            base_unit = Data.BASE_HANDLER[base]['BASE']
            mineral_deposits = Data.BASE_HANDLER[base]['MINERALS']

            """///SELECT A WORKER"""
            for worker in base_workers:

                """
                ///FIRST STEP: IS WORKER EVEN VALID?
                """

                """///CLEARS OUT DEAD WORKERS"""
                if not worker.is_alive:
                    Data.BASE_HANDLER[base]['WORKERS'].remove(worker)
                    if worker in Data.BASE_HANDLER[base]['MINERS']:
                        Data.BASE_HANDLER[base]['MINERS'].remove(worker)
                    if worker in gas_workers:
                        for i in refineries:
                            if worker in Data.BASE_HANDLER[base]['GAS'][i.id]:
                                Data.BASE_HANDLER[base]['GAS'][i.id].remove(worker)
                    if worker in base_builders:
                        Data.BASE_HANDLER[base]['BUILDER'].remove(worker)

                """///CLEARS OUT STRAY WORKERS"""
                if Bot.distance_to(self, base_unit, worker) > 20:

                    Data.BASE_HANDLER[base]['WORKERS'].remove(worker)
                    if worker in Data.BASE_HANDLER[base]['MINERS']:
                        Data.BASE_HANDLER[base]['MINERS'].remove(worker)
                    if worker in gas_workers:
                        for i in refineries:
                            if worker in Data.BASE_HANDLER[base]['GAS'][i.id]:
                                Data.BASE_HANDLER[base]['GAS'][i.id].remove(worker)
                    if worker in base_builders:
                        Data.BASE_HANDLER[base]['BUILDERS'].remove(worker)
                    continue

                """///APPENDS BUILDER AND ALSO APPENDS BUILDING TO BUILDQueue"""
                if Bot.is_building(self, worker) and worker not in base_builders:
                    if worker in Data.BASE_HANDLER[base]['MINERS']:
                        Data.BASE_HANDLER[base]['MINERS'].remove(worker)
                    if worker in gas_workers:
                        for i in refineries:
                            if worker in Data.BASE_HANDLER[base]['GAS'][i.id]:
                                Data.BASE_HANDLER[base]['GAS'][i.id].remove(worker)
                    Data.BASE_HANDLER[base]['BUILDERS'].append(worker)
                    continue

                """///REMOVES FINISHED BUILDER"""
                if not Bot.is_building(self, worker) and worker in base_builders:
                    Data.BASE_HANDLER[base]['BUILDERS'].remove(worker)

                """
                ///SECOND STEP: WORKER IS (MOST LIKELY) COLLECTING A RESOURCE
                """

                if not worker.is_idle and worker.has_target:

                    """///APPEND WORKER TO CORRESPONDING TASK-LIST"""
                    if worker.target in mineral_deposits and worker not in Data.BASE_HANDLER[base]['MINERS']:
                        Data.BASE_HANDLER[base]['MINERS'].append(worker)
                        continue
                    if worker.target in refineries and worker not in gas_workers:
                        for i in refineries:
                            if i.id not in Data.BASE_HANDLER[base]['GAS']:
                                Data.BASE_HANDLER[base]['GAS'].update({i.id: []})
                            if len(Data.BASE_HANDLER[base]['GAS'][i.id]) < 3:
                                Data.BASE_HANDLER[base]['GAS'][i.id].append(worker)
                            continue

                    """///REMOVE WORKERS FROM LISTS WHICH DOES NOT CORRESPOND TO TASK"""
                    if (worker.target != base_unit and worker.target not in mineral_deposits) \
                            and worker in Data.BASE_HANDLER[base]['MINERS']:
                        Data.BASE_HANDLER[base]['MINERS'].remove(worker)
                        continue
                    if worker.target != base_unit and worker.target not in refineries and worker in gas_workers:
                        for i in refineries:
                            with suppress(Exception):
                                if worker in Data.BASE_HANDLER[base]['GAS'][i.id]:
                                    Data.BASE_HANDLER[base]['GAS'][i.id].remove(worker)
                                continue

                """
                ///THIRD STEP: WORKER HAS A TASK BUT IS IDLE
                """

                if worker.is_idle:

                    """///REASSIGN IDLE WORKERS TO NEAREST RESOURCE NODE FOR CORRESPONDING TASK"""
                    distance = 100
                    if worker in Data.BASE_HANDLER[base]['MINERS']:
                        for minerals in mineral_deposits:
                            if distance < 20:
                                worker.right_click(minerals)
                                break
                            distance_to_resource = Bot.distance_to(self, worker, minerals)
                            if distance_to_resource < distance:
                                distance = distance_to_resource
                    elif worker in gas_workers:
                        for i in refineries:
                            if distance < 20 and worker in Data.BASE_HANDLER[base]['GAS'][i.id]:
                                worker.right_click(i)
                                break
                            distance_to_resource = Bot.distance_to(self, worker, i)
                            if distance_to_resource < distance:
                                distance = distance_to_resource
                    else:
                        for minerals in mineral_deposits:
                            if distance < 20:
                                worker.right_click(minerals)
                                break
                            distance_to_resource = Bot.distance_to(self, worker, minerals)
                            if distance_to_resource < distance:
                                distance = distance_to_resource
                        continue
            continue

    def stray_worker_handling(self) -> None:
        """Denna fungerar inte som den ska. Har försökt en mängd olika metoder utan framgång :c"""

        """Sätt allt i en for-loop som går igenom alla baser så funkar det! Alternativt använd Data.NEUTRALUNITS        
        /ERIK """

        for worker in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
            if not worker.is_idle or Bot.is_building(self, worker):
                continue
            if worker not in Bot.all_workers(self) and Bot.near(self,
                                                                Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BUNKER][0].position,
                                                                worker.position, 5):
                worker.move(Data.BASE_HANDLER[base]['BASE'].position)
            elif worker.is_idle:
                if Data.start_base(self) == 'NE':
                    x = 25
                    y = 111
                    worker.move(Point2D(x - 3, y + 2))
                else:
                    x = 126
                    y = 56
                    worker.move(Point2D(x + 3, y - 2))

    def base_handler(self) -> None:
        """Handles data in Data.BASE_HANDLER"""

        for x in self.base_location_manager.get_occupied_base_locations(0):
            for base in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]:

                if not Bot.near(self, x.position, base.position, 10):
                    continue

                def get_mineral_fields(self, base_location: BaseLocation):
                    """ Given a base_location, this method will find and return a list of all mineral fields (Unit) for that base """
                    mineral_fields = []
                    for mineral_field in base_location.minerals:
                        for unit in self.get_all_units():
                            if unit.unit_type.is_mineral \
                                    and mineral_field.tile_position.x == unit.tile_position.x \
                                    and mineral_field.tile_position.y == unit.tile_position.y:
                                mineral_fields.append(unit)
                    return mineral_fields

                def get_geysers(self, base_location: BaseLocation):
                    geysers = []
                    for geyser in base_location.geysers:
                        for unit in self.get_all_units():
                            if unit.unit_type.is_geyser \
                                    and geyser.tile_position.x == unit.tile_position.x \
                                    and geyser.tile_position.y == unit.tile_position.y:
                                geysers.append(unit)
                    return geysers

                if base.id not in Data.BASE_HANDLER and \
                        math.sqrt((base.position.x - x.position.x) ** 2 + (base.position.y - x.position.y) ** 2) < 5:
                    Data.BASE_HANDLER.update({base.id: {'MINERS': [], 'GAS': {}, 'WORKERS': [], 'BUILDERS': [],
                                                        'BASE': base, 'MINERALS': get_mineral_fields(self, x),
                                                        'GEYSERS': get_geysers(self, x)}})
                    return

        for base in Data.BASE_HANDLER:

            base_unit = Data.BASE_HANDLER[base]['BASE']
            ALL_WORKERS = Bot.all_workers(self)

            if not base_unit.is_completed:
                continue

            for worker in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
                if worker not in ALL_WORKERS:
                    if worker in Bot.get_agentunits_near(self, base_unit, UNIT_TYPEID.TERRAN_SCV, 13):
                        Data.BASE_HANDLER[base]['WORKERS'].append(worker)
                else:
                    continue

    """---  Combat Unit Handling  ---"""

    """---  General Unit Handling  ---"""

    def unit_death_handler(self):
        """Removes dead units from AGENTUNITS Dictionary"""

        """
        BEHÖVER UPPDATERAS SÅ ATT DET FUNKAR MED NYA DATATYPERNA      
        """

        for types in Data.AGENTUNITS:
            for unit in Data.AGENTUNITS[types]:
                if not unit.is_alive:
                    Data.AGENT_LOST[0] += unit.unit_type.mineral_price
                    Data.AGENT_LOST[1] += unit.unit_type.gas_price
                    Data.AGENTUNITS[types].remove(unit)

        for types in Data.ENEMYUNITS:
            for unit in Data.ENEMYUNITS[types]:
                if not unit.is_alive:
                    Data.ENEMY_LOST[0] += unit.unit_type.mineral_price
                    Data.ENEMY_LOST[1] += unit.unit_type.gas_price
                    Data.ENEMYUNITS[types].remove(unit)

        for types in Data.NEUTRALUNITS:
            for unit in Data.NEUTRALUNITS[types]:
                if not unit.is_alive:
                    Data.NEUTRALUNITS[types].remove(unit)

        for types in Data.AGENTUNITS:
            if types in Data.AGENT_COMBATUNITS:
                for unit in Data.AGENT_COMBATUNITS[types]:
                    if not unit.is_alive:
                        Data.AGENT_COMBATUNITS[types].remove(unit)

    def find_expired_minerals(self):
        """Finds and removes expired minerals from each base"""

        for base_manager, base_handler in \
                zip(self.base_location_manager.get_occupied_base_locations(0), Data.BASE_HANDLER):
            for manager_mineral, base_mineral in zip(base_manager.mineral_fields, base_handler[base_handler]['MINERALS']):
                if not manager_mineral.is_alive and manager_mineral == base_mineral:
                    base_handler[base_handler]['MINERALS'].remove(manager_mineral)

    """///////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                      ~RETURNERS~
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

    """---  Distance Related    ---"""

    def get_agentunits_near(self, Unit1: Unit, unit_typeID, distance) -> list:
        """Returns a list of agents units near another unit"""

        try:
            from_x = Unit1.position.x
            from_y = Unit1.position.y

            units_near = []

            for unit in Data.AGENTUNITS[unit_typeID]:
                to_x = unit.position.x
                to_y = unit.position.y

                if math.sqrt((from_x - to_x) ** 2 + (from_y - to_y) ** 2) < distance:
                    units_near.append(unit)
                else:
                    continue
            return units_near
        except:
            return []

    def get_neutralunits_near(self, Unit1: Unit, unit_typeID, distance) -> list:
        """returns a list of neutral units near a chosen unit"""

        from_x = Unit1.position.x
        from_y = Unit1.position.y

        if unit_typeID == UNIT_TYPEID.NEUTRAL_MINERALFIELD or UNIT_TYPEID.NEUTRAL_MINERALFIELD750 or \
                UNIT_TYPEID.NEUTRAL_SPACEPLATFORMGEYSER or UNIT_TYPEID.NEUTRAL_VESPENEGEYSER:

            base_neutrals = []
            for base in self.base_location_manager.get_occupied_base_locations(0):
                if unit_typeID == UNIT_TYPEID.NEUTRAL_MINERALFIELD or UNIT_TYPEID.NEUTRAL_MINERALFIELD750:
                    base_neutrals.extend(base.minerals)
                if UNIT_TYPEID.NEUTRAL_SPACEPLATFORMGEYSER or UNIT_TYPEID.NEUTRAL_VESPENEGEYSER:
                    base_neutrals.extend(base.geysers)
            send_neutrals = []
            for unit in base_neutrals:
                to_x = unit.position.x
                to_y = unit.position.y
                if math.sqrt((from_x - to_x) ** 2 + (from_y - to_y) ** 2) < distance:
                    send_neutrals.append(unit)
            return send_neutrals

        else:
            if unit_typeID not in Data.NEUTRALUNITS:
                return []
            for unit in Data.NEUTRALUNITS[unit_typeID]:
                to_x = unit.position.x
                to_y = unit.position.y

                if math.sqrt((from_x - to_x) ** 2 + (from_y - to_y) ** 2) < distance:
                    units_near.append(unit)
                else:
                    continue
            return units_near

    def near(self, pos: Point2D, unit_pos: Point2D, radius: int) -> bool:
        """Returns whether or not a unit is close to another unit"""

        distance = self.map_tools.get_ground_distance(unit_pos, pos)
        if distance <= radius:
            return True
        else:
            return False

    def distance_to(self, unit1, unit2) -> float:
        """Returns distance from a unit to another unit"""

        return math.sqrt((unit1.position.x - unit2.position.x) ** 2 + (unit1.position.y - unit2.position.y) ** 2)

    """---  State Related   ---"""

    def econ_check(self, unit_type: UnitType) -> bool:
        """Asserts that agents economy allows the requested build/train command"""

        return self.minerals >= unit_type.mineral_price \
               and self.gas >= unit_type.gas_price \
               and self.max_supply - self.current_supply >= unit_type.supply_required

    def supply_check(self) -> bool:
        """Checks to see if supply is running low"""

        if UNIT_TYPEID.TERRAN_BARRACKS in Data.AGENTUNITS:
            if (self.max_supply - self.current_supply) < 3 * len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]):
                return True
            else:
                return False
        else:
            if (self.max_supply - self.current_supply) < 4:
                return True
            else:
                return False

    """---  Building Related    ---"""

    def build(self, building: UnitType, near: Unit, range) -> None:
        """build(self: Bot, building: library.UnityType, near: library.Unit) -> None"""

        if Bot.build_queue_open(self) and Bot.econ_check(self, building):
            x = near.position.x
            y = near.position.y
            pos = Bot.find_build_target(self, x, y, building, range, 10)
            if self.building_placer.can_build_here(pos.x, pos.y, building):
                builder = Bot.get_worker(self)
                builder.build(building, pos)
                return
        else:
            return

    def build_queue_open(self) -> bool:
        """Returns true if build queue is < 3"""

        if len(Bot.build_queue(self)) < 2:
            return True
        else:
            return False

    def build_queue(self) -> list:
        """Handles build queue, returns list of all SCVs that are currently building something"""

        build_queue = []

        for base in Data.BASE_HANDLER:
            for builder in (Data.BASE_HANDLER[base]['BUILDERS'] + Data.QUEUED_BUILDINGS):
                if builder not in build_queue:
                    build_queue.append(builder)

        return build_queue

    def clear_build_list(self) -> None:
        """Clears builder-list every once in a while"""

        "DEPRECIATED"

        if len(Data.BUILDER) > 2:

            for builder in Data.BUILDER:
                if not Bot.is_building(self, builder) or not builder.is_alive or builder.is_idle:
                    Data.BUILDER.remove(builder)

    def queued_building_checker(self) -> None:
        """Checks queued buildings"""

        for builder in Data.QUEUED_BUILDINGS:
            if Bot.is_building(self, builder):
                Data.QUEUED_BUILDINGS.remove(builder)
                Data.BUILDER.append(builder)
            else:
                continue

    def find_build_target(self, pos_x, pos_y, unit_to_build, space, tilerange) -> Point2D:
        """Finds nearest buildable tile to a building"""

        for i in range(tilerange):
            shortplace = self.building_placer.get_build_location_near
            build_pos = shortplace(Point2DI(int(pos_x), int(pos_y)), unit_to_build, space, i * 10)
            if self.building_placer.can_build_here(build_pos.x, build_pos.y, unit_to_build):
                return build_pos

    """---  Unit Related    ---"""

    def is_building(self, unit) -> bool:
        """Checks if selected worker is currently building something"""

        if unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_REFINERY, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_REFINERY, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_ARMORY, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_BUNKER, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_ENGINEERINGBAY, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_FACTORY, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_GHOSTACADEMY, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_SENSORTOWER, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_STARPORT, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_MISSILETURRET, self)) or \
                unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_FUSIONCORE, self)):
            return True
        else:
            return False

    def is_building_name(self, unit) -> str:
        """Returns the name of the building the selected unit is building"""

        if unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)):
            return 'Barracks'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)):
            return 'Supply Depot'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_REFINERY, self)):
            return 'Refinery'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER, self)):
            return 'Command Center'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_ARMORY, self)):
            return 'Armory'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_BUNKER, self)):
            return 'Bunker'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_ENGINEERINGBAY, self)):
            return 'Engineering bay'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_FACTORY, self)):
            return 'Factory'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_GHOSTACADEMY, self)):
            return 'Ghost Academy'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_SENSORTOWER, self)):
            return 'Sensor Tower'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_STARPORT, self)):
            return 'Star Port'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_MISSILETURRET, self)):
            return 'Missile Turret'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_FUSIONCORE, self)):
            return 'Fusion Core'
        else:
            return 'None'

    def is_building_UNIT_TYPEID(self, unit) -> UNIT_TYPEID:
        """Returns the name of the building the selected unit is building"""

        if unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)):
            return UNIT_TYPEID.TERRAN_BARRACKS
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)):
            return UNIT_TYPEID.TERRAN_SUPPLYDEPOT
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_REFINERY, self)):
            return UNIT_TYPEID.TERRAN_REFINERY
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER, self)):
            return UNIT_TYPEID.TERRAN_COMMANDCENTER
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_ARMORY, self)):
            return UNIT_TYPEID.TERRAN_ARMORY
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_BUNKER, self)):
            return UNIT_TYPEID.TERRAN_BUNKER
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_ENGINEERINGBAY, self)):
            return UNIT_TYPEID.TERRAN_ENGINEERINGBAY
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_FACTORY, self)):
            return UNIT_TYPEID.TERRAN_FACTORY
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_GHOSTACADEMY, self)):
            return UNIT_TYPEID.TERRAN_GHOSTACADEMY
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_SENSORTOWER, self)):
            return UNIT_TYPEID.TERRAN_SENSORTOWER
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_STARPORT, self)):
            return UNIT_TYPEID.TERRAN_STARPORT
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_MISSILETURRET, self)):
            return UNIT_TYPEID.TERRAN_MISSILETURRET
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_FUSIONCORE, self)):
            return UNIT_TYPEID.TERRAN_FUSIONCORE
        else:
            return None

    def get_worker_near_base(self, base) -> list:
        """Gets arbitrary available worker"""

        for SCV in Data.BASE_HANDLER[base]['MINERS']:
            if not Bot.is_building(self, SCV) and SCV.is_alive:
                return SCV
            else:
                continue

        return Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV][2]

    def get_worker(self) -> UNIT_TYPEID.TERRAN_SCV:
        """Gets arbitrary available worker"""

        for SCV in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
            if SCV.has_target:
                if SCV.target in (Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_MINERALFIELD]
                                  or Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_MINERALFIELD750]):
                    return SCV
            else:
                continue

        return Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV][2]

    def get_my_producers(self, unit_type: UnitType) -> list:  # NOT IMPLEMENTED
        """ Returns a list of units which can build or train units of type unit_type """

        producers = []
        type_data = self.tech_tree.get_data(unit_type)
        what_builds = type_data.what_builds

        for unit in self.get_my_units():
            if unit.unit_type in what_builds:
                producers.append(unit)

        return producers

    def is_worker_collecting_gas(self, worker):
        """ Returns: True if a unit 'worker' is collecting gas, False otherwise """

        def squared_distance(unit_1, unit_2):
            a = self.minerals
            p1 = unit_1.position
            p2 = unit_2.position
            return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

        for refinery in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]:
            if refinery.is_completed and squared_distance(worker, refinery) < 2 ** 2:
                return True

    def has_addon(self, candidate: Unit, addon_type: UnitType) -> bool:
        """
        Looks through all units and checks if there is an addon of the type addon_type nearby to the supplied candidate.

        :return: True if the unit "candindate" has an addon of the type "addon_type"
        """
        for unit in self.get_my_units():
            if unit.unit_type.is_addon and unit.is_alive and unit.is_completed \
                    and unit.unit_type == addon_type \
                    and abs(unit.position.x - candidate.position.x) < 3 \
                    and abs(unit.position.y - candidate.position.y) < 3:
                return True

        return False

    def all_workers(self) -> list:
        """returns list of all agent workers"""

        all_workers = []

        for base in Data.BASE_HANDLER:
            if not Data.BASE_HANDLER[base]['BASE'].is_completed:
                continue
            all_workers.extend(Data.BASE_HANDLER[base]['WORKERS'])

        return all_workers

    def all_miners(self) -> list:
        """Returns list of all agent workers currently mining minerals"""

        all_miners = []
        for base in Data.BASE_HANDLER:
            if not Data.BASE_HANDLER[base]['BASE'].is_completed:
                continue
            all_miners.extend(Data.BASE_HANDLER[base]['MINERS'])

        return all_miners

    def all_gas_workers(self) -> list:
        """returns list of all agent workers currently gathering gas"""

        all_gas_workers = []
        for base in Data.BASE_HANDLER:
            if not Data.BASE_HANDLER[base]['BASE'].is_completed:
                continue
            for i in Data.BASE_HANDLER[base]['GAS']:
                all_gas_workers.extend(Data.BASE_HANDLER[base]['GAS'][i])

        return all_gas_workers

    """///////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                   ~STATE HANDLERS~
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

    """---  Strategy Pickers  ---"""

    def state_setter(self, state, routine) -> None:
        """Sets AgentState"""

        Data.AGENTSTATE[state] = routine
        return

    """---  Game Listeners  ---"""

    def state_listener(self) -> None:
        """listens to current AgentState"""

        if UNIT_TYPEID.TERRAN_BARRACKS in Data.AGENTUNITS \
                and UNIT_TYPEID.TERRAN_ENGINEERINGBAY in Data.AGENTUNITS \
                and UNIT_TYPEID.TERRAN_BARRACKSTECHLAB in Data.AGENTUNITS \
                and Data.AGENTSTATE['STATE'] == 0:
            if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]) > 2:
                Bot.state_setter('STATE', 1)

    def enemy_attacking(self) -> None:
        """Returns true if opponent is attacking a base"""

        if len(Data.enemies_in_base) > 3:
            Bot.state_setter('PURPOSE', 'DEFEND')
            return True

    def base_listener(self) -> None:
        """listens to base for enemy units"""

        for enemy_types in Data.ENEMYUNITS:
            for enemy in Data.ENEMYUNITS[enemy_types]:
                for base in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]:

                    distance_x = abs(enemy.position.x - base.position.x)
                    distance_y = abs(enemy.position.y - base.position.y)

                    if distance_x < 20 and distance_y < 20 and enemy not in Data.enemies_in_base:
                        Data.enemies_in_base.append(enemy)
                    else:
                        if enemy in Data.enemies_in_base:
                            Data.enemies_in_base.remove(enemy)

    """///////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                      ~GRAPHICS~
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

    """---  Unit Tags  ---"""

    def unit_debug(self) -> None:
        """"Prints a debug message over agents units, also adds each unit to gamestate.AGENTUNITS dictionary"""

        for unit in self.get_my_units():

            if unit.unit_type.unit_typeid in Data.AGENTUNITS:
                if unit in Data.AGENTUNITS[unit.unit_type.unit_typeid]:
                    continue

            if unit.player == PLAYER_SELF:
                type = unit.unit_type.unit_typeid

                if unit.unit_type.is_combat_unit:
                    if type not in Data.AGENT_COMBATUNITS:
                        Data.AGENT_COMBATUNITS.update({type: [unit]})
                    elif unit not in Data.AGENT_COMBATUNITS[type]:
                        Data.AGENT_COMBATUNITS[type].append(unit)

                if type not in Data.AGENTUNITS:
                    Data.AGENTUNITS.update({type: [unit]})
                elif unit not in Data.AGENTUNITS[type]:
                    Data.AGENTUNITS[type].append(unit)


    def neutral_debug(self) -> None:
        """"Prints a debug message over neutral units, also adds each unit to gamestate.AGENTUNITS dictionary"""

        if not Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][-1].is_completed:
            return

        for base in self.base_location_manager.get_occupied_base_locations(0):

            for mineral in base.mineral_fields:
                if not mineral.unit_type.is_mineral:
                    continue
                type = mineral.unit_type.unit_typeid
                if type not in Data.NEUTRALUNITS:
                    Data.NEUTRALUNITS.update({type: []})
                elif mineral not in Data.NEUTRALUNITS[type]:
                    Data.NEUTRALUNITS[type].append(mineral)

            for geyser in base.geysers:
                if not geyser.unit_type.is_geyser:
                    continue
                type = geyser.unit_type.unit_typeid
                if type not in Data.NEUTRALUNITS:
                    Data.NEUTRALUNITS.update({type: []})
                elif geyser not in Data.NEUTRALUNITS[type]:
                    Data.NEUTRALUNITS[type].append(geyser)

    def enemy_debug(self) -> None:
        """Gathers enemy units and adds them to Data.ENEMYUNITS"""

        for unit in self.get_all_units():

            if unit.player == PLAYER_ENEMY:

                type = unit.unit_type.unit_typeid

                if type not in Data.ENEMYUNITS:
                    Data.ENEMYUNITS.update({type: [unit]})
                elif unit not in Data.ENEMYUNITS[type]:
                    Data.ENEMYUNITS[type].append(unit)


    """---  Real Time Info  ---"""

    def unit_task(self) -> None:
        """Handles unit tags"""

        task = ""
        mapdraw = self.map_tools.draw_text_screen
        for unit in self.get_my_units():

            if unit.unit_type.is_building:
                if unit in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]:
                    continue

            if not unit.unit_type.is_building:

                if unit.unit_type.is_worker:
                    if unit in Bot.all_miners(self):
                        task = "Mining Minerals"

                    elif unit in Bot.all_gas_workers(self):
                        task = "Collecting Gas"

                    elif unit in Bot.build_queue(self):
                        task = str('Building:' + Bot.is_building_name(self, unit))

                    else:
                        task = "ERROR 404 - Task Not Found"

                elif unit.unit_type.is_combat_unit:

                    task = str("IDLE")

                    for orders in Data.AGENT_COMBATUNITS['DEFENCE']:
                        if unit in Data.AGENT_COMBATUNITS['DEFENCE'][orders]:
                            task = str('DEFEND' + " : " + orders)

                else:
                    task = ''

                type = unit.unit_type.unit_typeid
                pos = Data.AGENTUNITS[type].index(unit)
                self.map_tools.draw_text(unit.position, str(task) + " i: " + str(pos), Color(255, 255, 255))

    def session_info(self, runtime, performance) -> None:
        """Draws info about current session on screen"""

        mapdraw = self.map_tools.draw_text_screen

        AGENTPRINT = 0.02

        mapdraw(0.02, 0.007, "----AGENTDATA----", Color(255, 255, 255))
        mapdraw(0.02, AGENTPRINT, "EXPANSIONS: " + str(len(Data.BASE_HANDLER)), Color(255, 255, 255))
        AGENTPRINT += 0.015
        mapdraw(0.02, AGENTPRINT, "MINERS: " + str(len(Bot.all_miners(self))), Color(255, 255, 255))
        AGENTPRINT += 0.015
        mapdraw(0.02, AGENTPRINT, "GAS: " + str(len(Bot.all_gas_workers(self))), Color(255, 255, 255))
        AGENTPRINT += 0.015
        mapdraw(0.02, AGENTPRINT, "WORKERS: " + str(len(Bot.all_workers(self))), Color(255, 255, 255))
        AGENTPRINT += 0.015

        buildings = []
        for unit in Bot.build_queue(self):
            building = Bot.is_building_name(self, unit)
            buildings.append(building)
        for e in buildings:
            mapdraw(0.02, AGENTPRINT, "BUILDING: " + str(e) + ' x' + str(buildings.count(e)), Color(255, 255, 255))
            if buildings.count(e) > 1:
                continue
            AGENTPRINT += 0.015


        # mapdraw(0.02, 0.046, "Gas Spent:" + str(Data.total_value(self)[1]), Color(100, 200, 255))
        # mapdraw(0.02, 0.059, "Minerals Lost:" + str(Data.AGENT_LOST[0]), Color(100, 200, 255))
        # mapdraw(0.02, 0.072, "Gas Lost:" + str(Data.AGENT_LOST[1]), Color(100, 200, 255))
        # mapdraw(0.02, 0.085, "Workers:" + str(len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV])), Color(100, 200, 255))

        # mapdraw(0.02, 0.230, "----ENEMYDATA----", Color(255, 100, 0))
        # mapdraw(0.02, 0.243, "Enemy Minerals Spent:" + str(Data.enemy_total_value(self)[0]), Color(255, 100, 0))
        # mapdraw(0.02, 0.256, "Enemy Gas Spent:" + str(Data.enemy_total_value(self)[1]), Color(255, 100, 0))
        # mapdraw(0.02, 0.269, "Enemy Minerals Lost:" + str(Data.ENEMY_LOST[0]), Color(255, 100, 0))
        # mapdraw(0.02, 0.282, "Enemy Gas Lost:" + str(Data.ENEMY_LOST[1]), Color(255, 100, 0))

        # mapdraw(0.275, 0.72, str(Data.AGENTSTATE), Color(100, 200, 255))

        # mapdraw(0.02, 0.60, "Minerals:" + str(self.minerals), Color(100, 200, 255))
        # mapdraw(0.02, 0.615, "Gas:" + str(self.gas), Color(100, 200, 255))
        # mapdraw(0.02, 0.63, "Unused Supply:" + str(self.max_supply - self.current_supply), Color(100, 200, 255))
        mapdraw(0.02, 0.645, "Runtime " + str(round(runtime, 0)), Color(100, 200, 255))
        mapdraw(0.02, 0.66, "Performance: " + str(int(performance)) \
                + " Loops / Second on Frame: " + str(self.current_frame), Color(100, 200, 255))

    """---  Map Tags  ---"""

    def map_info(self) -> None:
        """Draws key-location names on map"""

        maptext = self.map_tools.draw_text
        ramp = Data.wall_positions(self, 2)
        maptext(Point2D(ramp[0], ramp[1]), str("Defence position"), Color(255, 255, 255))

        for b in Data.BASE_HANDLER:
            base = Data.BASE_HANDLER[b]['BASE']
            self.map_tools.draw_circle(base.position, 13, Color(100, 200, 255))


"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
"""//////////////////////////////////////////////////      END       ///////////////////////////////////////////////"""
"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

"""///////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                      TEST METHODS... (Aka, junk)
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

