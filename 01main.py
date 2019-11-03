import itertools
from heapq import heappush, heappop
from typing import List, Any



heap: List[Any] = []  #Zeitpunkt, Prio, Nr, Funktion
counter = itertools.count()

# Output Text Declare
UserDoc = open('supermarkt_customer.txt', 'w') 
stationDoc = open('supermarkt_station.txt', 'w') 
supermarktDoc = open('supermarkt.txt', 'w') 

# print("Test", file=UserDoc)



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


class User:
    def __init__(self, TypInformation, Name = ""):
        self.Name = Name
        self.Position = -1
        self.Laufen = TypInformation[0]
        self.WarteschlangeMax = TypInformation[1]
        self.KaufeAnzahl: int = TypInformation[2]

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
    A = 200
    B = 60

    #TypInfo: 4xLaufweg, 4xMaxWarteschlabnge, 4xMengeArtikel.
    #Baecker, Kaese, Wurst, Kasse
    TypInfoA = ([10, 30, 45, 60], [11, 11, 6, 21], [10, 5, 3, 30])

    #TypInfo: 3xLaufweg, 3xMaxWarteschlabnge, 3xMengeArtikel.
    #Wurst, Kasse, Baecker
    TypInfoB = ([30, 30, 20], [6, 21, 21], [2, 3, 3])

    def start(self):
        #init 10 Kunden von Typ1 und 30 Kunden von Typ2
        UserA1 = User(self.TypInfoA, "A1")
        UserA1 = User(self.TypInfoB, "A1")
        UserA2 = User(self.TypInfoA, "A2")
        UserA2 = User(self.TypInfoB, "A2")
        UserA3 = User(self.TypInfoA, "A3")
        UserA3 = User(self.TypInfoB, "A3")
        UserA4 = User(self.TypInfoA, "A4")
        UserA4 = User(self.TypInfoB, "A4")
        UserA5 = User(self.TypInfoA, "A5")
        UserA5 = User(self.TypInfoB, "A5")

        UserA6 = User(self.TypInfoA, "A6")
        UserA6 = User(self.TypInfoB, "A6")
        UserA7 = User(self.TypInfoA, "A7")
        UserA7 = User(self.TypInfoB, "A7")
        UserA8 = User(self.TypInfoA, "A8")
        UserA8 = User(self.TypInfoB, "A8")
        UserA9 = User(self.TypInfoA, "A9")
        UserA9 = User(self.TypInfoB, "A9")
        UserA10 = User(self.TypInfoA, "A10")
        UserA10 = User(self.TypInfoB, "A10")

        UserA11 = User(self.TypInfoB, "A11")
        UserA12 = User(self.TypInfoB, "A12")
        UserA13 = User(self.TypInfoB, "A13")
        UserA14 = User(self.TypInfoB, "A14")
        UserA15 = User(self.TypInfoB, "A15")
        UserA16 = User(self.TypInfoB, "A16")
        UserA17 = User(self.TypInfoB, "A17")
        UserA18 = User(self.TypInfoB, "A18")
        UserA19 = User(self.TypInfoB, "A19")
        UserA20 = User(self.TypInfoB, "A20")

        UserA21 = User(self.TypInfoB, "A21")
        UserA22 = User(self.TypInfoB, "A22")
        UserA23 = User(self.TypInfoB, "A23")
        UserA24 = User(self.TypInfoB, "A24")
        UserA25 = User(self.TypInfoB, "A25")
        UserA26 = User(self.TypInfoB, "A26")
        UserA27 = User(self.TypInfoB, "A27")
        UserA28 = User(self.TypInfoB, "A28")
        UserA29 = User(self.TypInfoB, "A29")
        UserA30 = User(self.TypInfoB, "A30")

        #alle Kunden auf den heap setzen.
        add_Task(0, UserA1, walk, [0, 2, 1, 3])
        add_Task(200, UserA2, walk, [0, 2, 1, 3])
        add_Task(400, UserA3, walk, [0, 2, 1, 3])
        add_Task(600, UserA4, walk, [0, 2, 1, 3])
        add_Task(800, UserA5, walk, [0, 2, 1, 3])
        add_Task(1000, UserA6, walk, [0, 2, 1, 3])
        add_Task(1200, UserA7, walk, [0, 2, 1, 3])
        add_Task(1400, UserA8, walk, [0, 2, 1, 3])
        add_Task(1600, UserA9, walk, [0, 2, 1, 3])
        add_Task(1800, UserA10, walk, [0, 2, 1, 3])

        add_Task(1, UserA1, walk, [2, 3, 0])
        add_Task(61, UserA2, walk, [2, 3, 0])
        add_Task(121, UserA3, walk, [2, 3, 0])
        add_Task(181, UserA4, walk, [2, 3, 0])
        add_Task(241, UserA5, walk, [2, 3, 0])
        add_Task(301, UserA6, walk, [2, 3, 0])
        add_Task(361, UserA7, walk, [2, 3, 0])
        add_Task(421, UserA8, walk, [2, 3, 0])
        add_Task(481, UserA9, walk, [2, 3, 0])
        add_Task(541, UserA10, walk, [2, 3, 0])
        add_Task(601, UserA11, walk, [2, 3, 0])
        add_Task(661, UserA12, walk, [2, 3, 0])
        add_Task(721, UserA13, walk, [2, 3, 0])
        add_Task(781, UserA14, walk, [2, 3, 0])
        add_Task(841, UserA15, walk, [2, 3, 0])

        add_Task(901, UserA16, walk, [2, 3, 0])
        add_Task(961, UserA17, walk, [2, 3, 0])
        add_Task(1021, UserA18, walk, [2, 3, 0])
        add_Task(1081, UserA19, walk, [2, 3, 0])
        add_Task(1141, UserA20, walk, [2, 3, 0])
        add_Task(1201, UserA21, walk, [2, 3, 0])
        add_Task(1261, UserA22, walk, [2, 3, 0])
        add_Task(1321, UserA23, walk, [2, 3, 0])
        add_Task(1381, UserA24, walk, [2, 3, 0])
        add_Task(1441, UserA25, walk, [2, 3, 0])
        add_Task(1501, UserA26, walk, [2, 3, 0])
        add_Task(1561, UserA27, walk, [2, 3, 0])
        add_Task(1621, UserA28, walk, [2, 3, 0])
        add_Task(1681, UserA29, walk, [2, 3, 0])
        add_Task(1741, UserA30, walk, [2, 3, 0])

        self.EventHandler()

    def EventHandler(self):
        while(heap):
            #hol den nachsten kunden von der heapqueue
            Zeit, Kunde, func, order, Prio, count = heappop(heap)    #
            #arbeite die aktion des kunden ab(laufen/kaufen/warten)
            tZeit, tfunc = func(Kunde, order)

            #kunde nur in die queue wieder reinsetzten wenn func nicht end ist
            if(tfunc != end):
                #berechne wann der kunde wieder eine aktion ausführen will
                Zeit = Zeit + tZeit
                #print(Kunde.Name ,Zeit, tfunc)
                #setze den kunden wieder auf die heapque
                add_Task(Zeit, Kunde, tfunc, order)
                # "debug" pfusch am bau
                if(tfunc != wait):
                    print(Zeit - tZeit, ":", Kunde.Name, tfunc, Prio, count) #  
            else:# Fertige Kunden
                print(Kunde.Name ,Zeit + tZeit, tZeit, tfunc)
                end(Kunde, order)

        # Statistic Print's after Symulation
        else:
            print("Simulationsende      : " + str(Zeit) + "s", file=supermarktDoc)
    #        print("Kunden               : " + str(AnzahlDerKunden), file=supermarktDoc)
    #        print("Einkäufe             : " + str(), file=supermarktDoc)
    #        print("Mittlere Einkaufszeit: " + str(), file=supermarktDoc)
    #        print("Mittlere Einkaufszeit (vollständig): " + str(), file=supermarktDoc)
    #        print("Drop percentage at Bäcker    : " + str(), file=supermarktDoc)
    #        print("Drop percentage at Metzger   : " + str(), file=supermarktDoc)
    #        print("Drop percentage at Käse      : " + str(), file=supermarktDoc)
    #        print("Drop percentage at Kasse     : " + str(), file=supermarktDoc)

            # Closing Writing Streams from Statistic Documents
            UserDoc.close
            stationDoc.close
            supermarktDoc.close

