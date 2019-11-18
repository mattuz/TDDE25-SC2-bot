from library import *
from data import *
from extra import *
from main import *
from Simplified import *


# from Simplified import *


class Bot(MyAgent):
    """ Main method handler for bot features. Inherits MyAgent """

    Debug_info = [0]

    def __init__(self):
        pass

    """//////////////COMMANDS///////////////"""

    def mineral_worker_handler(self):
        """Handles Worker-states"""

        """FIXA SÅ SKITEN KLICKAR LOL"""

        if UNIT_TYPEID.NEUTRAL_MINERALFIELD not in Data.NEUTRALUNITS:
            return

        mineral_deposits = Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_MINERALFIELD] #+ Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_MINERALFIELD750]
        base = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]

        for worker in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:

            if worker.is_idle and worker.is_alive:

                if len(Data.MINERAL_WORKER) < \
                        (len(Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_MINERALFIELD]) * 2
                         + len(Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_MINERALFIELD750]) * 2):
                    for minerals in mineral_deposits:
                        # minerals = random.choice(mineral_deposits)
                        worker.right_click(minerals)

                        # if worker not in Data.MINERAL_WORKER:
                        #     Data.MINERAL_WORKER.append(worker)
                        #     if worker in Data.GAS_WORKER:
                        #         Data.GAS_WORKER.remove(worker)
                        #     Bot.Debug_info[0] = "Added " + str(worker) + " to mineral line"
                        #     return

                #     for gas in refineries:
                #         if gas not in Data.WORKERS_REFINERIES:
                #             Data.WORKERS_REFINERIES.update({gas: []})
                #         if len(Data.GAS_WORKER) < (len(refineries) * 3) and \
                #                 Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY][-1].is_completed:
                #             if not Bot.is_worker_collecting_gas(self, worker):
                #                 for refineries in range(len(Data.WORKERS_REFINERIES)):
                #                     if len(refineries) < 3:
                #                         if worker not in Data.WORKERS_REFINERIES[gas]:
                #                             Data.WORKERS_REFINERIES[gas].append(worker)
                #                         worker.right_click(gas)
                #
                #         if worker not in Data.GAS_WORKER:
                #             Data.GAS_WORKER.append(worker)
                #             if worker in Data.MINERAL_WORKER:
                #                 Data.MINERAL_WORKER.remove(worker)
                #             Bot.Debug_info[0] = "Added " + str(worker) + " go gas line"
                #             return
            # else:
            #     if worker.is_alive and worker.has_target and not worker.is_idle and not Bot.is_building(self, worker):
            #
            #         if worker.target in mineral_deposits and worker not in Data.MINERAL_WORKER:
            #             Data.MINERAL_WORKER.append(worker)
            #             Bot.Debug_info[0] = "Added " + str(worker) + " to mineral line"
            #             return
            #         elif worker.target in refineries and worker not in Data.GAS_WORKER:
            #             Data.GAS_WORKER.append(worker)
            #             Bot.Debug_info[0] = "Added " + str(worker) + " go gas line"
            #             return
            #         elif worker.target not in mineral_deposits \
            #                 and worker.target not in base and worker in Data.MINERAL_WORKER:
            #             Data.MINERAL_WORKER.remove(worker)
            #             Bot.Debug_info[0] = "Removed " + str(worker) + " from mineral line"
            #             return
            #         elif worker.target not in refineries \
            #                 and worker.target not in base and worker in Data.GAS_WORKER:
            #             Data.GAS_WORKER.remove(worker)
            #             Bot.Debug_info[0] = ["Removed" + str(worker) + "from gas line"]
            #             return
            #         elif worker.target in mineral_deposits and len(Data.MINERAL_WORKER) > 16 \
            #                 and len(Data.GAS_WORKER) < (len(refineries) * 3):
            #             for gas in refineries:
            #                 if not Bot.is_worker_collecting_gas(self, worker):
            #                     pass
            #                     #worker.right_click(gas)
            #                 if worker in Data.MINERAL_WORKER:
            #                     Data.MINERAL_WORKER.remove(worker)
            #                 Data.GAS_WORKER.append(worker)
            #                 Bot.Debug_info[0] = ["Switched" + str(worker) + "to gas"]
            #                 return
            #
            # if not Bot.is_building(self, worker):
            #     if not worker.has_target and worker in Data.MINERAL_WORKER and worker.is_idle:
            #         Data.MINERAL_WORKER.remove(worker)
            #         return
            #     if not worker.has_target and worker in Data.GAS_WORKER and worker.is_idle:
            #         Data.GAS_WORKER.remove(worker)
            #         return
            # elif Bot.is_building(self, worker):
            #     if worker in Data.MINERAL_WORKER:
            #         Data.MINERAL_WORKER.remove(worker)
            #         return
            #     if worker in Data.GAS_WORKER:
            #         Data.GAS_WORKER.remove(worker)
            #         return

    def worker_task_checker(self):

        if UNIT_TYPEID.TERRAN_REFINERY not in Data.AGENTUNITS:
            refineries = []
        else:
            refineries = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]

        mineral_deposits = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF).minerals
        base = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]

        for worker in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:

            if worker.is_alive and worker.has_target and not worker.is_idle and not Bot.is_building(self, worker):
                if worker.target in mineral_deposits and worker not in Data.MINERAL_WORKER:
                    Data.MINERAL_WORKER.append(worker)
                    Bot.Debug_info[0] = "Added " + str(worker) + " to mineral line"
                    return
                elif worker.target in refineries and worker not in Data.GAS_WORKER:
                    Data.GAS_WORKER.append(worker)
                    Bot.Debug_info[0] = "Added " + str(worker) + " go gas line"
                    return
                elif worker.target not in mineral_deposits \
                        and worker.target not in base and worker in Data.MINERAL_WORKER:
                    Data.MINERAL_WORKER.remove(worker)
                    Bot.Debug_info[0] = "Removed " + str(worker) + " from mineral line"
                    return
                elif worker.target not in refineries \
                        and worker.target not in base and worker in Data.GAS_WORKER:
                    Data.GAS_WORKER.remove(worker)
                    Bot.Debug_info[0] = ["Removed" + str(worker) + "from gas line"]
                    return
            elif not Bot.is_building(self, worker):
                if not worker.has_target and worker in Data.MINERAL_WORKER and worker.is_idle:
                    Data.MINERAL_WORKER.remove(worker)
                    return
                if not worker.has_target and worker in Data.GAS_WORKER and worker.is_idle:
                    Data.GAS_WORKER.remove(worker)
                    return
            elif Bot.is_building(self, worker):
                if worker in Data.MINERAL_WORKER:
                    Data.MINERAL_WORKER.remove(worker)
                    return
                if worker in Data.GAS_WORKER:
                    Data.GAS_WORKER.remove(worker)
                    return

    def gas_worker_handler(self):
        """ Puts workers in refineries"""

        if UNIT_TYPEID.TERRAN_REFINERY in Data.AGENTUNITS:

            workers = []

            if len(Data.GAS_WORKER) == 3 * len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]):
                return True

            if len(Data.GAS_WORKER) > 3 * len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]):
                all_in_refinery = []
                for i in Data.WORKERS_REFINERIES:
                    for worker in Data.WORKERS_REFINERIES[i]:
                        all_in_refinery.append(worker)
                for worker in Data.GAS_WORKER:
                    if worker in Data.GAS_WORKER and worker not in all_in_refinery:
                        worker.right_click(Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_MINERALFIELD][0])

            for refinery in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]:
                if refinery.id not in Data.WORKERS_REFINERIES and refinery.is_completed:
                    Data.WORKERS_REFINERIES.update({refinery.id: []})
                    return
                elif refinery.id in Data.WORKERS_REFINERIES:
                    try:
                        if len(Data.WORKERS_REFINERIES[refinery.id]) <= 2 and len(Data.MINERAL_WORKER) > 0: #and \
                                #len(Data.GAS_WORKER) < len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]) * 3:

                            for worker in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
                                if Bot.is_building(self, worker):
                                    continue
                                for i in Data.WORKERS_REFINERIES:
                                    workers.extend(Data.WORKERS_REFINERIES[i])
                                if worker not in workers:
                                    print(workers, 'WORKER:', worker)
                                    Data.WORKERS_REFINERIES[refinery.id].append(worker)
                                    worker.right_click(refinery)
                                    return
                        for worker in Data.WORKERS_REFINERIES[refinery.id]:
                            if worker.is_idle:
                                worker.right_click(refinery)
                                return
                        if len(Data.GAS_WORKER) >= len(Data.WORKERS_REFINERIES) * 3:
                            for i in Data.WORKERS_REFINERIES:
                                workers.append(Data.WORKERS_REFINERIES[i])

                    except KeyError:
                        print(Data.WORKERS_REFINERIES.keys())

            # for worker in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
            #     for refinery in Data.WORKERS_REFINERIES:
            #         if worker in Data.WORKERS_REFINERIES[refinery]:
            #             continue
            #         else:
            #             worker = worker
            #             break
            #
            # for refinery in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]:
            #         if refinery.is_completed and refinery not in Data.WORKERS_REFINERIES:
            #             Data.WORKERS_REFINERIES.update({refinery.unit_type.unit_typeid: []})
            #         if worker not in Data.WORKERS_REFINERIES[refinery]:
            #             Data.WORKERS_REFINERIES.append(worker)
            #         if len(Data.WORKERS_REFINERIES[refinery]) < 3:
            #             worker.right_click(refinery)
            #         else:
            #             return

    def make_workers(self):
        """Creates workers"""

        if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]) \
                < len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER] * 22):

            TERRAN_SCV = UnitType(UNIT_TYPEID.TERRAN_SCV, self)

            for base in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]:
                if (len(Data.MINERAL_WORKER) < 16) \
                        and (Bot.econ_check(self, TERRAN_SCV) == True) and not base.is_training:
                    base.train(TERRAN_SCV)
                elif UNIT_TYPEID.TERRAN_REFINERY in Data.AGENTUNITS:
                    if (len(Data.GAS_WORKER) < len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]) * 3) and \
                            Bot.econ_check(self, TERRAN_SCV) == True and not base.is_training:
                        base.train(TERRAN_SCV)

    def make_refinery(self):
        """Builds refineries at nearby vespene geysers"""

        if len(Data.BUILDER) > 1:
            return False

        if UNIT_TYPEID.NEUTRAL_SPACEPLATFORMGEYSER in Data.NEUTRALUNITS and \
                UNIT_TYPEID.TERRAN_SUPPLYDEPOT in Data.AGENTUNITS and \
                Bot.build_queue_open():
            TERRAN_REFINERY = UnitType(UNIT_TYPEID.TERRAN_REFINERY, self)
            builder = Bot.get_worker(self)

            for GEYSER in Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_SPACEPLATFORMGEYSER]:
                    GEYSER = GEYSER

            if Bot.econ_check(self, TERRAN_REFINERY) and UNIT_TYPEID.TERRAN_REFINERY not in Data.AGENTUNITS:
                builder.build_target(TERRAN_REFINERY, GEYSER)
                Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_SPACEPLATFORMGEYSER].remove(GEYSER)
                Data.BUILDER.append(builder)
                return
            if Bot.econ_check(self, TERRAN_REFINERY) and len(Data.GAS_WORKER) >= 3 and \
                    UNIT_TYPEID.TERRAN_BARRACKS in Data.AGENTUNITS:
                builder.build_target(TERRAN_REFINERY, GEYSER)
                Data.BUILDER.append(builder)
                return

    def make_barracks(self):
        """makes barracks"""

        if len(Data.BUILDER) > 1:
            return False

        if self.max_supply >= 22 and UNIT_TYPEID.TERRAN_BARRACKS not in Data.AGENTUNITS:

            TERRAN_BARRACKS = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)

            if Bot.build_queue_open() and Bot.econ_check(self, TERRAN_BARRACKS):

                builder = Bot.get_worker(self)

                pos_x = int(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.x)
                pos_y = int(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.y)

                build_pos = Bot.find_build_target(self, pos_x, pos_y, TERRAN_BARRACKS, 2, 10)

                if build_pos is False:
                    return False
                else:
                    builder.build(TERRAN_BARRACKS, build_pos)
                    Data.BUILDER.append(builder)

        if self.max_supply >= 22 and UNIT_TYPEID.TERRAN_BARRACKS in Data.AGENTUNITS:
            if self.minerals > 150 and len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]) < 3 and \
                    Bot.build_queue_open():

                TERRAN_BARRACKS = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)

                if Bot.build_queue_open() and Bot.econ_check(self, TERRAN_BARRACKS):

                    builder = Bot.get_worker(self)

                    pos_x = int(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.x)
                    pos_y = int(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.y)

                    build_pos = Bot.find_build_target(self, pos_x, pos_y, TERRAN_BARRACKS, 2, 10)

                    if build_pos is False:
                        return False
                    else:
                        builder.build(TERRAN_BARRACKS, build_pos)
                        Data.BUILDER.append(builder)

    def test_build(self):

        if UNIT_TYPEID.TERRAN_SUPPLYDEPOT in Data.AGENTUNITS and UNIT_TYPEID.TERRAN_BARRACKS not in Data.AGENTUNITS:

            TERRAN_BARRACKS = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)
            base = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0]

            Bot.build(self, TERRAN_BARRACKS, base, 2)

    def make_engineering_bay(self):
        """makes engineering bay"""

        if len(Data.BUILDER) > 1:
            return False

        if UNIT_TYPEID.TERRAN_BARRACKS in Data.AGENTUNITS \
                and UNIT_TYPEID.TERRAN_ENGINEERINGBAY not in Data.AGENTUNITS:

            ENGINEERING_BAY = UnitType(UNIT_TYPEID.TERRAN_ENGINEERINGBAY, self)
            COMMANDCENTER = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0]

            # Ez.build(self, ENGINEERING_BAY, COMMANDCENTER)

            if Bot.econ_check(self, ENGINEERING_BAY) and Bot.build_queue_open() and \
                    len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]) > 1:

                builder = Bot.get_worker(self)

                pos_x = int(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.x)
                pos_y = int(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.y)

                build_pos = Bot.find_build_target(self, pos_x, pos_y, ENGINEERING_BAY, 0, 10)

                if build_pos is False:
                    return False
                else:
                    builder.build(ENGINEERING_BAY, build_pos)
                    Data.BUILDER.append(builder)

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

    def research_tech(self) -> object:
        """Researches available tech"""

        if self.minerals < 200 and self.gas < 150:
            return False

        if UNIT_TYPEID.TERRAN_BARRACKSTECHLAB in Data.AGENTUNITS:
            for lab in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKSTECHLAB]:
                if not lab.is_training:

                    if UPGRADE_ID.STIMPACK not in Data.AGENTUPGRADES:
                        lab.research(UPGRADE_ID.STIMPACK)
                        Data.AGENTUPGRADES.append(UPGRADE_ID.STIMPACK)

        if UNIT_TYPEID.TERRAN_ENGINEERINGBAY in Data.AGENTUNITS:
            for bay in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_ENGINEERINGBAY]:
                if not bay.is_training:

                    if UPGRADE_ID.TERRANINFANTRYWEAPONSLEVEL1 not in Data.AGENTUPGRADES and \
                            bay.research(UPGRADE_ID.TERRANINFANTRYWEAPONSLEVEL1):
                        Data.AGENTUPGRADES.append(UPGRADE_ID.TERRANINFANTRYWEAPONSLEVEL1)

                    if UPGRADE_ID.TERRANINFANTRYWEAPONSLEVEL1 in Data.AGENTUPGRADES and \
                            UPGRADE_ID.TERRANINFANTRYWEAPONSLEVEL2 not in Data.AGENTUPGRADES:
                        bay.research(UPGRADE_ID.TERRANINFANTRYWEAPONSLEVEL2)
                        Data.AGENTUPGRADES.append(UPGRADE_ID.TERRANINFANTRYWEAPONSLEVEL2)

    def make_marines(self):
        """Makes Marines, Pewpew"""

        if UNIT_TYPEID.TERRAN_MARINE in Data.AGENTUNITS:
            if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE]) > 7:
                return False

        if UNIT_TYPEID.TERRAN_BARRACKSREACTOR not in Data.AGENTUNITS:
            return False

        TERRAN_MARINE = UnitType(UNIT_TYPEID.TERRAN_MARINE, self)
        REACTOR = UnitType(UNIT_TYPEID.TERRAN_BARRACKSREACTOR, self)

        if Bot.econ_check(self, TERRAN_MARINE) and self.minerals > 200:
            for barrack in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]:
                if barrack.build_percentage == 1 and UNIT_TYPEID.TERRAN_BARRACKSREACTOR in Data.AGENTUNITS \
                        and not barrack.is_training and Bot.has_addon(self, barrack, REACTOR):
                    barrack.train(TERRAN_MARINE)
                    barrack.train(TERRAN_MARINE)

    def make_marauder(self):
        """Makes Marauders"""

        if UNIT_TYPEID.TERRAN_BARRACKSTECHLAB not in Data.AGENTUNITS:
            return False

        TERRAN_MARAUDER = UnitType(UNIT_TYPEID.TERRAN_MARAUDER, self)
        TECHLAB = UnitType(UNIT_TYPEID.TERRAN_BARRACKSTECHLAB, self)

        if Bot.econ_check(self, TERRAN_MARAUDER) and self.minerals > 200:
            for barrack in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]:
                if barrack.build_percentage == 1 and UNIT_TYPEID.TERRAN_BARRACKSTECHLAB in Data.AGENTUNITS \
                        and not barrack.is_training and Bot.has_addon(self, barrack, TECHLAB):
                    barrack.train(TERRAN_MARAUDER)

    def marine_charge(self):
        """Attacks with marines given conditions"""

        if UNIT_TYPEID.TERRAN_MARINE not in Data.AGENTUNITS:
            return False

        if Data.start_base(self) == 'NE':
            opponent_base_x = 125.5
            opponent_base_y = 30.5
        if Data.start_base(self) == 'SE':
            opponent_base_x = 26.5
            opponent_base_y = 137.5

        for marine in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE]:
            if marine.is_alive and marine.is_idle and marine not in Data.ATTACKER:
                Data.ATTACKER.append(marine)
            if not marine.is_alive and marine in Data.ATTACKER:
                Data.ATTACKER.remove(marine)
        if len(Data.ATTACKER) > 25:
            for attacker in Data.ATTACKER:
                if attacker.is_idle:
                    attacker.attack_move(Point2D(opponent_base_x, opponent_base_y))

    def marauder_charge(self):
        """Attacks with marauders given conditions"""

        if UNIT_TYPEID.TERRAN_MARAUDER not in Data.AGENTUNITS:
            return False

        if Data.start_base(self) == 'NE':
            opponent_base_x = 125.5
            opponent_base_y = 30.5
        if Data.start_base(self) == 'SE':
            opponent_base_x = 26.5
            opponent_base_y = 137.5

        for marauder in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARAUDER]:
            if marauder.is_alive and marauder.is_idle and marauder not in Data.ATTACKER:
                Data.ATTACKER.append(marauder)
            if not marauder.is_alive and marauder in Data.ATTACKER:
                Data.ATTACKER.remove(marauder)
        if len(Data.ATTACKER) > 25:
            for attacker in Data.ATTACKER:
                if attacker.is_idle:
                    attacker.attack_move(Point2D(opponent_base_x, opponent_base_y))

    def make_supply(self):
        """Creates supply depots"""

        if len(Data.BUILDER) > 1:
            return False
        else:

            if UNIT_TYPEID.TERRAN_SUPPLYDEPOT in Data.AGENTUNITS:
                if Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SUPPLYDEPOT][-1].is_being_constructed and \
                        self.minerals < 400:
                    return

            if Bot.supply_check(self) and Bot.build_queue_open():
                TERRAN_SUPPLYDEPOT = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)
                if Bot.econ_check(self, TERRAN_SUPPLYDEPOT):
                    pos_x = int(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.x)
                    pos_y = int(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.y)
                    builder = Bot.get_worker(self)

                    build_pos = Bot.find_build_target(self, pos_x, pos_y, TERRAN_SUPPLYDEPOT, 0, 10)

                    if build_pos is False:
                        return False
                    else:
                        builder.build(TERRAN_SUPPLYDEPOT, build_pos)
                        Data.BUILDER.append(builder)

    def send_scout(self):
        """Sends a scout to gather intel"""

        if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]) > 15 and len(Data.SCOUT) < 1:
            for SCV in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
                if not Bot.is_building(self, SCV) and SCV.is_alive and SCV in Data.MINERAL_WORKER:
                    scout = SCV
                    Data.SCOUT.append(scout)
                    continue

        if Data.start_base(self) == 'NE':
            opponent_base_x = Data.SE_BASE[0]
            opponent_base_y = Data.SE_BASE[1]
        elif Data.start_base(self) == 'SE':
            opponent_base_x = Data.NE_BASE[0]
            opponent_base_y = Data.NE_BASE[1]
        try:
            Data.MINERAL_WORKER.remove(scout)
            scout.move(Point2D(opponent_base_x, opponent_base_y))
            Bot.Debug_info[0] = ['sent scout']
            for i in range(10):
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

        except Exception as e:
            pass

    def upgrade_orbital_command(self):
        """Upgrades bases to orbital commands"""

        if not Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS][0].is_completed \
                or UNIT_TYPEID.TERRAN_COMMANDCENTER not in Data.AGENTUNITS:
            return False

        for base in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]:
            if UNIT_TYPEID.TERRAN_ORBITALCOMMAND not in Data.AGENTUNITS and not base.is_training:

                if self.minerals > 150 and len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]) > 2:
                    base.ability(ABILITY_ID.MORPH_ORBITALCOMMAND)

    def make_factory(self):
        """Dun do shit"""
        pass

    def defend_base(self):
        """Defends Base (poorly) if attacked"""

        for enemy in Data.enemies_in_base:
            if not enemy.is_alive:
                Data.enemies_in_base.remove(enemy)
            for i in range(2):
                for type in Data.AGENT_COMBAT_UNITS:
                    for defender in Data.AGENT_COMBAT_UNITS[type]:
                        if defender.unit_type.is_combat_unit and defender.is_alive and defender.is_completed:
                            defender.attack_unit(enemy)

        if len(Data.enemies_in_base) < 2 and Data.AGENTSTATE['PURPOSE'] != 'OFFENCE':
            Bot.state_setter('PURPOSE', 'OFFENCE')

    def move_marines_to_ramp(self):

        if UNIT_TYPEID.TERRAN_MARINE in Data.AGENTUNITS:



            ramp = Data.wall_positions(self, 2)
            if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE]) >= 8:
                for marine in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE][0:8]:
                    if not Bot.near(self, marine.position, Point2D(ramp[0], ramp[1]), 5):
                        marine.move(Point2D(ramp[0], ramp[1]))
                    elif Bot.near(self, marine.position, Point2D(ramp[0], ramp[1]), 5) and \
                        marine not in Data.DEFENDER["ramp"]:

                        Data.DEFENDER["ramp"].append(marine)

                    else:
                        continue

    def near(self, pos: Point2D, unit_pos: Point2D, radius: int):

        distance = self.map_tools.get_ground_distance(unit_pos, pos)
        if distance <= radius:
            return True
        else:
            return False
    # def make_wall(self):
    #
    #     TERRAN_SUPPLYDEPOT = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)
    #     builder = Bot.get_worker()
    #
    #     if Bot.econ_check(self, TERRAN_SUPPLYDEPOT):
    #         if self.max_supply < 23 and UNIT_TYPEID.TERRAN_SUPPLYDEPOT not in gamestate.AGENTUNITS:
    #             x = int(gamestate.wall_positions(self, 0)[0])
    #             y = int(gamestate.wall_positions(self, 0)[1])
    #             if self.building_placer.can_build_here(x, y, TERRAN_SUPPLYDEPOT):
    #                 builder.build(TERRAN_SUPPLYDEPOT, Point2DI(x, y))
    #                 Bot.task_remover(builder)
    #                 gamestate.BUILDER.append(builder)
    #                 Bot.Debug_info[0] = [ 'Added', builder, 'To BUILDER list')
    #                 return
    #
    #         if 15 == self.max_supply and \
    #                 gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SUPPLYDEPOT][0].build_percentage > 0.6:
    #             x = int(gamestate.wall_positions(self, 1)[0])
    #             y = int(gamestate.wall_positions(self, 1)[1])
    #             if self.building_placer.can_build_here(x, y, TERRAN_SUPPLYDEPOT):
    #                 builder.build(TERRAN_SUPPLYDEPOT, Point2DI(x, y))
    #                 Bot.task_remover(builder)
    #                 gamestate.BUILDER.append(builder)
    #                 Bot.Debug_info[0] = [ 'Added', builder, 'To BUILDER list')
    #                 return
    #         # else:

    """////////////VALUE_RETURNS///////////"""

    def is_worker_collecting_gas(self, worker):
        """ Returns: True if a unit 'worker' is collecting gas, False otherwise """

        def squared_distance(unit_1, unit_2):
            p1 = unit_1.position
            p2 = unit_2.position
            return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

        for refinery in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]:
            if refinery.is_completed and squared_distance(worker, refinery) < 2 ** 2:
                return True

    def has_addon(self, candidate: Unit, addon_type: UnitType):
        """
        Looks through all units and looks if there is an addon of the type addon_type nearby to the supplied candidate.

        :return: True if the unit "candindate" has an addon of the type "addon_type"
        """
        for unit in self.get_my_units():
            if unit.unit_type.is_addon and unit.is_alive and unit.is_completed \
                    and unit.unit_type == addon_type \
                    and abs(unit.position.x - candidate.position.x) < 3 \
                    and abs(unit.position.y - candidate.position.y) < 3:
                return True

        return False

    def find_build_target(self, pos_x, pos_y, unit_to_build, space, hej):
        """Finds nearest buildable tile to a building"""

        for i in range(hej):
            build_pos = self.building_placer.get_build_location_near(Point2DI(int(pos_x), int(pos_y)), unit_to_build, space,
                                                                     i * 10)
            if self.building_placer.can_build_here(build_pos.x, build_pos.y, unit_to_build):
                return build_pos
        else:
            return False

    def clear_build_list(self):
        """Clears builder-list every once in a while"""

        if len(Data.BUILDER) > 1:

            for builder in Data.BUILDER:
                if not Bot.is_building(self, builder) or not builder.is_alive or builder.is_idle:
                    Data.BUILDER.remove(builder)

    def is_building(self, unit):
        """Checks if selected worker is currently building something"""

        if unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_REFINERY, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_ARMORY, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_BUNKER, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_ENGINEERINGBAY, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_FACTORY, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_GHOSTACADEMY, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_SENSORTOWER, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_STARPORT, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_MISSILETURRET, self)):
            return True
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_FUSIONCORE, self)):
            return True
        else:
            return False

    def is_building_name(self, unit):

        if unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)):
            return 'barracks'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)):
            return 'supply depot'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_REFINERY, self)):
            return 'refinery'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_COMMANDCENTER, self)):
            return 'command center'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_ARMORY, self)):
            return 'armory'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_BUNKER, self)):
            return 'bunker'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_ENGINEERINGBAY, self)):
            return 'engineering bay'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_FACTORY, self)):
            return 'factory'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_GHOSTACADEMY, self)):
            return 'ghost academy'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_SENSORTOWER, self)):
            return 'sensor tower'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_STARPORT, self)):
            return 'starport'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_MISSILETURRET, self)):
            return 'missile turret'
        elif unit.is_constructing(UnitType(UNIT_TYPEID.TERRAN_FUSIONCORE, self)):
            return 'fusion core'
        else:
            return 'None'

    def econ_check(self, unit_type: UnitType):
        """Asserts that agents economy allows the requested build/train command"""

        return self.minerals >= unit_type.mineral_price \
               and self.gas >= unit_type.gas_price \
               and self.max_supply - self.current_supply >= unit_type.supply_required

    def get_worker(self):
        """Gets arbitrary available worker"""

        for SCV in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:

            if SCV.is_alive and SCV in Data.MINERAL_WORKER and not Bot.is_building(self, SCV):
                return SCV

    def get_my_producers(self, unit_type: UnitType):  # NOT IMPLEMENTED
        """ Returns a list of units which can build or train units of type unit_type """

        producers = []
        type_data = self.tech_tree.get_data(unit_type)
        what_builds = type_data.what_builds

        for unit in self.get_my_units():
            if unit.unit_type in what_builds:
                producers.append(unit)

        return producers

    def supply_check(self):
        """Checks to see if supply is running low"""

        if UNIT_TYPEID.TERRAN_BARRACKS in Data.AGENTUNITS:
            if (self.max_supply - self.current_supply) < 2 * len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]):
                return True
            else:
                return False
        else:
            if (self.max_supply - self.current_supply) < 2:
                return True
            else:
                return False

    @staticmethod
    def unit_death_handler():
        """Removes dead units from AGENTUNITS Dictionary"""

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

        for types in Data.AGENT_COMBAT_UNITS:
            for unit in Data.AGENT_COMBAT_UNITS[types]:
                if not unit.is_alive:
                    Data.AGENT_COMBAT_UNITS[types].remove(unit)

    @staticmethod
    def build_queue_open():
        """Returns true if build queue is < 3"""

        if len(Data.BUILDQ) < 3:
            return True
        else:
            return False

    @staticmethod
    def get_available_neutral_unit(unit_type_id):
        """Returns a seleced type of neutral unit"""

        for unit in Data.NEUTRALUNITS[unit_type_id]:
            return unit

    @staticmethod
    def build_queue():
        """Handles build queue"""

        types = len(list(Data.AGENTUNITS))

        for units in range(types):
            current = list(Data.AGENTUNITS)[units]

            try:
                if Data.AGENTUNITS[current][0].unit_type.is_building:
                    for building in Data.AGENTUNITS[current]:
                        if not building.is_completed and building not in Data.BUILDQ \
                                and building.player == PLAYER_SELF:
                            Data.BUILDQ.append(building)
                        elif building.is_completed and building in Data.BUILDQ \
                                and building.player == PLAYER_SELF:
                            Data.BUILDQ.remove(building)

                for UnitCheck in Data.BUILDQ:
                    try:
                        if UnitCheck.player != PLAYER_SELF:
                            Data.BUILDQ.remove(UnitCheck)
                    except Exception as e:
                        Data.BUILDQ.remove(UnitCheck)
            except IndexError:
                del Data.AGENTUNITS[current]

    def build(self, building: UnitType, near: Unit, range):
        """build(self: Bot, building: library.UnityType, near: library.Unit) -> None"""

        if Bot.build_queue_open() and Bot.econ_check(self, building):
            x = near.position.x
            y = near.position.y
            pos = Bot.find_build_target(self, x, y, building, range, 10)
            if self.building_placer.can_build_here(pos.x, pos.y, building):
                builder = Bot.get_worker(self)
                builder.build(building, pos)


    """///////////GRAPHICS//////////////////"""

    def unit_debug(self):
        """"Prints a debug message over agents units, also adds each unit to gamestate.AGENTUNITS dictionary"""

        for unit in self.get_my_units():

            if unit.player == PLAYER_SELF:

                type = unit.unit_type.unit_typeid

                if unit.unit_type.is_combat_unit:
                    if type not in Data.AGENT_COMBAT_UNITS:
                        Data.AGENT_COMBAT_UNITS.update({type: [unit]})
                        Bot.Debug_info[0] = ["Added" + str(type) + 'To Combat dictionary']
                    elif unit not in Data.AGENT_COMBAT_UNITS[type]:
                        Data.AGENT_COMBAT_UNITS[type].append(unit)

                if type not in Data.AGENTUNITS:
                    Data.AGENTUNITS.update({type: [unit]})
                    Bot.Debug_info[0] = ["Added" + str(type) + 'To Units dictionary']
                elif unit not in Data.AGENTUNITS[type]:
                    Data.AGENTUNITS[type].append(unit)

                pos = Data.AGENTUNITS[type].index(unit)

                # self.map_tools.draw_text(unit.position, (str(unit.unit_type) + "id: " + str(unit.id) + " i: " + str(pos)),
                #                         Color(255, 255, 255))

    def unit_task(self):

        task = ""
        mapdraw = self.map_tools.draw_text_screen
        for unit in self.get_my_units():
            if unit.unit_type.is_building:
                continue
            elif unit.unit_type.is_worker:
                if unit in Data.MINERAL_WORKER:
                    task = "minerals"
                    mapdraw(0.02, 0.033, "On Minerals:" + str(len(Data.MINERAL_WORKER)), Color(100, 200, 255))
                elif unit in Data.GAS_WORKER:
                    task = "gas"
                    mapdraw(0.02, 0.046, "On Gas:" + str(len(Data.GAS_WORKER)), Color(100, 200, 255))
                elif Bot.is_building(self, unit):
                    task = Bot.is_building_name(self, unit)
                    mapdraw(0.02, 0.059, str(task), Color(100, 200, 255))
                else:
                    task = "Bruh"
            elif unit.unit_type.is_combat_unit:
                if unit in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE]:
                    task = "marine"
                    mapdraw(0.02, 0.085, str(task), Color(100, 200, 255))
                if unit in Data.DEFENDER["ramp"]:
                    task = "defence"
                    mapdraw(0.02, 0.072, "Marines:" + str(task), Color(100, 200, 255))

            else:
                task = ''


            type = unit.unit_type.unit_typeid
            pos = Data.AGENTUNITS[type].index(unit)

            self.map_tools.draw_text(unit.position, str(task) + " i: " + str(pos) , Color(255, 255, 255))

    def neutral_debug(self):
        """"Prints a debug message over neutral units, also adds each unit to gamestate.AGENTUNITS dictionary"""

        mineral_deposits = self.base_location_manager.get_player_starting_base_location(0).minerals


        try:
            if len(Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_MINERALFIELD]) < 4 * len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]) and \
                len(Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_MINERALFIELD750]) < 4 * len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]) and \
                len(Data.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_SPACEPLATFORMGEYSER]) < 2 * len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]):

                for commandcenter in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]:
                    for mineral in self.get_all_units():
                        if mineral.unit_type.is_mineral and Bot.near(self, mineral.position, commandcenter.position, 10):
                            type = mineral.unit_type.unit_typeid
                            if type not in Data.NEUTRALUNITS:
                                Data.NEUTRALUNITS.update({type: [mineral]})
                                Bot.Debug_info[0] = ["Added" + str(type) + 'To Neutral dictionary']
                            elif mineral not in Data.NEUTRALUNITS[type]:
                                Data.NEUTRALUNITS[type].append(mineral)
            else:
                return True
        except Exception as e:
            print(e)
            mineral_deposits = self.base_location_manager.get_player_starting_base_location(0).minerals
            for unit in mineral_deposits:
                type = unit.unit_type.unit_typeid
                if type not in Data.NEUTRALUNITS:
                    Data.NEUTRALUNITS.update({type: [unit]})
                    Bot.Debug_info[0] = ["Added" + str(type) + 'To Neutral dictionary']
                elif unit not in Data.NEUTRALUNITS[type]:
                    Data.NEUTRALUNITS[type].append(unit)
        #pos = Data.NEUTRALUNITS[type].index(unit)
        gas_deposits = self.base_location_manager.get_player_starting_base_location(0).geysers



            # self.map_tools.draw_text(unit.position, (str(unit.unit_type) + "id: " + str(unit.id) + " i: " + str(pos)),
            #                         Color(255, 255, 255))

            # self.map_tools.draw_text(unit.position, (str(unit.unit_type.unit_typeid)[12::] + " Nr:" + str(pos)),
            #                         Color(255, 255, 255))

        for unit in gas_deposits:

            type = unit.unit_type.unit_typeid

            if type not in Data.NEUTRALUNITS:
                Data.NEUTRALUNITS.update({type: [unit]})
                Bot.Debug_info[0] = ["Added" + str(type) + 'To neutral dictionary']
            elif unit not in Data.NEUTRALUNITS[type]:
                Data.NEUTRALUNITS[type].append(unit)

            pos = Data.NEUTRALUNITS[type].index(unit)

            if UNIT_TYPEID.TERRAN_REFINERY in Data.AGENTUNITS:
                for refinery in Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]:
                    if refinery.position.x == unit.position.x:
                        unit = refinery
                        pos = Data.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY].index(refinery)

            self.map_tools.draw_text(unit.position, (str(unit.unit_type) + "id: " + str(unit.id) + " i: " + str(pos)),
                                     Color(255, 255, 255))

            # self.map_tools.draw_text(unit.position, (str(unit.unit_type.unit_typeid)[12::] + " Nr:" + str(pos)),
            #                         Color(255, 255, 255))

    def enemy_debug(self):
        """Gathers enemy units and adds them to Data.ENEMYUNITS"""

        for unit in self.get_all_units():

            if unit.player == PLAYER_ENEMY:

                type = unit.unit_type.unit_typeid

                if type not in Data.ENEMYUNITS:
                    Data.ENEMYUNITS.update({type: [unit]})
                    Bot.Debug_info[0] = ["Added" + str(type) + 'To Enemy dictionary']
                elif unit not in Data.ENEMYUNITS[type]:
                    Data.ENEMYUNITS[type].append(unit)

                pos = Data.ENEMYUNITS[type].index(unit)

                # self.map_tools.draw_text(unit.position,
                #                         ("ENEMY" + str(unit.unit_type) + "id: " + str(unit.id) + " i: " + str(pos)),
                #                         Color(255, 100, 0))

    def session_info(self, runtime, performance):
        """Draws info about current session on screen"""

        mapdraw = self.map_tools.draw_text_screen

        mapdraw(0.02, 0.020, "----AGENTDATA----", Color(100, 200, 255))
        #mapdraw(0.02, 0.033, "Minerals Spent:" + str(Data.total_value(self)[0]), Color(100, 200, 255))
        #mapdraw(0.02, 0.046, "Gas Spent:" + str(Data.total_value(self)[1]), Color(100, 200, 255))
        #mapdraw(0.02, 0.059, "Minerals Lost:" + str(Data.AGENT_LOST[0]), Color(100, 200, 255))
        #mapdraw(0.02, 0.072, "Gas Lost:" + str(Data.AGENT_LOST[1]), Color(100, 200, 255))
        #mapdraw(0.02, 0.085, "Workers:" + str(len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV])), Color(100, 200, 255))



        mapdraw(0.02, 0.130, "----ENEMYDATA----", Color(255, 100, 0))
        mapdraw(0.02, 0.143, "Enemy Minerals Spent:" + str(Data.enemy_total_value(self)[0]), Color(255, 100, 0))
        mapdraw(0.02, 0.156, "Enemy Gas Spent:" + str(Data.enemy_total_value(self)[1]), Color(255, 100, 0))
        mapdraw(0.02, 0.169, "Enemy Minerals Lost:" + str(Data.ENEMY_LOST[0]), Color(255, 100, 0))
        mapdraw(0.02, 0.182, "Enemy Gas Lost:" + str(Data.ENEMY_LOST[1]), Color(255, 100, 0))

        mapdraw(0.275, 0.72, str(Data.AGENTSTATE), Color(100, 200, 255))

        # mapdraw(0.02, 0.60, "Minerals:" + str(self.minerals), Color(100, 200, 255))
        # mapdraw(0.02, 0.615, "Gas:" + str(self.gas), Color(100, 200, 255))
        # mapdraw(0.02, 0.63, "Unused Supply:" + str(self.max_supply - self.current_supply), Color(100, 200, 255))
        mapdraw(0.02, 0.645, "Runtime " + str(round(runtime, 0)), Color(100, 200, 255))
        mapdraw(0.02, 0.66, "Performance: " + str(int(performance)) + " Loops / Second", Color(100, 200, 255))

    def map_info(self):

        maptext = self.map_tools.draw_text
        ramp = Data.wall_positions(self, 2)
        maptext(Point2D(ramp[0], ramp[1]), str("Defence position"), Color(255, 255, 255))

    def debug_info(self):
        pass
        mapdraw = self.map_tools.draw_text_screen

        mapdraw(0.02, 0.675, str(Bot.Debug_info), Color(100, 200, 255))

    """///////////STATE HANDLERS///////////"""

    def state_listener(self):
        """listens to current AgentState"""

        if UNIT_TYPEID.TERRAN_BARRACKS in Data.AGENTUNITS \
                and UNIT_TYPEID.TERRAN_ENGINEERINGBAY in Data.AGENTUNITS \
                and UNIT_TYPEID.TERRAN_BARRACKSTECHLAB in Data.AGENTUNITS \
                and Data.AGENTSTATE['STATE'] == 0:
            if len(Data.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]) > 2:
                Bot.state_setter('STATE', 1)
                Bot.Debug_info[0] = ['SET STATE TO 1 - GENERAL GAMEPLAY']

    @staticmethod
    def state_setter(state, routine):
        """Sets AgentState"""

        Data.AGENTSTATE[state] = routine
        return

    @staticmethod
    def enemy_attacking():
        """Returns true if opponent is attacking a base"""

        if len(Data.enemies_in_base) > 3:
            Bot.state_setter('PURPOSE', 'DEFEND')
            return True

    def base_listener(self):
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


