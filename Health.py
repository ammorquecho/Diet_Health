import pandas as pd
import os
from functools import reduce
import math
import matplotlib.pyplot as plt

#%%
os.chdir('/Users/marielmorquecho/PycharmProjects/Diet_Health/')
dat = pd.read_csv('/Users/marielmorquecho/Downloads/FoodBalanceSheets_E_All_Data/FoodBalanceSheets_E_All_Data_NOFLAG.csv',encoding='latin')
dat_pc = dat.loc[dat.Element == 'Food supply quantity (kg/capita/yr)']
filter_col = [col for col in dat_pc if col.startswith('Y')]
dat_pc.rename(columns=dict(zip(dat_pc[filter_col].columns,
dat_pc[filter_col].columns.str[1:].astype(int)))
              ,inplace=True)
year_list = [i for i in range(1961,2014)]
#%%
dat_app= pd.read_csv('/Users/marielmorquecho/PycharmProjects/Diet_Health/Environmental Impact')
dat_main = pd.read_excel('/Users/marielmorquecho/Desktop/Poore&Nemeecek/dat.xlsx')
dat_merge = pd.merge(dat_main,dat_app,on='Match',how='left')
