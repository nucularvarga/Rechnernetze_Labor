import itertools
from heapq import heappush, heappop
from typing import List, Any



heap: List[Any] = []  #Zeitpunkt, Prio, Nr, Funktion
counter = itertools.count()

# Output Text Declare
CustomerDoc = open('supermarkt_Customer.txt', 'w') 
stationDoc = open('supermarkt_station.txt', 'w') 
supermarktDoc = open('supermarkt.txt', 'w') 

# print("Test", file=CustomerDoc)



class Station:

    def __init__(self, Dauer, Liste, name="leer", bEmpty = 0):
        self.Warteschlange: List[Any] = Liste
        self.Name = name
        self.bEmpty = bEmpty
        self.Dauer: int = Dauer

    def isEmpty(self):
        return self.bEmpty

    def add(self, Kunde):
        self.bEmpty = 1
        self.Warteschlange.append(Kunde.Name)


    def isMyTurn(self, Kundename):
        if(self.Warteschlange[0] == Kundename):
            return True
        return False

    def remove(self, Kunde):
        if(len(self.Warteschlange) == 1 and self.Warteschlange.count(Kunde.Name) > 0):
            self.bEmpty = 0
            self.Warteschlange.remove(Kunde.Name)
        elif(len(self.Warteschlange) > 1 and self.Warteschlange.count(Kunde.Name) > 0):
            self.Warteschlange.remove(Kunde.Name)

Theken = []
# Theke[0] = Baecker, [1] = kaese, [2] = Wurst, [3] = kasse
Theken.append(Station(10, [], "Baecker"))
Theken.append(Station(60, [], "Kaese"))
Theken.append(Station(30, [], "Wurst"))
Theken.append(Station(5, [], "Kasse"))


class Guy:
    def __init__(self, Kundeninformation, Name = ""):
        self.Name = Name
        self.Position = -1
        self.Laufen = Kundeninformation[0]
        self.WarteschlangeMax = Kundeninformation[1]
        self.KaufeAnzahl: int = Kundeninformation[2]

    def anzahlDerEinkaeufe(self):
        return len(self.Laufen)

    def getPosition(self):
        return self.Position

    def incPosition(self):
        self.Position += 1

    def walk(self):
        return self.Laufen[self.Position]

    def getWarteschlangeMax(self):
        if(self.Position < self.anzahlDerEinkaeufe()):
            return self.WarteschlangeMax[self.Position]
        else:
            return -1


class Ordering:
    def __init__(self, ):
        self.Prio = 1
    def __lt__(self, other):
        return True



