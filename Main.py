import itertools
from heapq import heappush, heappop
from typing import List, Any



heap: List[Any] = []  #Zeitpunkt, Prio, Nr, Funktion
counter = itertools.count()


class Station:

    def __init__(self, Dauer, Liste, bEmpty = 0):
        self.Warteschlange: List[Any] = Liste
        self.bEmpty = bEmpty
        self.Dauer: int = Dauer

    def isEmpty(self):
        return self.bEmpty

    def add(self, Kunde):
        self.bEmpty = 1;
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
Theken.append(Station(10, []))
Theken.append(Station(60, []))
Theken.append(Station(30, []))
Theken.append(Station(5, []))


class Customer:
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
    KundeninfoTypEins = ([10, 30, 45, 60], [10, 10, 5, 20], [10, 5, 3, 30])

    #Kundeninfo: 3xLaufweg, 3xMaxWarteschlabnge, 3xMengeArtikel.
    #Wurst, Kasse, Baecker
    KundeninfoTypZwei = ([30, 30, 20], [5, 20, 20], [2, 3, 3])

    def start(self):
        #init 5 Kunden von Typ1 und 5 Kunden von Typ2
        CustomerT1_1 = Customer(self.KundeninfoTypEins, "T1_1")
        CustomerT2_1 = Customer(self.KundeninfoTypZwei, "T2_1")
        CustomerT1_2 = Customer(self.KundeninfoTypEins, "T1_2")
        CustomerT2_2 = Customer(self.KundeninfoTypZwei, "T2_2")
        CustomerT1_3 = Customer(self.KundeninfoTypEins, "T1_3")
        CustomerT2_3 = Customer(self.KundeninfoTypZwei, "T2_3")
        CustomerT1_4 = Customer(self.KundeninfoTypEins, "T1_4")
        CustomerT2_4 = Customer(self.KundeninfoTypZwei, "T2_4")
        CustomerT1_5 = Customer(self.KundeninfoTypEins, "T1_5")
        CustomerT2_5 = Customer(self.KundeninfoTypZwei, "T2_5")

        CustomerT1_6 = Customer(self.KundeninfoTypEins, "T1_6")
        CustomerT2_6 = Customer(self.KundeninfoTypZwei, "T2_6")
        CustomerT1_7 = Customer(self.KundeninfoTypEins, "T1_7")
        CustomerT2_7 = Customer(self.KundeninfoTypZwei, "T2_7")
        CustomerT1_8 = Customer(self.KundeninfoTypEins, "T1_8")
        CustomerT2_8 = Customer(self.KundeninfoTypZwei, "T2_8")
        CustomerT1_9 = Customer(self.KundeninfoTypEins, "T1_9")
        CustomerT2_9 = Customer(self.KundeninfoTypZwei, "T2_9")
        CustomerT1_10 = Customer(self.KundeninfoTypEins, "T1_10")
        CustomerT2_10 = Customer(self.KundeninfoTypZwei, "T2_10")

        CustomerT2_11 = Customer(self.KundeninfoTypZwei, "T2_11")
        CustomerT2_12 = Customer(self.KundeninfoTypZwei, "T2_12")
        CustomerT2_13 = Customer(self.KundeninfoTypZwei, "T2_13")
        CustomerT2_14 = Customer(self.KundeninfoTypZwei, "T2_14")
        CustomerT2_15 = Customer(self.KundeninfoTypZwei, "T2_15")
        CustomerT2_16 = Customer(self.KundeninfoTypZwei, "T2_16")
        CustomerT2_17 = Customer(self.KundeninfoTypZwei, "T2_17")
        CustomerT2_18 = Customer(self.KundeninfoTypZwei, "T2_18")
        CustomerT2_19 = Customer(self.KundeninfoTypZwei, "T2_19")
        CustomerT2_20 = Customer(self.KundeninfoTypZwei, "T2_20")

        CustomerT2_21 = Customer(self.KundeninfoTypZwei, "T2_21")
        CustomerT2_22 = Customer(self.KundeninfoTypZwei, "T2_22")
        CustomerT2_23 = Customer(self.KundeninfoTypZwei, "T2_23")
        CustomerT2_24 = Customer(self.KundeninfoTypZwei, "T2_24")
        CustomerT2_25 = Customer(self.KundeninfoTypZwei, "T2_25")
        CustomerT2_26 = Customer(self.KundeninfoTypZwei, "T2_26")
        CustomerT2_27 = Customer(self.KundeninfoTypZwei, "T2_27")
        CustomerT2_28 = Customer(self.KundeninfoTypZwei, "T2_28")
        CustomerT2_29 = Customer(self.KundeninfoTypZwei, "T2_29")
        CustomerT2_30 = Customer(self.KundeninfoTypZwei, "T2_30")

        #alle Kunden auf den heap setzen.
        add_task(0, CustomerT1_1, walk, [0, 2, 1, 3])
        add_task(200, CustomerT1_2, walk, [0, 2, 1, 3])
        add_task(400, CustomerT1_3, walk, [0, 2, 1, 3])
        add_task(600, CustomerT1_4, walk, [0, 2, 1, 3])
        add_task(800, CustomerT1_5, walk, [0, 2, 1, 3])
        add_task(1000, CustomerT1_6, walk, [0, 2, 1, 3])
        add_task(1200, CustomerT1_7, walk, [0, 2, 1, 3])
        add_task(1400, CustomerT1_8, walk, [0, 2, 1, 3])
        add_task(1600, CustomerT1_9, walk, [0, 2, 1, 3])
        add_task(1800, CustomerT1_10, walk, [0, 2, 1, 3])

        add_task(1, CustomerT2_1, walk, [2, 3, 0])
        add_task(61, CustomerT2_2, walk, [2, 3, 0])
        add_task(121, CustomerT2_3, walk, [2, 3, 0])
        add_task(181, CustomerT2_4, walk, [2, 3, 0])
        add_task(241, CustomerT2_5, walk, [2, 3, 0])
        add_task(301, CustomerT2_6, walk, [2, 3, 0])
        add_task(361, CustomerT2_7, walk, [2, 3, 0])
        add_task(421, CustomerT2_8, walk, [2, 3, 0])
        add_task(481, CustomerT2_9, walk, [2, 3, 0])
        add_task(541, CustomerT2_10, walk, [2, 3, 0])
        add_task(601, CustomerT2_11, walk, [2, 3, 0])
        add_task(661, CustomerT2_12, walk, [2, 3, 0])
        add_task(721, CustomerT2_13, walk, [2, 3, 0])
        add_task(781, CustomerT2_14, walk, [2, 3, 0])
        add_task(841, CustomerT2_15, walk, [2, 3, 0])

        add_task(901, CustomerT2_16, walk, [2, 3, 0])
        add_task(961, CustomerT2_17, walk, [2, 3, 0])
        add_task(1021, CustomerT2_18, walk, [2, 3, 0])
        add_task(1081, CustomerT2_19, walk, [2, 3, 0])
        add_task(1141, CustomerT2_20, walk, [2, 3, 0])
        add_task(1201, CustomerT2_21, walk, [2, 3, 0])
        add_task(1261, CustomerT2_22, walk, [2, 3, 0])
        add_task(1321, CustomerT2_23, walk, [2, 3, 0])
        add_task(1381, CustomerT2_24, walk, [2, 3, 0])
        add_task(1441, CustomerT2_25, walk, [2, 3, 0])
        add_task(1501, CustomerT2_26, walk, [2, 3, 0])
        add_task(1561, CustomerT2_27, walk, [2, 3, 0])
        add_task(1621, CustomerT2_28, walk, [2, 3, 0])
        add_task(1681, CustomerT2_29, walk, [2, 3, 0])
        add_task(1741, CustomerT2_30, walk, [2, 3, 0])

        self.EventHandler()

    def EventHandler(self):
        while(heap):
            #hol den nachsten kunden von der heapqueue
            Zeit, count, Kunde, func, order = heappop(heap)
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
                #print(Zeit, Kunde, func, num)
            else:
                print(Kunde.Name ,Zeit + tZeit, tZeit, tfunc)
                end(Kunde, order)

def add_task(Zeit, Kundeninfo, tfunc, order):
    count = next(counter)
    entry = [Zeit, count, Kundeninfo, tfunc, order]
    #print(Kundeninfo.Name, tfunc)
    heappush(heap, entry)

##################################################
#funktionen die abgelaufen werden vom kunden
##################################################
##################################################
#wenn kunde von station zu station will
##################################################
def walk(Kunde, order):
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
        return (Theken[order[Kunde.getPosition()]].Dauer, wait)

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
        print("Warteschlange voll",Kunde.getPosition())
        return walk(Kunde, order)

#####################################################
#kunde ist feritg mit den einkauf
#####################################################
def end(Kunde, order):
    print("end")
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
        print(Kunde.Name, tmp)
        return tmp, walk


##########################
#Programmstart! supermarkt wird geoefnnet
###########################
a = Supermarkt()
a.start()


