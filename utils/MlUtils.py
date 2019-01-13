import pandas as pd
import numpy as np
from datetime import datetime as dt


class MlUtils:

    def __init__(self):
        self.sample_count = 0

    def load_csv(self, fileloc, numRow=None):
        """
        This Method will load the data CSV through pandas
        :rtype: object
        """
        if numRow is None:
            dfFlight = pd.read_csv(fileloc, low_memory=False, encoding='utf-8')
        else:
            dfFlight = pd.read_csv(fileloc, low_memory=False, nrows=numRow, encoding='utf-8')

        self.sample_count = dfFlight.shape[0]
        return pd.read_csv(fileloc, low_memory=False, nrows=numRow)

    def Missing_Count(self, count):
        """
        :rtype: object
        """
        # print(count)
        return (int(count) / self.sample_count) * 100

    def missingPercent(self, dfFlight):
        """
        This Mehtod will return percentage of mising value in respect to perticular feature
        :rtype: object
        """
        t0 = dt.now()
        dfMissing = pd.DataFrame(dfFlight.isnull().sum(axis=0).reset_index())
        #     print(type(dfMissing))
        #     print(dfMissing.columns.T)
        #     print(dfMissing.dtypes)
        dfMissing.columns = ['FEATURE', 'COUNT_OF_MISSING']
        #     print(type(dfMissing))
        #     print(dfMissing.columns)
        #     print(dfMissing.dtypes)
        dfMissing["COUNT_OF_MISSING_%"] = dfMissing["COUNT_OF_MISSING"].map(lambda x: self.Missing_Count(x, ))
        print(dfMissing.set_index('FEATURE'))
        t1 = dt.now()
        print(t1 - t0)


def convert_time(rawtime):
    """
    This will convert given time data to HHMM format
    :rtype: object
    """
    if pd.isna(rawtime):
        return np.nan;
    else:
        # As rawdt is the integer, so it removing trailing zeros from data, This will create string al least 4 width with leading Zeros
        if rawtime != 2400:  # if time is 2400  date will increase of day (25-12-1-18 24:00:)  to 26-12-1-18 00:00:00
            rawtime = "{0:04d}".format(int(rawtime))
            rawtime = rawtime[:2] + ':' + rawtime[2:4] + ':00'
            # print("rawtime {}".format(rawtime))
            rawtime = pd.to_datetime(rawtime, format='%H:%M:%S').time()
            return rawtime


def concat_date_time(rawrow):
    """
    This will join date and time of two columns
    :rtype: object
    """
    if pd.isnull(rawrow['FLIGHT_DATE']) or pd.isnull(rawrow['SCHEDULED_DEPARTURE']):
        return np.nan;
    else:
        rowtime = rawrow['SCHEDULED_DEPARTURE']
        if rowtime != 2400:
            str_time = convert_time(rowtime)
            #            print('str_time {} '.format(str_time))
            return pd.datetime.combine(rawrow['FLIGHT_DATE'], str_time)
        else:
            print("FLIGHT_DATE : {} ".format(rawrow['FLIGHT_DATE']))
            return rawrow['FLIGHT_DATE'] + pd.DateOffset(1)


def concat_date_time_ARRIVAL(rawrow):
    """
    This will join date and time of two columns
    :rtype: object
    """
    if pd.isnull(rawrow['FLIGHT_DATE']) or pd.isnull(rawrow['SCHEDULED_ARRIVAL']):
        return np.nan;
    else:
        rowtime = rawrow['SCHEDULED_ARRIVAL']
        if rowtime != 2400:
            str_time = convert_time(rowtime)
            #            print('str_time {} '.format(str_time))
            return pd.datetime.combine(rawrow['FLIGHT_DATE'], str_time)
        else:
            print("FLIGHT_DATE : {} ".format(rawrow['FLIGHT_DATE']))
            return rawrow['FLIGHT_DATE'] + pd.DateOffset(1)


def concat_date_time_TaxiOut(rawrow):
    """
    This will join date and time of two columns
    :rtype: object
    """
    if pd.isnull(rawrow['FLIGHT_DATE']) or pd.isnull(rawrow['TAXI_OUT']):
        return np.nan;
    else:
        rowtime = rawrow['TAXI_OUT']
        if rowtime != 2400:
            str_time = convert_time(rowtime)
            #            print('str_time {} '.format(str_time))
            return pd.datetime.combine(rawrow['FLIGHT_DATE'], str_time)
        else:
            print("FLIGHT_DATE : {} ".format(rawrow['FLIGHT_DATE']))
            return rawrow['FLIGHT_DATE'] + pd.DateOffset(1)


from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()
feature_ls = ['YEAR', 'MONTH', 'DAY', 'DAY_OF_WEEK', 'AIRLINE', 'ORIGIN_AIRPORT',
              'DESTINATION_AIRPORT', 'DEPARTURE_DELAY', 'TAXI_OUT', 'WHEELS_OFF', 'SCHEDULED_TIME',
              'ELAPSED_TIME', 'AIR_TIME', 'DISTANCE', 'WHEELS_ON', 'TAXI_IN', 'DIVERTED', 'CANCELLED', 'FLIGHT_DELAY' ]
