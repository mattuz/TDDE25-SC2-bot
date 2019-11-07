from main import *
from library import *
from gamestate import *
import queue
import random

q = queue.Queue()


class Bot(MyAgent):
    """ Main method handler for bot features. Inherits MyAgent """

    def __init__(self):
        pass

    """//////////////COMMANDS///////////////"""

    def distribute_workers(self):
        """Distributes idle workers to nearby resource nodes"""

        mineral_deposits = self.base_location_manager.get_player_starting_base_location(PLAYER_SELF).minerals
        base = gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]

        if UNIT_TYPEID.TERRAN_REFINERY in gamestate.AGENTUNITS:
            refineries = gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]
        else:
            refineries = []

        for worker in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:

            if worker.is_idle and worker.is_alive:

                if len(gamestate.MINERAL_WORKER) < \
                        (len(gamestate.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_MINERALFIELD]) * 2
                         + len(gamestate.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_MINERALFIELD750]) * 2):
                    for minerals in mineral_deposits:
                        #minerals = random.choice(mineral_deposits)
                        worker.right_click(minerals)

                        if worker not in gamestate.MINERAL_WORKER:
                                gamestate.MINERAL_WORKER.append(worker)
                                print("Added", worker, "to mineral line")

                elif UNIT_TYPEID.TERRAN_REFINERY in gamestate.AGENTUNITS and len(gamestate.MINERAL_WORKER) > 14:
                    for gas in refineries:
                        if len(gamestate.GAS_WORKER) < (len(refineries) * 3):
                            worker.right_click(gas)
                            if worker not in gamestate.GAS_WORKER:
                                gamestate.GAS_WORKER.append(worker)
                                print("Added", worker, "to gas line")
            else:
                if worker.is_alive and worker.has_target and not worker.is_idle:

                    if worker.target in mineral_deposits and worker not in gamestate.MINERAL_WORKER:
                        gamestate.MINERAL_WORKER.append(worker)
                        print("Added", worker, "to mineral line")
                    elif worker.target in refineries and worker not in gamestate.GAS_WORKER:
                        gamestate.GAS_WORKER.append(worker)
                        print("Added", worker, "to gas line")
                    elif worker.target not in mineral_deposits \
                            and worker.target not in base and worker in gamestate.MINERAL_WORKER:
                        gamestate.MINERAL_WORKER.remove(worker)
                        print("Removed", worker, "from mineral line")
                    elif worker.target not in refineries \
                            and worker.target not in base and worker in gamestate.GAS_WORKER:
                        gamestate.GAS_WORKER.remove(worker)
                        print("Removed", worker, "from gas line")
                    elif worker.target in mineral_deposits and len(gamestate.MINERAL_WORKER) > 16 \
                            and len(gamestate.GAS_WORKER) < (len(refineries) * 3):
                        for gas in refineries:
                            worker.right_click(gas)
                            if worker in gamestate.MINERAL_WORKER:
                                gamestate.MINERAL_WORKER.remove(worker)
                            gamestate.GAS_WORKER.append(worker)
                            print("switched", worker, "to gas")

    def make_workers(self):
        """Creates workers"""

        TERRAN_SCV = UnitType(UNIT_TYPEID.TERRAN_SCV, self)

        for base in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]:
            if (len(gamestate.MINERAL_WORKER) < 16) \
                    and (Bot.econ_check(self, TERRAN_SCV) == True) and not base.is_training:
                base.train(TERRAN_SCV)
                #time.sleep(0.2)
            elif UNIT_TYPEID.TERRAN_REFINERY in gamestate.AGENTUNITS:
                if (len(gamestate.GAS_WORKER) < len(gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]) * 3) and \
                        Bot.econ_check(self, TERRAN_SCV) == True and not base.is_training:
                    base.train(TERRAN_SCV)
                    #time.sleep(0.2)

    def make_refinery(self):

        if UNIT_TYPEID.NEUTRAL_SPACEPLATFORMGEYSER in gamestate.NEUTRALUNITS and \
                UNIT_TYPEID.TERRAN_SUPPLYDEPOT in gamestate.AGENTUNITS:

            TERRAN_REFINERY = UnitType(UNIT_TYPEID.TERRAN_REFINERY, self)
            builder = Bot.get_worker()
            GEYSER = Bot.get_available_neutral_unit(UNIT_TYPEID.NEUTRAL_SPACEPLATFORMGEYSER)

            if Bot.econ_check(self, TERRAN_REFINERY) and UNIT_TYPEID.TERRAN_REFINERY not in gamestate.AGENTUNITS:
                builder.build_target(TERRAN_REFINERY, GEYSER)
                Bot.task_remover(builder)
                gamestate.BUILDER.append(builder)
                gamestate.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_SPACEPLATFORMGEYSER].remove(GEYSER)

            if Bot.econ_check(self, TERRAN_REFINERY) and len(gamestate.GAS_WORKER) == 3:
                builder.build_target(TERRAN_REFINERY, GEYSER)
                Bot.task_remover(builder)
                gamestate.BUILDER.append(builder)
                gamestate.NEUTRALUNITS[UNIT_TYPEID.NEUTRAL_SPACEPLATFORMGEYSER].remove(GEYSER)

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
    #                 print('Added', builder, 'To BUILDER list')
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
    #                 print('Added', builder, 'To BUILDER list')
    #                 return
    #         # else:

    def make_barracks(self):

        if self.max_supply > 22 and UNIT_TYPEID.TERRAN_BARRACKS not in gamestate.AGENTUNITS:

            TERRAN_BARRACKS = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)
            builder = Bot.get_worker()

            if Bot.econ_check(self, TERRAN_BARRACKS) and UNIT_TYPEID.TERRAN_BARRACKS not in gamestate.AGENTUNITS:
                x = int(gamestate.wall_positions(self, 2)[0])
                y = int(gamestate.wall_positions(self, 2)[1])
                if self.building_placer.can_build_here(x, y, TERRAN_BARRACKS):
                    builder.build(TERRAN_BARRACKS, Point2DI(x, y))
                    Bot.task_remover(builder)
                    gamestate.BUILDER.append(builder)
                    return

    def barracks_upgrade(self):

        REACTOR = UnitType(UNIT_TYPEID.TERRAN_BARRACKSREACTOR, self)
        TECHLAB = UnitType(UNIT_TYPEID.TERRAN_BARRACKSTECHLAB, self)

        if Bot.econ_check(self, REACTOR):
            for barrack in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]:
                if barrack.build_percentage == 1 and REACTOR not in gamestate.AGENTUNITS and not barrack.is_training:
                    barrack.train(REACTOR)

    def make_marines(self):

        TERRAN_MARINE = UnitType(UNIT_TYPEID.TERRAN_MARINE, self)

        if Bot.econ_check(self, TERRAN_MARINE) and self.minerals > 200:
            for barrack in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_BARRACKS]:
                if barrack.build_percentage == 1 and UNIT_TYPEID.TERRAN_BARRACKSREACTOR in gamestate.AGENTUNITS \
                        and not barrack.is_training:
                    barrack.train(TERRAN_MARINE)
                    barrack.train(TERRAN_MARINE)

    def marine_charge(self):

        if gamestate.start_base(self) == 'NE':
            opponent_base_x = 125.5
            opponent_base_y = 30.5
        if gamestate.start_base(self) == 'SE':
            opponent_base_x = 26.5
            opponent_base_y = 137.5

        for marine in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_MARINE]:
            if marine.is_alive and marine.is_idle and marine not in gamestate.ATTACKER:
                gamestate.ATTACKER.append(marine)
            if not marine.is_alive and marine in gamestate.ATTACKER:
                gamestate.ATTACKER.remove(marine)
        if len(gamestate.ATTACKER) > 15:
            for attacker in gamestate.ATTACKER:
                if attacker.is_idle:
                    attacker.attack_move(Point2D(opponent_base_x,opponent_base_y))

    def make_supply(self):


        if Bot.supply_check(self):
            TERRAN_SUPPLYDEPOT = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)
            if Bot.econ_check(self, TERRAN_SUPPLYDEPOT):
                pos_x = int(gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.x)
                pos_y = int(gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER][0].position.y)
                builder = Bot.get_worker()
                print("MAKE_SUPPLY")
                for i in range(10):
                    build_pos = self.building_placer.get_build_location_near(Point2DI(pos_x, pos_y), TERRAN_SUPPLYDEPOT, 1, i*10)
                    if self.building_placer.can_build_here(build_pos.x, build_pos.y, TERRAN_SUPPLYDEPOT):
                        print("found", build_pos)
                        builder.build(TERRAN_SUPPLYDEPOT, build_pos)
                        break
        else:
            print("Make_supply failed")

    """////////////VALUE_RETURNS///////////"""

    def econ_check(self, unit_type: UnitType):
        """Asserts that agents economy allows the requested build/train command"""

        return self.minerals >= unit_type.mineral_price \
               and self.gas >= unit_type.gas_price \
               and self.max_supply - self.current_supply >= unit_type.supply_required

    @staticmethod
    def get_worker():

        for SCV in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
            try:
                is_building = SCV.is_constructing(gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SUPPLYDEPOT][-1].unit_type)
            except:
                is_building = False
            if SCV.is_alive and SCV in gamestate.MINERAL_WORKER and not is_building:
                builder = SCV
                return builder

    @staticmethod
    def get_available_neutral_unit(unit_type_id):

        for unit in gamestate.NEUTRALUNITS[unit_type_id]:
            return unit

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

        if (self.max_supply - self.current_supply) < 3:
            print('Avaliable supply is ', self.max_supply - self.current_supply)
            return True
        else:
            return False

    @staticmethod
    def task_remover(unit):

        if unit in gamestate.MINERAL_WORKER:
            gamestate.MINERAL_WORKER.remove(unit)
            return
        if unit in gamestate.MINERAL_WORKER:
            gamestate.MINERAL_WORKER.remove(unit)
            return

    """///////////GRAPHICS//////////////////"""

    def unit_debug(self):
        """"Prints a debug message over agents units, also adds each unit to gamestate.AGENTUNITS dictionary"""

        for unit in self.get_my_units():

            type = unit.unit_type.unit_typeid

            if type not in gamestate.AGENTUNITS:
                gamestate.AGENTUNITS.update({type: [unit]})
                print("Added", type, 'To units dictionary')
            elif unit not in gamestate.AGENTUNITS[type]:
                gamestate.AGENTUNITS[type].append(unit)

            pos = gamestate.AGENTUNITS[type].index(unit)

            self.map_tools.draw_text(unit.position, (str(unit.unit_type) + "id: " + str(unit.id) + " i: " + str(pos)),
                                     Color(255, 255, 255))

    def neutral_debug(self):
        """"Prints a debug message over neutral units, also adds each unit to gamestate.AGENTUNITS dictionary"""

        mineral_deposits = self.base_location_manager.get_player_starting_base_location(0).minerals
        gas_deposits = self.base_location_manager.get_player_starting_base_location(0).geysers

        for unit in mineral_deposits:

            type = unit.unit_type.unit_typeid

            if type not in gamestate.NEUTRALUNITS:
                gamestate.NEUTRALUNITS.update({type: [unit]})
                print("Added", type, 'To neutral dictionary')
            elif unit not in gamestate.NEUTRALUNITS[type]:
                gamestate.NEUTRALUNITS[type].append(unit)

            pos = gamestate.NEUTRALUNITS[type].index(unit)
            self.map_tools.draw_text(unit.position, (str(unit.unit_type) + "id: " +str(unit.id) + " i: " + str(pos)),
                                     Color(255, 255, 255))

        for unit in gas_deposits:

            type = unit.unit_type.unit_typeid

            if type not in gamestate.NEUTRALUNITS:
                gamestate.NEUTRALUNITS.update({type: [unit]})
                print("Added", type, 'To neutral dictionary')
            elif unit not in gamestate.NEUTRALUNITS[type]:
                gamestate.NEUTRALUNITS[type].append(unit)

            pos = gamestate.NEUTRALUNITS[type].index(unit)

            if UNIT_TYPEID.TERRAN_REFINERY in gamestate.AGENTUNITS:
                for refinery in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY]:
                    if refinery.position.x == unit.position.x:
                        unit = refinery
                        pos = gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_REFINERY].index(refinery)

            self.map_tools.draw_text(unit.position, (str(unit.unit_type) + "id: " + str(unit.id) + " i: " + str(pos)),
                                     Color(255, 255, 255))

    def session_info(self, runtime):
        """Draws info about current session on screen"""

        mapdraw = self.map_tools.draw_text_screen

        mapdraw(0.02, 0.10, "Minerals Spent:" + str(gamestate.total_value(self)[0]), Color(100, 200, 255))
        mapdraw(0.02, 0.115, "Gas Spent:" + str(gamestate.total_value(self)[1]), Color(100, 200, 255))
        mapdraw(0.02, 0.13, "Minerals Lost:" + str(gamestate.total_lost(self)[0]), Color(100, 200, 255))
        mapdraw(0.02, 0.145, "Gas Lost:" + str(gamestate.total_lost(self)[1]), Color(100, 200, 255))

        mapdraw(0.02, 0.20, "Workers:" + str(len(gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV])), Color(100, 200, 255))
        mapdraw(0.02, 0.215, "On Minerals:" + str(len(gamestate.MINERAL_WORKER)), Color(50, 150, 255))
        mapdraw(0.02, 0.230, "On Gas:" + str(len(gamestate.GAS_WORKER)), Color(50, 150, 255))

        mapdraw(0.02, 0.60, "Minerals:" + str(self.minerals), Color(100, 200, 255))
        mapdraw(0.02, 0.615, "Gas:" + str(self.gas), Color(100, 200, 255))
        mapdraw(0.02, 0.63, "Unused Supply:" + str(self.max_supply - self.current_supply), Color(100, 200, 255))
        mapdraw(0.02, 0.645, "Runtime " + str(round(runtime, 0)), Color(100, 200, 255))