class Supermarkt:
    AnzahlDerKunden = 0
    Zeit = 0
    T1 = 200
    T2 = 60

    #Kundeninfo: 4xLaufweg, 4xMaxWarteschlabnge, 4xMengeArtikel.
    #Baecker, Kaese, Wurst, Kasse
    KundeninfoTypEins = ([10, 30, 45, 60], [11, 11, 6, 21], [10, 5, 3, 30])

    #Kundeninfo: 3xLaufweg, 3xMaxWarteschlabnge, 3xMengeArtikel.
    #Wurst, Kasse, Baecker
    KundeninfoTypZwei = ([30, 30, 20], [6, 21, 21], [2, 3, 3])

    def start(self):
        #init 5 Kunden von Typ1 und 5 Kunden von Typ2
        GuyA1 = Guy(self.KundeninfoTypEins, "A1")
        GuyB1 = Guy(self.KundeninfoTypZwei, "B1")
        GuyA2 = Guy(self.KundeninfoTypEins, "A2")
        GuyB2 = Guy(self.KundeninfoTypZwei, "B2")
        GuyA3 = Guy(self.KundeninfoTypEins, "A3")
        GuyB3 = Guy(self.KundeninfoTypZwei, "B3")
        GuyA4 = Guy(self.KundeninfoTypEins, "A4")
        GuyB4 = Guy(self.KundeninfoTypZwei, "B4")
        GuyA5 = Guy(self.KundeninfoTypEins, "A5")
        GuyB5 = Guy(self.KundeninfoTypZwei, "B5")

        GuyA6 = Guy(self.KundeninfoTypEins, "A6")
        GuyB6 = Guy(self.KundeninfoTypZwei, "B6")
        GuyA7 = Guy(self.KundeninfoTypEins, "A7")
        GuyB7 = Guy(self.KundeninfoTypZwei, "B7")
        GuyA8 = Guy(self.KundeninfoTypEins, "A8")
        GuyB8 = Guy(self.KundeninfoTypZwei, "B8")
        GuyA9 = Guy(self.KundeninfoTypEins, "A9")
        GuyB9 = Guy(self.KundeninfoTypZwei, "B9")
        GuyA10 = Guy(self.KundeninfoTypEins, "A10")
        GuyB10 = Guy(self.KundeninfoTypZwei, "B10")

        GuyB11 = Guy(self.KundeninfoTypZwei, "B11")
        GuyB12 = Guy(self.KundeninfoTypZwei, "B12")
        GuyB13 = Guy(self.KundeninfoTypZwei, "B13")
        GuyB14 = Guy(self.KundeninfoTypZwei, "B14")
        GuyB15 = Guy(self.KundeninfoTypZwei, "B15")
        GuyB16 = Guy(self.KundeninfoTypZwei, "B16")
        GuyB17 = Guy(self.KundeninfoTypZwei, "B17")
        GuyB18 = Guy(self.KundeninfoTypZwei, "B18")
        GuyB19 = Guy(self.KundeninfoTypZwei, "B19")
        GuyB20 = Guy(self.KundeninfoTypZwei, "B20")

        GuyB21 = Guy(self.KundeninfoTypZwei, "B21")
        GuyB22 = Guy(self.KundeninfoTypZwei, "B22")
        GuyB23 = Guy(self.KundeninfoTypZwei, "B23")
        GuyB24 = Guy(self.KundeninfoTypZwei, "B24")
        GuyB25 = Guy(self.KundeninfoTypZwei, "B25")
        GuyB26 = Guy(self.KundeninfoTypZwei, "B26")
        GuyB27 = Guy(self.KundeninfoTypZwei, "B27")
        GuyB28 = Guy(self.KundeninfoTypZwei, "B28")
        GuyB29 = Guy(self.KundeninfoTypZwei, "B29")
        GuyB30 = Guy(self.KundeninfoTypZwei, "B30")

        #alle Kunden auf den heap setzen.
        add_task(0, GuyA1, walk, [0, 2, 1, 3])
        add_task(200, GuyA2, walk, [0, 2, 1, 3])
        add_task(400, GuyA3, walk, [0, 2, 1, 3])
        add_task(600, GuyA4, walk, [0, 2, 1, 3])
        add_task(800, GuyA5, walk, [0, 2, 1, 3])
        add_task(1000, GuyA6, walk, [0, 2, 1, 3])
        add_task(1200, GuyA7, walk, [0, 2, 1, 3])
        add_task(1400, GuyA8, walk, [0, 2, 1, 3])
        add_task(1600, GuyA9, walk, [0, 2, 1, 3])
        add_task(1800, GuyA10, walk, [0, 2, 1, 3])

        add_task(1, GuyB1, walk, [2, 3, 0])
        add_task(61, GuyB2, walk, [2, 3, 0])
        add_task(121, GuyB3, walk, [2, 3, 0])
        add_task(181, GuyB4, walk, [2, 3, 0])
        add_task(241, GuyB5, walk, [2, 3, 0])
        add_task(301, GuyB6, walk, [2, 3, 0])
        add_task(361, GuyB7, walk, [2, 3, 0])
        add_task(421, GuyB8, walk, [2, 3, 0])
        add_task(481, GuyB9, walk, [2, 3, 0])
        add_task(541, GuyB10, walk, [2, 3, 0])
        add_task(601, GuyB11, walk, [2, 3, 0])
        add_task(661, GuyB12, walk, [2, 3, 0])
        add_task(721, GuyB13, walk, [2, 3, 0])
        add_task(781, GuyB14, walk, [2, 3, 0])
        add_task(841, GuyB15, walk, [2, 3, 0])

        add_task(901, GuyB16, walk, [2, 3, 0])
        add_task(961, GuyB17, walk, [2, 3, 0])
        add_task(1021, GuyB18, walk, [2, 3, 0])
        add_task(1081, GuyB19, walk, [2, 3, 0])
        add_task(1141, GuyB20, walk, [2, 3, 0])
        add_task(1201, GuyB21, walk, [2, 3, 0])
        add_task(1261, GuyB22, walk, [2, 3, 0])
        add_task(1321, GuyB23, walk, [2, 3, 0])
        add_task(1381, GuyB24, walk, [2, 3, 0])
        add_task(1441, GuyB25, walk, [2, 3, 0])
        add_task(1501, GuyB26, walk, [2, 3, 0])
        add_task(1561, GuyB27, walk, [2, 3, 0])
        add_task(1621, GuyB28, walk, [2, 3, 0])
        add_task(1681, GuyB29, walk, [2, 3, 0])
        add_task(1741, GuyB30, walk, [2, 3, 0])


        self.EventHandler()

    def EventHandler(self):
        while(heap):
            #hol den nachsten kunden von der heapqueue
            Zeit, Prio, count, Kunde, func, order = heappop(heap)
            #arbeite die aktion des kunden ab(laufen/kaufen/warten)
            tZeit, tfunc = func(Kunde, order)

            #kunde nur in die queue wieder reinsetzten wenn func nicht end ist
            if(tfunc != end):
                #berechne wann der kunde wieder eine aktion ausführen will
                Zeit = Zeit + tZeit
                #print(Kunde.Name ,Zeit, tfunc)
                #setze den kunden wieder auf die heapque
                add_task(Zeit, Kunde, tfunc, order)
                # "debug" pfusch am bau
                if(tfunc != wait):
                    print(Zeit - tZeit, Prio, count,  Kunde.Name, tfunc)
            else:
                print(Kunde.Name ,Zeit + tZeit, tZeit, tfunc)
                end(Kunde, order)

