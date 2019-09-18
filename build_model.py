import pandas as pd
from models.signal_controller_model import build_model
from filter.filter_results import filter_best
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def main():
    file_loc = './sim_results/results_sep08'
    df = pd.read_csv(file_loc+'.csv')
    for i in range(2,31):
        temp_df = pd.read_csv(file_loc+'_'+str(i)+'.csv')
        df = pd.concat([df,temp_df])

    metric = 'avgdelay'
    predictors = ['losttime(s)', 'flow(1)', 'flow(2)', 'flow(3)', 'flow(4)']
    to_predict = ['green_time(1)', 'green_time(2)', 'green_time(3)', 'green_time(4)']
    train = filter_best(df, to_predict, predictors, metric, 'min')
    build_model(train)

if __name__ == "__main__":
    main()
