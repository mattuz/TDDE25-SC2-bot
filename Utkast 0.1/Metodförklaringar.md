TDDE25: StarCraft II AI Bot

    Tänker att vi kan antecka förklaringar eller förenklingar för vissa av IDAbots 
    klasser och metoder här! 
    
    Vissa av IDAbots metoder är lite komplicerade att använda och kräver (tydligen) 
    att objekt omvandlas till en annan typ av objekt för att metoden i klassen ska 
    kunna användas! 



.Unit och .UnitType

    Om man itererar över listan IDAbot.get_my_units() för
    att kolla om en enhet i listan är en arbetare (TERRAN_SCV) med hjälp av medtoden
    .UnitType.is_worker måste .Unit klassen först omvandlas till .UnitType innan
    .UnitType.is_worker kan köras på den valda enheten. Superflummigt, men i kod
    ser det ut typ såhär:
    
    def is_worker(self):
        for unit in self.get_my_units():
            if unit.unit_type.is_worker: -> bool
                print("Enheten är en arbetare")
    
    där (self) är klassen som metoden körs ifrån.
    
    Något nerkokat kan man se det som att .Unit hanterar enhetens handlingar som 
    exempelvis förflyttning och realtime-status såsom position eller HP medans 
    .UnitType hanterar enhetens konstanta egenskaper såsom dess typ eller hur 
    mycket enheten kostar att träna


    
.UNIT_TYPEID

    klassen .UNIT_TYPEID hanterar namnet på enheten. I metoden session_info()
    i klassen Bot finns exempelvis uttrycket
    
        mapdraw ... gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_SCV])
    
    Som samlar in data från dictionaryn där alla enheter har sparats under 
    respektive namn (UNIT_TYPEID)
    
    UNIT_TYPEID.[enhet] är i sig varken en .Unit eller en .UnitType, men det
    går att omvandla en UNIT_TYPEID enhet till en .UnitType genom att passera
    det som ett argument genom klassen .UnitType! Ex från metoden make_workers():
    
        TERRAN_SCV = UnitType(UNIT_TYPEID.TERRAN_SCV, self)

    TERRAN_SCV kan nu passeras som argument för olika metoder, exempelvis i 
    .Unit. Ex från metoden make_workers():
    
        TERRAN_SCV = UnitType(UNIT_TYPEID.TERRAN_SCV, self)
        
        for base in gamestate.AGENTUNITS[UNIT_TYPEID.TERRAN_COMMANDCENTER]:
            ........
            .......
            base.train(TERRAN_SCV)

    där 'base' är .Unit = .TERRAN_COMMANDCENTER







