import itertools
from heapq import heappush, heappop
from typing import List, Any



heap = []  #Zeitpunkt, Prio, Nr, Funktion
counter = itertools.count()


class Station:
    def __init__(self, Dauer, Liste, bEmpty = 0):
        self.Warteschlange = Liste
        self.bEmpty = bEmpty
        self.Dauer = Dauer

    def isEmpty(self):
        return self.bEmpty

    def add(self, Kunde):
        self.Warteschlange.append(Kunde)
        self.bEmpty = 1;

    def entry(self):
        return 0

    def remove(self, Kunde):
        if(len(self.Warteschlange) == 1):
            self.bEmpty = 0

        return self.Warteschlange.remove(Kunde)

Theken = []
# Theke[0] = Baecker, [1] = kaese, [2] = Wurst, [3] = kasse
Theken.append(Station(10, []))
Theken.append(Station(60, []))
Theken.append(Station(30, []))
Theken.append(Station(5, []))


class Customer:
    def __init__(self, Kundeninformation, Name = ""):
        self.Name = Name
        self.Position = 0
        self.Laufen = Kundeninformation[0]
        self.WarteschlangeMax = Kundeninformation[1]
        self.KaufeAnzahl = Kundeninformation[2]

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

        #alle Kunden auf den heap setzen.
        add_task(0, CustomerT1_1, walk, [0, 2, 1, 3])
        add_task(200, CustomerT1_2, walk, [0, 1, 2, 3])
        add_task(400, CustomerT1_3, walk, [0, 1, 2, 3])
        add_task(600, CustomerT1_4, walk, [0, 1, 2, 3])
        add_task(800, CustomerT1_5, walk, [0, 1, 2, 3])
        add_task(1, CustomerT2_1, walk, [2, 3, 0])
        add_task(61, CustomerT2_2, walk, [0, 1, 2])
        add_task(121, CustomerT2_3, walk, [0, 1, 2])
        add_task(181, CustomerT2_4, walk, [0, 1, 2])
        add_task(241, CustomerT2_5, walk, [0, 1, 2])

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
                print(Kunde.Name ,Zeit, tfunc)
                #setze den kunden wieder auf die heapque
                add_task(Zeit, Kunde, tfunc, order)
                # "debug" pfusch am bau
                #print(Zeit, Kunde, func, num)
            else:
                print(Kunde.Name ,Zeit + tZeit, tZeit, tfunc)

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
def walk(Kundeninfo, order):
    return (Kundeninfo.walk(), entry)

##################################################
#kunde wartet an der station
##################################################
def wait(Kunde, order):
    Theken[order[Kunde.getPosition()]].add(Kunde)
    return (len(Theken[order[Kunde.getPosition()]].Warteschlange) * Theken[order[Kunde.getPosition()]].Dauer, service)

##################################################
#kunde kommt an der sation an
##################################################
def entry(Kunde, order):
    if(Kunde.getWarteschlangeMax() > len(Theken[order[Kunde.getPosition()]].Warteschlange)):
        if(Theken[order[Kunde.getPosition()]].bEmpty == 0):
            #TODO: Kunden in die Warteschlange der Station setzen
             return service(Kunde, order)
        else:
            # TODO: Kunden in die Warteschlange der Station setzen
            return wait(Kunde, order)
    else:
        Kunde.incPosition()
        return walk(Kunde, order)

#####################################################
#kunde ist feritg mit den einkauf
#####################################################
def end():
    print("end")
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
        Kunde.incPosition()
        return tmp, walk


##########################
#Programmstart! supermarkt wird geoefnnet
###########################
a = Supermarkt()
a.start()


