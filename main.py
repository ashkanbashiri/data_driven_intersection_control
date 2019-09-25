import pandas as pd
from models.signal_controller_model import build_model,build_single_model
from filter.filter_results import filter_best
from analysis.sensitivity_analysis import analyse
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import time

def main():
    file_loc = './sim_results/results_sep17'
    df = pd.read_csv(file_loc+'.csv')
    for i in range(2,23):
        temp_df = pd.read_csv(file_loc+'_'+str(i)+'.csv')
        df = pd.concat([df,temp_df])

    metric = 'avgdelay'
    predictors = ['flow(1)', 'flow(2)', 'flow(3)', 'flow(4)', 'losttime(s)']
    to_predict = ['green_time(1)', 'green_time(2)', 'green_time(3)', 'green_time(4)']
    print(df.shape)
    train = filter_best(df, to_predict=to_predict, predictors=predictors, metric=metric)
    print(len(train))
    batch_size = 600
    n_epochs = 1500
    predictions,model = build_model(train,batch_size,n_epochs)
    new_df = pd.DataFrame(predictions,columns=['predicted(1)','predicted(2)','predicted(3)','predicted(4)'])
    print(new_df.head())
    print(train[to_predict].head())
    print(new_df.tail())
    print(train[to_predict].tail())
    analyse(model,100000)








if __name__ == "__main__":
    main()