def add_task(Zeit, Kundeninfo, tfunc, order):
    count = next(counter)
    Prio = 3
    if(tfunc == walk):
        Prio = 0
    elif(tfunc == entry):
        Prio = 2
    else:
        Prio = 1
    eantry = [Zeit, Prio, count, Kundeninfo, tfunc, order]
    #print(Kundeninfo.Name, tfunc)
    heappush(heap, eantry)

##################################################
#funktionen die abgelaufen werden vom kunden
##################################################
##################################################
#wenn kunde von station zu station will
##################################################
def walk(Kunde, order):
    print(Kunde.Name, " ist mit",  Theken[order[Kunde.getPosition()]].Name, " fertig")
    Theken[order[Kunde.getPosition()]].remove(Kunde)
    Kunde.incPosition()
    return (Kunde.walk(), entry)

##################################################
#kunde wartet an der station
##################################################
def wait(Kunde, order):
    if(Theken[order[Kunde.getPosition()]].isMyTurn(Kunde.Name)):
        return service(Kunde, order)
    else:
        return (1, wait) #Theken[order[Kunde.getPosition()]].Dauer

##################################################
#kunde kommt an der sation an
##################################################
def entry(Kunde, order):
    if(Kunde.getWarteschlangeMax() > len(Theken[order[Kunde.getPosition()]].Warteschlange)):
        if(Theken[order[Kunde.getPosition()]].bEmpty == 0):
             Theken[order[Kunde.getPosition()]].add(Kunde)
             return service(Kunde, order)
        else:
            Theken[order[Kunde.getPosition()]].add(Kunde)
            return wait(Kunde, order)
    else:
        #Kunde.incPosition()
        print("Warteschlange voll",Kunde.Name, Theken[order[Kunde.getPosition()]].Warteschlange)
        return walk(Kunde, order)

#####################################################
#kunde ist feritg mit den einkauf
#####################################################
def end(Kunde, order):
    #print("end")
    Theken[order[Kunde.getPosition()]].remove(Kunde)
    return 0

###################################################
#kunde wird an einer station bedient
###################################################
def service(Kunde, order):
    #TODO: Kunde aus der Warteschlange der Station nehmen
    if((Kunde.anzahlDerEinkaeufe() - 1) == Kunde.getPosition()):
        return Theken[order[Kunde.getPosition()]].Dauer * Kunde.KaufeAnzahl[Kunde.getPosition()], end
    else:
        tmp = Theken[order[Kunde.getPosition()]].Dauer * Kunde.KaufeAnzahl[Kunde.getPosition()]
        #print(Kunde.Name, Theken[order[Kunde.getPosition()]].Dauer ,tmp, Theken[order[Kunde.getPosition()]].Name)
        return tmp, walk


##########################
#Programmstart! supermarkt wird geoefnnet
###########################
a = Supermarkt()
a.start()
