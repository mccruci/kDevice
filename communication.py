#!/usr/bin/python3

"""communication.py: basic example of connecting to a Kinsei system for people tracking"""

import sys
import os
import re

#absolutePath = os.path.abspath(__file__)
#processRoot = os.path.dirname(absolutePath)
#os.chdir(processRoot)
#sys.path.insert(0, '../../libs')
from .KinseiClient import KinseiSocket as KinseiClient
from .KinseiTuner import *
from cod.ihg.xetal.models import Sito

#from recordPeople import *  #ADD
import time #ADD

__author__ = "Francesco Pessolano"
__copyright__ = "Copyright 2017, Xetal nv"
__license__ = "MIT"
__version__ = "2.0.2"
__maintainer__ = "Francesco Pessolano"
__email__ = "francesco@xetal.eu"
__status__ = "release"
__requiredtrackingserver__ = "february2017 or later"


# Set to false with trackingservers older than july2017
FWB4july2017 = True

def is_valid_ip(ip):
    m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))


def start():
    # create a socket connection to the device
    #################################### START ADD ###########################
    oldTime = 0
    positionOld = 0
    #################################### END ADD #############################

    ipDevice = input("Please enter the device IP: ")

    if is_valid_ip(ipDevice):
        demoKit = KinseiClient.KinseiSocket(ipDevice)

        if FWB4july2017 and demoKit.checkIfOnline():
            demoKitTuning = KinseiTuner(ipDevice)
            print("\nCurrent settings of the Kinsei system are:\n")
            print("Background Alfa:", demoKitTuning.execGet(getCommand["backgroundAlfa"]))
            print("Background Threshold:", demoKitTuning.execGet(getCommand["backgroundThreshold"]))
            print("Temperature Threshold:", demoKitTuning.execGet(getCommand["temperatureThreshold"]))
            print("Fusion Background Threshold:", demoKitTuning.execGet(getCommand["fusionBackgroundThreshold"]))
            print("Fusion Consensum Factor:", demoKitTuning.execGet(getCommand["fusionConsensumFactor"]))
            print("Fusion Threshold:", demoKitTuning.execGet(getCommand["fusionThreshold"]))
            input("\nPress Enter to continue...")

        # check if the system is online before asking data
        if demoKit.checkIfOnline():
            # get room bounding box dimensions
            dimensions = demoKit.getRoomSize()
            if dimensions:
                print("\nThe Kinsei system is online. \nRoom size is " + str(dimensions[0]) + "mm by " + str(
                    dimensions[1]) + "mm.\n")
                print("Starting persons tracking")
                while True:
                    # get position data
                    positionData = demoKit.getPersonsPositions(False)
                    if positionData:
                        print("Coordinates of present persons ")
                        print("\t\t", positionData)
                    # get the number of people in float mode
                    positionData = demoKit.getNumberPersonsFloat()
                    if positionData:
                        print("Number of detected people is " + str(positionData) + "\n")
                        #################################### START ADD ###########################
                        #create positionOld = 0
                        #create oldTime = 0
                        newTime = time.time()  
                        if posizionData != positionOLD: 
                            insertNewPersona(positionData, newTime) 
                            if oldTime != 0 :  #non sono nella condizione iniziale
                                updateTimeStamp(newTime,oldTime)
                            positionOld = positionData 
                            oldTime = newTime                
                        #################################### END ADD #############################
            else:
                print("There has been an error in communicating with the Kinsei system")
        else:
            print("\nERROR: The Kinsei system has not been found")

    else:
        print("The provided IP", ipDevice, "is not valid")


if __name__ == "__main__": start()