"""///////////////////////// TEST METHODS ////////////////////////"""

# def make_wall(self, step):  # NOT FUNCTIONING AS INTENDED
#     """Builds Supply Depots in case the supply dips below a threshold value"""
#
#     TERRAN_SUPPLYDEPOT = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)
#     TERRAN_BARRACKS = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)
#
#     if gamestate.start_base(self) == 'NE':
#         Wall_Supply_1 = (37.0, 122.0)
#         Wall_Supply_2 = (34.0, 125.0)
#         Wall_Barrack = (36.5, 124.5)
#     elif gamestate.start_base(self) == 'SE':
#         Wall_Supply_1 = (118.0, 43.0)
#         Wall_Supply_2 = (115.0, 46.0)
#         Wall_Barrack = (115.5, 43.5)
#
#     for SCV in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
#         if SCV.is_alive and not SCV.unit_type.is_building:
#             builder = SCV
#
#     if self.minerals >= 100:
#
#         builder.build(TERRAN_SUPPLYDEPOT, Point2DI(int(Wall_Supply_1[0]), int(Wall_Supply_1[1])))
#         if not gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SUPPLYDEPOT][0].unit_type.is_building:
#             builder.build(TERRAN_SUPPLYDEPOT, Point2DI(int(Wall_Supply_2[0]), int(Wall_Supply_2[1])))
#             time.sleep(3)
#             if not gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SUPPLYDEPOT][1].unit_type.is_building:
#                 builder.build(TERRAN_BARRACKS, Point2DI(int(Wall_Barrack[0]), int(Wall_Barrack[1])))
#                 time.sleep(3)
#                 return True

# def build_order(self):
#    self.make_supply(self, 0)

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
#             print("Added", type, 'To neutral dictionary')
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
#             print("Added", type, 'To neutral dictionary')
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