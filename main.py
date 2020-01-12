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
        Bot.unit_debug(self)
        Bot.neutral_debug(self)
        Bot.stray_worker_handling(self)
        Bot.enemy_debug(self)
        Bot.unit_task(self)
        Bot.clear_build_list(self)
        Bot.state_listener(self)
        Bot.base_listener(self)

        if UNIT_TYPEID.NEUTRAL_MINERALFIELD and UNIT_TYPEID.NEUTRAL_MINERALFIELD750 in Data.NEUTRALUNITS:
            Bot.base_handler(self)
            Bot.mineral_worker_handler(self)
            Bot.gas_worker_handler(self)
            Bot.worker_task_handler(self)
            Bot.make_supply_depot(self)  # BOT ACTION
            Bot.make_bunker(self)
            Bot.make_marines(self)
            Bot.barracks_upgrade(self)
            Bot.make_refinery(self)
            Bot.make_barracks(self)
            Bot.make_workers(self)
            Bot.make_factory(self)
            Bot.factory_upgrade(self)
            Bot.make_siege_tanks(self)
            Bot.map_info(self)
            Bot.send_scout(self)
            Bot.upgrade_orbital_command(self)
            Bot.lower_supply(self)
            Bot.make_marauders(self)
            Bot.unit_attack_handler(self)

            if UNIT_TYPEID.TERRAN_SUPPLYDEPOT in Data.AGENTUNITS:
                Bot.make_expansion(self)
            if 'ATTACKERS' not in Data.AGENT_COMBATUNITS:
                Bot.move_marines_to_ramp(self)
                Bot.move_siege_to_defend(self)

        performance = 0
        Bot.session_info(self, runtime, performance)  # GRAPHICS


def main():

    coordinator = Coordinator(r'F:\StarCraft II\Versions\Base69232\SC2_x64.exe')
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

