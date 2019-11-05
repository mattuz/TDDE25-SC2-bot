# encoding: utf-8
# module library
# from F:/sc2-python-bot\library.cp37-win_amd64.pyd
# by generator 1.145
""" Python API for playing Starcraft II """

# imports
import library.util as util  # <module 'library.util'>
import pybind11_builtins as __pybind11_builtins

# Variables with simple values

PLAYER_ALLY = 3
PLAYER_ENEMY = 1
PLAYER_NEUTRAL = 2
PLAYER_SELF = 0


# functions

"""/////////////////////////////////////////////////////////////////
TÄNK PÅ ATT DENNA FILEN INTE KAN IMPORTERAS TILL SJÄLVASTE BOTTEN
DETTA ÄR BARA FÖR ATT GÖRA API-SÖKANDE ENKLARE OCH MER INTE-SVINDRYGT
PLUS, OFFLINEARBETE OM MAN NU VILL GÖRA DET

Erik, 5/11
//////////////////////////////////////////////////////////////////"""




def create_computer(race, difficulty):  # real signature unknown; restored from __doc__
    """
    create_computer(race: library.Race, difficulty: library.Difficulty) -> library.PlayerSetup

    Create participant from built-in Starcraft computer
    """
    pass


def create_participants(race, bot):  # real signature unknown; restored from __doc__
    """
    create_participants(race: library.Race, bot: library.Agent) -> library.PlayerSetup

    Create participant from bot
    """
    pass


# classes

