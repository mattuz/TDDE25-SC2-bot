"""FRÅN CLASS.BOT"""

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







def make_wall(self):

    TERRAN_SUPPLYDEPOT = UnitType(UNIT_TYPEID.TERRAN_SUPPLYDEPOT, self)
    builder = Bot.get_worker()

    if Bot.econ_check(self, TERRAN_SUPPLYDEPOT):
        if self.max_supply < 23 and UNIT_TYPEID.TERRAN_SUPPLYDEPOT not in gamestate.AGENTUNITS:
            x = int(gamestate.wall_positions(self, 0)[0])
            y = int(gamestate.wall_positions(self, 0)[1])
            if self.building_placer.can_build_here(x, y, TERRAN_SUPPLYDEPOT):
                builder.build(TERRAN_SUPPLYDEPOT, Point2DI(x, y))
                Bot.task_remover(builder)
                gamestate.BUILDER.append(builder)
                Bot.Debug_info[0] = [ 'Added', builder, 'To BUILDER list')
                return

        if 15 == self.max_supply and \
                gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SUPPLYDEPOT][0].build_percentage > 0.6:
            x = int(gamestate.wall_positions(self, 1)[0])
            y = int(gamestate.wall_positions(self, 1)[1])
            if self.building_placer.can_build_here(x, y, TERRAN_SUPPLYDEPOT):
                builder.build(TERRAN_SUPPLYDEPOT, Point2DI(x, y))
                Bot.task_remover(builder)
                gamestate.BUILDER.append(builder)
                Bot.Debug_info[0] = [ 'Added', builder, 'To BUILDER list')
                return

def make_barracks_old(self):
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


