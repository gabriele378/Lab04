from cabine import Cabine
from passeggeri import Passeggeri
from cabine_animali import Animali
from cabine_deluxe import Deluxe
import csv

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.passeggeri = []
        self.cabine = []
        self.animali = []
        self.deluxe = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nuovo_nome):
        self.nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                for line in csv_reader:
                    if len(line) == 3:
                        codice = line[0]
                        nome = line[1]
                        cognome = line[2]
                        passeggero = Passeggeri(codice, nome, cognome)
                        self.passeggeri.append(passeggero)

                    elif len(line) == 4:
                        codice = line[0]
                        letti = line[1]
                        ponte = line[2]
                        prezzo = line[3]
                        cabina = Cabine(codice, letti, ponte, prezzo)
                        self.cabine.append(cabina)

                    elif len(line) == 5 and line[-1] == int:
                        codice = line[0]
                        letti = line[1]
                        ponte = line[2]
                        prezzo = line[3]
                        max_animali = line[4]
                        cabine_animali = Animali(codice, letti, ponte, prezzo, max_animali)
                        self.animali.append(cabine_animali)

                    else:
                        codice = line[0]
                        letti = line[1]
                        ponte = line[2]
                        prezzo = line[3]
                        tipologia = line[4]
                        cabine_deluxe = Deluxe(codice, letti, ponte, prezzo, tipologia)
                        self.deluxe.append(cabine_deluxe)








    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