def add_Task(Zeit, TypInfo, tfunc, order):
    count = next(counter)
    Prio = 3
    if(tfunc == walk):
        Prio = 0
    elif(tfunc == entry):
        Prio = 2
    else:
        Prio = 1
    eantry = [Zeit, Prio, count, TypInfo, tfunc, order]
    #print(TypInfo.Name, tfunc)
    heappush(heap, eantry)

#############################################################
#       funktionen die abgelaufen werden vom kunden         #
#############################################################
#   wenn kunde von station zu station will      #
#################################################
def walk(Kunde, order):
    print(Kunde.Name, " ist mit",  Theken[order[Kunde.getPosition()]].Name, " fertig")
    Theken[order[Kunde.getPosition()]].remove(Kunde)
    Kunde.incPosition()
    return (Kunde.walk(), entry)

#################################################
#   kunde wartet an der station                 #
#################################################
def wait(Kunde, order):
    if(Theken[order[Kunde.getPosition()]].isMyTurn(Kunde.Name)):
        return service(Kunde, order)
    else:
        return (1, wait) #Theken[order[Kunde.getPosition()]].Dauer

#################################################
#   kunde kommt an der sation an                #
#################################################
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

#################################################
#   kunde ist feritg mit den einkauf            #
#################################################
def end(Kunde, order):
    #print("end")
    Theken[order[Kunde.getPosition()]].remove(Kunde)
    return 0

#################################################
#   kunde wird an einer station bedient         #
#################################################
def service(Kunde, order):
    #TODO: Kunde aus der Warteschlange der Station nehmen
    if((Kunde.anzahlDerEinkaeufe() - 1) == Kunde.getPosition()):
        return Theken[order[Kunde.getPosition()]].Dauer * Kunde.KaufeAnzahl[Kunde.getPosition()], end
    else:
        tmp = Theken[order[Kunde.getPosition()]].Dauer * Kunde.KaufeAnzahl[Kunde.getPosition()]
        #print(Kunde.Name, Theken[order[Kunde.getPosition()]].Dauer ,tmp, Theken[order[Kunde.getPosition()]].Name)
        return tmp, walk


#############################################################
#           Programmstart! supermarkt wird geoefnnet        #
#############################################################
a = Supermarkt()
a.start()