class AbilityID(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: library.AbilityID, arg0: library.ABILITY_ID) -> None """
        pass


class ABILITY_ID(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, arg0):  # real signature unknown; restored from __doc__
        """ __eq__(self: library.ABILITY_ID, arg0: library.ABILITY_ID) -> bool """
        return False

    def __getstate__(self):  # real signature unknown; restored from __doc__
        """ __getstate__(self: library.ABILITY_ID) -> tuple """
        return ()

    def __hash__(self):  # real signature unknown; restored from __doc__
        """ __hash__(self: library.ABILITY_ID) -> int """
        return 0

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: library.ABILITY_ID, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: library.ABILITY_ID) -> int """
        return 0

    def __ne__(self, arg0):  # real signature unknown; restored from __doc__
        """ __ne__(self: library.ABILITY_ID, arg0: library.ABILITY_ID) -> bool """
        return False

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: library.ABILITY_ID) -> str """
        return ""

    def __setstate__(self, arg0):  # real signature unknown; restored from __doc__
        """ __setstate__(self: library.ABILITY_ID, arg0: tuple) -> None """
        pass

    ATTACK = None  # (!) real value is ''
    ATTACK_ATTACK = None  # (!) real value is ''
    ATTACK_ATTACKBUILDING = None  # (!) real value is ''
    ATTACK_REDIRECT = None  # (!) real value is ''
    BEHAVIOR_BUILDINGATTACKOFF = None  # (!) real value is ''
    BEHAVIOR_BUILDINGATTACKON = None  # (!) real value is ''
    BEHAVIOR_CLOAKOFF = None  # (!) real value is ''
    BEHAVIOR_CLOAKOFF_BANSHEE = None  # (!) real value is ''
    BEHAVIOR_CLOAKOFF_GHOST = None  # (!) real value is ''
    BEHAVIOR_CLOAKON = None  # (!) real value is ''
    BEHAVIOR_CLOAKON_BANSHEE = None  # (!) real value is ''
    BEHAVIOR_CLOAKON_GHOST = None  # (!) real value is ''
    BEHAVIOR_GENERATECREEPOFF = None  # (!) real value is ''
    BEHAVIOR_GENERATECREEPON = None  # (!) real value is ''
    BEHAVIOR_HOLDFIREOFF = None  # (!) real value is ''
    BEHAVIOR_HOLDFIREOFF_LURKER = None  # (!) real value is ''
    BEHAVIOR_HOLDFIREON = None  # (!) real value is ''
    BEHAVIOR_HOLDFIREON_GHOST = None  # (!) real value is ''
    BEHAVIOR_HOLDFIREON_LURKER = None  # (!) real value is ''
    BEHAVIOR_PULSARBEAMOFF = None  # (!) real value is ''
    BEHAVIOR_PULSARBEAMON = None  # (!) real value is ''
    BUILD_ARMORY = None  # (!) real value is ''
    BUILD_ASSIMILATOR = None  # (!) real value is ''
    BUILD_BANELINGNEST = None  # (!) real value is ''
    BUILD_BARRACKS = None  # (!) real value is ''
    BUILD_BUNKER = None  # (!) real value is ''
    BUILD_COMMANDCENTER = None  # (!) real value is ''
    BUILD_CREEPTUMOR = None  # (!) real value is ''
    BUILD_CREEPTUMOR_QUEEN = None  # (!) real value is ''
    BUILD_CREEPTUMOR_TUMOR = None  # (!) real value is ''
    BUILD_CYBERNETICSCORE = None  # (!) real value is ''
    BUILD_DARKSHRINE = None  # (!) real value is ''
    BUILD_ENGINEERINGBAY = None  # (!) real value is ''
    BUILD_EVOLUTIONCHAMBER = None  # (!) real value is ''
    BUILD_EXTRACTOR = None  # (!) real value is ''
    BUILD_FACTORY = None  # (!) real value is ''
    BUILD_FLEETBEACON = None  # (!) real value is ''
    BUILD_FORGE = None  # (!) real value is ''
    BUILD_FUSIONCORE = None  # (!) real value is ''
    BUILD_GATEWAY = None  # (!) real value is ''
    BUILD_GHOSTACADEMY = None  # (!) real value is ''
    BUILD_HATCHERY = None  # (!) real value is ''
    BUILD_HYDRALISKDEN = None  # (!) real value is ''
    BUILD_INFESTATIONPIT = None  # (!) real value is ''
    BUILD_INTERCEPTORS = None  # (!) real value is ''
    BUILD_MISSILETURRET = None  # (!) real value is ''
    BUILD_NEXUS = None  # (!) real value is ''
    BUILD_NUKE = None  # (!) real value is ''
    BUILD_NYDUSNETWORK = None  # (!) real value is ''
    BUILD_NYDUSWORM = None  # (!) real value is ''
    BUILD_PHOTONCANNON = None  # (!) real value is ''
    BUILD_PYLON = None  # (!) real value is ''
    BUILD_REACTOR = None  # (!) real value is ''
    BUILD_REACTOR_BARRACKS = None  # (!) real value is ''
    BUILD_REACTOR_FACTORY = None  # (!) real value is ''
    BUILD_REACTOR_STARPORT = None  # (!) real value is ''
    BUILD_REFINERY = None  # (!) real value is ''
    BUILD_ROACHWARREN = None  # (!) real value is ''
    BUILD_ROBOTICSBAY = None  # (!) real value is ''
    BUILD_ROBOTICSFACILITY = None  # (!) real value is ''
    BUILD_SENSORTOWER = None  # (!) real value is ''
    BUILD_SHIELDBATTERY = None  # (!) real value is ''
    BUILD_SPAWNINGPOOL = None  # (!) real value is ''
    BUILD_SPINECRAWLER = None  # (!) real value is ''
    BUILD_SPIRE = None  # (!) real value is ''
    BUILD_SPORECRAWLER = None  # (!) real value is ''
    BUILD_STARGATE = None  # (!) real value is ''
    BUILD_STARPORT = None  # (!) real value is ''
    BUILD_STASISTRAP = None  # (!) real value is ''
    BUILD_SUPPLYDEPOT = None  # (!) real value is ''
    BUILD_TECHLAB = None  # (!) real value is ''
    BUILD_TECHLAB_BARRACKS = None  # (!) real value is ''
    BUILD_TECHLAB_FACTORY = None  # (!) real value is ''
    BUILD_TECHLAB_STARPORT = None  # (!) real value is ''
    BUILD_TEMPLARARCHIVE = None  # (!) real value is ''
    BUILD_TWILIGHTCOUNCIL = None  # (!) real value is ''
    BUILD_ULTRALISKCAVERN = None  # (!) real value is ''
    BURROWDOWN = None  # (!) real value is ''
    BURROWDOWN_BANELING = None  # (!) real value is ''
    BURROWDOWN_DRONE = None  # (!) real value is ''
    BURROWDOWN_HYDRALISK = None  # (!) real value is ''
    BURROWDOWN_INFESTOR = None  # (!) real value is ''
    BURROWDOWN_LURKER = None  # (!) real value is ''
    BURROWDOWN_QUEEN = None  # (!) real value is ''
    BURROWDOWN_RAVAGER = None  # (!) real value is ''
    BURROWDOWN_ROACH = None  # (!) real value is ''
    BURROWDOWN_SWARMHOST = None  # (!) real value is ''
    BURROWDOWN_WIDOWMINE = None  # (!) real value is ''
    BURROWDOWN_ZERGLING = None  # (!) real value is ''
    BURROWUP = None  # (!) real value is ''
    BURROWUP_BANELING = None  # (!) real value is ''
    BURROWUP_DRONE = None  # (!) real value is ''
    BURROWUP_HYDRALISK = None  # (!) real value is ''
    BURROWUP_INFESTOR = None  # (!) real value is ''
    BURROWUP_LURKER = None  # (!) real value is ''
    BURROWUP_QUEEN = None  # (!) real value is ''
    BURROWUP_RAVAGER = None  # (!) real value is ''
    BURROWUP_ROACH = None  # (!) real value is ''
    BURROWUP_SWARMHOST = None  # (!) real value is ''
    BURROWUP_WIDOWMINE = None  # (!) real value is ''
    BURROWUP_ZERGLING = None  # (!) real value is ''
    CANCEL = None  # (!) real value is ''
    CANCELSLOT_ADDON = None  # (!) real value is ''
    CANCELSLOT_QUEUE1 = None  # (!) real value is ''
    CANCELSLOT_QUEUE5 = None  # (!) real value is ''
    CANCELSLOT_QUEUECANCELTOSELECTION = None  # (!) real value is ''
    CANCELSLOT_QUEUEPASSIVE = None  # (!) real value is ''
    CANCEL_ADEPTPHASESHIFT = None  # (!) real value is ''
    CANCEL_ADEPTSHADEPHASESHIFT = None  # (!) real value is ''
    CANCEL_BARRACKSADDON = None  # (!) real value is ''
    CANCEL_BUILDINPROGRESS = None  # (!) real value is ''
    CANCEL_CREEPTUMOR = None  # (!) real value is ''
    CANCEL_FACTORYADDON = None  # (!) real value is ''
    CANCEL_GRAVITONBEAM = None  # (!) real value is ''
    CANCEL_LAST = None  # (!) real value is ''
    CANCEL_MORPHBROODLORD = None  # (!) real value is ''
    CANCEL_MORPHLAIR = None  # (!) real value is ''
    CANCEL_MORPHLURKER = None  # (!) real value is ''
    CANCEL_MORPHLURKERDEN = None  # (!) real value is ''
    CANCEL_MORPHMOTHERSHIP = None  # (!) real value is ''
    CANCEL_MORPHORBITAL = None  # (!) real value is ''
    CANCEL_MORPHOVERLORDTRANSPORT = None  # (!) real value is ''
    CANCEL_MORPHOVERSEER = None  # (!) real value is ''
    CANCEL_MORPHPLANETARYFORTRESS = None  # (!) real value is ''
    CANCEL_MORPHRAVAGER = None  # (!) real value is ''
    CANCEL_QUEUE1 = None  # (!) real value is ''
    CANCEL_QUEUE5 = None  # (!) real value is ''
    CANCEL_QUEUEADDON = None  # (!) real value is ''
    CANCEL_QUEUECANCELTOSELECTION = None  # (!) real value is ''
    CANCEL_QUEUEPASIVE = None  # (!) real value is ''
    CANCEL_QUEUEPASSIVECANCELTOSELECTION = None  # (!) real value is ''
    CANCEL_SPINECRAWLERROOT = None  # (!) real value is ''
    CANCEL_STARPORTADDON = None  # (!) real value is ''
    EFFECT_ABDUCT = None  # (!) real value is ''
    EFFECT_ADEPTPHASESHIFT = None  # (!) real value is ''
    EFFECT_AUTOTURRET = None  # (!) real value is ''
    EFFECT_BLINDINGCLOUD = None  # (!) real value is ''
    EFFECT_BLINK = None  # (!) real value is ''
    EFFECT_BLINK_STALKER = None  # (!) real value is ''
    EFFECT_CALLDOWNMULE = None  # (!) real value is ''
    EFFECT_CAUSTICSPRAY = None  # (!) real value is ''
    EFFECT_CHARGE = None  # (!) real value is ''
    EFFECT_CHRONOBOOST = None  # (!) real value is ''
    EFFECT_CONTAMINATE = None  # (!) real value is ''
    EFFECT_CORROSIVEBILE = None  # (!) real value is ''
    EFFECT_EMP = None  # (!) real value is ''
    EFFECT_EXPLODE = None  # (!) real value is ''
    EFFECT_FEEDBACK = None  # (!) real value is ''
    EFFECT_FORCEFIELD = None  # (!) real value is ''
    EFFECT_FUNGALGROWTH = None  # (!) real value is ''
    EFFECT_GHOSTSNIPE = None  # (!) real value is ''
    EFFECT_GRAVITONBEAM = None  # (!) real value is ''
    EFFECT_GUARDIANSHIELD = None  # (!) real value is ''
    EFFECT_HEAL = None  # (!) real value is ''
    EFFECT_HUNTERSEEKERMISSILE = None  # (!) real value is ''
    EFFECT_IMMORTALBARRIER = None  # (!) real value is ''
    EFFECT_INFESTEDTERRANS = None  # (!) real value is ''
    EFFECT_INJECTLARVA = None  # (!) real value is ''
    EFFECT_KD8CHARGE = None  # (!) real value is ''
    EFFECT_LOCKON = None  # (!) real value is ''
    EFFECT_LOCUSTSWOOP = None  # (!) real value is ''
    EFFECT_MASSRECALL = None  # (!) real value is ''
    EFFECT_MASSRECALL_MOTHERSHIP = None  # (!) real value is ''
    EFFECT_MASSRECALL_MOTHERSHIPCORE = None  # (!) real value is ''
    EFFECT_MEDIVACIGNITEAFTERBURNERS = None  # (!) real value is ''
    EFFECT_NEURALPARASITE = None  # (!) real value is ''
    EFFECT_NUKECALLDOWN = None  # (!) real value is ''
    EFFECT_ORACLEREVELATION = None  # (!) real value is ''
    EFFECT_PARASITICBOMB = None  # (!) real value is ''
    EFFECT_PHOTONOVERCHARGE = None  # (!) real value is ''
    EFFECT_POINTDEFENSEDRONE = None  # (!) real value is ''
    EFFECT_PSISTORM = None  # (!) real value is ''
    EFFECT_PURIFICATIONNOVA = None  # (!) real value is ''
    EFFECT_REPAIR = None  # (!) real value is ''
    EFFECT_REPAIR_MULE = None  # (!) real value is ''
    EFFECT_REPAIR_SCV = None  # (!) real value is ''
    EFFECT_RESTORE = None  # (!) real value is ''
    EFFECT_SALVAGE = None  # (!) real value is ''
    EFFECT_SCAN = None  # (!) real value is ''
    EFFECT_SHADOWSTRIDE = None  # (!) real value is ''
    EFFECT_SPAWNCHANGELING = None  # (!) real value is ''
    EFFECT_SPAWNLOCUSTS = None  # (!) real value is ''
    EFFECT_SPRAY = None  # (!) real value is ''
    EFFECT_SPRAY_PROTOSS = None  # (!) real value is ''
    EFFECT_SPRAY_TERRAN = None  # (!) real value is ''
    EFFECT_SPRAY_ZERG = None  # (!) real value is ''
    EFFECT_STIM = None  # (!) real value is ''
    EFFECT_STIM_MARAUDER = None  # (!) real value is ''
    EFFECT_STIM_MARINE = None  # (!) real value is ''
    EFFECT_STIM_MARINE_REDIRECT = None  # (!) real value is ''
    EFFECT_SUPPLYDROP = None  # (!) real value is ''
    EFFECT_TACTICALJUMP = None  # (!) real value is ''
    EFFECT_TEMPESTDISRUPTIONBLAST = None  # (!) real value is ''
    EFFECT_TIMEWARP = None  # (!) real value is ''
    EFFECT_TRANSFUSION = None  # (!) real value is ''
    EFFECT_VIPERCONSUME = None  # (!) real value is ''
    EFFECT_VOIDRAYPRISMATICALIGNMENT = None  # (!) real value is ''
    EFFECT_WIDOWMINEATTACK = None  # (!) real value is ''
    EFFECT_YAMATOGUN = None  # (!) real value is ''
    HALLUCINATION_ADEPT = None  # (!) real value is ''
    HALLUCINATION_ARCHON = None  # (!) real value is ''
    HALLUCINATION_COLOSSUS = None  # (!) real value is ''
    HALLUCINATION_DISRUPTOR = None  # (!) real value is ''
    HALLUCINATION_HIGHTEMPLAR = None  # (!) real value is ''
    HALLUCINATION_IMMORTAL = None  # (!) real value is ''
    HALLUCINATION_ORACLE = None  # (!) real value is ''
    HALLUCINATION_PHOENIX = None  # (!) real value is ''
    HALLUCINATION_PROBE = None  # (!) real value is ''
    HALLUCINATION_STALKER = None  # (!) real value is ''
    HALLUCINATION_VOIDRAY = None  # (!) real value is ''
    HALLUCINATION_WARPPRISM = None  # (!) real value is ''
    HALLUCINATION_ZEALOT = None  # (!) real value is ''
    HALT = None  # (!) real value is ''
    HALT_BUILDING = None  # (!) real value is ''
    HALT_TERRANBUILD = None  # (!) real value is ''
    HARVEST_GATHER = None  # (!) real value is ''
    HARVEST_GATHER_DRONE = None  # (!) real value is ''
    HARVEST_GATHER_PROBE = None  # (!) real value is ''
    HARVEST_GATHER_SCV = None  # (!) real value is ''
    HARVEST_RETURN = None  # (!) real value is ''
    HARVEST_RETURN_DRONE = None  # (!) real value is ''
    HARVEST_RETURN_MULE = None  # (!) real value is ''
    HARVEST_RETURN_PROBE = None  # (!) real value is ''
    HARVEST_RETURN_SCV = None  # (!) real value is ''
    HOLDPOSITION = None  # (!) real value is ''
    INVALID = None  # (!) real value is ''
    LAND = None  # (!) real value is ''
    LAND_BARRACKS = None  # (!) real value is ''
    LAND_COMMANDCENTER = None  # (!) real value is ''
    LAND_FACTORY = None  # (!) real value is ''
    LAND_ORBITALCOMMAND = None  # (!) real value is ''
    LAND_STARPORT = None  # (!) real value is ''
    LIFT = None  # (!) real value is ''
    LIFT_BARRACKS = None  # (!) real value is ''
    LIFT_COMMANDCENTER = None  # (!) real value is ''
    LIFT_FACTORY = None  # (!) real value is ''
    LIFT_ORBITALCOMMAND = None  # (!) real value is ''
    LIFT_STARPORT = None  # (!) real value is ''
    LOAD = None  # (!) real value is ''
    LOADALL = None  # (!) real value is ''
    LOADALL_COMMANDCENTER = None  # (!) real value is ''
    LOAD_BUNKER = None  # (!) real value is ''
    LOAD_MEDIVAC = None  # (!) real value is ''
    MORPH_ARCHON = None  # (!) real value is ''
    MORPH_BROODLORD = None  # (!) real value is ''
    MORPH_GATEWAY = None  # (!) real value is ''
    MORPH_GREATERSPIRE = None  # (!) real value is ''
    MORPH_HELLBAT = None  # (!) real value is ''
    MORPH_HELLION = None  # (!) real value is ''
    MORPH_HIVE = None  # (!) real value is ''
    MORPH_LAIR = None  # (!) real value is ''
    MORPH_LIBERATORAAMODE = None  # (!) real value is ''
    MORPH_LIBERATORAGMODE = None  # (!) real value is ''
    MORPH_LURKER = None  # (!) real value is ''
    MORPH_LURKERDEN = None  # (!) real value is ''
    MORPH_MOTHERSHIP = None  # (!) real value is ''
    MORPH_ORBITALCOMMAND = None  # (!) real value is ''
    MORPH_OVERLORDTRANSPORT = None  # (!) real value is ''
    MORPH_OVERSEER = None  # (!) real value is ''
    MORPH_PLANETARYFORTRESS = None  # (!) real value is ''
    MORPH_RAVAGER = None  # (!) real value is ''
    MORPH_ROOT = None  # (!) real value is ''
    MORPH_SIEGEMODE = None  # (!) real value is ''
    MORPH_SPINECRAWLERROOT = None  # (!) real value is ''
    MORPH_SPINECRAWLERUPROOT = None  # (!) real value is ''
    MORPH_SPORECRAWLERROOT = None  # (!) real value is ''
    MORPH_SPORECRAWLERUPROOT = None  # (!) real value is ''
    MORPH_SUPPLYDEPOT_LOWER = None  # (!) real value is ''
    MORPH_SUPPLYDEPOT_RAISE = None  # (!) real value is ''
    MORPH_THOREXPLOSIVEMODE = None  # (!) real value is ''
    MORPH_THORHIGHIMPACTMODE = None  # (!) real value is ''
    MORPH_UNSIEGE = None  # (!) real value is ''
    MORPH_UPROOT = None  # (!) real value is ''
    MORPH_VIKINGASSAULTMODE = None  # (!) real value is ''
    MORPH_VIKINGFIGHTERMODE = None  # (!) real value is ''
    MORPH_WARPGATE = None  # (!) real value is ''
    MORPH_WARPPRISMPHASINGMODE = None  # (!) real value is ''
    MORPH_WARPPRISMTRANSPORTMODE = None  # (!) real value is ''
    MOVE = None  # (!) real value is ''
    PATROL = None  # (!) real value is ''
    RALLY_BUILDING = None  # (!) real value is ''
    RALLY_COMMANDCENTER = None  # (!) real value is ''
    RALLY_HATCHERY_UNITS = None  # (!) real value is ''
    RALLY_HATCHERY_WORKERS = None  # (!) real value is ''
    RALLY_MORPHING_UNIT = None  # (!) real value is ''
    RALLY_NEXUS = None  # (!) real value is ''
    RALLY_UNITS = None  # (!) real value is ''
    RALLY_WORKERS = None  # (!) real value is ''
    RESEARCH_ADEPTRESONATINGGLAIVES = None  # (!) real value is ''
    RESEARCH_ADVANCEDBALLISTICS = None  # (!) real value is ''
    RESEARCH_BANSHEECLOAKINGFIELD = None  # (!) real value is ''
    RESEARCH_BANSHEEHYPERFLIGHTROTORS = None  # (!) real value is ''
    RESEARCH_BATTLECRUISERWEAPONREFIT = None  # (!) real value is ''
    RESEARCH_BLINK = None  # (!) real value is ''
    RESEARCH_BURROW = None  # (!) real value is ''
    RESEARCH_CENTRIFUGALHOOKS = None  # (!) real value is ''
    RESEARCH_CHARGE = None  # (!) real value is ''
    RESEARCH_CHITINOUSPLATING = None  # (!) real value is ''
    RESEARCH_COMBATSHIELD = None  # (!) real value is ''
    RESEARCH_CONCUSSIVESHELLS = None  # (!) real value is ''
    RESEARCH_DRILLINGCLAWS = None  # (!) real value is ''
    RESEARCH_ENHANCEDMUNITIONS = None  # (!) real value is ''
    RESEARCH_EXTENDEDTHERMALLANCE = None  # (!) real value is ''
    RESEARCH_GLIALREGENERATION = None  # (!) real value is ''
    RESEARCH_GRAVITICBOOSTER = None  # (!) real value is ''
    RESEARCH_GRAVITICDRIVE = None  # (!) real value is ''
    RESEARCH_GROOVEDSPINES = None  # (!) real value is ''
    RESEARCH_HIGHCAPACITYFUELTANKS = None  # (!) real value is ''
    RESEARCH_HISECAUTOTRACKING = None  # (!) real value is ''
    RESEARCH_INFERNALPREIGNITER = None  # (!) real value is ''
    RESEARCH_INTERCEPTORGRAVITONCATAPULT = None  # (!) real value is ''
    RESEARCH_MAGFIELDLAUNCHERS = None  # (!) real value is ''
    RESEARCH_MUSCULARAUGMENTS = None  # (!) real value is ''
    RESEARCH_NEOSTEELFRAME = None  # (!) real value is ''
    RESEARCH_NEURALPARASITE = None  # (!) real value is ''
    RESEARCH_PATHOGENGLANDS = None  # (!) real value is ''
    RESEARCH_PERSONALCLOAKING = None  # (!) real value is ''
    RESEARCH_PHOENIXANIONPULSECRYSTALS = None  # (!) real value is ''
    RESEARCH_PNEUMATIZEDCARAPACE = None  # (!) real value is ''
    RESEARCH_PROTOSSAIRARMOR = None  # (!) real value is ''
    RESEARCH_PROTOSSAIRARMORLEVEL1 = None  # (!) real value is ''
    RESEARCH_PROTOSSAIRARMORLEVEL2 = None  # (!) real value is ''
    RESEARCH_PROTOSSAIRARMORLEVEL3 = None  # (!) real value is ''
    RESEARCH_PROTOSSAIRWEAPONS = None  # (!) real value is ''
    RESEARCH_PROTOSSAIRWEAPONSLEVEL1 = None  # (!) real value is ''
    RESEARCH_PROTOSSAIRWEAPONSLEVEL2 = None  # (!) real value is ''
    RESEARCH_PROTOSSAIRWEAPONSLEVEL3 = None  # (!) real value is ''
    RESEARCH_PROTOSSGROUNDARMOR = None  # (!) real value is ''
    RESEARCH_PROTOSSGROUNDARMORLEVEL1 = None  # (!) real value is ''
    RESEARCH_PROTOSSGROUNDARMORLEVEL2 = None  # (!) real value is ''
    RESEARCH_PROTOSSGROUNDARMORLEVEL3 = None  # (!) real value is ''
    RESEARCH_PROTOSSGROUNDWEAPONS = None  # (!) real value is ''
    RESEARCH_PROTOSSGROUNDWEAPONSLEVEL1 = None  # (!) real value is ''
    RESEARCH_PROTOSSGROUNDWEAPONSLEVEL2 = None  # (!) real value is ''
    RESEARCH_PROTOSSGROUNDWEAPONSLEVEL3 = None  # (!) real value is ''
    RESEARCH_PROTOSSSHIELDS = None  # (!) real value is ''
    RESEARCH_PROTOSSSHIELDSLEVEL1 = None  # (!) real value is ''
    RESEARCH_PROTOSSSHIELDSLEVEL2 = None  # (!) real value is ''
    RESEARCH_PROTOSSSHIELDSLEVEL3 = None  # (!) real value is ''
    RESEARCH_PSISTORM = None  # (!) real value is ''
    RESEARCH_RAPIDFIRELAUNCHERS = None  # (!) real value is ''
    RESEARCH_RAVENCORVIDREACTOR = None  # (!) real value is ''
    RESEARCH_RAVENRECALIBRATEDEXPLOSIVES = None  # (!) real value is ''
    RESEARCH_SHADOWSTRIKE = None  # (!) real value is ''
    RESEARCH_SMARTSERVOS = None  # (!) real value is ''
    RESEARCH_STIMPACK = None  # (!) real value is ''
    RESEARCH_TERRANINFANTRYARMOR = None  # (!) real value is ''
    RESEARCH_TERRANINFANTRYARMORLEVEL1 = None  # (!) real value is ''
    RESEARCH_TERRANINFANTRYARMORLEVEL2 = None  # (!) real value is ''
    RESEARCH_TERRANINFANTRYARMORLEVEL3 = None  # (!) real value is ''
    RESEARCH_TERRANINFANTRYWEAPONS = None  # (!) real value is ''
    RESEARCH_TERRANINFANTRYWEAPONSLEVEL1 = None  # (!) real value is ''
    RESEARCH_TERRANINFANTRYWEAPONSLEVEL2 = None  # (!) real value is ''
    RESEARCH_TERRANINFANTRYWEAPONSLEVEL3 = None  # (!) real value is ''
    RESEARCH_TERRANSHIPWEAPONS = None  # (!) real value is ''
    RESEARCH_TERRANSHIPWEAPONSLEVEL1 = None  # (!) real value is ''
    RESEARCH_TERRANSHIPWEAPONSLEVEL2 = None  # (!) real value is ''
    RESEARCH_TERRANSHIPWEAPONSLEVEL3 = None  # (!) real value is ''
    RESEARCH_TERRANSTRUCTUREARMORUPGRADE = None  # (!) real value is ''
    RESEARCH_TERRANVEHICLEANDSHIPPLATING = None  # (!) real value is ''
    RESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL1 = None  # (!) real value is ''
    RESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL2 = None  # (!) real value is ''
    RESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL3 = None  # (!) real value is ''
    RESEARCH_TERRANVEHICLEWEAPONS = None  # (!) real value is ''
    RESEARCH_TERRANVEHICLEWEAPONSLEVEL1 = None  # (!) real value is ''
    RESEARCH_TERRANVEHICLEWEAPONSLEVEL2 = None  # (!) real value is ''
    RESEARCH_TERRANVEHICLEWEAPONSLEVEL3 = None  # (!) real value is ''
    RESEARCH_TUNNELINGCLAWS = None  # (!) real value is ''
    RESEARCH_WARPGATE = None  # (!) real value is ''
    RESEARCH_ZERGFLYERARMOR = None  # (!) real value is ''
    RESEARCH_ZERGFLYERARMORLEVEL1 = None  # (!) real value is ''
    RESEARCH_ZERGFLYERARMORLEVEL2 = None  # (!) real value is ''
    RESEARCH_ZERGFLYERARMORLEVEL3 = None  # (!) real value is ''
    RESEARCH_ZERGFLYERATTACK = None  # (!) real value is ''
    RESEARCH_ZERGFLYERATTACKLEVEL1 = None  # (!) real value is ''
    RESEARCH_ZERGFLYERATTACKLEVEL2 = None  # (!) real value is ''
    RESEARCH_ZERGFLYERATTACKLEVEL3 = None  # (!) real value is ''
    RESEARCH_ZERGGROUNDARMOR = None  # (!) real value is ''
    RESEARCH_ZERGGROUNDARMORLEVEL1 = None  # (!) real value is ''
    RESEARCH_ZERGGROUNDARMORLEVEL2 = None  # (!) real value is ''
    RESEARCH_ZERGGROUNDARMORLEVEL3 = None  # (!) real value is ''
    RESEARCH_ZERGLINGADRENALGLANDS = None  # (!) real value is ''
    RESEARCH_ZERGLINGMETABOLICBOOST = None  # (!) real value is ''
    RESEARCH_ZERGMELEEWEAPONS = None  # (!) real value is ''
    RESEARCH_ZERGMELEEWEAPONSLEVEL1 = None  # (!) real value is ''
    RESEARCH_ZERGMELEEWEAPONSLEVEL2 = None  # (!) real value is ''
    RESEARCH_ZERGMELEEWEAPONSLEVEL3 = None  # (!) real value is ''
    RESEARCH_ZERGMISSILEWEAPONS = None  # (!) real value is ''
    RESEARCH_ZERGMISSILEWEAPONSLEVEL1 = None  # (!) real value is ''
    RESEARCH_ZERGMISSILEWEAPONSLEVEL2 = None  # (!) real value is ''
    RESEARCH_ZERGMISSILEWEAPONSLEVEL3 = None  # (!) real value is ''
    SCAN_MOVE = None  # (!) real value is ''
    SMART = None  # (!) real value is ''
    STOP = None  # (!) real value is ''
    STOP_BUILDING = None  # (!) real value is ''
    STOP_CHEER = None  # (!) real value is ''
    STOP_DANCE = None  # (!) real value is ''
    STOP_REDIRECT = None  # (!) real value is ''
    STOP_STOP = None  # (!) real value is ''
    TRAINWARP_ADEPT = None  # (!) real value is ''
    TRAINWARP_DARKTEMPLAR = None  # (!) real value is ''
    TRAINWARP_HIGHTEMPLAR = None  # (!) real value is ''
    TRAINWARP_SENTRY = None  # (!) real value is ''
    TRAINWARP_STALKER = None  # (!) real value is ''
    TRAINWARP_ZEALOT = None  # (!) real value is ''
    TRAIN_ADEPT = None  # (!) real value is ''
    TRAIN_BANELING = None  # (!) real value is ''
    TRAIN_BANSHEE = None  # (!) real value is ''
    TRAIN_BATTLECRUISER = None  # (!) real value is ''
    TRAIN_CARRIER = None  # (!) real value is ''
    TRAIN_COLOSSUS = None  # (!) real value is ''
    TRAIN_CORRUPTOR = None  # (!) real value is ''
    TRAIN_CYCLONE = None  # (!) real value is ''
    TRAIN_DARKTEMPLAR = None  # (!) real value is ''
    TRAIN_DISRUPTOR = None  # (!) real value is ''
    TRAIN_DRONE = None  # (!) real value is ''
    TRAIN_GHOST = None  # (!) real value is ''
    TRAIN_HELLBAT = None  # (!) real value is ''
    TRAIN_HELLION = None  # (!) real value is ''
    TRAIN_HIGHTEMPLAR = None  # (!) real value is ''
    TRAIN_HYDRALISK = None  # (!) real value is ''
    TRAIN_IMMORTAL = None  # (!) real value is ''
    TRAIN_INFESTOR = None  # (!) real value is ''
    TRAIN_LIBERATOR = None  # (!) real value is ''
    TRAIN_MARAUDER = None  # (!) real value is ''
    TRAIN_MARINE = None  # (!) real value is ''
    TRAIN_MEDIVAC = None  # (!) real value is ''
    TRAIN_MOTHERSHIP = None  # (!) real value is ''
    TRAIN_MOTHERSHIPCORE = None  # (!) real value is ''
    TRAIN_MUTALISK = None  # (!) real value is ''
    TRAIN_OBSERVER = None  # (!) real value is ''
    TRAIN_ORACLE = None  # (!) real value is ''
    TRAIN_OVERLORD = None  # (!) real value is ''
    TRAIN_PHOENIX = None  # (!) real value is ''
    TRAIN_PROBE = None  # (!) real value is ''
    TRAIN_QUEEN = None  # (!) real value is ''
    TRAIN_RAVEN = None  # (!) real value is ''
    TRAIN_REAPER = None  # (!) real value is ''
    TRAIN_ROACH = None  # (!) real value is ''
    TRAIN_SCV = None  # (!) real value is ''
    TRAIN_SENTRY = None  # (!) real value is ''
    TRAIN_SIEGETANK = None  # (!) real value is ''
    TRAIN_STALKER = None  # (!) real value is ''
    TRAIN_SWARMHOST = None  # (!) real value is ''
    TRAIN_TEMPEST = None  # (!) real value is ''
    TRAIN_THOR = None  # (!) real value is ''
    TRAIN_ULTRALISK = None  # (!) real value is ''
    TRAIN_VIKINGFIGHTER = None  # (!) real value is ''
    TRAIN_VIPER = None  # (!) real value is ''
    TRAIN_VOIDRAY = None  # (!) real value is ''
    TRAIN_WARPPRISM = None  # (!) real value is ''
    TRAIN_WIDOWMINE = None  # (!) real value is ''
    TRAIN_ZEALOT = None  # (!) real value is ''
    TRAIN_ZERGLING = None  # (!) real value is ''
    UNLOADALL = None  # (!) real value is ''
    UNLOADALLAT = None  # (!) real value is ''
    UNLOADALLAT_MEDIVAC = None  # (!) real value is ''
    UNLOADALLAT_OVERLORD = None  # (!) real value is ''
    UNLOADALLAT_WARPPRISM = None  # (!) real value is ''
    UNLOADALL_BUNKER = None  # (!) real value is ''
    UNLOADALL_COMMANDCENTER = None  # (!) real value is ''
    UNLOADALL_NYDASNETWORK = None  # (!) real value is ''
    UNLOADALL_NYDUSWORM = None  # (!) real value is ''
    UNLOADUNIT_BUNKER = None  # (!) real value is ''
    UNLOADUNIT_COMMANDCENTER = None  # (!) real value is ''
    UNLOADUNIT_MEDIVAC = None  # (!) real value is ''
    UNLOADUNIT_NYDASNETWORK = None  # (!) real value is ''
    UNLOADUNIT_OVERLORD = None  # (!) real value is ''
    UNLOADUNIT_WARPPRISM = None  # (!) real value is ''
    __members__ = {
        'ATTACK': '<failed to retrieve the value>',
        'ATTACK_ATTACK': '<failed to retrieve the value>',
        'ATTACK_ATTACKBUILDING': '<failed to retrieve the value>',
        'ATTACK_REDIRECT': '<failed to retrieve the value>',
        'BEHAVIOR_BUILDINGATTACKOFF': '<failed to retrieve the value>',
        'BEHAVIOR_BUILDINGATTACKON': '<failed to retrieve the value>',
        'BEHAVIOR_CLOAKOFF': '<failed to retrieve the value>',
        'BEHAVIOR_CLOAKOFF_BANSHEE': '<failed to retrieve the value>',
        'BEHAVIOR_CLOAKOFF_GHOST': '<failed to retrieve the value>',
        'BEHAVIOR_CLOAKON': '<failed to retrieve the value>',
        'BEHAVIOR_CLOAKON_BANSHEE': '<failed to retrieve the value>',
        'BEHAVIOR_CLOAKON_GHOST': '<failed to retrieve the value>',
        'BEHAVIOR_GENERATECREEPOFF': '<failed to retrieve the value>',
        'BEHAVIOR_GENERATECREEPON': '<failed to retrieve the value>',
        'BEHAVIOR_HOLDFIREOFF': '<failed to retrieve the value>',
        'BEHAVIOR_HOLDFIREOFF_LURKER': '<failed to retrieve the value>',
        'BEHAVIOR_HOLDFIREON': '<failed to retrieve the value>',
        'BEHAVIOR_HOLDFIREON_GHOST': '<failed to retrieve the value>',
        'BEHAVIOR_HOLDFIREON_LURKER': '<failed to retrieve the value>',
        'BEHAVIOR_PULSARBEAMOFF': '<failed to retrieve the value>',
        'BEHAVIOR_PULSARBEAMON': '<failed to retrieve the value>',
        'BUILD_ARMORY': '<failed to retrieve the value>',
        'BUILD_ASSIMILATOR': '<failed to retrieve the value>',
        'BUILD_BANELINGNEST': '<failed to retrieve the value>',
        'BUILD_BARRACKS': '<failed to retrieve the value>',
        'BUILD_BUNKER': '<failed to retrieve the value>',
        'BUILD_COMMANDCENTER': '<failed to retrieve the value>',
        'BUILD_CREEPTUMOR': '<failed to retrieve the value>',
        'BUILD_CREEPTUMOR_QUEEN': '<failed to retrieve the value>',
        'BUILD_CREEPTUMOR_TUMOR': '<failed to retrieve the value>',
        'BUILD_CYBERNETICSCORE': '<failed to retrieve the value>',
        'BUILD_DARKSHRINE': '<failed to retrieve the value>',
        'BUILD_ENGINEERINGBAY': '<failed to retrieve the value>',
        'BUILD_EVOLUTIONCHAMBER': '<failed to retrieve the value>',
        'BUILD_EXTRACTOR': '<failed to retrieve the value>',
        'BUILD_FACTORY': '<failed to retrieve the value>',
        'BUILD_FLEETBEACON': '<failed to retrieve the value>',
        'BUILD_FORGE': '<failed to retrieve the value>',
        'BUILD_FUSIONCORE': '<failed to retrieve the value>',
        'BUILD_GATEWAY': '<failed to retrieve the value>',
        'BUILD_GHOSTACADEMY': '<failed to retrieve the value>',
        'BUILD_HATCHERY': '<failed to retrieve the value>',
        'BUILD_HYDRALISKDEN': '<failed to retrieve the value>',
        'BUILD_INFESTATIONPIT': '<failed to retrieve the value>',
        'BUILD_INTERCEPTORS': '<failed to retrieve the value>',
        'BUILD_MISSILETURRET': '<failed to retrieve the value>',
        'BUILD_NEXUS': '<failed to retrieve the value>',
        'BUILD_NUKE': '<failed to retrieve the value>',
        'BUILD_NYDUSNETWORK': '<failed to retrieve the value>',
        'BUILD_NYDUSWORM': '<failed to retrieve the value>',
        'BUILD_PHOTONCANNON': '<failed to retrieve the value>',
        'BUILD_PYLON': '<failed to retrieve the value>',
        'BUILD_REACTOR': '<failed to retrieve the value>',
        'BUILD_REACTOR_BARRACKS': '<failed to retrieve the value>',
        'BUILD_REACTOR_FACTORY': '<failed to retrieve the value>',
        'BUILD_REACTOR_STARPORT': '<failed to retrieve the value>',
        'BUILD_REFINERY': '<failed to retrieve the value>',
        'BUILD_ROACHWARREN': '<failed to retrieve the value>',
        'BUILD_ROBOTICSBAY': '<failed to retrieve the value>',
        'BUILD_ROBOTICSFACILITY': '<failed to retrieve the value>',
        'BUILD_SENSORTOWER': '<failed to retrieve the value>',
        'BUILD_SHIELDBATTERY': '<failed to retrieve the value>',
        'BUILD_SPAWNINGPOOL': '<failed to retrieve the value>',
        'BUILD_SPINECRAWLER': '<failed to retrieve the value>',
        'BUILD_SPIRE': '<failed to retrieve the value>',
        'BUILD_SPORECRAWLER': '<failed to retrieve the value>',
        'BUILD_STARGATE': '<failed to retrieve the value>',
        'BUILD_STARPORT': '<failed to retrieve the value>',
        'BUILD_STASISTRAP': '<failed to retrieve the value>',
        'BUILD_SUPPLYDEPOT': '<failed to retrieve the value>',
        'BUILD_TECHLAB': '<failed to retrieve the value>',
        'BUILD_TECHLAB_BARRACKS': '<failed to retrieve the value>',
        'BUILD_TECHLAB_FACTORY': '<failed to retrieve the value>',
        'BUILD_TECHLAB_STARPORT': '<failed to retrieve the value>',
        'BUILD_TEMPLARARCHIVE': '<failed to retrieve the value>',
        'BUILD_TWILIGHTCOUNCIL': '<failed to retrieve the value>',
        'BUILD_ULTRALISKCAVERN': '<failed to retrieve the value>',
        'BURROWDOWN': '<failed to retrieve the value>',
        'BURROWDOWN_BANELING': '<failed to retrieve the value>',
        'BURROWDOWN_DRONE': '<failed to retrieve the value>',
        'BURROWDOWN_HYDRALISK': '<failed to retrieve the value>',
        'BURROWDOWN_INFESTOR': '<failed to retrieve the value>',
        'BURROWDOWN_LURKER': '<failed to retrieve the value>',
        'BURROWDOWN_QUEEN': '<failed to retrieve the value>',
        'BURROWDOWN_RAVAGER': '<failed to retrieve the value>',
        'BURROWDOWN_ROACH': '<failed to retrieve the value>',
        'BURROWDOWN_SWARMHOST': '<failed to retrieve the value>',
        'BURROWDOWN_WIDOWMINE': '<failed to retrieve the value>',
        'BURROWDOWN_ZERGLING': '<failed to retrieve the value>',
        'BURROWUP': '<failed to retrieve the value>',
        'BURROWUP_BANELING': '<failed to retrieve the value>',
        'BURROWUP_DRONE': '<failed to retrieve the value>',
        'BURROWUP_HYDRALISK': '<failed to retrieve the value>',
        'BURROWUP_INFESTOR': '<failed to retrieve the value>',
        'BURROWUP_LURKER': '<failed to retrieve the value>',
        'BURROWUP_QUEEN': '<failed to retrieve the value>',
        'BURROWUP_RAVAGER': '<failed to retrieve the value>',
        'BURROWUP_ROACH': '<failed to retrieve the value>',
        'BURROWUP_SWARMHOST': '<failed to retrieve the value>',
        'BURROWUP_WIDOWMINE': '<failed to retrieve the value>',
        'BURROWUP_ZERGLING': '<failed to retrieve the value>',
        'CANCEL': '<failed to retrieve the value>',
        'CANCELSLOT_ADDON': '<failed to retrieve the value>',
        'CANCELSLOT_QUEUE1': '<failed to retrieve the value>',
        'CANCELSLOT_QUEUE5': '<failed to retrieve the value>',
        'CANCELSLOT_QUEUECANCELTOSELECTION': '<failed to retrieve the value>',
        'CANCELSLOT_QUEUEPASSIVE': '<failed to retrieve the value>',
        'CANCEL_ADEPTPHASESHIFT': '<failed to retrieve the value>',
        'CANCEL_ADEPTSHADEPHASESHIFT': '<failed to retrieve the value>',
        'CANCEL_BARRACKSADDON': '<failed to retrieve the value>',
        'CANCEL_BUILDINPROGRESS': '<failed to retrieve the value>',
        'CANCEL_CREEPTUMOR': '<failed to retrieve the value>',
        'CANCEL_FACTORYADDON': '<failed to retrieve the value>',
        'CANCEL_GRAVITONBEAM': '<failed to retrieve the value>',
        'CANCEL_LAST': '<failed to retrieve the value>',
        'CANCEL_MORPHBROODLORD': '<failed to retrieve the value>',
        'CANCEL_MORPHLAIR': '<failed to retrieve the value>',
        'CANCEL_MORPHLURKER': '<failed to retrieve the value>',
        'CANCEL_MORPHLURKERDEN': '<failed to retrieve the value>',
        'CANCEL_MORPHMOTHERSHIP': '<failed to retrieve the value>',
        'CANCEL_MORPHORBITAL': '<failed to retrieve the value>',
        'CANCEL_MORPHOVERLORDTRANSPORT': '<failed to retrieve the value>',
        'CANCEL_MORPHOVERSEER': '<failed to retrieve the value>',
        'CANCEL_MORPHPLANETARYFORTRESS': '<failed to retrieve the value>',
        'CANCEL_MORPHRAVAGER': '<failed to retrieve the value>',
        'CANCEL_QUEUE1': '<failed to retrieve the value>',
        'CANCEL_QUEUE5': '<failed to retrieve the value>',
        'CANCEL_QUEUEADDON': '<failed to retrieve the value>',
        'CANCEL_QUEUECANCELTOSELECTION': '<failed to retrieve the value>',
        'CANCEL_QUEUEPASIVE': '<failed to retrieve the value>',
        'CANCEL_QUEUEPASSIVECANCELTOSELECTION': '<failed to retrieve the value>',
        'CANCEL_SPINECRAWLERROOT': '<failed to retrieve the value>',
        'CANCEL_STARPORTADDON': '<failed to retrieve the value>',
        'EFFECT_ABDUCT': '<failed to retrieve the value>',
        'EFFECT_ADEPTPHASESHIFT': '<failed to retrieve the value>',
        'EFFECT_AUTOTURRET': '<failed to retrieve the value>',
        'EFFECT_BLINDINGCLOUD': '<failed to retrieve the value>',
        'EFFECT_BLINK': '<failed to retrieve the value>',
        'EFFECT_BLINK_STALKER': '<failed to retrieve the value>',
        'EFFECT_CALLDOWNMULE': '<failed to retrieve the value>',
        'EFFECT_CAUSTICSPRAY': '<failed to retrieve the value>',
        'EFFECT_CHARGE': '<failed to retrieve the value>',
        'EFFECT_CHRONOBOOST': '<failed to retrieve the value>',
        'EFFECT_CONTAMINATE': '<failed to retrieve the value>',
        'EFFECT_CORROSIVEBILE': '<failed to retrieve the value>',
        'EFFECT_EMP': '<failed to retrieve the value>',
        'EFFECT_EXPLODE': '<failed to retrieve the value>',
        'EFFECT_FEEDBACK': '<failed to retrieve the value>',
        'EFFECT_FORCEFIELD': '<failed to retrieve the value>',
        'EFFECT_FUNGALGROWTH': '<failed to retrieve the value>',
        'EFFECT_GHOSTSNIPE': '<failed to retrieve the value>',
        'EFFECT_GRAVITONBEAM': '<failed to retrieve the value>',
        'EFFECT_GUARDIANSHIELD': '<failed to retrieve the value>',
        'EFFECT_HEAL': '<failed to retrieve the value>',
        'EFFECT_HUNTERSEEKERMISSILE': '<failed to retrieve the value>',
        'EFFECT_IMMORTALBARRIER': '<failed to retrieve the value>',
        'EFFECT_INFESTEDTERRANS': '<failed to retrieve the value>',
        'EFFECT_INJECTLARVA': '<failed to retrieve the value>',
        'EFFECT_KD8CHARGE': '<failed to retrieve the value>',
        'EFFECT_LOCKON': '<failed to retrieve the value>',
        'EFFECT_LOCUSTSWOOP': '<failed to retrieve the value>',
        'EFFECT_MASSRECALL': '<failed to retrieve the value>',
        'EFFECT_MASSRECALL_MOTHERSHIP': '<failed to retrieve the value>',
        'EFFECT_MASSRECALL_MOTHERSHIPCORE': '<failed to retrieve the value>',
        'EFFECT_MEDIVACIGNITEAFTERBURNERS': '<failed to retrieve the value>',
        'EFFECT_NEURALPARASITE': '<failed to retrieve the value>',
        'EFFECT_NUKECALLDOWN': '<failed to retrieve the value>',
        'EFFECT_ORACLEREVELATION': '<failed to retrieve the value>',
        'EFFECT_PARASITICBOMB': '<failed to retrieve the value>',
        'EFFECT_PHOTONOVERCHARGE': '<failed to retrieve the value>',
        'EFFECT_POINTDEFENSEDRONE': '<failed to retrieve the value>',
        'EFFECT_PSISTORM': '<failed to retrieve the value>',
        'EFFECT_PURIFICATIONNOVA': '<failed to retrieve the value>',
        'EFFECT_REPAIR': '<failed to retrieve the value>',
        'EFFECT_REPAIR_MULE': '<failed to retrieve the value>',
        'EFFECT_REPAIR_SCV': '<failed to retrieve the value>',
        'EFFECT_RESTORE': '<failed to retrieve the value>',
        'EFFECT_SALVAGE': '<failed to retrieve the value>',
        'EFFECT_SCAN': '<failed to retrieve the value>',
        'EFFECT_SHADOWSTRIDE': '<failed to retrieve the value>',
        'EFFECT_SPAWNCHANGELING': '<failed to retrieve the value>',
        'EFFECT_SPAWNLOCUSTS': '<failed to retrieve the value>',
        'EFFECT_SPRAY': '<failed to retrieve the value>',
        'EFFECT_SPRAY_PROTOSS': '<failed to retrieve the value>',
        'EFFECT_SPRAY_TERRAN': '<failed to retrieve the value>',
        'EFFECT_SPRAY_ZERG': '<failed to retrieve the value>',
        'EFFECT_STIM': '<failed to retrieve the value>',
        'EFFECT_STIM_MARAUDER': '<failed to retrieve the value>',
        'EFFECT_STIM_MARINE': '<failed to retrieve the value>',
        'EFFECT_STIM_MARINE_REDIRECT': '<failed to retrieve the value>',
        'EFFECT_SUPPLYDROP': '<failed to retrieve the value>',
        'EFFECT_TACTICALJUMP': '<failed to retrieve the value>',
        'EFFECT_TEMPESTDISRUPTIONBLAST': '<failed to retrieve the value>',
        'EFFECT_TIMEWARP': '<failed to retrieve the value>',
        'EFFECT_TRANSFUSION': '<failed to retrieve the value>',
        'EFFECT_VIPERCONSUME': '<failed to retrieve the value>',
        'EFFECT_VOIDRAYPRISMATICALIGNMENT': '<failed to retrieve the value>',
        'EFFECT_WIDOWMINEATTACK': '<failed to retrieve the value>',
        'EFFECT_YAMATOGUN': '<failed to retrieve the value>',
        'HALLUCINATION_ADEPT': '<failed to retrieve the value>',
        'HALLUCINATION_ARCHON': '<failed to retrieve the value>',
        'HALLUCINATION_COLOSSUS': '<failed to retrieve the value>',
        'HALLUCINATION_DISRUPTOR': '<failed to retrieve the value>',
        'HALLUCINATION_HIGHTEMPLAR': '<failed to retrieve the value>',
        'HALLUCINATION_IMMORTAL': '<failed to retrieve the value>',
        'HALLUCINATION_ORACLE': '<failed to retrieve the value>',
        'HALLUCINATION_PHOENIX': '<failed to retrieve the value>',
        'HALLUCINATION_PROBE': '<failed to retrieve the value>',
        'HALLUCINATION_STALKER': '<failed to retrieve the value>',
        'HALLUCINATION_VOIDRAY': '<failed to retrieve the value>',
        'HALLUCINATION_WARPPRISM': '<failed to retrieve the value>',
        'HALLUCINATION_ZEALOT': '<failed to retrieve the value>',
        'HALT': '<failed to retrieve the value>',
        'HALT_BUILDING': '<failed to retrieve the value>',
        'HALT_TERRANBUILD': '<failed to retrieve the value>',
        'HARVEST_GATHER': '<failed to retrieve the value>',
        'HARVEST_GATHER_DRONE': '<failed to retrieve the value>',
        'HARVEST_GATHER_PROBE': '<failed to retrieve the value>',
        'HARVEST_GATHER_SCV': '<failed to retrieve the value>',
        'HARVEST_RETURN': '<failed to retrieve the value>',
        'HARVEST_RETURN_DRONE': '<failed to retrieve the value>',
        'HARVEST_RETURN_MULE': '<failed to retrieve the value>',
        'HARVEST_RETURN_PROBE': '<failed to retrieve the value>',
        'HARVEST_RETURN_SCV': '<failed to retrieve the value>',
        'HOLDPOSITION': '<failed to retrieve the value>',
        'INVALID': '<failed to retrieve the value>',
        'LAND': '<failed to retrieve the value>',
        'LAND_BARRACKS': '<failed to retrieve the value>',
        'LAND_COMMANDCENTER': '<failed to retrieve the value>',
        'LAND_FACTORY': '<failed to retrieve the value>',
        'LAND_ORBITALCOMMAND': '<failed to retrieve the value>',
        'LAND_STARPORT': '<failed to retrieve the value>',
        'LIFT': '<failed to retrieve the value>',
        'LIFT_BARRACKS': '<failed to retrieve the value>',
        'LIFT_COMMANDCENTER': '<failed to retrieve the value>',
        'LIFT_FACTORY': '<failed to retrieve the value>',
        'LIFT_ORBITALCOMMAND': '<failed to retrieve the value>',
        'LIFT_STARPORT': '<failed to retrieve the value>',
        'LOAD': '<failed to retrieve the value>',
        'LOADALL': '<failed to retrieve the value>',
        'LOADALL_COMMANDCENTER': '<failed to retrieve the value>',
        'LOAD_BUNKER': '<failed to retrieve the value>',
        'LOAD_MEDIVAC': '<failed to retrieve the value>',
        'MORPH_ARCHON': '<failed to retrieve the value>',
        'MORPH_BROODLORD': '<failed to retrieve the value>',
        'MORPH_GATEWAY': '<failed to retrieve the value>',
        'MORPH_GREATERSPIRE': '<failed to retrieve the value>',
        'MORPH_HELLBAT': '<failed to retrieve the value>',
        'MORPH_HELLION': '<failed to retrieve the value>',
        'MORPH_HIVE': '<failed to retrieve the value>',
        'MORPH_LAIR': '<failed to retrieve the value>',
        'MORPH_LIBERATORAAMODE': '<failed to retrieve the value>',
        'MORPH_LIBERATORAGMODE': '<failed to retrieve the value>',
        'MORPH_LURKER': '<failed to retrieve the value>',
        'MORPH_LURKERDEN': '<failed to retrieve the value>',
        'MORPH_MOTHERSHIP': '<failed to retrieve the value>',
        'MORPH_ORBITALCOMMAND': '<failed to retrieve the value>',
        'MORPH_OVERLORDTRANSPORT': '<failed to retrieve the value>',
        'MORPH_OVERSEER': '<failed to retrieve the value>',
        'MORPH_PLANETARYFORTRESS': '<failed to retrieve the value>',
        'MORPH_RAVAGER': '<failed to retrieve the value>',
        'MORPH_ROOT': '<failed to retrieve the value>',
        'MORPH_SIEGEMODE': '<failed to retrieve the value>',
        'MORPH_SPINECRAWLERROOT': '<failed to retrieve the value>',
        'MORPH_SPINECRAWLERUPROOT': '<failed to retrieve the value>',
        'MORPH_SPORECRAWLERROOT': '<failed to retrieve the value>',
        'MORPH_SPORECRAWLERUPROOT': '<failed to retrieve the value>',
        'MORPH_SUPPLYDEPOT_LOWER': '<failed to retrieve the value>',
        'MORPH_SUPPLYDEPOT_RAISE': '<failed to retrieve the value>',
        'MORPH_THOREXPLOSIVEMODE': '<failed to retrieve the value>',
        'MORPH_THORHIGHIMPACTMODE': '<failed to retrieve the value>',
        'MORPH_UNSIEGE': '<failed to retrieve the value>',
        'MORPH_UPROOT': '<failed to retrieve the value>',
        'MORPH_VIKINGASSAULTMODE': '<failed to retrieve the value>',
        'MORPH_VIKINGFIGHTERMODE': '<failed to retrieve the value>',
        'MORPH_WARPGATE': '<failed to retrieve the value>',
        'MORPH_WARPPRISMPHASINGMODE': '<failed to retrieve the value>',
        'MORPH_WARPPRISMTRANSPORTMODE': '<failed to retrieve the value>',
        'MOVE': '<failed to retrieve the value>',
        'PATROL': '<failed to retrieve the value>',
        'RALLY_BUILDING': '<failed to retrieve the value>',
        'RALLY_COMMANDCENTER': '<failed to retrieve the value>',
        'RALLY_HATCHERY_UNITS': '<failed to retrieve the value>',
        'RALLY_HATCHERY_WORKERS': '<failed to retrieve the value>',
        'RALLY_MORPHING_UNIT': '<failed to retrieve the value>',
        'RALLY_NEXUS': '<failed to retrieve the value>',
        'RALLY_UNITS': '<failed to retrieve the value>',
        'RALLY_WORKERS': '<failed to retrieve the value>',
        'RESEARCH_ADEPTRESONATINGGLAIVES': '<failed to retrieve the value>',
        'RESEARCH_ADVANCEDBALLISTICS': '<failed to retrieve the value>',
        'RESEARCH_BANSHEECLOAKINGFIELD': '<failed to retrieve the value>',
        'RESEARCH_BANSHEEHYPERFLIGHTROTORS': '<failed to retrieve the value>',
        'RESEARCH_BATTLECRUISERWEAPONREFIT': '<failed to retrieve the value>',
        'RESEARCH_BLINK': '<failed to retrieve the value>',
        'RESEARCH_BURROW': '<failed to retrieve the value>',
        'RESEARCH_CENTRIFUGALHOOKS': '<failed to retrieve the value>',
        'RESEARCH_CHARGE': '<failed to retrieve the value>',
        'RESEARCH_CHITINOUSPLATING': '<failed to retrieve the value>',
        'RESEARCH_COMBATSHIELD': '<failed to retrieve the value>',
        'RESEARCH_CONCUSSIVESHELLS': '<failed to retrieve the value>',
        'RESEARCH_DRILLINGCLAWS': '<failed to retrieve the value>',
        'RESEARCH_ENHANCEDMUNITIONS': '<failed to retrieve the value>',
        'RESEARCH_EXTENDEDTHERMALLANCE': '<failed to retrieve the value>',
        'RESEARCH_GLIALREGENERATION': '<failed to retrieve the value>',
        'RESEARCH_GRAVITICBOOSTER': '<failed to retrieve the value>',
        'RESEARCH_GRAVITICDRIVE': '<failed to retrieve the value>',
        'RESEARCH_GROOVEDSPINES': '<failed to retrieve the value>',
        'RESEARCH_HIGHCAPACITYFUELTANKS': '<failed to retrieve the value>',
        'RESEARCH_HISECAUTOTRACKING': '<failed to retrieve the value>',
        'RESEARCH_INFERNALPREIGNITER': '<failed to retrieve the value>',
        'RESEARCH_INTERCEPTORGRAVITONCATAPULT': '<failed to retrieve the value>',
        'RESEARCH_MAGFIELDLAUNCHERS': '<failed to retrieve the value>',
        'RESEARCH_MUSCULARAUGMENTS': '<failed to retrieve the value>',
        'RESEARCH_NEOSTEELFRAME': '<failed to retrieve the value>',
        'RESEARCH_NEURALPARASITE': '<failed to retrieve the value>',
        'RESEARCH_PATHOGENGLANDS': '<failed to retrieve the value>',
        'RESEARCH_PERSONALCLOAKING': '<failed to retrieve the value>',
        'RESEARCH_PHOENIXANIONPULSECRYSTALS': '<failed to retrieve the value>',
        'RESEARCH_PNEUMATIZEDCARAPACE': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSAIRARMOR': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSAIRARMORLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSAIRARMORLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSAIRARMORLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSAIRWEAPONS': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSAIRWEAPONSLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSAIRWEAPONSLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSAIRWEAPONSLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSGROUNDARMOR': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSGROUNDARMORLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSGROUNDARMORLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSGROUNDARMORLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSGROUNDWEAPONS': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSGROUNDWEAPONSLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSGROUNDWEAPONSLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSGROUNDWEAPONSLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSSHIELDS': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSSHIELDSLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSSHIELDSLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_PROTOSSSHIELDSLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_PSISTORM': '<failed to retrieve the value>',
        'RESEARCH_RAPIDFIRELAUNCHERS': '<failed to retrieve the value>',
        'RESEARCH_RAVENCORVIDREACTOR': '<failed to retrieve the value>',
        'RESEARCH_RAVENRECALIBRATEDEXPLOSIVES': '<failed to retrieve the value>',
        'RESEARCH_SHADOWSTRIKE': '<failed to retrieve the value>',
        'RESEARCH_SMARTSERVOS': '<failed to retrieve the value>',
        'RESEARCH_STIMPACK': '<failed to retrieve the value>',
        'RESEARCH_TERRANINFANTRYARMOR': '<failed to retrieve the value>',
        'RESEARCH_TERRANINFANTRYARMORLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_TERRANINFANTRYARMORLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_TERRANINFANTRYARMORLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_TERRANINFANTRYWEAPONS': '<failed to retrieve the value>',
        'RESEARCH_TERRANINFANTRYWEAPONSLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_TERRANINFANTRYWEAPONSLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_TERRANINFANTRYWEAPONSLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_TERRANSHIPWEAPONS': '<failed to retrieve the value>',
        'RESEARCH_TERRANSHIPWEAPONSLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_TERRANSHIPWEAPONSLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_TERRANSHIPWEAPONSLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_TERRANSTRUCTUREARMORUPGRADE': '<failed to retrieve the value>',
        'RESEARCH_TERRANVEHICLEANDSHIPPLATING': '<failed to retrieve the value>',
        'RESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_TERRANVEHICLEWEAPONS': '<failed to retrieve the value>',
        'RESEARCH_TERRANVEHICLEWEAPONSLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_TERRANVEHICLEWEAPONSLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_TERRANVEHICLEWEAPONSLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_TUNNELINGCLAWS': '<failed to retrieve the value>',
        'RESEARCH_WARPGATE': '<failed to retrieve the value>',
        'RESEARCH_ZERGFLYERARMOR': '<failed to retrieve the value>',
        'RESEARCH_ZERGFLYERARMORLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_ZERGFLYERARMORLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_ZERGFLYERARMORLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_ZERGFLYERATTACK': '<failed to retrieve the value>',
        'RESEARCH_ZERGFLYERATTACKLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_ZERGFLYERATTACKLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_ZERGFLYERATTACKLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_ZERGGROUNDARMOR': '<failed to retrieve the value>',
        'RESEARCH_ZERGGROUNDARMORLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_ZERGGROUNDARMORLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_ZERGGROUNDARMORLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_ZERGLINGADRENALGLANDS': '<failed to retrieve the value>',
        'RESEARCH_ZERGLINGMETABOLICBOOST': '<failed to retrieve the value>',
        'RESEARCH_ZERGMELEEWEAPONS': '<failed to retrieve the value>',
        'RESEARCH_ZERGMELEEWEAPONSLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_ZERGMELEEWEAPONSLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_ZERGMELEEWEAPONSLEVEL3': '<failed to retrieve the value>',
        'RESEARCH_ZERGMISSILEWEAPONS': '<failed to retrieve the value>',
        'RESEARCH_ZERGMISSILEWEAPONSLEVEL1': '<failed to retrieve the value>',
        'RESEARCH_ZERGMISSILEWEAPONSLEVEL2': '<failed to retrieve the value>',
        'RESEARCH_ZERGMISSILEWEAPONSLEVEL3': '<failed to retrieve the value>',
        'SCAN_MOVE': '<failed to retrieve the value>',
        'SMART': '<failed to retrieve the value>',
        'STOP': '<failed to retrieve the value>',
        'STOP_BUILDING': '<failed to retrieve the value>',
        'STOP_CHEER': '<failed to retrieve the value>',
        'STOP_DANCE': '<failed to retrieve the value>',
        'STOP_REDIRECT': '<failed to retrieve the value>',
        'STOP_STOP': '<failed to retrieve the value>',
        'TRAINWARP_ADEPT': '<failed to retrieve the value>',
        'TRAINWARP_DARKTEMPLAR': '<failed to retrieve the value>',
        'TRAINWARP_HIGHTEMPLAR': '<failed to retrieve the value>',
        'TRAINWARP_SENTRY': '<failed to retrieve the value>',
        'TRAINWARP_STALKER': '<failed to retrieve the value>',
        'TRAINWARP_ZEALOT': '<failed to retrieve the value>',
        'TRAIN_ADEPT': '<failed to retrieve the value>',
        'TRAIN_BANELING': '<failed to retrieve the value>',
        'TRAIN_BANSHEE': '<failed to retrieve the value>',
        'TRAIN_BATTLECRUISER': '<failed to retrieve the value>',
        'TRAIN_CARRIER': '<failed to retrieve the value>',
        'TRAIN_COLOSSUS': '<failed to retrieve the value>',
        'TRAIN_CORRUPTOR': '<failed to retrieve the value>',
        'TRAIN_CYCLONE': '<failed to retrieve the value>',
        'TRAIN_DARKTEMPLAR': '<failed to retrieve the value>',
        'TRAIN_DISRUPTOR': '<failed to retrieve the value>',
        'TRAIN_DRONE': '<failed to retrieve the value>',
        'TRAIN_GHOST': '<failed to retrieve the value>',
        'TRAIN_HELLBAT': '<failed to retrieve the value>',
        'TRAIN_HELLION': '<failed to retrieve the value>',
        'TRAIN_HIGHTEMPLAR': '<failed to retrieve the value>',
        'TRAIN_HYDRALISK': '<failed to retrieve the value>',
        'TRAIN_IMMORTAL': '<failed to retrieve the value>',
        'TRAIN_INFESTOR': '<failed to retrieve the value>',
        'TRAIN_LIBERATOR': '<failed to retrieve the value>',
        'TRAIN_MARAUDER': '<failed to retrieve the value>',
        'TRAIN_MARINE': '<failed to retrieve the value>',
        'TRAIN_MEDIVAC': '<failed to retrieve the value>',
        'TRAIN_MOTHERSHIP': '<failed to retrieve the value>',
        'TRAIN_MOTHERSHIPCORE': '<failed to retrieve the value>',
        'TRAIN_MUTALISK': '<failed to retrieve the value>',
        'TRAIN_OBSERVER': '<failed to retrieve the value>',
        'TRAIN_ORACLE': '<failed to retrieve the value>',
        'TRAIN_OVERLORD': '<failed to retrieve the value>',
        'TRAIN_PHOENIX': '<failed to retrieve the value>',
        'TRAIN_PROBE': '<failed to retrieve the value>',
        'TRAIN_QUEEN': '<failed to retrieve the value>',
        'TRAIN_RAVEN': '<failed to retrieve the value>',
        'TRAIN_REAPER': '<failed to retrieve the value>',
        'TRAIN_ROACH': '<failed to retrieve the value>',
        'TRAIN_SCV': '<failed to retrieve the value>',
        'TRAIN_SENTRY': '<failed to retrieve the value>',
        'TRAIN_SIEGETANK': '<failed to retrieve the value>',
        'TRAIN_STALKER': '<failed to retrieve the value>',
        'TRAIN_SWARMHOST': '<failed to retrieve the value>',
        'TRAIN_TEMPEST': '<failed to retrieve the value>',
        'TRAIN_THOR': '<failed to retrieve the value>',
        'TRAIN_ULTRALISK': '<failed to retrieve the value>',
        'TRAIN_VIKINGFIGHTER': '<failed to retrieve the value>',
        'TRAIN_VIPER': '<failed to retrieve the value>',
        'TRAIN_VOIDRAY': '<failed to retrieve the value>',
        'TRAIN_WARPPRISM': '<failed to retrieve the value>',
        'TRAIN_WIDOWMINE': '<failed to retrieve the value>',
        'TRAIN_ZEALOT': '<failed to retrieve the value>',
        'TRAIN_ZERGLING': '<failed to retrieve the value>',
        'UNLOADALL': '<failed to retrieve the value>',
        'UNLOADALLAT': '<failed to retrieve the value>',
        'UNLOADALLAT_MEDIVAC': '<failed to retrieve the value>',
        'UNLOADALLAT_OVERLORD': '<failed to retrieve the value>',
        'UNLOADALLAT_WARPPRISM': '<failed to retrieve the value>',
        'UNLOADALL_BUNKER': '<failed to retrieve the value>',
        'UNLOADALL_COMMANDCENTER': '<failed to retrieve the value>',
        'UNLOADALL_NYDASNETWORK': '<failed to retrieve the value>',
        'UNLOADALL_NYDUSWORM': '<failed to retrieve the value>',
        'UNLOADUNIT_BUNKER': '<failed to retrieve the value>',
        'UNLOADUNIT_COMMANDCENTER': '<failed to retrieve the value>',
        'UNLOADUNIT_MEDIVAC': '<failed to retrieve the value>',
        'UNLOADUNIT_NYDASNETWORK': '<failed to retrieve the value>',
        'UNLOADUNIT_OVERLORD': '<failed to retrieve the value>',
        'UNLOADUNIT_WARPPRISM': '<failed to retrieve the value>',
    }


class Agent(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: library.Agent) -> None """
        pass


