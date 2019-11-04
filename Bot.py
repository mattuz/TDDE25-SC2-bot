from main import *
from library import *
from gamestate import *
import inspect


class Bot(MyAgent):
    """ Main method handler for bot features. Inherits MyAgent """

    def __init__(self):
        pass

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

            self.map_tools.draw_text(unit.position, (str(unit.unit_type) + " id: " + str(unit.id) + " i: " + str(pos)),
                                     Color(255, 255, 255))

    def neutral_debug(self):
        """"Prints a debug message over neutral units, also adds each unit to gamestate.AGENTUNITS dictionary"""

        for unit in self.base_location_manager.starting_base_locations[0].mineral_fields:

            #if unit in self.base_location_manager.starting_base_locations[0].mineral_fields or \
             #            self.base_location_manager.starting_base_locations[0].geysers:

            type = unit.unit_type.unit_typeid

            if type not in gamestate.AGENTUNITS:
                gamestate.AGENTUNITS.update({type: [unit]})
                print("Added", type, 'To units dictionary')
            elif unit not in gamestate.AGENTUNITS[type]:
                gamestate.AGENTUNITS[type].append(unit)

            pos = gamestate.AGENTUNITS[type].index(unit)

            self.map_tools.draw_text(unit.position, (str(unit.unit_type) + " id: " + str(unit.id) + " i: " + str(pos)),
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

    def make_supply(self):  # NOT FUNCTIONING AS INTENDED
        """Builds Supply Depots in case the supply dips below a threshold value"""

        TERRAN_SUPPLYDEPOT = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)

        supply_1 = (120, 75)
        supply_2 = (124, 80)

        # if self.base_location_manager.get_player_starting_base_location(0).is_start_location:

        if Bot.econ_check(self, TERRAN_SUPPLYDEPOT):
            # BuildingPlacer.get_build_location_near(self, 120, 41, TERRAN_SUPPLYDEPOT, 2, 10)
            Unit.build(TERRAN_SUPPLYDEPOT, supply_1)

    def session_info(self, runtime):
        """Draws info about current session on screen"""

        mapdraw = self.map_tools.draw_text_screen

        mapdraw(0.02, 0.20, "Workers:" + str(len(gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV])), Color(100, 200, 255))
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
