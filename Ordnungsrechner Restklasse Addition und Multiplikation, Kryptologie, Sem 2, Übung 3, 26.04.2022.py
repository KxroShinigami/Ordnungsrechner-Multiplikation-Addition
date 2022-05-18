#!/usr/bin/env python
# coding: utf-8

# # Willkommen zum Ordnungsrechner 
# ## Der Ordnungsrechner berechnet die Ordnung eines bestimmten Elements in einer Gruppe mit der Multiplikation und/oder Addition als Verknüpfung!


# Initialisierung

modulo = None
element = None
Verknüpfung = None


# Fehlerabfrage und Eingabe

while(type(modulo) != int):
    try:
        print("\nBitte geben Sie eine gültige Ganzzahl ein.")
        modulo = int(input("Modulo n der Restklasse: "))
    except Exception as e:
        print("\nFehlercode: ", e)

while(type(element) != int):
    try:
        print("\nBitte geben Sie eine gültige Ganzzahl ein.")
        element = int(input("Element g, deren Ordnung bestimmt werden muss: "))
    except Exception as e:
        print("\nFehlercode: ", e)

while(Verknüpfung != "+" and Verknüpfung != "*" and Verknüpfung != "Beide"):
    try:
        print("\nBitte geben Sie eine gültige Verknüpfung (+, *, Beide) ein.")
        Verknüpfung = input("Verknüpfung, welche in der Gruppe herrscht: ")
    except Exception as e:
        print("\nFehlercode: ", e)


# ### Multiplikative Verknüpfung:
# ##### Teileranzahl und Teiler von n-1 bestimmen:



if(Verknüpfung == "*" or Verknüpfung == "Beide"):
    
    
    teileranzahl = 0
    teiler = []
    zaehler = 0



if(Verknüpfung == "*" or Verknüpfung == "Beide"):


    for zaehler in range(1, int(((modulo-1)/2)+1)): # Die for-Schleife findet alle echten Teiler von n-1 und die 1
        if((modulo-1)%zaehler == 0):
            teileranzahl = teileranzahl + 1; # Weiterer Teiler wurde gefunden
            teiler.append(zaehler) #Teiler wird zur Teilerliste hinzugefügt
            #print("Teileranzahl: ", teileranzahl)
            #print("Die Teiler sind: ", teiler)

    # Dieser Abschnitt fügt noch den unechten Teiler n-1 zu den Teilern hinzu
    teileranzahl = teileranzahl + 1
    teiler.append((modulo-1))

    print("Teileranzahl: ", teileranzahl)
    print("Die Teiler sind: ", teiler)


# ##### Nun wird nach der Ordnung des Elementes g geschaut:



if(Verknüpfung == "*" or Verknüpfung == "Beide"):


    index = 0
    ordnung = None
    ergebnis = None




if(Verknüpfung == "*" or Verknüpfung == "Beide"):


    for index in range(teileranzahl):
        ergebnis = (element**teiler[index])%modulo
        if(ergebnis == 1):
            ordnung = teiler[index]
            break
            
    if(ordnung == None): # Abfangabfrage, wenn sich die Ordnung des Elements nicht berechnen lässt, da z.b. die Eingabe falsch war oder die Ordnung nicht errechenbar ist in dem Körper
        print("Bei der Berechnung der Ordnung ist entweder ein Fehler unterlaufen oder es kann keine Ordnung für dieses Element in dem Körper mit einer multiplikativen Verknüpfung berechnet werden. Überprüfen Sie ihre Eingabe oder kontaktieren Sie den Hersteller")
    else:
        print("Die Ordnung des Elements ", element, " in der Restklasse ", modulo, " ist: ", ordnung)


# ### Additive Verknüpfung:



if(Verknüpfung == "+" or Verknüpfung == "Beide"):


    ordnung = None
    ergebnis = None



if(Verknüpfung == "+" or Verknüpfung == "Beide"):


    for ordnung in range(1, modulo):
        ergebnis = (element*ordnung)%modulo
        if(ergebnis == 0):
            #print(ordnung)
            break


    if(ordnung == None): # Abfangabfrage, wenn sich die Ordnung des Elements nicht berechnen lässt, da z.b. die Eingabe falsch war oder die Ordnung nicht errechenbar ist in dem Körper
        print("Bei der Berechnung der Ordnung ist entweder ein Fehler unterlaufen oder es kann keine Ordnung für dieses Element in dem Körper mit einer multiplikativen Verknüpfung berechnet werden. Überprüfen Sie ihre Eingabe oder kontaktieren Sie den Ersteller")
    elif(ergebnis != 0):
        print("Das Element ", element, " in der Restklasse ", modulo, " hat keine Ordnung")
    else:
        print("Die Ordnung des Elements ", element, " in der Restklasse ", modulo, " ist: ", ordnung)