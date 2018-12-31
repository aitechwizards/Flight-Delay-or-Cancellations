# import os
# os.environ["PROJ_LIB"] = "C:\\Users\\S727953\\AppData\\Local\\Continuum\\anaconda3\\share\\proj\\"; #fixr
#
# import datetime, warnings, scipy
# import pandas as pd
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# from matplotlib.patches import ConnectionPatch
# from collections import OrderedDict
# from matplotlib.gridspec import GridSpec
# from mpl_toolkits.basemap import Basemap
# from sklearn import metrics, linear_model
# from sklearn.preprocessing import PolynomialFeatures, StandardScaler
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
# from scipy.optimize import curve_fit
# plt.rcParams["patch.force_edgecolor"] = True
# plt.style.use('fivethirtyeight')
# mpl.rc('patch', edgecolor = 'dimgray', linewidth=1)
# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "last_expr"
# pd.options.display.max_columns = 50
# warnings.filterwarnings("ignore")
#
#
# class GraphUtils:
#     #    def __init__(self):
#     #        pass
#     #
#     #    def load_csvs(self):
#     """
#     This is loading for Data File
#     :rtype: DataFrame
#     """
#
#
# dfFlight = pd.read_csv('../data/flights.csv', nrows=1000, low_memory=False)
# dfFlights_shape = dfFlight.shape
# temp_info1 = pd.DataFrame(dfFlight.dtypes).T.rename(index={0: 'TYPE'})
# print(temp_info1)
# temp_info2 = pd.DataFrame(dfFlight.isna().sum()).T.rename(index={0: 'Null Column'})
# print(temp_info2)
# temp_null_per = pd.DataFrame((dfFlight.isna().sum() / dfFlights_shape[0]) * 100).T.rename(index={0: 'Null %'})
# print(temp_null_per)
#
# temp_info1 = temp_info1.append(temp_info2)
# temp_null_per = temp_info1.append(temp_null_per)
# temp_null_per = temp_null_per.T
#
# dfAirport = pd.read_csv('../data/airports.csv', low_memory=False)
#
# airport_count = dfFlight['ORIGIN_AIRPORT'].value_counts()
#
# plt.figure(figsize=(11, 11))
# colors = ['Yellow', 'red', 'lightblue', 'purple', 'green', 'orange']
# limit_size = [1, 100, 1000, 10000, 100000, 1000000]
# labels = []
# for l in range(len(limit_size) - 1):
#     labels.append("{}<.<{}".format(limit_size[l]), limit_size[l + 1])
#
# map = Basemap(resolution='i', llcrnrlon=-180, urcrnrlon=-50,
#               llcrnrlat=10, urcrnrlat=75, lat_0=0, lon_0=0, )
# map.shadedrelief()
# map.drawcoastlines()
# map.drawcountries(linewidth=3)
# map.drawstates(color='0.3')
#
# # if __name__ == '__main__':
# #    ut = DataUtils()
# #    ut.load_csvs()


from datetime import datetime
import time

fmt = '%Y-%m-%d %H:%M:%S'
d1 = datetime.strptime('2010-01-01 17:31:22', fmt)
d2 = datetime.strptime('2010-01-03 20:15:14', fmt)

# Convert to Unix timestamp
d1_ts = time.mktime(d1.timetuple())
d2_ts = time.mktime(d2.timetuple())

# They are now in seconds, subtract and then divide by 60 to get minutes.
print(nt(d2_ts-d1_ts) / 60