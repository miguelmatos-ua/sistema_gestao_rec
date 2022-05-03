import time
from typing import Optional

import pandas as pd
import xgboost

from house import House


class Community:
    houses: list[House]
    weather: pd.DataFrame
    prices: pd.DataFrame
    real_consume: pd.DataFrame
    sleep_time = 5

    def __init__(self, weather: pd.DataFrame, prices: pd.DataFrame, model: xgboost.XGBModel, real_consume: pd.DataFrame,
                 houses: list[House] = None):
        if not houses:
            houses = []
        self.houses = houses
        self.weather = weather
        self.prices = prices
        self.model = model
        self.real_consume = real_consume

    def add_house(self, house: House):
        """
        Adds a house to the community.

        :param house: The house to add.
        """
        self.houses.append(house)

    def get_house(self, house_id: int) -> Optional[House]:
        """
        Gets a house from the community.

        :param house_id: The id of the house.
        :return: The house.
        """
        for house in self.houses:
            if house.house_number == house_id:
                return house
        return None

    def run(self):
        """
        Runs the simulation.
        """
        print("Starting simulation...")
        print("\ttime\t|\tHouse #\t|\tReal Consumed\t|\tPredicted Consumed\t|\tPrice")
        print("-" * 50)
        for row in self.weather.iterrows():
            _time = row[0]
            print("\t{}\t|".format(_time), end="")
            for house in self.houses:
                print("\t{}\t|".format(house.house_number), end="")
                print("\t{}\t|".format(self.real_consume[self.real_consume['time'] == _time]['energy'].values[0]), end="")
                print()
            time.sleep(self.sleep_time)
