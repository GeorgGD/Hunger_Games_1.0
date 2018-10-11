from microbit import *
import random

#variabler---------------------------------------------------------------
#Boulin för att få pixeln att blinka

player = True
spawn = True

#Variabler: y and x är koordinater, k = karta, kTuple = karta in tuple form,
#n = spelares index, N = matens index, X = spelaren,

#Animationer



wave = [ Image("00000:"
                "00000:"
                "00100:"
                "00000:"
                "00000"),
                
         Image("00000:"
               "00100:"
               "01410:"
               "00100:"
               "00000"),
                            
        Image("00100:"
              "01410:"
              "14641:"
              "01410:"
              "00100"),
                            
        Image("01410:"
              "14614:"
              "46764:"
              "14641:"
              "01410"),
                            
        Image("14641:"
              "46764:"
              "67676:"
              "46764:"
              "14641"),
                            
        Image("46764:"
              "67676:"
              "76467:"
              "67676:"
              "46764"),
              
        Image("67676:"
              "76467:"
              "64146:"
              "76467:"
              "67676"),
    
        Image("76467:"
              "64146:"
              "41014:"
              "64146:"
              "76467"),
                            
        Image("64146:"
              "41014:"
              "10001:"
              "41014:"
              "64146"),
                            
        Image("41014:"
              "10001:"
              "00000:"
              "10001:"
              "41014"),
                            
        Image("10001:"
              "00000:"
              "00000:"
              "00000:"
              "10001")]

#------------------------------------------------------------------------
#Detta ska spelas BARA vid påslag av Micro:biten
def startScreen():
    sleep (1000)
    display.scroll("Eat Or Die!")
    display.clear()


def blinkandeLjusAn(X, n):
        display.set_pixel(X[0], X[1], 9)
        sleep(250)
        display.set_pixel(X[0], X[1], 0)
        sleep(250)


def karta():
    k = []
    for x in range(0,5):
        for y in range(0,5):
            z = [x, y]
            k.append(z)        
    kTuple = tuple(k)
    return kTuple
    
    
def playerSpawn():
    #Skapar spelaren spawn position
    n = random.randint(0,24)
    X = kTuple[n]
    
    #spawnar spelaren
    display.set_pixel(X[0], X[1], 5)
    return (X, n)


def matSpawn():
    #skapar mat
    domainSet = set()
    while len(domainSet) < 4:
        N = random.randint(0,24)
        K = kTuple[N]
        if K != X:
            d = (K[0], K[1])
            domainSet.add(d)
        #spawnar mat
    domainList = list(domainSet)
        
    for i in range(0,4):
        I = domainList[i]
        display.set_pixel(I[0], I[1], 5)
            
    matResultat = (False, domainList, domainSet)
    return matResultat 
        

def delFood():
    for i in range(0,len(domainList)):
            f = tuple(X)
            if f == domainList[i]:
                del domainList[i]
                break
    return domainList

def noFood():
    domainSet = set()
    all_waves = wave
    display.show(all_waves, delay=70)
    spawn = True
    return (spawn, domainSet)    

startScreen()


#skapar karta
kTuple = karta()


#själva spelet
while player == True:
    if spawn == True:
        #Skapar spelaren spawn position
        (X, n) = playerSpawn()
        (spawn, domainList, domainSet) = matSpawn()
        

    blinkandeLjusAn(X, n)
    
    #Gör så spelaren rör på sig, rad 172-181 kan skrivas i funktion
    if button_a.was_pressed():
        X = [X[0] + 1, X[1]]
    elif button_b.was_pressed():
        X = [X[0], X[1] + 1]
    
    #spawnar spelaren i andra sidan av kartan (kan skrivas i funk. men komm. är bättre!)
    if X[0] > 4:
        X[0] = 0
    elif X[1] > 4:
            X[1] = 0
    
    #Verifierar om spelaren är på samma koord. som det finns mat
    if len(domainList) > 0:
        delFood()
    
    #När maten på kartan är slut
    if domainList == []:
        (spawn, domainSet) = noFood()
        

#Code was written by Georgios Davakos,
#for more projects by Georgios Davakos visit georgiosdavakos.com