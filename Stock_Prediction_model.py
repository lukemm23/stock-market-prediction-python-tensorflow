# pandas and numpy restructures data
import pandas as pd
import numpy as np
import matplotlib as plt
import tensorflow as tf

# variablizing data files
GOLD_TRAIN_DATA = 'CSV_Files/Gold Data Last Year.csv'
GOLD_TEST_DATA = 'CSV_Files/Gold Data Last Month.csv'

# differentiation data usage
current_train_data = GOLD_TRAIN_DATA
current_test_data = GOLD_TEST_DATA

# number of data points to retrieve
NUM_TRAIN_DATA_POINTS = 266
NUM_TEST_DATA_POINTS = 22


# function to load data, correct structure, and make it an array from csv
def load_stock_data(stock_name, num_data_points):
    data = pd.read_csv(stock_name,
                       skiprows=0,
                       nrows=num_data_points,
                       usecols=['Price', 'Open', 'Vol.'])

    # price at end of each day
    final_prices = data['Price'].astype(str).str.replace(',', '').astype(np.float)
    # price at beginning of each day
    opening_prices = data['Open'].astype(str).str.replace(',', '').astype(np.float)
    # volumes traded through that day
    volumes = data['Vol.'].str.strip('MK').astype(np.float)
    return final_prices, opening_prices, volumes


def calculate_price_differences(final_prices, opening_prices):
    price_differences = []
    for d_i in range(len(final_prices) - 1):
        price_difference = opening_prices[d_i + 1] - final_prices[d_i]
        price_differences.append(price_difference)
        return price_differences


# returning correct data structure
finals, openings, volumes = load_stock_data(current_test_data, NUM_TEST_DATA_POINTS)
differences = calculate_price_differences(finals, openings)
print(differences)
