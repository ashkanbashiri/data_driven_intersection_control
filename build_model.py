import pandas as pd

def main():
    file_loc = './sim_results/results_sep08'
    train = pd.read_csv(file_loc+'.csv')
    for i in range(2,31):
        temp_df = pd.read_csv(file_loc+'_'+str(i)+'.csv')
        train = pd.concat([train,temp_df])

    print(train.head())
    print(train.tail())
    columns = train.columns
    print(columns)




if __name__ == "__main__":
    main()