class BaseLocation(__pybind11_builtins.pybind11_object):
    # no doc
    def contains_position(self, arg0):  # real signature unknown; restored from __doc__
        """ contains_position(self: library.BaseLocation, arg0: library.Point2D) -> bool """
        return False

    def get_ground_distance(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        get_ground_distance(*args, **kwargs)
        Overloaded function.

        1. get_ground_distance(self: library.BaseLocation, arg0: library.Point2D) -> int

        2. get_ground_distance(self: library.BaseLocation, arg0: library.Point2DI) -> int
        """
        pass

    def is_occupied_by_player(self, player_constant):  # real signature unknown; restored from __doc__
        """ is_occupied_by_player(self: library.BaseLocation, player constant: int) -> bool """
        return False

    def is_player_start_location(self, player_constant):  # real signature unknown; restored from __doc__
        """ is_player_start_location(self: library.BaseLocation, player_constant: int) -> bool """
        return False

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    depot_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Point2DI position suitable for placing a town hall (base structure)"""

    geysers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of geysers at base location (List of units)"""

    is_start_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the base location is a start location, False otherwise"""

    minerals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of mineral fields at base location (List of unit)"""

    mineral_fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for minerals in order to differentiate from harvested minerals"""

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


class BaseLocationManager(__pybind11_builtins.pybind11_object):
    # no doc
    def get_next_expansion(self, player_constant):  # real signature unknown; restored from __doc__
        """ get_next_expansion(self: library.BaseLocationManager, player_constant: int) -> library.BaseLocation """
        pass

    def get_occupied_base_locations(self, player_constant):  # real signature unknown; restored from __doc__
        """ get_occupied_base_locations(self: library.BaseLocationManager, player_constant: int) -> Set[library.BaseLocation] """
        pass

    def get_player_starting_base_location(self, player_constant):  # real signature unknown; restored from __doc__
        """ get_player_starting_base_location(self: library.BaseLocationManager, player_constant: int) -> library.BaseLocation """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    base_locations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    starting_base_locations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


class BuffID(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: library.BuffID, arg0: library.BUFF_ID) -> None """
        pass


class BUFF_ID(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, arg0):  # real signature unknown; restored from __doc__
        """ __eq__(self: library.BUFF_ID, arg0: library.BUFF_ID) -> bool """
        return False

    def __getstate__(self):  # real signature unknown; restored from __doc__
        """ __getstate__(self: library.BUFF_ID) -> tuple """
        return ()

    def __hash__(self):  # real signature unknown; restored from __doc__
        """ __hash__(self: library.BUFF_ID) -> int """
        return 0

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: library.BUFF_ID, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: library.BUFF_ID) -> int """
        return 0

    def __ne__(self, arg0):  # real signature unknown; restored from __doc__
        """ __ne__(self: library.BUFF_ID, arg0: library.BUFF_ID) -> bool """
        return False

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: library.BUFF_ID) -> str """
        return ""

    def __setstate__(self, arg0):  # real signature unknown; restored from __doc__
        """ __setstate__(self: library.BUFF_ID, arg0: tuple) -> None """
        pass

    BANSHEECLOAK = None  # (!) real value is ''
    BLINDINGCLOUD = None  # (!) real value is ''
    BLINDINGCLOUDSTRUCTURE = None  # (!) real value is ''
    CARRYHARVESTABLEVESPENEGEYSERGAS = None  # (!) real value is ''
    CARRYHARVESTABLEVESPENEGEYSERGASPROTOSS = None  # (!) real value is ''
    CARRYHARVESTABLEVESPENEGEYSERGASZERG = None  # (!) real value is ''
    CARRYHIGHYIELDMINERALFIELDMINERALS = None  # (!) real value is ''
    CARRYMINERALFIELDMINERALS = None  # (!) real value is ''
    CHANNELSNIPECOMBAT = None  # (!) real value is ''
    CHARGING = None  # (!) real value is ''
    CLOAKFIELDEFFECT = None  # (!) real value is ''
    CONTAMINATED = None  # (!) real value is ''
    EMPDECLOAK = None  # (!) real value is ''
    FUNGALGROWTH = None  # (!) real value is ''
    GHOSTCLOAK = None  # (!) real value is ''
    GHOSTHOLDFIRE = None  # (!) real value is ''
    GHOSTHOLDFIREB = None  # (!) real value is ''
    GRAVITONBEAM = None  # (!) real value is ''
    GUARDIANSHIELD = None  # (!) real value is ''
    IMMORTALOVERLOAD = None  # (!) real value is ''
    INVALID = None  # (!) real value is ''
    LOCKON = None  # (!) real value is ''
    LURKERHOLDFIREB = None  # (!) real value is ''
    MEDIVACSPEEDBOOST = None  # (!) real value is ''
    NEURALPARASITE = None  # (!) real value is ''
    ORACLEREVELATION = None  # (!) real value is ''
    ORACLESTASISTRAPTARGET = None  # (!) real value is ''
    ORACLEWEAPON = None  # (!) real value is ''
    PARASITICBOMB = None  # (!) real value is ''
    PARASITICBOMBSECONDARYUNITSEARCH = None  # (!) real value is ''
    PARASITICBOMBUNITKU = None  # (!) real value is ''
    POWERUSERWARPABLE = None  # (!) real value is ''
    PSISTORM = None  # (!) real value is ''
    PURIFY = None  # (!) real value is ''
    QUEENSPAWNLARVATIMER = None  # (!) real value is ''
    SEEKERMISSILE = None  # (!) real value is ''
    SLOW = None  # (!) real value is ''
    STIMPACK = None  # (!) real value is ''
    STIMPACKMARAUDER = None  # (!) real value is ''
    SUPPLYDROP = None  # (!) real value is ''
    TEMPESTDISRUPTIONBLASTSTUNBEHAVIOR = None  # (!) real value is ''
    TEMPORALFIELD = None  # (!) real value is ''
    TIMEWARPPRODUCTION = None  # (!) real value is ''
    VIPERCONSUMESTRUCTURE = None  # (!) real value is ''
    VOIDRAYSWARMDAMAGEBOOST = None  # (!) real value is ''
    __members__ = {
        'BANSHEECLOAK': '<failed to retrieve the value>',
        'BLINDINGCLOUD': '<failed to retrieve the value>',
        'BLINDINGCLOUDSTRUCTURE': '<failed to retrieve the value>',
        'CARRYHARVESTABLEVESPENEGEYSERGAS': '<failed to retrieve the value>',
        'CARRYHARVESTABLEVESPENEGEYSERGASPROTOSS': '<failed to retrieve the value>',
        'CARRYHARVESTABLEVESPENEGEYSERGASZERG': '<failed to retrieve the value>',
        'CARRYHIGHYIELDMINERALFIELDMINERALS': '<failed to retrieve the value>',
        'CARRYMINERALFIELDMINERALS': '<failed to retrieve the value>',
        'CHANNELSNIPECOMBAT': '<failed to retrieve the value>',
        'CHARGING': '<failed to retrieve the value>',
        'CLOAKFIELDEFFECT': '<failed to retrieve the value>',
        'CONTAMINATED': '<failed to retrieve the value>',
        'EMPDECLOAK': '<failed to retrieve the value>',
        'FUNGALGROWTH': '<failed to retrieve the value>',
        'GHOSTCLOAK': '<failed to retrieve the value>',
        'GHOSTHOLDFIRE': '<failed to retrieve the value>',
        'GHOSTHOLDFIREB': '<failed to retrieve the value>',
        'GRAVITONBEAM': '<failed to retrieve the value>',
        'GUARDIANSHIELD': '<failed to retrieve the value>',
        'IMMORTALOVERLOAD': '<failed to retrieve the value>',
        'INVALID': '<failed to retrieve the value>',
        'LOCKON': '<failed to retrieve the value>',
        'LURKERHOLDFIREB': '<failed to retrieve the value>',
        'MEDIVACSPEEDBOOST': '<failed to retrieve the value>',
        'NEURALPARASITE': '<failed to retrieve the value>',
        'ORACLEREVELATION': '<failed to retrieve the value>',
        'ORACLESTASISTRAPTARGET': '<failed to retrieve the value>',
        'ORACLEWEAPON': '<failed to retrieve the value>',
        'PARASITICBOMB': '<failed to retrieve the value>',
        'PARASITICBOMBSECONDARYUNITSEARCH': '<failed to retrieve the value>',
        'PARASITICBOMBUNITKU': '<failed to retrieve the value>',
        'POWERUSERWARPABLE': '<failed to retrieve the value>',
        'PSISTORM': '<failed to retrieve the value>',
        'PURIFY': '<failed to retrieve the value>',
        'QUEENSPAWNLARVATIMER': '<failed to retrieve the value>',
        'SEEKERMISSILE': '<failed to retrieve the value>',
        'SLOW': '<failed to retrieve the value>',
        'STIMPACK': '<failed to retrieve the value>',
        'STIMPACKMARAUDER': '<failed to retrieve the value>',
        'SUPPLYDROP': '<failed to retrieve the value>',
        'TEMPESTDISRUPTIONBLASTSTUNBEHAVIOR': '<failed to retrieve the value>',
        'TEMPORALFIELD': '<failed to retrieve the value>',
        'TIMEWARPPRODUCTION': '<failed to retrieve the value>',
        'VIPERCONSUMESTRUCTURE': '<failed to retrieve the value>',
        'VOIDRAYSWARMDAMAGEBOOST': '<failed to retrieve the value>',
    }


class BuildingPlacer(__pybind11_builtins.pybind11_object):
    # no doc
    def can_build_here(self, x, y, unit_type):  # real signature unknown; restored from __doc__
        """ can_build_here(self: library.BuildingPlacer, x: int, y: int, unit_type: library.UnitType) -> bool """
        return False

    def can_build_here_with_spaces(self, x, y, unit_type,
                                   build_distance):  # real signature unknown; restored from __doc__
        """ can_build_here_with_spaces(self: library.BuildingPlacer, x: int, y: int, unit_type: library.UnitType, build_distance: int) -> bool """
        return False

    def free_tiles(self, x, y, width, height):  # real signature unknown; restored from __doc__
        """ free_tiles(self: library.BuildingPlacer, x: int, y: int, width: int, height: int) -> None """
        pass

    def get_build_location_near(self, point2di, unit_type, build_distance=2,
                                search_count=1000):  # real signature unknown; restored from __doc__
        """ get_build_location_near(self: library.BuildingPlacer, point2di: library.Point2DI, unit_type: library.UnitType, build_distance: int=2, search_count: int=1000) -> library.Point2DI """
        pass

    def reserve_tiles(self, x, y, width, height):  # real signature unknown; restored from __doc__
        """ reserve_tiles(self: library.BuildingPlacer, x: int, y: int, width: int, height: int) -> None """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


class Color(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: library.Color) -> None

        2. __init__(self: library.Color, r: int, g: int, b: int) -> None
        """
        pass

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: library.Color) -> str """
        return ""

    b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Blue"""

    g = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Green"""

    r = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Red"""

    BLACK = None  # (!) real value is ''
    BLUE = None  # (!) real value is ''
    GRAY = None  # (!) real value is ''
    GREEN = None  # (!) real value is ''
    PURPLE = None  # (!) real value is ''
    RED = None  # (!) real value is ''
    TEAL = None  # (!) real value is ''
    WHITE = None  # (!) real value is ''
    YELLOW = None  # (!) real value is ''


