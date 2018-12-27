import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os
os.environ["PROJ_LIB"] = "C:\\Users\\S727953\\AppData\\Local\Continuum\\anaconda3\\envs\\AI_MLND\\share"; #fixr


class GraphUtils:
    #    def __init__(self):
    #        pass
    #
    #    def load_csvs(self):
    """
    This is loading for Data File
    :rtype: DataFrame
    """


dfFlight = pd.read_csv('../data/flights.csv', nrows=1000, low_memory=False)
dfFlights_shape = dfFlight.shape
temp_info1 = pd.DataFrame(dfFlight.dtypes).T.rename(index={0: 'TYPE'})
print(temp_info1)
temp_info2 = pd.DataFrame(dfFlight.isna().sum()).T.rename(index={0: 'Null Column'})
print(temp_info2)
temp_null_per = pd.DataFrame((dfFlight.isna().sum() / dfFlights_shape[0]) * 100).T.rename(index={0: 'Null %'})
print(temp_null_per)

temp_info1 = temp_info1.append(temp_info2)
temp_null_per = temp_info1.append(temp_null_per)
temp_null_per = temp_null_per.T

dfAirport = pd.read_csv('../data/airports.csv', low_memory=False)

airport_count = dfFlight['ORIGIN_AIRPORT'].value_counts()

plt.figure(figsize=(11, 11))
colors = ['Yellow', 'red', 'lightblue', 'purple', 'green', 'orange']
limit_size = [1, 100, 1000, 10000, 100000, 1000000]
labels = []
for l in range(len(limit_size) - 1):
    labels.append("{}<.<{}".format(limit_size[l]), limit_size[l + 1])

map = Basemap(resolution='i', llcrnrlon=-180, urcrnrlon=-50,
              llcrnrlat=10, urcrnrlat=75, lat_0=0, lon_0=0, )
map.shadedrelief()
map.drawcoastlines()
map.drawcountries(linewidth=3)
map.drawstates(color='0.3')

# if __name__ == '__main__':
#    ut = DataUtils()
#    ut.load_csvs()
