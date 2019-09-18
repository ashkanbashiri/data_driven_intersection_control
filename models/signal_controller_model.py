import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

from sklearn.metrics import mean_squared_error, r2_score
from keras.layers import Dense, Activation
from keras.models import Sequential

def build_model(df):
    y = np.column_stack((df['green_time(1)'].values.tolist(), df['green_time(2)'].values.tolist(),
                         df['green_time(3)'].values.tolist(), df['green_time(4)'].values.tolist()))
    x = np.column_stack((df['flow(1)'].values.tolist(), df['flow(2)'].values.tolist(),
                         df['flow(3)'].values.tolist(), df['flow(4)'].values.tolist(),
                         df['losttime(s)'].values.tolist()))
    model = Sequential()
    model.add(Dense(512, activation='relu', input_dim = 5))
    model.add(Dense(units=256, activation='relu'))
    model.add(Dense(units=256, activation='relu'))
    model.add(Dense(units=256, activation='relu'))
    model.add(Dense(units=256, activation='relu'))
    model.add(Dense(units=256, activation='relu'))
    model.add(Dense(units = 4))
    model.compile(optimizer = 'adam',loss = 'mean_squared_error')
    model.fit(x, y, batch_size = 150, epochs = 5000,verbose=2)
    my_ct_ann = model.predict(x)
    print(my_ct_ann)
    return model