class Coordinator(__pybind11_builtins.pybind11_object):
    # no doc
    def launch_starcraft(self):  # real signature unknown; restored from __doc__
        """ launch_starcraft(self: library.Coordinator) -> None """
        pass

    def set_participants(self, participants, *args,
                         **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """ set_participants(self: library.Coordinator, participants: List[sc2::PlayerSetup]) -> None """
        pass

    def set_real_time(self, arg0):  # real signature unknown; restored from __doc__
        """ set_real_time(self: library.Coordinator, arg0: bool) -> None """
        pass

    def start_game(self, map_path):  # real signature unknown; restored from __doc__
        """ start_game(self: library.Coordinator, map_path: str) -> bool """
        return False

    def update(self):  # real signature unknown; restored from __doc__
        """ update(self: library.Coordinator) -> bool """
        return False

    def __init__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: library.Coordinator) -> None

        2. __init__(self: library.Coordinator, arg0: str) -> None
        """
        pass


class Difficulty(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.

        1. __eq__(self: library.Difficulty, arg0: library.Difficulty) -> bool

        2. __eq__(self: library.Difficulty, arg0: int) -> bool
        """
        pass

    def __getstate__(self):  # real signature unknown; restored from __doc__
        """ __getstate__(self: library.Difficulty) -> tuple """
        return ()

    def __hash__(self):  # real signature unknown; restored from __doc__
        """ __hash__(self: library.Difficulty) -> int """
        return 0

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: library.Difficulty, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: library.Difficulty) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.

        1. __ne__(self: library.Difficulty, arg0: library.Difficulty) -> bool

        2. __ne__(self: library.Difficulty, arg0: int) -> bool
        """
        pass

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: library.Difficulty) -> str """
        return ""

    def __setstate__(self, arg0):  # real signature unknown; restored from __doc__
        """ __setstate__(self: library.Difficulty, arg0: tuple) -> None """
        pass

    CheatInsane = None  # (!) real value is ''
    CheatMoney = None  # (!) real value is ''
    CheatVision = None  # (!) real value is ''
    Easy = None  # (!) real value is ''
    Hard = None  # (!) real value is ''
    HardVeryHard = None  # (!) real value is ''
    Medium = None  # (!) real value is ''
    MediumHard = None  # (!) real value is ''
    VeryEasy = None  # (!) real value is ''
    VeryHard = None  # (!) real value is ''
    __members__ = {
        'CheatInsane': '<failed to retrieve the value>',
        'CheatMoney': '<failed to retrieve the value>',
        'CheatVision': '<failed to retrieve the value>',
        'Easy': '<failed to retrieve the value>',
        'Hard': '<failed to retrieve the value>',
        'HardVeryHard': '<failed to retrieve the value>',
        'Medium': '<failed to retrieve the value>',
        'MediumHard': '<failed to retrieve the value>',
        'VeryEasy': '<failed to retrieve the value>',
        'VeryHard': '<failed to retrieve the value>',
    }


