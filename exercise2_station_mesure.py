import numpy as np
from abc import ABC, abstractmethod

class Capteur(ABC):
    __idcapteur = 0


def __init__(self, unite):
    self,unite = unite

    @abstractmethod
    def mesurer(self):
        pass
