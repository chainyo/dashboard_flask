import numpy as np
import pandas as pd

class Data:
    data = pd.read_csv('covid-hospit-incid-reg-2021-01-21-19h20.csv', delimiter=';', encoding='latin1')
    lst_reg = {94 : 'fr-cor', 53: 'fr-bre', 52:'fr-pdl', 93:'fr-pac', 76:'fr-occ', 75:'fr-naq', 27:'fr-bfc', 24:'fr-cvl', 11:'fr-idf' , 32:'fr-hdf', 84:'fr-ara', 44:'fr-ges', 28:'fr-nor', 4:'fr-lre', 6:'fr-may', 3:'fr-gf', 2:'fr-mq', 1:'fr-gua'}
    lst_reg2 = {'Corse' : 'fr-cor', 'Bretagne': 'fr-bre', 'Pays de la Loire':'fr-pdl', "Provence-Alpes-Côte d'Azur":'fr-pac', "Occitanie":'fr-occ', "Nouvelle-Aquitaine":'fr-naq', "Bourgogne-Franche-Comté":'fr-bfc', "Centre-Val de Loire":'fr-cvl', "Ile-de-France":'fr-idf' , "Hauts-de-France":'fr-hdf', "Auvergne-Rhône-Alpes":'fr-ara', "Grand-Est":'fr-ges', "Normandie":'fr-nor', "La Réunion":'fr-lre', "Mayotte":'fr-may', "Guyane":'fr-gf', "Martinique":'fr-mq', "Guadeloupe":'fr-gua'}

    #Recupère les données par region à une date donnée
    def rea_date(self, date_choice):
        data_date = self.data[self.data['jour']==date_choice]
        incid_rea = np.array(data_date['incid_rea'])
        numReg = np.array(data_date['numReg'])
        
        liste = []
        for elem in self.lst_reg.items():
            for x, y in zip(incid_rea, numReg):
                if elem[0]==y:
                    liste.append([elem[1], x])

        return liste

    #Recupère la valeur min, max et moyenne de réanimation par jours
    def get_data_area_graph(self):

        liste_date = np.unique(self.data['jour'])
        liste_data = []

        for date in liste_date:
            data = self.data[self.data['jour']==date]
            data_min = min(np.array(data['incid_rea']))
            data_max = max(np.array(data['incid_rea']))
            data_moy = round(np.mean(np.array(data['incid_rea'])), 0)
            liste_data.append([data_min, data_moy, data_max])

        liste_ranges = []
        liste_averages = []

        for data, date in zip(liste_data, liste_date):
            liste_ranges.append([date, data[0], data[2]])
            liste_averages.append([date, round(data[1], 2)])

        return liste_ranges, liste_averages

    #Compte et classe les regions selon le nombre de réanimations
    def get_data_column_bar(self):
        incid_rea = np.array(self.data['incid_rea'])
        nomReg = np.array(self.data['nomReg'])
        classement = {}
        for elem in self.lst_reg2.items():
            classement[elem[0]] = 0
            for x, y in zip(incid_rea, nomReg):
                if elem[0]==y:
                    classement[elem[0]] += x 
        classement = {k: v for k, v in sorted(classement.items(), key=lambda item: item[1], reverse=True)}   
        liste = []
        for elem in classement.items():
            liste.append([elem[0], elem[1]])
        return liste



test = Data().get_data_column_bar()