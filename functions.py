import pandas as pd


class AppFunctions(object):
    dataFrame: pd.DataFrame

    def __init__(self, source: str = None):
        if source is not None:
            self.dataFrame = pd.read_csv(source, encoding="ISO-8859-1")
        else:
            self.dataFrame = pd.DataFrame()

    def find_auto(self, brand, from_year, to_year):
        data_slice = self.dataFrame.loc[(self.dataFrame['brand'] == brand) &
                                        (self.dataFrame['yearOfRegistration'] >= from_year) &
                                        (self.dataFrame['yearOfRegistration'] <= to_year)];
        return data_slice