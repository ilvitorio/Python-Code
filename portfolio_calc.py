import numpy as np
import pandas as pd


#class PredictionCalculator(object):
#    def calculate(observations, predictions, values) -> (ERs, cov):
        


#Home
#observations=pd.read_csv("C:\\Users\\Vitty2\\Documents\\Upwork\\Betasmartz - Black Litterman\\Deliver Datasets\\IndexData.csv",index_col=0,header=0)
#cycle=pd.read_csv("C:\\Users\\Vitty2\\Documents\\Upwork\\Betasmartz - Black Litterman\\Deliver Datasets\\CycleVar.csv",index_col=0,header=0)
#hist_probs=pd.read_csv("C:\\Users\\Vitty2\\Documents\\Upwork\\Betasmartz - Black Litterman\\Deliver Datasets\\predict_probs12.csv",index_col=0,header=0)


#Work
observations = pd.read_csv("C:\\Users\\U447354\\Documents\\Python Scripts\\Beta\\IndexData.csv",index_col=0,header=0)
cycle=pd.read_csv("C:\\Users\\U447354\\Documents\\Python Scripts\\Beta\\CycleVar.csv",index_col=0,header=0)
hist_probs=pd.read_csv("C:\\Users\\U447354\\Documents\\Python Scripts\\Beta\\predict_probs12.csv",index_col=0,header=0)



def preprocess_data(leveldf):
    "leveldf: The dataframe that is going to be indexed and cleaned"
    leveldf.index = pd.to_datetime(leveldf.index, format='%d/%m/%Y')
    leveldf = leveldf.dropna()
    return(leveldf)

def returns_dataframe(cleandf,periods=1):
    "leveldf: The dataframe that is going to be indexed and cleaned"
    returns = np.log(cleandf)
    returns = returns - returns.shift(periods)
    return(returns)

def merge_cycle_obs(daydf,monthdf):
    daydf['Cycle'] = 0
    int_cycles = monthdf['Cycle'].unique()
    for i in int_cycles:
       index_cycle = monthdf[monthdf['Cycle'] == i].index.to_datetime()
       for j in index_cycle:
           date_indexer = (daydf.index.month == j.month) & (daydf.index.year == j.year)
           rep_days=np.sum(date_indexer)
           daydf.loc[date_indexer,'Cycle'] = [i]*rep_days
    return(daydf)

def clean_cycle_merge(merged_df):
    new_df=merged_df[merged_df['Cycle']!=0]
    return(new_df)
    
def normalize_probs(probsdf):
    
    pass

clean_obs = preprocess_data(observations)
clean_cycle = preprocess_data(cycle)
returns_obs = returns_dataframe(clean_obs)
returns_obs = returns_obs.dropna()
index_cycle = merge_cycle_obs(returns_obs,clean_cycle)
clean_index_cycle = clean_cycle_merge(index_cycle)

