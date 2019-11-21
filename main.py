import os
import time

from library import *

from Bot import *
from data import *


class MyAgent(IDABot):

    global init_time
    init_time = time.time()
    global counter
    counter = 0

    def __init__(self):
        IDABot.__init__(self)

    def on_game_start(self):
        IDABot.on_game_start(self)

    def on_step(self):
        runtime = time.time() - init_time
        start = time.time()

        IDABot.on_step(self)

        "MAIN"

        "CO-ROUTINES"
        Bot.unit_debug(self)  # DEBUG
        Bot.neutral_debug(self)  # DEBUG
        Bot.enemy_debug(self)  # DEBUG
        Bot.debug_info(self)
        Bot.unit_task(self)
        Bot.map_info(self)
        Bot.base_handler(self)

        Bot.clear_build_list(self)  # DATA HANDLER
        Bot.build_queue(self)  # DATA HANDLER
        Bot.unit_death_handler()  # DATA HANDLER
        Bot.worker_task_checker(self)

        Bot.make_barracks(self)

        Bot.state_listener(self)  # STATE HANDLER
        Bot.base_listener(self)  # STATE HANDLER
        if Bot.enemy_attacking():
            Bot.state_setter('PURPOSE', 'DEFENCE')

        Bot.mineral_worker_handler(self)  # BOT ACTION
        Bot.gas_worker_handler(self)
        Bot.make_supply_depot(self)  # BOT ACTION
        Bot.make_workers(self)  # BOT ACTION
        Bot.move_marines_to_ramp(self)


        "STATE-LOGIC"
        if Data.AGENTSTATE['STATE'] == 0:

            #Bot.send_scout(self)  # BOT ACTION
            Bot.make_refinery(self)  # BOT ACTION
            #Bot.make_barracks(self)  # BOT ACTION
            if UNIT_TYPEID.TERRAN_BARRACKS in Data.AGENTUNITS:
                Bot.barracks_upgrade(self)  # BOT ACTION
                Bot.make_marines(self)  # BOT ACTION
                Bot.expand(self)
                #Bot.make_marauder(self)
                #Bot.make_engineering_bay(self)  # BOT ACTION
        #
        # if Data.AGENTSTATE['STATE'] == 1:
        #
        #     if Data.AGENTSTATE['ROUTINE'] == 'UPKEEP':
        #         Bot.make_factory(self)  # BOT ACTION
        #         Bot.upgrade_orbital_command(self)  # BOT ACTION
        #         Bot.research_tech(self)  # BOT ACTION
        #         Bot.barracks_upgrade(self)  # BOT ACTION
        #         #Bot.make_armory
        #         #Bot.expand_base
        #         #Bot.make_starport
        #
        #     if Data.AGENTSTATE['STRATEGY'] == 'BIOPRESSURE':
        #         Bot.make_marines(self)  # BOT ACTION
        #         Bot.make_marauder(self)  # BOT ACTION
        #         if UNIT_TYPEID.TERRAN_STARPORT in Data.AGENTSTATE:
        #             pass
        #
        #     if Data.AGENTSTATE['PURPOSE'] == 'OFFENCE':
        #         if UNIT_TYPEID.TERRAN_MARINE in Data.AGENTUNITS:
        #             Bot.marine_charge(self)  # BOT ACTION
        #             Bot.marauder_charge(self)
        #
        #     if Data.AGENTSTATE['PURPOSE'] == 'DEFENCE':
        #         Bot.defend_base(self)






















        # if Bot.supply_check(self):
        #    Bot.make_wall(self)
        #Bot.make_barracks(self)
        #if UNIT_TYPEID.TERRAN_BARRACKS in gamestate.AGENTUNITS:
        #Bot.build_order(self) # NOT FUNCTIONING AS INDENTED




        performance = 0 #60 / (time.time() - start)
        Bot.session_info(self, runtime, performance)  # GRAPHICS


def main():

    coordinator = Coordinator(r'E:\StarCraft II\Versions\Base69232\SC2_x64.exe')
    bot1 = MyAgent()
    # bot2 =

    participant_1 = create_participants(Race.Terran, bot1)
    # participant_2 = create_participants(Race.Terran, bot2)
    participant_2 = create_computer(Race.Terran, Difficulty.Easy)

    coordinator.set_real_time(False)
    coordinator.set_participants([participant_1, participant_2])
    coordinator.launch_starcraft()

    path = os.path.join(os.getcwd(), "maps", "InterloperTest.SC2Map")
    coordinator.start_game(path)

    while coordinator.update():
        pass


if __name__ == "__main__":
    main()

