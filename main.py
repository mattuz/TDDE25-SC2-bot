from Bot import *
from library import *
import time
import os


class MyAgent(IDABot):

    global init_time
    init_time = time.time()

    def __init__(self):
        IDABot.__init__(self)

    def on_game_start(self):
        IDABot.on_game_start(self)

    def on_step(self):
        runtime = time.time() - init_time

        IDABot.on_step(self)

        """MAIN"""

        Bot.unit_debug(self)
        Bot.neutral_debug(self)
        Bot.distribute_workers(self)
        Bot.make_supply(self)
        Bot.make_workers(self)
        Bot.make_refinery(self)


        # if Bot.supply_check(self):
        #    Bot.make_wall(self)
        #Bot.make_barracks(self)
        #if UNIT_TYPEID.TERRAN_BARRACKS in gamestate.AGENTUNITS:
        #    Bot.barracks_upgrade(self)
        #    Bot.make_marines(self)
        #    if UNIT_TYPEID.TERRAN_MARINE in gamestate.AGENTUNITS:
        #        Bot.marine_charge(self)




        #Bot.build_order(self) # NOT FUNCTIONING AS INDENTED

        Bot.session_info(self, runtime)


def main():

    coordinator = Coordinator(r'D:\StarCraft II\Versions\Base69232\SC2_x64.exe')
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

