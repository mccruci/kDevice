from .kinsei import *


class CoordPersona(object):
    """
    modelle per le coordinate
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Device(CoordPersona):
    def __init__(self,ip,listaCoord):
        pass

class Area(object):
    ipDevice = ''
    lCoodPer = ''

    def setLCoodPer(self,listaOfDict):
        """
        :param listaOfDict: [{x:'',y:''}]
        :return:
        """
        self.numero = len(listaOfDict)
        pass




class Kinsei(object):
    """
    questa classe si occupa di eseguire la connessione con i device e aggiornare il db
    inoltra i dati della posizione
    coordinatePersona-->Device
    apro una connessione verso molti client con un dato ip, mia arrivano da ogni singolo ip le coordinata X,Y di ogni singola persona

    """

    pass
