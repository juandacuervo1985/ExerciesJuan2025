import pickle
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

import numpy as np


# Classe abstraite Capteur

class Capteur(ABC):
    # Compteur de capteurs pour l'ID automatique, variable de classe
    __id_counter = 1

    # variables d'instances
    __id_capteur: str
    __unite: str

    def __init__(self, unite):
        self.__id_capteur = "ID" + str(Capteur.__id_counter).zfill(3)
        Capteur.__id_counter += 1
        self.__unite = unite

    @property
    def id_capteur(self):
        return self.__id_capteur

    @id_capteur.setter
    def id_capteur(self, value):
        self.__id_capteur = value

    @property
    def unite(self):
        return self.__unite

    @unite.setter
    def unite(self, value):
        self.__unite = value

    @abstractmethod
    def mesurer(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} {self.__id_capteur} qui mesure en {self.__unite}"


# Sous-classe Thermometre

class Thermometre(Capteur):
    def __init__(self):
        super().__init__("°C")

    def mesurer(self):
        return np.random.uniform(-20, 50)


# Sous-classe Barometre

class Barometre(Capteur):
    def __init__(self):
        super().__init__("hPa")

    def mesurer(self):
        return np.random.uniform(950, 1050)


# Sous-classe Luxmetre

class Luxmetre(Capteur):
    def __init__(self):
        super().__init__("lux")

    def mesurer(self):
        return np.random.uniform(0, 100000)


# Classe StationMesure

class StationMesure:
    nom_station: str
    capteurs: List[Capteur]

    def __init__(self, nom_station):
        self.nom_station = nom_station
        self.capteurs = []

    def ajouter_capteur(self, capteur):
        self.capteurs.append(capteur)

    def effectuer_mesures(self):
        resultats = {}
        for capteur in self.capteurs:
            resultats[capteur.id_capteur] = capteur.mesurer()
        return resultats

    def __str__(self):
        desc = "\nStation:" + self.nom_station
        for capteur in self.capteurs:
            desc += "\n" + str(capteur)
        return desc
        # méthode fromDict

    @classmethod
    def from_dict(cls, dict) :
        station = cls(dict["nom_station"])

    for capteur_dict in dict["capteurs"]:
        #recuperer le nom
        class_name = capteur_dict["class_name"]
    capteur_cls = globals().get(class_name)
    if capteur_cls is None:
        raise ValueError(f"Type de capteur inconnu: {class_name}")
    capteur = capteur_cls.


# Programme principal
if __name__ == "__main__":
    station = StationMesure("Limoilou")

    # Ajout des capteurs
    station.ajouter_capteur(Thermometre())
    station.ajouter_capteur(Barometre())
    station.ajouter_capteur(Luxmetre())
    station.ajouter_capteur(Luxmetre())

    # Affichage des descriptions
    print(station)

    # Lancer plusieurs séries de mesures
    for i in range(5):
        print(f"\n----Mesure {i}-----")
        resultats = station.effectuer_mesures()
        for capteur in station.capteurs:
            valeur = resultats[capteur.id_capteur]
            print(
                f"\tMesure de {capteur.__class__.__name__} ({capteur.id_capteur}) : {round(valeur, 2)} {capteur.unite} .")
