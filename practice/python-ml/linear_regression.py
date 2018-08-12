import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D


DATA_PATH = "data.csv" # path of initial data
TICKER = "aapl" # ticker to work with
TO_LOAD = False # use to create ticker.csv

def cost_function(theta):
    """Computes the cost function and gradient for linear regression
    """
    pass

def extract_stock():
    df = pd.read_csv(DATA_PATH)
    df[df.ticker==TICKER.upper()].to_csv(TICKER+".csv")
    return

def print_shape(np_shapes):
    for shape in np_shapes:
        print(shape, np.shape(shape))

def price_over_time(ticker):
    # loading ticker.csv data
    df = pd.read_csv(TICKER+'.csv')
    df.fillna(method='ffill', inplace=True)

    # get x and y values
    x, y = df['date'].map(lambda x:x.split("-")[0]+"-"+x.split("-")[1]).values, df['price'].values

    # plot data
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    # creating ticker.csv file if set
    if TO_LOAD: extract_stock()

    # loading ticker.csv data
    df = pd.read_csv(TICKER+'.csv')
    df.fillna(method='ffill', inplace=True)

    # computing x and y
    payout, y = df['upcoming_payout'].values, df['price'].values
    delta_y = np.array([y[i] - y[i-1] if i > 0 else 0 for i, v in enumerate(y)])
    x = np.transpose((payout, delta_y))

    # printing shapes
    # print_shape([delta_y, payout, x, y])

    # visualizing price over time
    # price_over_time(TICKER)

    # plotting parameters
    plt.plot(x[:,1], x[:,0], "ro")
    plt.show()

    # # plotting delta_y and y
    # plt.figure(1)
    # plt.subplot(211)
    # plt.plot(y,x[:,0], 'ro')
    # # plotting payout and y
    # plt.subplot(212)
    # plt.plot(y,x[:,1],'yo')
    # plt.show()