class DistanceMap(__pybind11_builtins.pybind11_object):
    # no doc
    def computer_distance_map(self, bot, start_tile):  # real signature unknown; restored from __doc__
        """ computer_distance_map(self: library.DistanceMap, bot: IDABot, start_tile: library.Point2DI) -> None """
        pass

    def draw(self, bot):  # real signature unknown; restored from __doc__
        """ draw(self: library.DistanceMap, bot: IDABot) -> None """
        pass

    def get_distance(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        get_distance(*args, **kwargs)
        Overloaded function.

        1. get_distance(self: library.DistanceMap, position: library.Point2DI) -> int

        2. get_distance(self: library.DistanceMap, position: library.Point2D) -> int
        """
        pass

    def get_sorted_tiles(self):  # real signature unknown; restored from __doc__
        """ get_sorted_tiles(self: library.DistanceMap) -> List[library.Point2DI] """
        return []

    def get_start_tile(self):  # real signature unknown; restored from __doc__
        """ get_start_tile(self: library.DistanceMap) -> library.Point2DI """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


class IDABot(Agent):
    # no doc
    def get_all_units(self):  # real signature unknown; restored from __doc__
        """
        get_all_units(self: library.IDABot) -> List[library.Unit]

        Returns a list of all units
        """
        return []

    def get_my_units(self):  # real signature unknown; restored from __doc__
        """
        get_my_units(self: library.IDABot) -> List[library.Unit]

        Returns a list of all units beloning to the player
        """
        return []

    def get_player_race(self, arg0):  # real signature unknown; restored from __doc__
        """ get_player_race(self: library.IDABot, arg0: int) -> library.Race """
        pass

    def on_game_start(self):  # real signature unknown; restored from __doc__
        """ on_game_start(self: library.IDABot) -> None """
        pass

    def on_step(self):  # real signature unknown; restored from __doc__
        """ on_step(self: library.IDABot) -> None """
        pass

    def __init__(self):  # real signature unknown; restored from __doc__
        """ __init__(self: library.IDABot) -> None """
        pass

    base_location_manager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    building_placer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    current_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Which frame we are currently on"""

    current_supply = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How much supply we are currently using"""

    gas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How much gas we currently have"""

    map_tools = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_supply = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How much supply we can currently use"""

    minerals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How much minerals we currently have"""

    start_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """CCPosition representing the start location"""

    start_locations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """CCPosition representing the start locations"""

    tech_tree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


class MapTools(__pybind11_builtins.pybind11_object):
    # no doc
    def can_build_type_at_position(self, x, y, unit_type):  # real signature unknown; restored from __doc__
        """ can_build_type_at_position(self: library.MapTools, x: int, y: int, unit_type: library.UnitType) -> bool """
        return False

    def draw_box(self, top_left, bottom_right, color, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """ draw_box(self: library.MapTools, top_left: library.Point2D, bottom_right: library.Point2D, color: library.Color=<Color (255, 255, 255)>) -> None """
        pass

    def draw_circle(self, center, radius, color, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """ draw_circle(self: library.MapTools, center: library.Point2D, radius: float, color: library.Color=<Color (255, 255, 255)>) -> None """
        pass

    def draw_line(self, start, stop, color, *args,
                  **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """ draw_line(self: library.MapTools, start: library.Point2D, stop: library.Point2D, color: library.Color=<Color (255, 255, 255)>) -> None """
        pass

    def draw_text(self, position, text, color, *args,
                  **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """ draw_text(self: library.MapTools, position: library.Point2D, text: str, color: library.Color=<Color (255, 255, 255)>) -> None """
        pass

    def draw_text_screen(self, percentage_x, percentage_y, text, color, *args,
                         **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """ draw_text_screen(self: library.MapTools, percentage_x: float, percentage_y: float, text: str, color: library.Color=<Color (255, 255, 255)>) -> None """
        pass

    def get_closest_tiles_to(self, point2di):  # real signature unknown; restored from __doc__
        """
        get_closest_tiles_to(self: library.MapTools, point2di: library.Point2DI) -> List[library.Point2DI]

        Returns a list of positions, where the first position is the closest and the last is the furthest
        """
        return []

    def get_distance_map(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        get_distance_map(*args, **kwargs)
        Overloaded function.

        1. get_distance_map(self: library.MapTools, point2di: library.Point2DI) -> library.DistanceMap

        2. get_distance_map(self: library.MapTools, point2d: library.Point2D) -> library.DistanceMap
        """
        pass

    def get_ground_distance(self, from_, to):  # real signature unknown; restored from __doc__
        """ get_ground_distance(self: library.MapTools, from: library.Point2D, to: library.Point2D) -> int """
        return 0

    def get_least_recently_seen_tile(self):  # real signature unknown; restored from __doc__
        """ get_least_recently_seen_tile(self: library.MapTools) -> library.Point2DI """
        pass

    def is_buildable(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        is_buildable(*args, **kwargs)
        Overloaded function.

        1. is_buildable(self: library.MapTools, x: int, y: int) -> bool

        2. is_buildable(self: library.MapTools, point2di: library.Point2DI) -> bool
        """
        pass

    def is_connected(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        is_connected(*args, **kwargs)
        Overloaded function.

        1. is_connected(self: library.MapTools, x1: int, y1: int, x2: int, y2: int) -> bool

        2. is_connected(self: library.MapTools, from: library.Point2DI, too: library.Point2DI) -> bool

        3. is_connected(self: library.MapTools, from: library.Point2D, too: library.Point2D) -> bool
        """
        pass

    def is_depot_buildable_tile(self, x, y):  # real signature unknown; restored from __doc__
        """ is_depot_buildable_tile(self: library.MapTools, x: int, y: int) -> bool """
        return False

    def is_explored(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        is_explored(*args, **kwargs)
        Overloaded function.

        1. is_explored(self: library.MapTools, x: int, y: int) -> bool

        2. is_explored(self: library.MapTools, point2d: library.Point2D) -> bool

        3. is_explored(self: library.MapTools, point2di: library.Point2DI) -> bool
        """
        pass

    def is_powered(self, x, y):  # real signature unknown; restored from __doc__
        """ is_powered(self: library.MapTools, x: int, y: int) -> bool """
        return False

    def is_valid_position(self, point_2d):  # real signature unknown; restored from __doc__
        """ is_valid_position(self: library.MapTools, point_2d: library.Point2D) -> bool """
        return False

    def is_valid_tile(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        is_valid_tile(*args, **kwargs)
        Overloaded function.

        1. is_valid_tile(self: library.MapTools, x: int, y: int) -> bool

        2. is_valid_tile(self: library.MapTools, point_2di: library.Point2DI) -> bool
        """
        pass

    def is_visible(self, x, y):  # real signature unknown; restored from __doc__
        """ is_visible(self: library.MapTools, x: int, y: int) -> bool """
        return False

    def is_walkable(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        is_walkable(*args, **kwargs)
        Overloaded function.

        1. is_walkable(self: library.MapTools, x: int, y: int) -> bool

        2. is_walkable(self: library.MapTools, point2di: library.Point2DI) -> bool
        """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the map"""

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of the map"""


class PlayerSetup(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


class Point2D(__pybind11_builtins.pybind11_object):
    # no doc
    def __add__(self, arg0):  # real signature unknown; restored from __doc__
        """ __add__(self: library.Point2D, arg0: library.Point2D) -> library.Point2D """
        pass

    def __iadd__(self, arg0):  # real signature unknown; restored from __doc__
        """ __iadd__(self: library.Point2D, arg0: library.Point2D) -> library.Point2D """
        pass

    def __imul__(self, arg0):  # real signature unknown; restored from __doc__
        """ __imul__(self: library.Point2D, arg0: float) -> library.Point2D """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: library.Point2D, arg0: float, arg1: float) -> None

        2. __init__(self: library.Point2D) -> None
        """
        pass

    def __isub__(self, arg0):  # real signature unknown; restored from __doc__
        """ __isub__(self: library.Point2D, arg0: library.Point2D) -> library.Point2D """
        pass

    def __itruediv__(self, arg0):  # real signature unknown; restored from __doc__
        """ __itruediv__(self: library.Point2D, arg0: float) -> library.Point2D """
        pass

    def __mul__(self, arg0):  # real signature unknown; restored from __doc__
        """ __mul__(self: library.Point2D, arg0: float) -> library.Point2D """
        pass

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: library.Point2D) -> str """
        return ""

    def __rmul__(self, arg0):  # real signature unknown; restored from __doc__
        """ __rmul__(self: library.Point2D, arg0: float) -> library.Point2D """
        pass

    def __rtruediv__(self, arg0):  # real signature unknown; restored from __doc__
        """ __rtruediv__(self: library.Point2D, arg0: float) -> library.Point2D """
        pass

    def __str__(self):  # real signature unknown; restored from __doc__
        """ __str__(self: library.Point2D) -> str """
        return ""

    def __sub__(self, arg0):  # real signature unknown; restored from __doc__
        """ __sub__(self: library.Point2D, arg0: library.Point2D) -> library.Point2D """
        pass

    def __truediv__(self, arg0):  # real signature unknown; restored from __doc__
        """ __truediv__(self: library.Point2D, arg0: float) -> library.Point2D """
        pass

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __dict__ = None  # (!) real value is ''


class Point2DI(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, arg0):  # real signature unknown; restored from __doc__
        """ __eq__(self: library.Point2DI, arg0: library.Point2DI) -> bool """
        return False

    def __init__(self, arg0, arg1):  # real signature unknown; restored from __doc__
        """ __init__(self: library.Point2DI, arg0: int, arg1: int) -> None """
        pass

    def __ne__(self, arg0):  # real signature unknown; restored from __doc__
        """ __ne__(self: library.Point2DI, arg0: library.Point2DI) -> bool """
        return False

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: library.Point2DI) -> str """
        return ""

    def __str__(self):  # real signature unknown; restored from __doc__
        """ __str__(self: library.Point2DI) -> str """
        return ""

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __dict__ = None  # (!) real value is ''


class Race(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.

        1. __eq__(self: library.Race, arg0: library.Race) -> bool

        2. __eq__(self: library.Race, arg0: int) -> bool
        """
        pass

    def __getstate__(self):  # real signature unknown; restored from __doc__
        """ __getstate__(self: library.Race) -> tuple """
        return ()

    def __hash__(self):  # real signature unknown; restored from __doc__
        """ __hash__(self: library.Race) -> int """
        return 0

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: library.Race, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: library.Race) -> int """
        return 0

    def __ne__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.

        1. __ne__(self: library.Race, arg0: library.Race) -> bool

        2. __ne__(self: library.Race, arg0: int) -> bool
        """
        pass

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: library.Race) -> str """
        return ""

    def __setstate__(self, arg0):  # real signature unknown; restored from __doc__
        """ __setstate__(self: library.Race, arg0: tuple) -> None """
        pass

    Protoss = None  # (!) real value is ''
    Random = None  # (!) real value is ''
    Terran = None  # (!) real value is ''
    Zerg = None  # (!) real value is ''
    __members__ = {
        'Protoss': '<failed to retrieve the value>',
        'Random': '<failed to retrieve the value>',
        'Terran': '<failed to retrieve the value>',
        'Zerg': '<failed to retrieve the value>',
    }


class TechTree(__pybind11_builtins.pybind11_object):
    # no doc
    def get_data(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        get_data(*args, **kwargs)
        Overloaded function.

        1. get_data(self: library.TechTree, arg0: library.UnitType) -> library.TypeData

        2. get_data(self: library.TechTree, arg0: sc2::SC2Type<sc2::UPGRADE_ID>) -> library.TypeData
        """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


class TypeData(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    build_ability = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the ability that creates this item"""

    build_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """build time of the item"""

    gas_cost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """gas cost of the item"""

    is_addon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_building = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_refinery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_resource_depot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_supply_provider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_worker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mineral_cost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """mineral cost of the item"""

    race = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    required_addons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """a unit of this type must be present next to the producer"""

    required_units = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """owning ONE of these is required to make"""

    required_upgrades = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """having ALL of these is required to make"""

    supply_cost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """supply cost of the item"""

    warp_ability = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the ability that creates this item via warp-in"""

    what_builds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """any of these units can build the item"""


class Unit(__pybind11_builtins.pybind11_object):
    # no doc
    def ability(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        ability(*args, **kwargs)
        Overloaded function.

        1. ability(self: library.Unit, arg0: sc2::SC2Type<sc2::ABILITY_ID>) -> None

        2. ability(self: library.Unit, arg0: sc2::SC2Type<sc2::ABILITY_ID>, arg1: sc2::Point2D) -> None

        3. ability(self: library.Unit, arg0: sc2::SC2Type<sc2::ABILITY_ID>, arg1: library.Unit) -> None
        """
        pass

    def attack_move(self, arg0, *args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """ attack_move(self: library.Unit, arg0: sc2::Point2D) -> None """
        pass

    def attack_unit(self, arg0):  # real signature unknown; restored from __doc__
        """ attack_unit(self: library.Unit, arg0: library.Unit) -> None """
        pass

    def build(self, building_type, position, *args,
              **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        build(self: library.Unit, building_type: UnitType, position: sc2::Point2DI) -> None

        Build unit of type building_type at given position
        """
        pass

    def build_target(self, building_type, target):  # real signature unknown; restored from __doc__
        """
        build_target(self: library.Unit, building_type: UnitType, target: library.Unit) -> None

        Build building_type on top of target Unit, useful for building refineries
        """
        pass

    def hold_position(self):  # real signature unknown; restored from __doc__
        """ hold_position(self: library.Unit) -> None """
        pass

    def is_constructing(self, unit_type):  # real signature unknown; restored from __doc__
        """ is_constructing(self: library.Unit, unit_type: UnitType) -> bool """
        return False

    def morph(self, unit_type):  # real signature unknown; restored from __doc__
        """
        morph(self: library.Unit, unit_type: UnitType) -> None

        Morph into type of unit_type
        """
        pass

    def move(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        move(*args, **kwargs)
        Overloaded function.

        1. move(self: library.Unit, arg0: sc2::Point2D) -> None

        2. move(self: library.Unit, arg0: sc2::Point2DI) -> None
        """
        pass

    def patrol(self, arg0, *args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """ patrol(self: library.Unit, arg0: sc2::Point2D) -> None """
        pass

    def repair(self, arg0):  # real signature unknown; restored from __doc__
        """ repair(self: library.Unit, arg0: library.Unit) -> None """
        pass

    def research(self, upgrade_id, *args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        research(self: library.Unit, upgrade_id: sc2::SC2Type<sc2::UPGRADE_ID>) -> None

        Research the given :class:`library.UPGRADE_ID`
        """
        pass

    def right_click(self, arg0):  # real signature unknown; restored from __doc__
        """
        right_click(self: library.Unit, arg0: library.Unit) -> None

        Same as right-clicking in the game, for example making workers mine minerals
        """
        pass

    def stop(self):  # real signature unknown; restored from __doc__
        """ stop(self: library.Unit) -> None """
        pass

    def stop_dance(self):  # real signature unknown; restored from __doc__
        """ stop_dance(self: library.Unit) -> None """
        pass

    def train(self, unit_type):  # real signature unknown; restored from __doc__
        """
        train(self: library.Unit, unit_type: UnitType) -> None

        Train unit of type
        """
        pass

    def __eq__(self, arg0):  # real signature unknown; restored from __doc__
        """ __eq__(self: library.Unit, arg0: library.Unit) -> bool """
        return False

    def __hash__(self):  # real signature unknown; restored from __doc__
        """ __hash__(self: library.Unit) -> int """
        return 0

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: library.Unit) -> str """
        return ""

    buffs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    build_percentage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    current_ability_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The AbilityID of currently used ability"""

    energy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    facing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hit_points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_alive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_being_constructed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_blip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_burrowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_cloaked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_completed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_flying = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_idle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_powered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_training = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_hit_points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    player = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`library.Point2D` of the unit"""

    progress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tile_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`library.Point2DI` of the unit"""

    unit_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`library.UnitType` of the unit"""

    weapon_cooldown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


class UnitType(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.

        1. __eq__(self: library.UnitType, arg0: library.UnitType) -> bool

        2. __eq__(self: library.UnitType, arg0: library.UnitType) -> bool
        """
        pass

    def __hash__(self):  # real signature unknown; restored from __doc__
        """ __hash__(self: library.UnitType) -> int """
        return 0

    def __init__(self, arg0, *args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """ __init__(self: library.UnitType, arg0: sc2::SC2Type<sc2::UNIT_TYPEID>, arg1: IDABot) -> None """
        pass

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: library.UnitType) -> str """
        return ""

    attack_range = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gas_price = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_addon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_building = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_combat_unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unit is not any of the following: worker, supply provider, building, larva, egg"""

    is_detector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_egg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_geyser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_larva = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_mineral = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_morphed_building = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_overlord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_queen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_refinery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_resource_depot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_supply_provider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_tank = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_worker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mineral_price = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    movement_speed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    race = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    required_structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sight_range = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supply_provided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supply_required = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tile_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tile_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unit_typeid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


class UnitTypeID(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: library.UnitTypeID, arg0: library.UNIT_TYPEID) -> None """
        pass


class UNIT_TYPEID(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, arg0):  # real signature unknown; restored from __doc__
        """ __eq__(self: library.UNIT_TYPEID, arg0: library.UNIT_TYPEID) -> bool """
        return False

    def __getstate__(self):  # real signature unknown; restored from __doc__
        """ __getstate__(self: library.UNIT_TYPEID) -> tuple """
        return ()

    def __hash__(self):  # real signature unknown; restored from __doc__
        """ __hash__(self: library.UNIT_TYPEID) -> int """
        return 0

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: library.UNIT_TYPEID, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: library.UNIT_TYPEID) -> int """
        return 0

    def __ne__(self, arg0):  # real signature unknown; restored from __doc__
        """ __ne__(self: library.UNIT_TYPEID, arg0: library.UNIT_TYPEID) -> bool """
        return False

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: library.UNIT_TYPEID) -> str """
        return ""

    def __setstate__(self, arg0):  # real signature unknown; restored from __doc__
        """ __setstate__(self: library.UNIT_TYPEID, arg0: tuple) -> None """
        pass

    INVALID = None  # (!) real value is ''
    NEUTRAL_BATTLESTATIONMINERALFIELD = None  # (!) real value is ''
    NEUTRAL_BATTLESTATIONMINERALFIELD750 = None  # (!) real value is ''
    NEUTRAL_COLLAPSIBLEROCKTOWERDEBRIS = None  # (!) real value is ''
    NEUTRAL_COLLAPSIBLEROCKTOWERDIAGONAL = None  # (!) real value is ''
    NEUTRAL_COLLAPSIBLEROCKTOWERPUSHUNIT = None  # (!) real value is ''
    NEUTRAL_COLLAPSIBLETERRANTOWERDEBRIS = None  # (!) real value is ''
    NEUTRAL_COLLAPSIBLETERRANTOWERDIAGONAL = None  # (!) real value is ''
    NEUTRAL_COLLAPSIBLETERRANTOWERPUSHUNIT = None  # (!) real value is ''
    NEUTRAL_COLLAPSIBLETERRANTOWERPUSHUNITRAMPLEFT = None  # (!) real value is ''
    NEUTRAL_COLLAPSIBLETERRANTOWERPUSHUNITRAMPRIGHT = None  # (!) real value is ''
    NEUTRAL_COLLAPSIBLETERRANTOWERRAMPLEFT = None  # (!) real value is ''
    NEUTRAL_COLLAPSIBLETERRANTOWERRAMPRIGHT = None  # (!) real value is ''
    NEUTRAL_DEBRISRAMPLEFT = None  # (!) real value is ''
    NEUTRAL_DEBRISRAMPRIGHT = None  # (!) real value is ''
    NEUTRAL_DESTRUCTIBLEDEBRIS6X6 = None  # (!) real value is ''
    NEUTRAL_DESTRUCTIBLEDEBRISRAMPDIAGONALHUGEBLUR = None  # (!) real value is ''
    NEUTRAL_DESTRUCTIBLEDEBRISRAMPDIAGONALHUGEULBR = None  # (!) real value is ''
    NEUTRAL_DESTRUCTIBLEROCK6X6 = None  # (!) real value is ''
    NEUTRAL_DESTRUCTIBLEROCKEX1DIAGONALHUGEBLUR = None  # (!) real value is ''
    NEUTRAL_FORCEFIELD = None  # (!) real value is ''
    NEUTRAL_KARAKFEMALE = None  # (!) real value is ''
    NEUTRAL_LABMINERALFIELD = None  # (!) real value is ''
    NEUTRAL_LABMINERALFIELD750 = None  # (!) real value is ''
    NEUTRAL_MINERALFIELD = None  # (!) real value is ''
    NEUTRAL_MINERALFIELD750 = None  # (!) real value is ''
    NEUTRAL_PROTOSSVESPENEGEYSER = None  # (!) real value is ''
    NEUTRAL_PURIFIERMINERALFIELD = None  # (!) real value is ''
    NEUTRAL_PURIFIERMINERALFIELD750 = None  # (!) real value is ''
    NEUTRAL_PURIFIERRICHMINERALFIELD = None  # (!) real value is ''
    NEUTRAL_PURIFIERRICHMINERALFIELD750 = None  # (!) real value is ''
    NEUTRAL_PURIFIERVESPENEGEYSER = None  # (!) real value is ''
    NEUTRAL_RICHMINERALFIELD = None  # (!) real value is ''
    NEUTRAL_RICHMINERALFIELD750 = None  # (!) real value is ''
    NEUTRAL_RICHVESPENEGEYSER = None  # (!) real value is ''
    NEUTRAL_SCANTIPEDE = None  # (!) real value is ''
    NEUTRAL_SHAKURASVESPENEGEYSER = None  # (!) real value is ''
    NEUTRAL_SPACEPLATFORMGEYSER = None  # (!) real value is ''
    NEUTRAL_UNBUILDABLEBRICKSDESTRUCTIBLE = None  # (!) real value is ''
    NEUTRAL_UNBUILDABLEPLATESDESTRUCTIBLE = None  # (!) real value is ''
    NEUTRAL_UTILITYBOT = None  # (!) real value is ''
    NEUTRAL_VESPENEGEYSER = None  # (!) real value is ''
    NEUTRAL_XELNAGATOWER = None  # (!) real value is ''
    PROTOSS_ADEPT = None  # (!) real value is ''
    PROTOSS_ADEPTPHASESHIFT = None  # (!) real value is ''
    PROTOSS_ARCHON = None  # (!) real value is ''
    PROTOSS_ASSIMILATOR = None  # (!) real value is ''
    PROTOSS_CARRIER = None  # (!) real value is ''
    PROTOSS_COLOSSUS = None  # (!) real value is ''
    PROTOSS_CYBERNETICSCORE = None  # (!) real value is ''
    PROTOSS_DARKSHRINE = None  # (!) real value is ''
    PROTOSS_DARKTEMPLAR = None  # (!) real value is ''
    PROTOSS_DISRUPTOR = None  # (!) real value is ''
    PROTOSS_DISRUPTORPHASED = None  # (!) real value is ''
    PROTOSS_FLEETBEACON = None  # (!) real value is ''
    PROTOSS_FORGE = None  # (!) real value is ''
    PROTOSS_GATEWAY = None  # (!) real value is ''
    PROTOSS_HIGHTEMPLAR = None  # (!) real value is ''
    PROTOSS_IMMORTAL = None  # (!) real value is ''
    PROTOSS_INTERCEPTOR = None  # (!) real value is ''
    PROTOSS_MOTHERSHIP = None  # (!) real value is ''
    PROTOSS_MOTHERSHIPCORE = None  # (!) real value is ''
    PROTOSS_NEXUS = None  # (!) real value is ''
    PROTOSS_OBSERVER = None  # (!) real value is ''
    PROTOSS_ORACLE = None  # (!) real value is ''
    PROTOSS_ORACLESTASISTRAP = None  # (!) real value is ''
    PROTOSS_PHOENIX = None  # (!) real value is ''
    PROTOSS_PHOTONCANNON = None  # (!) real value is ''
    PROTOSS_PROBE = None  # (!) real value is ''
    PROTOSS_PYLON = None  # (!) real value is ''
    PROTOSS_PYLONOVERCHARGED = None  # (!) real value is ''
    PROTOSS_ROBOTICSBAY = None  # (!) real value is ''
    PROTOSS_ROBOTICSFACILITY = None  # (!) real value is ''
    PROTOSS_SENTRY = None  # (!) real value is ''
    PROTOSS_SHIELDBATTERY = None  # (!) real value is ''
    PROTOSS_STALKER = None  # (!) real value is ''
    PROTOSS_STARGATE = None  # (!) real value is ''
    PROTOSS_TEMPEST = None  # (!) real value is ''
    PROTOSS_TEMPLARARCHIVE = None  # (!) real value is ''
    PROTOSS_TWILIGHTCOUNCIL = None  # (!) real value is ''
    PROTOSS_VOIDRAY = None  # (!) real value is ''
    PROTOSS_WARPGATE = None  # (!) real value is ''
    PROTOSS_WARPPRISM = None  # (!) real value is ''
    PROTOSS_WARPPRISMPHASING = None  # (!) real value is ''
    PROTOSS_ZEALOT = None  # (!) real value is ''
    TERRAN_ARMORY = None  # (!) real value is ''
    TERRAN_AUTOTURRET = None  # (!) real value is ''
    TERRAN_BANSHEE = None  # (!) real value is ''
    TERRAN_BARRACKS = None  # (!) real value is ''
    TERRAN_BARRACKSFLYING = None  # (!) real value is ''
    TERRAN_BARRACKSREACTOR = None  # (!) real value is ''
    TERRAN_BARRACKSTECHLAB = None  # (!) real value is ''
    TERRAN_BATTLECRUISER = None  # (!) real value is ''
    TERRAN_BUNKER = None  # (!) real value is ''
    TERRAN_COMMANDCENTER = None  # (!) real value is ''
    TERRAN_COMMANDCENTERFLYING = None  # (!) real value is ''
    TERRAN_CYCLONE = None  # (!) real value is ''
    TERRAN_ENGINEERINGBAY = None  # (!) real value is ''
    TERRAN_FACTORY = None  # (!) real value is ''
    TERRAN_FACTORYFLYING = None  # (!) real value is ''
    TERRAN_FACTORYREACTOR = None  # (!) real value is ''
    TERRAN_FACTORYTECHLAB = None  # (!) real value is ''
    TERRAN_FUSIONCORE = None  # (!) real value is ''
    TERRAN_GHOST = None  # (!) real value is ''
    TERRAN_GHOSTACADEMY = None  # (!) real value is ''
    TERRAN_HELLION = None  # (!) real value is ''
    TERRAN_HELLIONTANK = None  # (!) real value is ''
    TERRAN_KD8CHARGE = None  # (!) real value is ''
    TERRAN_LIBERATOR = None  # (!) real value is ''
    TERRAN_LIBERATORAG = None  # (!) real value is ''
    TERRAN_MARAUDER = None  # (!) real value is ''
    TERRAN_MARINE = None  # (!) real value is ''
    TERRAN_MEDIVAC = None  # (!) real value is ''
    TERRAN_MISSILETURRET = None  # (!) real value is ''
    TERRAN_MULE = None  # (!) real value is ''
    TERRAN_NUKE = None  # (!) real value is ''
    TERRAN_ORBITALCOMMAND = None  # (!) real value is ''
    TERRAN_ORBITALCOMMANDFLYING = None  # (!) real value is ''
    TERRAN_PLANETARYFORTRESS = None  # (!) real value is ''
    TERRAN_POINTDEFENSEDRONE = None  # (!) real value is ''
    TERRAN_RAVEN = None  # (!) real value is ''
    TERRAN_REACTOR = None  # (!) real value is ''
    TERRAN_REAPER = None  # (!) real value is ''
    TERRAN_REFINERY = None  # (!) real value is ''
    TERRAN_SCV = None  # (!) real value is ''
    TERRAN_SENSORTOWER = None  # (!) real value is ''
    TERRAN_SIEGETANK = None  # (!) real value is ''
    TERRAN_SIEGETANKSIEGED = None  # (!) real value is ''
    TERRAN_STARPORT = None  # (!) real value is ''
    TERRAN_STARPORTFLYING = None  # (!) real value is ''
    TERRAN_STARPORTREACTOR = None  # (!) real value is ''
    TERRAN_STARPORTTECHLAB = None  # (!) real value is ''
    TERRAN_SUPPLYDEPOT = None  # (!) real value is ''
    TERRAN_SUPPLYDEPOTLOWERED = None  # (!) real value is ''
    TERRAN_TECHLAB = None  # (!) real value is ''
    TERRAN_THOR = None  # (!) real value is ''
    TERRAN_THORAP = None  # (!) real value is ''
    TERRAN_VIKINGASSAULT = None  # (!) real value is ''
    TERRAN_VIKINGFIGHTER = None  # (!) real value is ''
    TERRAN_WIDOWMINE = None  # (!) real value is ''
    TERRAN_WIDOWMINEBURROWED = None  # (!) real value is ''
    ZERG_BANELING = None  # (!) real value is ''
    ZERG_BANELINGBURROWED = None  # (!) real value is ''
    ZERG_BANELINGCOCOON = None  # (!) real value is ''
    ZERG_BANELINGNEST = None  # (!) real value is ''
    ZERG_BROODLING = None  # (!) real value is ''
    ZERG_BROODLORD = None  # (!) real value is ''
    ZERG_BROODLORDCOCOON = None  # (!) real value is ''
    ZERG_CHANGELING = None  # (!) real value is ''
    ZERG_CHANGELINGMARINE = None  # (!) real value is ''
    ZERG_CHANGELINGMARINESHIELD = None  # (!) real value is ''
    ZERG_CHANGELINGZEALOT = None  # (!) real value is ''
    ZERG_CHANGELINGZERGLING = None  # (!) real value is ''
    ZERG_CHANGELINGZERGLINGWINGS = None  # (!) real value is ''
    ZERG_CORRUPTOR = None  # (!) real value is ''
    ZERG_CREEPTUMOR = None  # (!) real value is ''
    ZERG_CREEPTUMORBURROWED = None  # (!) real value is ''
    ZERG_CREEPTUMORQUEEN = None  # (!) real value is ''
    ZERG_DRONE = None  # (!) real value is ''
    ZERG_DRONEBURROWED = None  # (!) real value is ''
    ZERG_EGG = None  # (!) real value is ''
    ZERG_EVOLUTIONCHAMBER = None  # (!) real value is ''
    ZERG_EXTRACTOR = None  # (!) real value is ''
    ZERG_GREATERSPIRE = None  # (!) real value is ''
    ZERG_HATCHERY = None  # (!) real value is ''
    ZERG_HIVE = None  # (!) real value is ''
    ZERG_HYDRALISK = None  # (!) real value is ''
    ZERG_HYDRALISKBURROWED = None  # (!) real value is ''
    ZERG_HYDRALISKDEN = None  # (!) real value is ''
    ZERG_INFESTATIONPIT = None  # (!) real value is ''
    ZERG_INFESTEDTERRANSEGG = None  # (!) real value is ''
    ZERG_INFESTOR = None  # (!) real value is ''
    ZERG_INFESTORBURROWED = None  # (!) real value is ''
    ZERG_INFESTORTERRAN = None  # (!) real value is ''
    ZERG_LAIR = None  # (!) real value is ''
    ZERG_LARVA = None  # (!) real value is ''
    ZERG_LOCUSTMP = None  # (!) real value is ''
    ZERG_LOCUSTMPFLYING = None  # (!) real value is ''
    ZERG_LURKERDENMP = None  # (!) real value is ''
    ZERG_LURKERMP = None  # (!) real value is ''
    ZERG_LURKERMPBURROWED = None  # (!) real value is ''
    ZERG_LURKERMPEGG = None  # (!) real value is ''
    ZERG_MUTALISK = None  # (!) real value is ''
    ZERG_NYDUSCANAL = None  # (!) real value is ''
    ZERG_NYDUSNETWORK = None  # (!) real value is ''
    ZERG_OVERLORD = None  # (!) real value is ''
    ZERG_OVERLORDCOCOON = None  # (!) real value is ''
    ZERG_OVERLORDTRANSPORT = None  # (!) real value is ''
    ZERG_OVERSEER = None  # (!) real value is ''
    ZERG_PARASITICBOMBDUMMY = None  # (!) real value is ''
    ZERG_QUEEN = None  # (!) real value is ''
    ZERG_QUEENBURROWED = None  # (!) real value is ''
    ZERG_RAVAGER = None  # (!) real value is ''
    ZERG_RAVAGERCOCOON = None  # (!) real value is ''
    ZERG_ROACH = None  # (!) real value is ''
    ZERG_ROACHBURROWED = None  # (!) real value is ''
    ZERG_ROACHWARREN = None  # (!) real value is ''
    ZERG_SPAWNINGPOOL = None  # (!) real value is ''
    ZERG_SPINECRAWLER = None  # (!) real value is ''
    ZERG_SPINECRAWLERUPROOTED = None  # (!) real value is ''
    ZERG_SPIRE = None  # (!) real value is ''
    ZERG_SPORECRAWLER = None  # (!) real value is ''
    ZERG_SPORECRAWLERUPROOTED = None  # (!) real value is ''
    ZERG_SWARMHOSTBURROWEDMP = None  # (!) real value is ''
    ZERG_SWARMHOSTMP = None  # (!) real value is ''
    ZERG_TRANSPORTOVERLORDCOCOON = None  # (!) real value is ''
    ZERG_ULTRALISK = None  # (!) real value is ''
    ZERG_ULTRALISKCAVERN = None  # (!) real value is ''
    ZERG_VIPER = None  # (!) real value is ''
    ZERG_ZERGLING = None  # (!) real value is ''
    ZERG_ZERGLINGBURROWED = None  # (!) real value is ''
    __members__ = {
        'INVALID': '<failed to retrieve the value>',
        'NEUTRAL_BATTLESTATIONMINERALFIELD': '<failed to retrieve the value>',
        'NEUTRAL_BATTLESTATIONMINERALFIELD750': '<failed to retrieve the value>',
        'NEUTRAL_COLLAPSIBLEROCKTOWERDEBRIS': '<failed to retrieve the value>',
        'NEUTRAL_COLLAPSIBLEROCKTOWERDIAGONAL': '<failed to retrieve the value>',
        'NEUTRAL_COLLAPSIBLEROCKTOWERPUSHUNIT': '<failed to retrieve the value>',
        'NEUTRAL_COLLAPSIBLETERRANTOWERDEBRIS': '<failed to retrieve the value>',
        'NEUTRAL_COLLAPSIBLETERRANTOWERDIAGONAL': '<failed to retrieve the value>',
        'NEUTRAL_COLLAPSIBLETERRANTOWERPUSHUNIT': '<failed to retrieve the value>',
        'NEUTRAL_COLLAPSIBLETERRANTOWERPUSHUNITRAMPLEFT': '<failed to retrieve the value>',
        'NEUTRAL_COLLAPSIBLETERRANTOWERPUSHUNITRAMPRIGHT': '<failed to retrieve the value>',
        'NEUTRAL_COLLAPSIBLETERRANTOWERRAMPLEFT': '<failed to retrieve the value>',
        'NEUTRAL_COLLAPSIBLETERRANTOWERRAMPRIGHT': '<failed to retrieve the value>',
        'NEUTRAL_DEBRISRAMPLEFT': '<failed to retrieve the value>',
        'NEUTRAL_DEBRISRAMPRIGHT': '<failed to retrieve the value>',
        'NEUTRAL_DESTRUCTIBLEDEBRIS6X6': '<failed to retrieve the value>',
        'NEUTRAL_DESTRUCTIBLEDEBRISRAMPDIAGONALHUGEBLUR': '<failed to retrieve the value>',
        'NEUTRAL_DESTRUCTIBLEDEBRISRAMPDIAGONALHUGEULBR': '<failed to retrieve the value>',
        'NEUTRAL_DESTRUCTIBLEROCK6X6': '<failed to retrieve the value>',
        'NEUTRAL_DESTRUCTIBLEROCKEX1DIAGONALHUGEBLUR': '<failed to retrieve the value>',
        'NEUTRAL_FORCEFIELD': '<failed to retrieve the value>',
        'NEUTRAL_KARAKFEMALE': '<failed to retrieve the value>',
        'NEUTRAL_LABMINERALFIELD': '<failed to retrieve the value>',
        'NEUTRAL_LABMINERALFIELD750': '<failed to retrieve the value>',
        'NEUTRAL_MINERALFIELD': '<failed to retrieve the value>',
        'NEUTRAL_MINERALFIELD750': '<failed to retrieve the value>',
        'NEUTRAL_PROTOSSVESPENEGEYSER': '<failed to retrieve the value>',
        'NEUTRAL_PURIFIERMINERALFIELD': '<failed to retrieve the value>',
        'NEUTRAL_PURIFIERMINERALFIELD750': '<failed to retrieve the value>',
        'NEUTRAL_PURIFIERRICHMINERALFIELD': '<failed to retrieve the value>',
        'NEUTRAL_PURIFIERRICHMINERALFIELD750': '<failed to retrieve the value>',
        'NEUTRAL_PURIFIERVESPENEGEYSER': '<failed to retrieve the value>',
        'NEUTRAL_RICHMINERALFIELD': '<failed to retrieve the value>',
        'NEUTRAL_RICHMINERALFIELD750': '<failed to retrieve the value>',
        'NEUTRAL_RICHVESPENEGEYSER': '<failed to retrieve the value>',
        'NEUTRAL_SCANTIPEDE': '<failed to retrieve the value>',
        'NEUTRAL_SHAKURASVESPENEGEYSER': '<failed to retrieve the value>',
        'NEUTRAL_SPACEPLATFORMGEYSER': '<failed to retrieve the value>',
        'NEUTRAL_UNBUILDABLEBRICKSDESTRUCTIBLE': '<failed to retrieve the value>',
        'NEUTRAL_UNBUILDABLEPLATESDESTRUCTIBLE': '<failed to retrieve the value>',
        'NEUTRAL_UTILITYBOT': '<failed to retrieve the value>',
        'NEUTRAL_VESPENEGEYSER': '<failed to retrieve the value>',
        'NEUTRAL_XELNAGATOWER': '<failed to retrieve the value>',
        'PROTOSS_ADEPT': '<failed to retrieve the value>',
        'PROTOSS_ADEPTPHASESHIFT': '<failed to retrieve the value>',
        'PROTOSS_ARCHON': '<failed to retrieve the value>',
        'PROTOSS_ASSIMILATOR': '<failed to retrieve the value>',
        'PROTOSS_CARRIER': '<failed to retrieve the value>',
        'PROTOSS_COLOSSUS': '<failed to retrieve the value>',
        'PROTOSS_CYBERNETICSCORE': '<failed to retrieve the value>',
        'PROTOSS_DARKSHRINE': '<failed to retrieve the value>',
        'PROTOSS_DARKTEMPLAR': '<failed to retrieve the value>',
        'PROTOSS_DISRUPTOR': '<failed to retrieve the value>',
        'PROTOSS_DISRUPTORPHASED': '<failed to retrieve the value>',
        'PROTOSS_FLEETBEACON': '<failed to retrieve the value>',
        'PROTOSS_FORGE': '<failed to retrieve the value>',
        'PROTOSS_GATEWAY': '<failed to retrieve the value>',
        'PROTOSS_HIGHTEMPLAR': '<failed to retrieve the value>',
        'PROTOSS_IMMORTAL': '<failed to retrieve the value>',
        'PROTOSS_INTERCEPTOR': '<failed to retrieve the value>',
        'PROTOSS_MOTHERSHIP': '<failed to retrieve the value>',
        'PROTOSS_MOTHERSHIPCORE': '<failed to retrieve the value>',
        'PROTOSS_NEXUS': '<failed to retrieve the value>',
        'PROTOSS_OBSERVER': '<failed to retrieve the value>',
        'PROTOSS_ORACLE': '<failed to retrieve the value>',
        'PROTOSS_ORACLESTASISTRAP': '<failed to retrieve the value>',
        'PROTOSS_PHOENIX': '<failed to retrieve the value>',
        'PROTOSS_PHOTONCANNON': '<failed to retrieve the value>',
        'PROTOSS_PROBE': '<failed to retrieve the value>',
        'PROTOSS_PYLON': '<failed to retrieve the value>',
        'PROTOSS_PYLONOVERCHARGED': '<failed to retrieve the value>',
        'PROTOSS_ROBOTICSBAY': '<failed to retrieve the value>',
        'PROTOSS_ROBOTICSFACILITY': '<failed to retrieve the value>',
        'PROTOSS_SENTRY': '<failed to retrieve the value>',
        'PROTOSS_SHIELDBATTERY': '<failed to retrieve the value>',
        'PROTOSS_STALKER': '<failed to retrieve the value>',
        'PROTOSS_STARGATE': '<failed to retrieve the value>',
        'PROTOSS_TEMPEST': '<failed to retrieve the value>',
        'PROTOSS_TEMPLARARCHIVE': '<failed to retrieve the value>',
        'PROTOSS_TWILIGHTCOUNCIL': '<failed to retrieve the value>',
        'PROTOSS_VOIDRAY': '<failed to retrieve the value>',
        'PROTOSS_WARPGATE': '<failed to retrieve the value>',
        'PROTOSS_WARPPRISM': '<failed to retrieve the value>',
        'PROTOSS_WARPPRISMPHASING': '<failed to retrieve the value>',
        'PROTOSS_ZEALOT': '<failed to retrieve the value>',
        'TERRAN_ARMORY': '<failed to retrieve the value>',
        'TERRAN_AUTOTURRET': '<failed to retrieve the value>',
        'TERRAN_BANSHEE': '<failed to retrieve the value>',
        'TERRAN_BARRACKS': '<failed to retrieve the value>',
        'TERRAN_BARRACKSFLYING': '<failed to retrieve the value>',
        'TERRAN_BARRACKSREACTOR': '<failed to retrieve the value>',
        'TERRAN_BARRACKSTECHLAB': '<failed to retrieve the value>',
        'TERRAN_BATTLECRUISER': '<failed to retrieve the value>',
        'TERRAN_BUNKER': '<failed to retrieve the value>',
        'TERRAN_COMMANDCENTER': '<failed to retrieve the value>',
        'TERRAN_COMMANDCENTERFLYING': '<failed to retrieve the value>',
        'TERRAN_CYCLONE': '<failed to retrieve the value>',
        'TERRAN_ENGINEERINGBAY': '<failed to retrieve the value>',
        'TERRAN_FACTORY': '<failed to retrieve the value>',
        'TERRAN_FACTORYFLYING': '<failed to retrieve the value>',
        'TERRAN_FACTORYREACTOR': '<failed to retrieve the value>',
        'TERRAN_FACTORYTECHLAB': '<failed to retrieve the value>',
        'TERRAN_FUSIONCORE': '<failed to retrieve the value>',
        'TERRAN_GHOST': '<failed to retrieve the value>',
        'TERRAN_GHOSTACADEMY': '<failed to retrieve the value>',
        'TERRAN_HELLION': '<failed to retrieve the value>',
        'TERRAN_HELLIONTANK': '<failed to retrieve the value>',
        'TERRAN_KD8CHARGE': '<failed to retrieve the value>',
        'TERRAN_LIBERATOR': '<failed to retrieve the value>',
        'TERRAN_LIBERATORAG': '<failed to retrieve the value>',
        'TERRAN_MARAUDER': '<failed to retrieve the value>',
        'TERRAN_MARINE': '<failed to retrieve the value>',
        'TERRAN_MEDIVAC': '<failed to retrieve the value>',
        'TERRAN_MISSILETURRET': '<failed to retrieve the value>',
        'TERRAN_MULE': '<failed to retrieve the value>',
        'TERRAN_NUKE': '<failed to retrieve the value>',
        'TERRAN_ORBITALCOMMAND': '<failed to retrieve the value>',
        'TERRAN_ORBITALCOMMANDFLYING': '<failed to retrieve the value>',
        'TERRAN_PLANETARYFORTRESS': '<failed to retrieve the value>',
        'TERRAN_POINTDEFENSEDRONE': '<failed to retrieve the value>',
        'TERRAN_RAVEN': '<failed to retrieve the value>',
        'TERRAN_REACTOR': '<failed to retrieve the value>',
        'TERRAN_REAPER': '<failed to retrieve the value>',
        'TERRAN_REFINERY': '<failed to retrieve the value>',
        'TERRAN_SCV': '<failed to retrieve the value>',
        'TERRAN_SENSORTOWER': '<failed to retrieve the value>',
        'TERRAN_SIEGETANK': '<failed to retrieve the value>',
        'TERRAN_SIEGETANKSIEGED': '<failed to retrieve the value>',
        'TERRAN_STARPORT': '<failed to retrieve the value>',
        'TERRAN_STARPORTFLYING': '<failed to retrieve the value>',
        'TERRAN_STARPORTREACTOR': '<failed to retrieve the value>',
        'TERRAN_STARPORTTECHLAB': '<failed to retrieve the value>',
        'TERRAN_SUPPLYDEPOT': '<failed to retrieve the value>',
        'TERRAN_SUPPLYDEPOTLOWERED': '<failed to retrieve the value>',
        'TERRAN_TECHLAB': '<failed to retrieve the value>',
        'TERRAN_THOR': '<failed to retrieve the value>',
        'TERRAN_THORAP': '<failed to retrieve the value>',
        'TERRAN_VIKINGASSAULT': '<failed to retrieve the value>',
        'TERRAN_VIKINGFIGHTER': '<failed to retrieve the value>',
        'TERRAN_WIDOWMINE': '<failed to retrieve the value>',
        'TERRAN_WIDOWMINEBURROWED': '<failed to retrieve the value>',
        'ZERG_BANELING': '<failed to retrieve the value>',
        'ZERG_BANELINGBURROWED': '<failed to retrieve the value>',
        'ZERG_BANELINGCOCOON': '<failed to retrieve the value>',
        'ZERG_BANELINGNEST': '<failed to retrieve the value>',
        'ZERG_BROODLING': '<failed to retrieve the value>',
        'ZERG_BROODLORD': '<failed to retrieve the value>',
        'ZERG_BROODLORDCOCOON': '<failed to retrieve the value>',
        'ZERG_CHANGELING': '<failed to retrieve the value>',
        'ZERG_CHANGELINGMARINE': '<failed to retrieve the value>',
        'ZERG_CHANGELINGMARINESHIELD': '<failed to retrieve the value>',
        'ZERG_CHANGELINGZEALOT': '<failed to retrieve the value>',
        'ZERG_CHANGELINGZERGLING': '<failed to retrieve the value>',
        'ZERG_CHANGELINGZERGLINGWINGS': '<failed to retrieve the value>',
        'ZERG_CORRUPTOR': '<failed to retrieve the value>',
        'ZERG_CREEPTUMOR': '<failed to retrieve the value>',
        'ZERG_CREEPTUMORBURROWED': '<failed to retrieve the value>',
        'ZERG_CREEPTUMORQUEEN': '<failed to retrieve the value>',
        'ZERG_DRONE': '<failed to retrieve the value>',
        'ZERG_DRONEBURROWED': '<failed to retrieve the value>',
        'ZERG_EGG': '<failed to retrieve the value>',
        'ZERG_EVOLUTIONCHAMBER': '<failed to retrieve the value>',
        'ZERG_EXTRACTOR': '<failed to retrieve the value>',
        'ZERG_GREATERSPIRE': '<failed to retrieve the value>',
        'ZERG_HATCHERY': '<failed to retrieve the value>',
        'ZERG_HIVE': '<failed to retrieve the value>',
        'ZERG_HYDRALISK': '<failed to retrieve the value>',
        'ZERG_HYDRALISKBURROWED': '<failed to retrieve the value>',
        'ZERG_HYDRALISKDEN': '<failed to retrieve the value>',
        'ZERG_INFESTATIONPIT': '<failed to retrieve the value>',
        'ZERG_INFESTEDTERRANSEGG': '<failed to retrieve the value>',
        'ZERG_INFESTOR': '<failed to retrieve the value>',
        'ZERG_INFESTORBURROWED': '<failed to retrieve the value>',
        'ZERG_INFESTORTERRAN': '<failed to retrieve the value>',
        'ZERG_LAIR': '<failed to retrieve the value>',
        'ZERG_LARVA': '<failed to retrieve the value>',
        'ZERG_LOCUSTMP': '<failed to retrieve the value>',
        'ZERG_LOCUSTMPFLYING': '<failed to retrieve the value>',
        'ZERG_LURKERDENMP': '<failed to retrieve the value>',
        'ZERG_LURKERMP': '<failed to retrieve the value>',
        'ZERG_LURKERMPBURROWED': '<failed to retrieve the value>',
        'ZERG_LURKERMPEGG': '<failed to retrieve the value>',
        'ZERG_MUTALISK': '<failed to retrieve the value>',
        'ZERG_NYDUSCANAL': '<failed to retrieve the value>',
        'ZERG_NYDUSNETWORK': '<failed to retrieve the value>',
        'ZERG_OVERLORD': '<failed to retrieve the value>',
        'ZERG_OVERLORDCOCOON': '<failed to retrieve the value>',
        'ZERG_OVERLORDTRANSPORT': '<failed to retrieve the value>',
        'ZERG_OVERSEER': '<failed to retrieve the value>',
        'ZERG_PARASITICBOMBDUMMY': '<failed to retrieve the value>',
        'ZERG_QUEEN': '<failed to retrieve the value>',
        'ZERG_QUEENBURROWED': '<failed to retrieve the value>',
        'ZERG_RAVAGER': '<failed to retrieve the value>',
        'ZERG_RAVAGERCOCOON': '<failed to retrieve the value>',
        'ZERG_ROACH': '<failed to retrieve the value>',
        'ZERG_ROACHBURROWED': '<failed to retrieve the value>',
        'ZERG_ROACHWARREN': '<failed to retrieve the value>',
        'ZERG_SPAWNINGPOOL': '<failed to retrieve the value>',
        'ZERG_SPINECRAWLER': '<failed to retrieve the value>',
        'ZERG_SPINECRAWLERUPROOTED': '<failed to retrieve the value>',
        'ZERG_SPIRE': '<failed to retrieve the value>',
        'ZERG_SPORECRAWLER': '<failed to retrieve the value>',
        'ZERG_SPORECRAWLERUPROOTED': '<failed to retrieve the value>',
        'ZERG_SWARMHOSTBURROWEDMP': '<failed to retrieve the value>',
        'ZERG_SWARMHOSTMP': '<failed to retrieve the value>',
        'ZERG_TRANSPORTOVERLORDCOCOON': '<failed to retrieve the value>',
        'ZERG_ULTRALISK': '<failed to retrieve the value>',
        'ZERG_ULTRALISKCAVERN': '<failed to retrieve the value>',
        'ZERG_VIPER': '<failed to retrieve the value>',
        'ZERG_ZERGLING': '<failed to retrieve the value>',
        'ZERG_ZERGLINGBURROWED': '<failed to retrieve the value>',
    }


class UpgradeID(__pybind11_builtins.pybind11_object):
    # no doc
    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: library.UpgradeID, arg0: library.UPGRADE_ID) -> None """
        pass


class UPGRADE_ID(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, arg0):  # real signature unknown; restored from __doc__
        """ __eq__(self: library.UPGRADE_ID, arg0: library.UPGRADE_ID) -> bool """
        return False

    def __getstate__(self):  # real signature unknown; restored from __doc__
        """ __getstate__(self: library.UPGRADE_ID) -> tuple """
        return ()

    def __hash__(self):  # real signature unknown; restored from __doc__
        """ __hash__(self: library.UPGRADE_ID) -> int """
        return 0

    def __init__(self, arg0):  # real signature unknown; restored from __doc__
        """ __init__(self: library.UPGRADE_ID, arg0: int) -> None """
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ __int__(self: library.UPGRADE_ID) -> int """
        return 0

    def __ne__(self, arg0):  # real signature unknown; restored from __doc__
        """ __ne__(self: library.UPGRADE_ID, arg0: library.UPGRADE_ID) -> bool """
        return False

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ __repr__(self: library.UPGRADE_ID) -> str """
        return ""

    def __setstate__(self, arg0):  # real signature unknown; restored from __doc__
        """ __setstate__(self: library.UPGRADE_ID, arg0: tuple) -> None """
        pass

    ADEPTPIERCINGATTACK = None  # (!) real value is ''
    BANSHEECLOAK = None  # (!) real value is ''
    BANSHEESPEED = None  # (!) real value is ''
    BATTLECRUISERENABLESPECIALIZATIONS = None  # (!) real value is ''
    BLINKTECH = None  # (!) real value is ''
    BURROW = None  # (!) real value is ''
    CARRIERLAUNCHSPEEDUPGRADE = None  # (!) real value is ''
    CENTRIFICALHOOKS = None  # (!) real value is ''
    CHARGE = None  # (!) real value is ''
    CHITINOUSPLATING = None  # (!) real value is ''
    DARKTEMPLARBLINKUPGRADE = None  # (!) real value is ''
    DRILLCLAWS = None  # (!) real value is ''
    ENHANCEDMUNITIONS = None  # (!) real value is ''
    EVOLVEGROOVEDSPINES = None  # (!) real value is ''
    EVOLVEMUSCULARAUGMENTS = None  # (!) real value is ''
    EXTENDEDTHERMALLANCE = None  # (!) real value is ''
    GLIALRECONSTITUTION = None  # (!) real value is ''
    GRAVITICDRIVE = None  # (!) real value is ''
    HIGHCAPACITYBARRELS = None  # (!) real value is ''
    HISECAUTOTRACKING = None  # (!) real value is ''
    INFESTORENERGYUPGRADE = None  # (!) real value is ''
    INVALID = None  # (!) real value is ''
    LIBERATORAGRANGEUPGRADE = None  # (!) real value is ''
    MAGFIELDLAUNCHERS = None  # (!) real value is ''
    MEDIVACINCREASESPEEDBOOST = None  # (!) real value is ''
    NEOSTEELFRAME = None  # (!) real value is ''
    NEURALPARASITE = None  # (!) real value is ''
    OBSERVERGRAVITICBOOSTER = None  # (!) real value is ''
    OVERLORDSPEED = None  # (!) real value is ''
    PERSONALCLOAKING = None  # (!) real value is ''
    PHOENIXRANGEUPGRADE = None  # (!) real value is ''
    PROTOSSAIRARMORSLEVEL1 = None  # (!) real value is ''
    PROTOSSAIRARMORSLEVEL2 = None  # (!) real value is ''
    PROTOSSAIRARMORSLEVEL3 = None  # (!) real value is ''
    PROTOSSAIRWEAPONSLEVEL1 = None  # (!) real value is ''
    PROTOSSAIRWEAPONSLEVEL2 = None  # (!) real value is ''
    PROTOSSAIRWEAPONSLEVEL3 = None  # (!) real value is ''
    PROTOSSGROUNDARMORSLEVEL1 = None  # (!) real value is ''
    PROTOSSGROUNDARMORSLEVEL2 = None  # (!) real value is ''
    PROTOSSGROUNDARMORSLEVEL3 = None  # (!) real value is ''
    PROTOSSGROUNDWEAPONSLEVEL1 = None  # (!) real value is ''
    PROTOSSGROUNDWEAPONSLEVEL2 = None  # (!) real value is ''
    PROTOSSGROUNDWEAPONSLEVEL3 = None  # (!) real value is ''
    PROTOSSSHIELDSLEVEL1 = None  # (!) real value is ''
    PROTOSSSHIELDSLEVEL2 = None  # (!) real value is ''
    PROTOSSSHIELDSLEVEL3 = None  # (!) real value is ''
    PSISTORMTECH = None  # (!) real value is ''
    PUNISHERGRENADES = None  # (!) real value is ''
    RAPIDFIRELAUNCHERS = None  # (!) real value is ''
    RAVENCORVIDREACTOR = None  # (!) real value is ''
    RAVENRECALIBRATEDEXPLOSIVES = None  # (!) real value is ''
    SHIELDWALL = None  # (!) real value is ''
    SMARTSERVOS = None  # (!) real value is ''
    STIMPACK = None  # (!) real value is ''
    TERRANBUILDINGARMOR = None  # (!) real value is ''
    TERRANINFANTRYARMORSLEVEL1 = None  # (!) real value is ''
    TERRANINFANTRYARMORSLEVEL2 = None  # (!) real value is ''
    TERRANINFANTRYARMORSLEVEL3 = None  # (!) real value is ''
    TERRANINFANTRYWEAPONSLEVEL1 = None  # (!) real value is ''
    TERRANINFANTRYWEAPONSLEVEL2 = None  # (!) real value is ''
    TERRANINFANTRYWEAPONSLEVEL3 = None  # (!) real value is ''
    TERRANSHIPWEAPONSLEVEL1 = None  # (!) real value is ''
    TERRANSHIPWEAPONSLEVEL2 = None  # (!) real value is ''
    TERRANSHIPWEAPONSLEVEL3 = None  # (!) real value is ''
    TERRANVEHICLEANDSHIPARMORSLEVEL1 = None  # (!) real value is ''
    TERRANVEHICLEANDSHIPARMORSLEVEL2 = None  # (!) real value is ''
    TERRANVEHICLEANDSHIPARMORSLEVEL3 = None  # (!) real value is ''
    TERRANVEHICLEWEAPONSLEVEL1 = None  # (!) real value is ''
    TERRANVEHICLEWEAPONSLEVEL2 = None  # (!) real value is ''
    TERRANVEHICLEWEAPONSLEVEL3 = None  # (!) real value is ''
    TUNNELINGCLAWS = None  # (!) real value is ''
    WARPGATERESEARCH = None  # (!) real value is ''
    ZERGFLYERARMORSLEVEL1 = None  # (!) real value is ''
    ZERGFLYERARMORSLEVEL2 = None  # (!) real value is ''
    ZERGFLYERARMORSLEVEL3 = None  # (!) real value is ''
    ZERGFLYERWEAPONSLEVEL1 = None  # (!) real value is ''
    ZERGFLYERWEAPONSLEVEL2 = None  # (!) real value is ''
    ZERGFLYERWEAPONSLEVEL3 = None  # (!) real value is ''
    ZERGGROUNDARMORSLEVEL1 = None  # (!) real value is ''
    ZERGGROUNDARMORSLEVEL2 = None  # (!) real value is ''
    ZERGGROUNDARMORSLEVEL3 = None  # (!) real value is ''
    ZERGLINGATTACKSPEED = None  # (!) real value is ''
    ZERGLINGMOVEMENTSPEED = None  # (!) real value is ''
    ZERGMELEEWEAPONSLEVEL1 = None  # (!) real value is ''
    ZERGMELEEWEAPONSLEVEL2 = None  # (!) real value is ''
    ZERGMELEEWEAPONSLEVEL3 = None  # (!) real value is ''
    ZERGMISSILEWEAPONSLEVEL1 = None  # (!) real value is ''
    ZERGMISSILEWEAPONSLEVEL2 = None  # (!) real value is ''
    ZERGMISSILEWEAPONSLEVEL3 = None  # (!) real value is ''
    __members__ = {
        'ADEPTPIERCINGATTACK': '<failed to retrieve the value>',
        'BANSHEECLOAK': '<failed to retrieve the value>',
        'BANSHEESPEED': '<failed to retrieve the value>',
        'BATTLECRUISERENABLESPECIALIZATIONS': '<failed to retrieve the value>',
        'BLINKTECH': '<failed to retrieve the value>',
        'BURROW': '<failed to retrieve the value>',
        'CARRIERLAUNCHSPEEDUPGRADE': '<failed to retrieve the value>',
        'CENTRIFICALHOOKS': '<failed to retrieve the value>',
        'CHARGE': '<failed to retrieve the value>',
        'CHITINOUSPLATING': '<failed to retrieve the value>',
        'DARKTEMPLARBLINKUPGRADE': '<failed to retrieve the value>',
        'DRILLCLAWS': '<failed to retrieve the value>',
        'ENHANCEDMUNITIONS': '<failed to retrieve the value>',
        'EVOLVEGROOVEDSPINES': '<failed to retrieve the value>',
        'EVOLVEMUSCULARAUGMENTS': '<failed to retrieve the value>',
        'EXTENDEDTHERMALLANCE': '<failed to retrieve the value>',
        'GLIALRECONSTITUTION': '<failed to retrieve the value>',
        'GRAVITICDRIVE': '<failed to retrieve the value>',
        'HIGHCAPACITYBARRELS': '<failed to retrieve the value>',
        'HISECAUTOTRACKING': '<failed to retrieve the value>',
        'INFESTORENERGYUPGRADE': '<failed to retrieve the value>',
        'INVALID': '<failed to retrieve the value>',
        'LIBERATORAGRANGEUPGRADE': '<failed to retrieve the value>',
        'MAGFIELDLAUNCHERS': '<failed to retrieve the value>',
        'MEDIVACINCREASESPEEDBOOST': '<failed to retrieve the value>',
        'NEOSTEELFRAME': '<failed to retrieve the value>',
        'NEURALPARASITE': '<failed to retrieve the value>',
        'OBSERVERGRAVITICBOOSTER': '<failed to retrieve the value>',
        'OVERLORDSPEED': '<failed to retrieve the value>',
        'PERSONALCLOAKING': '<failed to retrieve the value>',
        'PHOENIXRANGEUPGRADE': '<failed to retrieve the value>',
        'PROTOSSAIRARMORSLEVEL1': '<failed to retrieve the value>',
        'PROTOSSAIRARMORSLEVEL2': '<failed to retrieve the value>',
        'PROTOSSAIRARMORSLEVEL3': '<failed to retrieve the value>',
        'PROTOSSAIRWEAPONSLEVEL1': '<failed to retrieve the value>',
        'PROTOSSAIRWEAPONSLEVEL2': '<failed to retrieve the value>',
        'PROTOSSAIRWEAPONSLEVEL3': '<failed to retrieve the value>',
        'PROTOSSGROUNDARMORSLEVEL1': '<failed to retrieve the value>',
        'PROTOSSGROUNDARMORSLEVEL2': '<failed to retrieve the value>',
        'PROTOSSGROUNDARMORSLEVEL3': '<failed to retrieve the value>',
        'PROTOSSGROUNDWEAPONSLEVEL1': '<failed to retrieve the value>',
        'PROTOSSGROUNDWEAPONSLEVEL2': '<failed to retrieve the value>',
        'PROTOSSGROUNDWEAPONSLEVEL3': '<failed to retrieve the value>',
        'PROTOSSSHIELDSLEVEL1': '<failed to retrieve the value>',
        'PROTOSSSHIELDSLEVEL2': '<failed to retrieve the value>',
        'PROTOSSSHIELDSLEVEL3': '<failed to retrieve the value>',
        'PSISTORMTECH': '<failed to retrieve the value>',
        'PUNISHERGRENADES': '<failed to retrieve the value>',
        'RAPIDFIRELAUNCHERS': '<failed to retrieve the value>',
        'RAVENCORVIDREACTOR': '<failed to retrieve the value>',
        'RAVENRECALIBRATEDEXPLOSIVES': '<failed to retrieve the value>',
        'SHIELDWALL': '<failed to retrieve the value>',
        'SMARTSERVOS': '<failed to retrieve the value>',
        'STIMPACK': '<failed to retrieve the value>',
        'TERRANBUILDINGARMOR': '<failed to retrieve the value>',
        'TERRANINFANTRYARMORSLEVEL1': '<failed to retrieve the value>',
        'TERRANINFANTRYARMORSLEVEL2': '<failed to retrieve the value>',
        'TERRANINFANTRYARMORSLEVEL3': '<failed to retrieve the value>',
        'TERRANINFANTRYWEAPONSLEVEL1': '<failed to retrieve the value>',
        'TERRANINFANTRYWEAPONSLEVEL2': '<failed to retrieve the value>',
        'TERRANINFANTRYWEAPONSLEVEL3': '<failed to retrieve the value>',
        'TERRANSHIPWEAPONSLEVEL1': '<failed to retrieve the value>',
        'TERRANSHIPWEAPONSLEVEL2': '<failed to retrieve the value>',
        'TERRANSHIPWEAPONSLEVEL3': '<failed to retrieve the value>',
        'TERRANVEHICLEANDSHIPARMORSLEVEL1': '<failed to retrieve the value>',
        'TERRANVEHICLEANDSHIPARMORSLEVEL2': '<failed to retrieve the value>',
        'TERRANVEHICLEANDSHIPARMORSLEVEL3': '<failed to retrieve the value>',
        'TERRANVEHICLEWEAPONSLEVEL1': '<failed to retrieve the value>',
        'TERRANVEHICLEWEAPONSLEVEL2': '<failed to retrieve the value>',
        'TERRANVEHICLEWEAPONSLEVEL3': '<failed to retrieve the value>',
        'TUNNELINGCLAWS': '<failed to retrieve the value>',
        'WARPGATERESEARCH': '<failed to retrieve the value>',
        'ZERGFLYERARMORSLEVEL1': '<failed to retrieve the value>',
        'ZERGFLYERARMORSLEVEL2': '<failed to retrieve the value>',
        'ZERGFLYERARMORSLEVEL3': '<failed to retrieve the value>',
        'ZERGFLYERWEAPONSLEVEL1': '<failed to retrieve the value>',
        'ZERGFLYERWEAPONSLEVEL2': '<failed to retrieve the value>',
        'ZERGFLYERWEAPONSLEVEL3': '<failed to retrieve the value>',
        'ZERGGROUNDARMORSLEVEL1': '<failed to retrieve the value>',
        'ZERGGROUNDARMORSLEVEL2': '<failed to retrieve the value>',
        'ZERGGROUNDARMORSLEVEL3': '<failed to retrieve the value>',
        'ZERGLINGATTACKSPEED': '<failed to retrieve the value>',
        'ZERGLINGMOVEMENTSPEED': '<failed to retrieve the value>',
        'ZERGMELEEWEAPONSLEVEL1': '<failed to retrieve the value>',
        'ZERGMELEEWEAPONSLEVEL2': '<failed to retrieve the value>',
        'ZERGMELEEWEAPONSLEVEL3': '<failed to retrieve the value>',
        'ZERGMISSILEWEAPONSLEVEL1': '<failed to retrieve the value>',
        'ZERGMISSILEWEAPONSLEVEL2': '<failed to retrieve the value>',
        'ZERGMISSILEWEAPONSLEVEL3': '<failed to retrieve the value>',
    }


# variables with complex values

__loader__ = None  # (!) real value is ''

__spec__ = None  # (!) real value is ''

