#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
moteur = Motor(Port.D) # Définit la variable du port utilisé par le moteur
scan = ColorSensor(Port.S1) # Définit la variable du port utilisé par le scan
couleur = scan.rgb() # détecte la couleur

while True :
    couleur = scan.rgb() # détecte la couleur
    if couleur[2] > 43 : #Si la couleur est bleu...
        moteur.run(720) # le moteur tourne 

    elif couleur[0] > 43 : # si la couleur est rouge...
        moteur.run(-720) # le moteur tourne mais dans le sens inverse 


    else :
        moteur.stop() #arrête le moteur
    ev3.screen.print(couleur) #affiche le rgb de la couleur
    wait(200) #"veuillez patientez..."
    ev3.screen.clear()