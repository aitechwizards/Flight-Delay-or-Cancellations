import pandas as pd
import numpy as np


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
            print('str_time {} '.format(str_time))
            return pd.datetime.combine(rawrow['FLIGHT_DATE'], str_time)
        else:
            print("FLIGHT_DATE : {} ".format(rawrow['FLIGHT_DATE']))
            return rawrow['FLIGHT_DATE'] + pd.DateOffset(1)


# class ProjectUtils:
#    def __init__(self):
#        pass
#
#    def load_csvs(self):
dfFlight = pd.read_csv('../data/flights.csv', nrows=100, low_memory=False)
dfFlight['FLIGHT_DATE'] = pd.to_datetime(dfFlight[['YEAR', 'MONTH', 'DAY']])

dfFlight['SCHEDULED_DEPARTURE'] = dfFlight.apply(concat_date_time, axis=1)
dfFlight['DEPARTURE_TIME'] = dfFlight['DEPARTURE_TIME'].map(convert_time)
dfFlight['SCHEDULED_ARRIVAL'] = dfFlight['SCHEDULED_ARRIVAL'].map(convert_time)
dfFlight['ARRIVAL_TIME'] = dfFlight['ARRIVAL_TIME'].map(convert_time)
print(dfFlight.columns)
variables_to_remove = ['YEAR', 'MONTH', 'DAY', 'DAY_OF_WEEK', 'FLIGHT_NUMBER', 'TAIL_NUMBER', 'TAXI_OUT', 'TAXI_IN',
                       'WHEELS_ON', 'WHEELS_OFF',
                       'FLIGHT_DATE', 'AIR_SYSTEM_DELAY',
                       'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY',
                       'WEATHER_DELAY', 'DIVERTED', 'CANCELLED', 'CANCELLATION_REASON',
                       'AIR_TIME']
dfFlight.drop(variables_to_remove, axis=1, inplace=True)
print("Missing % value of per  col")


# missing_df = dfFlight.isnull().sum(axis=0)
def missing_per(count):
    print(type(count))
    print(dfFlight.shape)
    return (count / (dfFlight.shape[1] * 100)  )


missing_count = dfFlight.isnull().sum(axis=0).reset_index()
missing_count.columns = {"Feature", "Null Count"}
missing_count["% Null"] = missing_count["Null Count"].map(missing_per)
print(missing_count)

# if __name__ == '__main__':
#    ut = ProjectUtils()
#    ut.load_csvs()