"""///////////////////////// TEST METHODS ////////////////////////"""

# def neutral_debug(self):
#     """"Prints a debug message over neutral units, also adds each unit to gamestate.AGENTUNITS dictionary"""
#
#     mineral_deposits = self.base_location_manager.get_player_starting_base_location(0).minerals
#     gas_deposits = self.base_location_manager.get_player_starting_base_location(0).geysers
#
#     for unit in mineral_deposits:
#
#         type = unit.unit_type.unit_typeid
#
#         if type not in gamestate.NEUTRALUNITS:
#             gamestate.NEUTRALUNITS.update({type: [unit]})
#             Bot.Debug_info[0] = [ "Added", type, 'To neutral dictionary')
#         elif unit not in gamestate.NEUTRALUNITS[type]:
#             gamestate.NEUTRALUNITS[type].append(unit)
#
#         pos = gamestate.NEUTRALUNITS[type].index(unit)
#         self.map_tools.draw_text(unit.position, (str(unit.unit_type.unit_typeid)[12::] + " Nr:" + str(pos)),
#                                  Color(255, 255, 255))
#
#     for unit in gas_deposits:
#
#         type = unit.unit_type.unit_typeid
#
#         if type not in gamestate.NEUTRALUNITS:
#             gamestate.NEUTRALUNITS.update({type: [unit]})
#             Bot.Debug_info[0] = [ "Added", type, 'To neutral dictionary')
#         elif unit not in gamestate.NEUTRALUNITS[type]:
#             gamestate.NEUTRALUNITS[type].append(unit)
#
#         pos = gamestate.NEUTRALUNITS[type].index(unit)
#
#         if UNIT_TYPEID.TERRAN_REFINERY in gamestate.AGENTUNITS:
#             for refinery in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]:
#                 if refinery.position.x == unit.position.x:
#                     unit = refinery
#                     pos = gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY].index(refinery)
#
#         self.map_tools.draw_text(unit.position, (str(unit.unit_type.unit_typeid)[12::] + " Nr:" + str(pos)),
#                                  Color(255, 255, 255))
#
#
#
#  if Bot.econ_check(self, TERRAN_BARRACKS) and UNIT_TYPEID.TERRAN_BARRACKS not in gamestate.AGENTUNITS:
#  x = int(gamestate.wall_positions(self, 2)[0])
#  y = int(gamestate.wall_positions(self, 2)[1])
#  if self.building_placer.can_build_here(x, y, TERRAN_BARRACKS):
#  builder.build(TERRAN_BARRACKS, Point2DI(x, y))
#  gamestate.BUILDER.append(builder)
#  return
#
#
