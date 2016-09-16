import numpy as np
import pandas as pd


#class PredictionCalculator(object):
#    def calculate(observations, predictions, values) -> (ERs, cov):
        


#Home
observations=pd.read_csv("C:\\Users\\Vitty2\\Documents\\Upwork\\Betasmartz - Black Litterman\\Deliver Datasets\\IndexData.csv",index_col=0,header=0)
cycle=pd.read_csv("C:\\Users\\Vitty2\\Documents\\Upwork\\Betasmartz - Black Litterman\\Deliver Datasets\\CycleVar.csv",index_col=0,header=0)
hist_probs=pd.read_csv("C:\\Users\\Vitty2\\Documents\\Upwork\\Betasmartz - Black Litterman\\Deliver Datasets\\predict_probs12.csv",index_col=0,header=0)


#Work
#observations = pd.read_csv("C:\\Users\\U447354\\Documents\\Python Scripts\\Beta\\IndexData.csv",index_col=0,header=0)
#cycle=pd.read_csv("C:\\Users\\U447354\\Documents\\Python Scripts\\Beta\\CycleVar.csv",index_col=0,header=0)
#hist_probs=pd.read_csv("C:\\Users\\U447354\\Documents\\Python Scripts\\Beta\\predict_probs12.csv",index_col=0,header=0)



def preprocess_data(level_df):
    "leveldf: The dataframe that is going to be indexed and cleaned"
    level_df.index = pd.to_datetime(level_df.index, format='%d/%m/%Y')
    level_df = level_df.dropna()
    return(level_df)

def returns_dataframe(clean_df,periods=1):
    "leveldf: The dataframe that is going to be indexed and cleaned"
    returns = np.log(clean_df)
    returns = returns - returns.shift(periods)
    return(returns)

def merge_cycle_obs(day_df,month_df,string,default = 0):
    day_df[string] = default
    var_merge = month_df[string].unique()
    for i in var_merge:
       index_day = month_df[month_df[string] == i].index.to_datetime()
       for j in index_day:
           date_indexer = (day_df.index.month == j.month) & (day_df.index.year == j.year)
           rep_days = np.sum(date_indexer)
           day_df.loc[date_indexer,string] = [i]*rep_days
    return(day_df)

def clean_cycle_merge(merged_df, string, default = 0):
    new_df = merged_df[merged_df[string] != default]
    return(new_df)
    
def normalize_probs(probs_df):
    new_probs = probs_df.drop('pred_date', axis = 1)
    sum_row = new_probs.sum(axis = 1)
    norm_probs = new_probs.div(sum_row, axis = 0)
    return(norm_probs)

def expected_returns_prob_v1(merged_df,norm_probs):
    summary_df = merged_df.groupby('Cycle', as_index=True).mean().T
    prob_vector = pd.np.array(norm_probs.tail(1))
    expected_return = summary_df.dot(prob_vector.T)
    return(expected_return)

def covariance_matrix_prob_v1():
    pass

clean_obs = preprocess_data(observations)
clean_cycle = preprocess_data(cycle)
returns_obs = returns_dataframe(clean_obs)
returns_obs = returns_obs.dropna()
index_cycle = merge_cycle_obs(returns_obs,clean_cycle,'Cycle')
clean_index_cycle = clean_cycle_merge(index_cycle,'Cycle')
normal_probs = normalize_probs(hist_probs)
ERs = expected_returns_prob_v1(clean_index_cycle, normal_probs)
