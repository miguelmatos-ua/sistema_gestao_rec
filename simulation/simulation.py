import argparse
import pickle
from random import random

import pandas as pd

from house import House
from community import Community


def main(arguments: argparse.Namespace) -> None:
    """
    Main function for the simulation.

    :param arguments: Arguments from the command line.
    :return: None
    """
    model = arguments.model
    model = pickle.load(open(model, 'rb'))
    community = Community(pd.read_csv(arguments.weather), pd.read_excel(arguments.price), model,
                          pd.read_csv(arguments.consumption))

    for i in range(arguments.houses):
        h = House(house_number=i, a=random() * 5, p=random())
        community.add_house(h)

    community.sleep_time = arguments.time
    try:
        community.run()
    except KeyboardInterrupt:
        print('Simulation interrupted by user.')

    print('Simulation finished.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", help="Already trained model to use in pickle format", type=str,
                        default="models/model_v1.pkl")
    parser.add_argument("-t", "--time", help="Time between simulations", type=int, default=0)
    parser.add_argument("-w", "--weather", help="Weather data with solar irradiance", type=str,
                        default="data/Solcast_PT30M.csv")
    parser.add_argument("-c", "--consumption", help="Consumption data", type=str, default="data/BANES_v4_featureimportance.csv")
    parser.add_argument("-p", "--price", help="Market Price data", type=str, default="data/PrecoMerc.xlsx")
    parser.add_argument("-n", "--houses", help="Number of houses in the community", type=int, default=5)

    args = parser.parse_args()

    main(args)
