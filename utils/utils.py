import pandas as pd

class DataUtils:
    def __init__(self):
        pass

    def load_csvs(self):
        """
        This is loading for Data File
        :rtype: DataFrame
        """
        flight_details = pd.read_csv('../data/flights.csv', )
        print(flight_details.clomuns)


if __name__ == '__main__':
    ut = DataUtils()
    print(ut.load_csvs())