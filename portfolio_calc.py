import numpy as np
import pandas as pd


#class PredictionCalculator(object):
#    def calculate(observations, predictions, values) -> (ERs, cov):
        
observations=pd.read_csv("C:\\Users\\Vitty2\\Documents\\Upwork\\Betasmartz - Black Litterman\\Deliver Datasets\\IndexData.csv",index_col=0,header=0)
cycle=pd.read_csv("C:\\Users\\Vitty2\\Documents\\Upwork\\Betasmartz - Black Litterman\\Deliver Datasets\\CycleVar.csv",index_col=0,header=0)
hist_probs=pd.read_csv("C:\\Users\\Vitty2\\Documents\\Upwork\\Betasmartz - Black Litterman\\Deliver Datasets\\predict_probs12.csv",index_col=0,header=0)

def preprocessdata(leveldf):
    "leveldf: The dataframe that is going to be indexed and cleaned"
    leveldf.index = leveldf.index.to_datetime()
    leveldf = leveldf.dropna()
    return(leveldf)

def returnsdataframe(cleandf,periods=1):
    "leveldf: The dataframe that is going to be indexed and cleaned"
    returns=np.log(cleandf)
    returns=returns - returns.shift(periods)
    return(returns)

def mergemonth2day(daydf,monthdf):
    int_cycles=monthdf.['Cycle'].unique()
    #for i in int_cycles:
       #monthdf[]



clean_obs = preprocessdata(observations)
returns_obs = returnsdataframe(clean_obs)
returns_obs = returns_obs.dropna()


#df.loc[(df['date'].month==12) & (df['date'].day==25), 'xmas'] = 1
