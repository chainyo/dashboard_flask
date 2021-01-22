import json
import plotly.express as px
import numpy as np 

from data import Incid_csv

data = Incid_csv()

class Plotly():

    @classmethod
    def graph_line(cls):
        fig = px.line(data.data_line(), x='jour', y='incid_rea')
        return fig

    @classmethod
    def graph_map(cls, lat, long, zm, date):
        df = data.data_map(date)[0]
        geo = data.data_map(date)[1]
        df['count_color'] = df['incid_rea'].apply(np.log10)
        max_log = df['count_color'].max()
        max_val = int(max_log) + 1
        values = [i for i in range(max_val)]
        ticks = [10**i for i in values]

        fig = px.choropleth_mapbox(df, geojson=geo, 
            locations='nomReg', color=df['count_color'], 
            color_continuous_scale='YlOrRd', 
            range_color=(0, df['count_color'].max()), 
            hover_name='nomReg', 
            hover_data={'count_color': False, 'nomReg': False, 'incid_rea': True}, 
            mapbox_style='open-street-map', zoom=zm, 
            center={'lat': lat, 'lon': long}, opacity=0.5)

        fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0}, 
            coloraxis_colorbar={'title':'Taux d\'incidence', 'tickvals':values, 'ticktext':ticks})

        return fig

#Plotly.graph_line()
# Métropole
Plotly.graph_map(47, 3, 4.2, '2021-01-21')
# Guyane
#Plotly.graph_map(4, -53, 6.4, '2021-01-21')
# Guadeloupe
#Plotly.graph_map(16.2, -61.5, 8.5, '2021-01-21')
# Mayotte
#Plotly.graph_map(-12.8, 45.1, 9, '2021-01-21')