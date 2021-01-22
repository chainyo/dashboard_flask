import pandas as pd 
import json

class Incid_csv():

    def __init__(self):
        self.df = pd.read_csv('covid-hospit-incid-reg-2021-01-21-19h20.csv', encoding='latin1', delimiter=';')

    def data_line(self):
        df_line = self.df.copy(deep=True)
        df_line = df_line.drop(labels=['nomReg', 'numReg'], axis=1)
        return df_line

    def data_map(self, date):
        self.df_tab = self.df.loc[self.df['jour']==date]
        self.df_tab = self.df_tab.drop(labels=['jour', 'numReg'], axis=1)
        self.geojson = Geo_data(self.df).rtrn()
        return self.df_tab, self.geojson

class Geo_data():

    def __init__(self, dataframe):
        fr_path = './regions.geojson'
        with open(fr_path) as f:
            self.geo = json.load(f)

        self.found = []
        self.missing = []
        self.region_geo = []

        self.tmp = dataframe.set_index('nomReg')

        for reg in self.geo['features']:
            reg_name = reg['properties']['nom']
            if reg_name in self.tmp.index:
                self.found.append(reg_name)
                self.geometry = reg['geometry']
                self.region_geo.append({'type':'Feature', 'geometry':self.geometry, 'id':reg_name})
            else:
                self.missing.append(reg_name)
        
    def rtrn(self):
        geo_region_ok = {'type':'FeatureCollection', 'features':self.region_geo}

        return geo_region_ok