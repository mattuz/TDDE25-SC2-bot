from main import *
from library import *
from gamestate import *
import asyncio

class Bot(MyAgent):
    """ Main method handler for bot features. Inherits MyAgent """

    def __init__(self):
        pass

    def build_order(self):



        self.make_supply(self, gamestate.wall_positions(self, 0))

    def make_supply(self, pos):

        TERRAN_SUPPLYDEPOT = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)

        for SCV in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
            if SCV.is_alive and not SCV.unit_type.is_building:
                builder = SCV

        builder.build(TERRAN_SUPPLYDEPOT, pos)

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

            self.map_tools.draw_text(unit.position, (str(unit.unit_type.unit_typeid)[12::] + " Nr:" + str(pos)
                                                     + " POSITION:" + str(unit.position)), Color(255, 255, 255))

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
            self.map_tools.draw_text(unit.position, (str(unit.unit_type.unit_typeid)[12::] + " Nr:" + str(pos)),
                                    Color(255, 255, 255))

        for unit in gas_deposits:

            type = unit.unit_type.unit_typeid

            if type not in gamestate.NEUTRALUNITS:
                gamestate.NEUTRALUNITS.update({type: [unit]})
                print("Added", type, 'To neutral dictionary')
            elif unit not in gamestate.NEUTRALUNITS[type]:
                gamestate.NEUTRALUNITS[type].append(unit)

            pos = gamestate.NEUTRALUNITS[type].index(unit)
            self.map_tools.draw_text(unit.position, (str(unit.unit_type.unit_typeid)[12::] + " Nr:" + str(pos)),
                                     Color(255, 255, 255))

    def distribute_workers(self):
        """Distributes idle workers to nearby mineral nodes"""

        mineral_deposits = self.base_location_manager.get_player_starting_base_location(0).minerals
        gas_deposits = self.base_location_manager.get_player_starting_base_location(0).geysers

        for worker in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
            if worker.is_idle:
                for minerals in mineral_deposits:
                    worker.right_click(minerals)
                    gamestate.MINERAL_WORKER.append(worker)
                if UNIT_TYPEID.TERRAN_REFINERY in gamestate.AGENTUNITS:
                    for gas in gas_deposits:
                        worker.right_click(gas)
                        gamestate.GAS_WORKER.append(worker)

    def econ_check(self, unit_type: UnitType):
        """Asserts that agents economy allows the requested build/train command"""

        return self.minerals >= unit_type.mineral_price \
               and self.gas >= unit_type.gas_price \
               and self.max_supply - self.current_supply >= unit_type.supply_required

    def make_workers(self):
        """Creates workers"""

        TERRAN_SCV = UnitType(UNIT_TYPEID.TERRAN_SCV, self)

        for base in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]:
            if (len(gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]) < 22) \
                    and (Bot.econ_check(self, TERRAN_SCV) == True) \
                    and not base.is_training:
                base.train(TERRAN_SCV)

    def make_wall(self, step):  # NOT FUNCTIONING AS INTENDED
        """Builds Supply Depots in case the supply dips below a threshold value"""

        TERRAN_SUPPLYDEPOT = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)
        TERRAN_BARRACKS = UnitType(UNIT_TYPEID.TERRAN_BARRACKS, self)

        if gamestate.start_base(self) == 'NE':
            Wall_Supply_1 = (37.0, 122.0)
            Wall_Supply_2 = (34.0, 125.0)
            Wall_Barrack = (36.5, 124.5)
        elif gamestate.start_base(self) == 'SE':
            Wall_Supply_1 = (118.0, 43.0)
            Wall_Supply_2 = (115.0, 46.0)
            Wall_Barrack = (115.5, 43.5)

        for SCV in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV]:
            if SCV.is_alive and not SCV.unit_type.is_building:
                builder = SCV

        if self.minerals >= 100:

            builder.build(TERRAN_SUPPLYDEPOT, Point2DI(int(Wall_Supply_1[0]),int(Wall_Supply_1[1])))
            await if not gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SUPPLYDEPOT][0].unit_type.is_building:
                builder.build(TERRAN_SUPPLYDEPOT, Point2DI(int(Wall_Supply_2[0]),int(Wall_Supply_2[1])))
                time.sleep(3)
                if not gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SUPPLYDEPOT][1].unit_type.is_building:
                    builder.build(TERRAN_BARRACKS, Point2DI(int(Wall_Barrack[0]), int(Wall_Barrack[1])))
                    time.sleep(3)
                    return True

    def session_info(self, runtime):
        """Draws info about current session on screen"""

        mapdraw = self.map_tools.draw_text_screen

        mapdraw(0.02, 0.20, "Workers:" + str(len(gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV])), Color(100, 200, 255))

        mapdraw(0.02, 0.10, "Minerals Spent:" + str(gamestate.total_value(self)[0]), Color(100, 200, 255))
        mapdraw(0.02, 0.115, "Gas Spent:" + str(gamestate.total_value(self)[1]), Color(100, 200, 255))
        mapdraw(0.02, 0.13, "Minerals Lost:" + str(gamestate.total_lost(self)[0]), Color(100, 200, 255))
        mapdraw(0.02, 0.145, "Gas Lost:" + str(gamestate.total_lost(self)[1]), Color(100, 200, 255))

        mapdraw(0.02, 0.60, "Minerals:" + str(self.minerals), Color(100, 200, 255))
        mapdraw(0.02, 0.615, "Gas:" + str(self.gas), Color(100, 200, 255))
        mapdraw(0.02, 0.63, "Unused Supply:" + str(self.max_supply - self.current_supply), Color(100, 200, 255))
        mapdraw(0.02, 0.645, "Runtime " + str(round(runtime, 0)), Color(100, 200, 255))

    def get_my_producers(self, unit_type: UnitType):  # NOT IMPLEMENTED
        """ Returns a list of units which can build or train units of type unit_type """

        producers = []
        type_data = self.tech_tree.get_data(unit_type)
        what_builds = type_data.what_builds

        for unit in self.get_my_units():
            if unit.unit_type in what_builds:
                producers.append(unit)

        return producers



"""///////////////////////// TEST METHODS ////////////////////////"""

