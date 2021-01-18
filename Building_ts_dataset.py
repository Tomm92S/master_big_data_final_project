#!/usr/bin/env python
# coding: utf-8



import numpy as np
import pandas as pd
from datetime import datetime

import os
os.chdir('C:\\Users\\Tommaso\\Desktop\\IRPET\\TS_Pred_models')


# ### FUNZIONE PER RIEMPIRE NULL VALUES
def fillnullvalues(column):
    index = len(column)
    for i in range(index):
        if np.isnan(column.iloc[i]) == True:
            column.iloc[i] = column.iloc[i-1]
        else:
            continue
    return column



data = datetime.strptime('2019-01-01',"%Y-%m-%d")
    
    
for capoluogo in ['arezzo','firenze','grosseto','livorno','lucca','massa','pisa','pistoia','prato','siena']:
        
        
    # ## PREZZI VENDITA
    
    df1 = pd.read_csv('..\\Data\\df_toscana_cv.csv')
    df1 = df1.set_index('comune').T[capoluogo]
    df1.index = pd.to_datetime(df1.index)
    df1.name = 'prezzi_vendita'


    # ## Turismo (2011-2019)
    
    
    
    
    df_arrivi_tot = pd.read_csv('../Data_turismo/Data/turismo_arrivi.csv',index_col='time',parse_dates=True)
    df_arrivi_tot = df_arrivi_tot[capoluogo]
    df_arrivi_tot.name = 'arrivi_tot'
    
    
    df_arrivi_ita = pd.read_csv('../Data_turismo/Data/turismo_arrivi_ITA.csv',index_col='time',parse_dates=True)
    df_arrivi_ita = df_arrivi_ita[capoluogo]
    df_arrivi_ita.name = 'arrivi_ita'
    
    
    df_arrivi_str = pd.read_csv('../Data_turismo/Data/turismo_arrivi_STR.csv',index_col='time',parse_dates=True)
    df_arrivi_str = df_arrivi_str[capoluogo]
    df_arrivi_str.name = 'arrivi_str'
    
    
    
    
    # ## Reddito (2012-2018)
    
  
    
    df_reddito = pd.read_csv('../Data_reddito/Data/toscana_reddito.csv',index_col='index',parse_dates=False)
    df_reddito  = df_reddito.T[capoluogo]
    df_reddito.name = 'reddito'
    df_reddito.index = pd.to_datetime(df_reddito.index)
    df_reddito.loc[data] = df_reddito.loc['2017':'2018'].mean()
        
        
    # ## Popolazione (2012-05-2020)
    
    
    df_popolazione_anagr_altri_com_canc = pd.read_csv('../Data_popolazione/Data/anagr_altri_com_canc.csv')
    df_popolazione_anagr_altri_com_canc = df_popolazione_anagr_altri_com_canc.set_index('Territorio').T[capoluogo]
    df_popolazione_anagr_altri_com_canc.name = 'anagr_altri_com_canc'
    df_popolazione_anagr_altri_com_canc.index = pd.to_datetime(df_popolazione_anagr_altri_com_canc.index)
    
    
    df_popolazione_anagr_altri_com_iscr = pd.read_csv('../Data_popolazione/Data/anagr_altri_com_iscr.csv')
    df_popolazione_anagr_altri_com_iscr = df_popolazione_anagr_altri_com_iscr.set_index('Territorio').T[capoluogo]
    df_popolazione_anagr_altri_com_iscr.name = 'anagr_altri_com_iscr'
    df_popolazione_anagr_altri_com_iscr.index = pd.to_datetime(df_popolazione_anagr_altri_com_iscr.index)
    
    
    df_popolazione_canc_anagr = pd.read_csv('../Data_popolazione/Data/canc_anagr.csv')
    df_popolazione_canc_anagr = df_popolazione_canc_anagr.set_index('Territorio').T[capoluogo]
    df_popolazione_canc_anagr.name = 'canc_anagr'
    df_popolazione_canc_anagr.index = pd.to_datetime(df_popolazione_canc_anagr.index)
    
    df_popolazione_canc_anagr_altrimot = pd.read_csv('../Data_popolazione/Data/canc_anagr_altrimot.csv')
    df_popolazione_canc_anagr_altrimot = df_popolazione_canc_anagr_altrimot.set_index('Territorio').T[capoluogo]
    df_popolazione_canc_anagr_altrimot.name = 'canc_anagr_altrimot'
    df_popolazione_canc_anagr_altrimot.index = pd.to_datetime(df_popolazione_canc_anagr_altrimot.index)
    
    df_popolazione_canc_anagr_est = pd.read_csv('../Data_popolazione/Data/canc_anagr_est.csv')
    df_popolazione_canc_anagr_est = df_popolazione_canc_anagr_est.set_index('Territorio').T[capoluogo]
    df_popolazione_canc_anagr_est.name = 'canc_anagr_est'
    df_popolazione_canc_anagr_est.index = pd.to_datetime(df_popolazione_canc_anagr_est.index)
    
    df_popolazione_iscr_anagr = pd.read_csv('../Data_popolazione/Data/iscr_anagr.csv')
    df_popolazione_iscr_anagr = df_popolazione_iscr_anagr.set_index('Territorio').T[capoluogo]
    df_popolazione_iscr_anagr.name = 'iscr_anagr'
    df_popolazione_iscr_anagr.index = pd.to_datetime(df_popolazione_iscr_anagr.index)
    
    df_popolazione_iscr_anagr_altrimot = pd.read_csv('../Data_popolazione/Data/iscr_anagr_altrimot.csv')
    df_popolazione_iscr_anagr_altrimot = df_popolazione_iscr_anagr_altrimot.set_index('Territorio').T[capoluogo]
    df_popolazione_iscr_anagr_altrimot.name = 'iscr_anagr_altrimot'
    df_popolazione_iscr_anagr_altrimot.index = pd.to_datetime(df_popolazione_iscr_anagr_altrimot.index)
    
    df_popolazione_iscr_anagr_est = pd.read_csv('../Data_popolazione/Data/iscr_anagr_est.csv')
    df_popolazione_iscr_anagr_est = df_popolazione_iscr_anagr_est.set_index('Territorio').T[capoluogo]
    df_popolazione_iscr_anagr_est.name = 'iscr_anagr_est'
    df_popolazione_iscr_anagr_est.index = pd.to_datetime(df_popolazione_iscr_anagr_est.index)
    
    df_popolazione_morti = pd.read_csv('../Data_popolazione/Data/morti.csv')
    df_popolazione_morti = df_popolazione_morti.set_index('Territorio').T[capoluogo]
    df_popolazione_morti.name = 'morti'
    df_popolazione_morti.index = pd.to_datetime(df_popolazione_morti.index)
    
    df_popolazione_nati_vivi = pd.read_csv('../Data_popolazione/Data/nati_vivi.csv')
    df_popolazione_nati_vivi = df_popolazione_nati_vivi.set_index('Territorio').T[capoluogo]
    df_popolazione_nati_vivi.name = 'nati_vivi'
    df_popolazione_nati_vivi.index = pd.to_datetime(df_popolazione_nati_vivi.index)
    
    df_popolazione_popol_iniz = pd.read_csv('../Data_popolazione/Data/popol_iniz.csv')
    df_popolazione_popol_iniz = df_popolazione_popol_iniz.set_index('Territorio').T[capoluogo]
    df_popolazione_popol_iniz.name = 'popol_fin'
    df_popolazione_popol_iniz.index = pd.to_datetime(df_popolazione_popol_iniz.index)
    
    df_popolazione_saldo_altrimot = pd.read_csv('../Data_popolazione/Data/saldo_altrimot.csv')
    df_popolazione_saldo_altrimot = df_popolazione_saldo_altrimot.set_index('Territorio').T[capoluogo]
    df_popolazione_saldo_altrimot.name = 'saldo_altrimot'
    df_popolazione_saldo_altrimot.index = pd.to_datetime(df_popolazione_saldo_altrimot.index)
    
    df_popolazione_saldo_migr = pd.read_csv('../Data_popolazione/Data/saldo_migr.csv')
    df_popolazione_saldo_migr = df_popolazione_saldo_migr.set_index('Territorio').T[capoluogo]
    df_popolazione_saldo_migr.name = 'saldo_migr'
    df_popolazione_saldo_migr.index = pd.to_datetime(df_popolazione_saldo_migr.index)
    
    df_popolazione_saldo_migr_e_altrimot = pd.read_csv('../Data_popolazione/Data/saldo_migr_e_altrimot.csv')
    df_popolazione_saldo_migr_e_altrimot = df_popolazione_saldo_migr_e_altrimot.set_index('Territorio').T[capoluogo]
    df_popolazione_saldo_migr_e_altrimot.name = 'saldo_migr_e_altrimot'
    df_popolazione_saldo_migr_e_altrimot.index = pd.to_datetime(df_popolazione_saldo_migr_e_altrimot.index)
    
    df_popolazione_saldo_migr_est = pd.read_csv('../Data_popolazione/Data/saldo_migr_est.csv')
    df_popolazione_saldo_migr_est = df_popolazione_saldo_migr_est.set_index('Territorio').T[capoluogo]
    df_popolazione_saldo_migr_est.name = 'saldo_migr_est'
    df_popolazione_saldo_migr_est.index = pd.to_datetime(df_popolazione_saldo_migr_e_altrimot.index)
    
    df_popolazione_saldo_migr_int = pd.read_csv('../Data_popolazione/Data/saldo_migr_int.csv')
    df_popolazione_saldo_migr_int = df_popolazione_saldo_migr_int.set_index('Territorio').T[capoluogo]
    df_popolazione_saldo_migr_int.name = 'saldo_migr_int'
    df_popolazione_saldo_migr_int.index = pd.to_datetime(df_popolazione_saldo_migr_int.index)
    
    df_popolazione_saldo_naturale = pd.read_csv('../Data_popolazione/Data/saldo_naturale.csv')
    df_popolazione_saldo_naturale = df_popolazione_saldo_naturale.set_index('Territorio').T[capoluogo]
    df_popolazione_saldo_naturale.name = 'saldo_naturale'
    df_popolazione_saldo_naturale.index = pd.to_datetime(df_popolazione_saldo_naturale.index)
    
    df_popolazione_saldotot_incr_decr = pd.read_csv('../Data_popolazione/Data/saldotot_incr_decr.csv')
    df_popolazione_saldotot_incr_decr = df_popolazione_saldotot_incr_decr.set_index('Territorio').T[capoluogo]
    df_popolazione_saldotot_incr_decr.name = 'saldotot_incr_decr'
    df_popolazione_saldotot_incr_decr.index = pd.to_datetime(df_popolazione_saldotot_incr_decr.index)
    
    
    # ### OCCUPATI (2012-2018)
    
    
    
    
    df_imprese_BDE = pd.read_csv('../Data_imprese/Data/BDE_imprese.csv ')
    df_imprese_BDE = df_imprese_BDE.set_index('Comune').T[capoluogo]
    df_imprese_BDE.name = 'UL_BDE'
    df_imprese_BDE.index = pd.to_datetime(df_imprese_BDE.index)      
    df_imprese_BDE.loc[data] = df_imprese_BDE.loc['2017':'2018'].mean()
    
    df_addetti_BDE = pd.read_csv('../Data_imprese/Data/BDE_addetti.csv ')
    df_addetti_BDE = df_addetti_BDE.set_index('Comune').T[capoluogo]
    df_addetti_BDE.name = 'ADD_BDE'
    df_addetti_BDE.index = pd.to_datetime(df_addetti_BDE.index)
    df_addetti_BDE.loc[data] = df_addetti_BDE.loc['2017':'2018'].mean()    
    
    
    df_imprese_C = pd.read_csv('../Data_imprese/Data/C_imprese.csv ')
    df_imprese_C = df_imprese_C.set_index('Comune').T[capoluogo]
    df_imprese_C.name = 'UL_C'
    df_imprese_C.index = pd.to_datetime(df_imprese_C.index)
    df_imprese_C.loc[data] = df_imprese_C.loc['2017':'2018'].mean()
    
    df_addetti_C = pd.read_csv('../Data_imprese/Data/C_addetti.csv ')
    df_addetti_C = df_addetti_C.set_index('Comune').T[capoluogo]
    df_addetti_C.name = 'ADD_C'
    df_addetti_C.index = pd.to_datetime(df_addetti_C.index)
    df_addetti_C.loc[data] = df_addetti_C.loc['2017':'2018'].mean()    
    
    
    df_imprese_F = pd.read_csv('../Data_imprese/Data/F_imprese.csv ')
    df_imprese_F = df_imprese_F.set_index('Comune').T[capoluogo]
    df_imprese_F.name = 'UL_F'
    df_imprese_F.index = pd.to_datetime(df_imprese_F.index)
    df_imprese_F.loc[data] = df_imprese_F.loc['2017':'2018'].mean()
    
    df_addetti_F = pd.read_csv('../Data_imprese/Data/F_addetti.csv ')
    df_addetti_F = df_addetti_F.set_index('Comune').T[capoluogo]
    df_addetti_F.name = 'ADD_F'
    df_addetti_F.index = pd.to_datetime(df_addetti_F.index)  
    df_addetti_F.loc[data] = df_addetti_F.loc['2017':'2018'].mean()    
    
    
    df_imprese_G = pd.read_csv('../Data_imprese/Data/G_imprese.csv ')
    df_imprese_G = df_imprese_G.set_index('Comune').T[capoluogo]
    df_imprese_G.name = 'UL_G'
    df_imprese_G.index = pd.to_datetime(df_imprese_G.index)
    df_imprese_G.loc[data] = df_imprese_G.loc['2017':'2018'].mean()
    
    df_addetti_G = pd.read_csv('../Data_imprese/Data/G_addetti.csv ')
    df_addetti_G = df_addetti_G.set_index('Comune').T[capoluogo]
    df_addetti_G.name = 'ADD_G'
    df_addetti_G.index = pd.to_datetime(df_addetti_G.index)
    df_addetti_G.loc[data] = df_addetti_G.loc['2017':'2018'].mean()
    
    
    df_imprese_HI = pd.read_csv('../Data_imprese/Data/HI_imprese.csv ')
    df_imprese_HI = df_imprese_HI.set_index('Comune').T[capoluogo]
    df_imprese_HI.name = 'UL_HI'
    df_imprese_HI.index = pd.to_datetime(df_imprese_HI.index)
    df_imprese_HI.loc[data] = df_imprese_HI.loc['2017':'2018'].mean()
    
    df_addetti_HI = pd.read_csv('../Data_imprese/Data/HI_addetti.csv ')
    df_addetti_HI = df_addetti_HI.set_index('Comune').T[capoluogo]
    df_addetti_HI.name = 'ADD_HI'
    df_addetti_HI.index = pd.to_datetime(df_addetti_HI.index)
    df_addetti_HI.loc[data] = df_addetti_HI.loc['2017':'2018'].mean()
    
    
    df_imprese_JKL = pd.read_csv('../Data_imprese/Data/JKL_imprese.csv ')
    df_imprese_JKL = df_imprese_JKL.set_index('Comune').T[capoluogo]
    df_imprese_JKL.name = 'UL_JKL'
    df_imprese_JKL.index = pd.to_datetime(df_imprese_JKL.index)
    df_imprese_JKL.loc[data] = df_imprese_JKL.loc['2017':'2018'].mean()
    
    df_addetti_JKL = pd.read_csv('../Data_imprese/Data/JKL_addetti.csv ')
    df_addetti_JKL = df_addetti_JKL.set_index('Comune').T[capoluogo]
    df_addetti_JKL.name = 'ADD_JKL'
    df_addetti_JKL.index = pd.to_datetime(df_addetti_JKL.index)
    df_addetti_JKL.loc[data] = df_addetti_JKL.loc['2017':'2018'].mean()
    
    
    df_imprese_MN = pd.read_csv('../Data_imprese/Data/MN_imprese.csv ')
    df_imprese_MN = df_imprese_MN.set_index('Comune').T[capoluogo]
    df_imprese_MN.name = 'UL_MN'
    df_imprese_MN.index = pd.to_datetime(df_imprese_MN.index)
    df_imprese_MN.loc[data] = df_imprese_MN.loc['2017':'2018'].mean()
    
    df_addetti_MN = pd.read_csv('../Data_imprese/Data/MN_addetti.csv ')
    df_addetti_MN = df_addetti_MN.set_index('Comune').T[capoluogo]
    df_addetti_MN.name = 'ADD_MN'
    df_addetti_MN.index = pd.to_datetime(df_addetti_MN.index)
    df_addetti_MN.loc[data] = df_addetti_MN.loc['2017':'2018'].mean()
    
    
    df_imprese_OPQ = pd.read_csv('../Data_imprese/Data/OPQ_imprese.csv ')
    df_imprese_OPQ = df_imprese_OPQ.set_index('Comune').T[capoluogo]
    df_imprese_OPQ.name = 'UL_OPQ'
    df_imprese_OPQ.index = pd.to_datetime(df_imprese_OPQ.index)
    df_imprese_OPQ.loc[data] = df_imprese_OPQ.loc['2017':'2018'].mean()
    
    df_addetti_OPQ = pd.read_csv('../Data_imprese/Data/OPQ_addetti.csv ')
    df_addetti_OPQ = df_addetti_OPQ.set_index('Comune').T[capoluogo]
    df_addetti_OPQ.name = 'ADD_OPQ'
    df_addetti_OPQ.index = pd.to_datetime(df_addetti_OPQ.index)
    df_addetti_OPQ.loc[data] = df_addetti_OPQ.loc['2017':'2018'].mean()
    
    
    df_imprese_RSTU = pd.read_csv('../Data_imprese/Data/RSTU_imprese.csv ')
    df_imprese_RSTU = df_imprese_RSTU.set_index('Comune').T[capoluogo]
    df_imprese_RSTU.name = 'UL_RSTU'
    df_imprese_RSTU.index = pd.to_datetime(df_imprese_RSTU.index)
    df_imprese_RSTU.loc[data] = df_imprese_RSTU.loc['2017':'2018'].mean()
    
    df_addetti_RSTU = pd.read_csv('../Data_imprese/Data/RSTU_addetti.csv ')
    df_addetti_RSTU = df_addetti_RSTU.set_index('Comune').T[capoluogo]
    df_addetti_RSTU.name = 'ADD_RSTU'
    df_addetti_RSTU.index = pd.to_datetime(df_addetti_RSTU.index)
    df_addetti_RSTU.loc[data] = df_addetti_RSTU.loc['2017':'2018'].mean()   
    
    
    
    
    
    # ### DENSITY OF POPULATION
    
    df_sup = pd.read_excel('../Pred_models/Classificazioni statistiche-e-dimensione-dei-comuni_31_12_2018.xls')[['Denominazione (italiana e straniera)','Superficie territoriale (kmq) al 01/01/2018']]
    df_sup['Denominazione (italiana e straniera)'] = df_sup['Denominazione (italiana e straniera)'].apply(lambda x : x.strip().lower().replace(' ','-').replace('ò','o')\
                                  .replace('à','a').replace('è','e').replace('ì','i').replace('ù','u')\
                                 .replace('\'','-').split('/')[0].replace('--','-').replace('é','e'))
    superficie = float(df_sup[df_sup['Denominazione (italiana e straniera)']==capoluogo]['Superficie territoriale (kmq) al 01/01/2018'])
    
    df_pop_density = df_popolazione_popol_iniz/superficie
    df_pop_density.name = 'pop_density'
    
    # ### REDDITO PRO CAPITE (annuo)
    
    df_reddito_procapite_ann = df_reddito/df_popolazione_popol_iniz
    df_reddito_procapite_ann.name = 'reddito_procapite_ann'
    
    
    # ### JOIN ALL TOGETHER
    df = pd.DataFrame(data=[df1,df_reddito,df_arrivi_tot,df_arrivi_ita,df_arrivi_str,\
                            df_popolazione_anagr_altri_com_canc,
                            df_popolazione_anagr_altri_com_iscr,
                            df_popolazione_canc_anagr,
                            df_popolazione_canc_anagr_altrimot,
                            df_popolazione_canc_anagr_est,
                            df_popolazione_iscr_anagr,
                            df_popolazione_iscr_anagr_altrimot,
                            df_popolazione_iscr_anagr_est,
                            df_popolazione_morti,
                            df_popolazione_nati_vivi,
                            df_popolazione_popol_iniz,
                            df_popolazione_saldo_altrimot,
                            df_popolazione_saldo_migr,
                            df_popolazione_saldo_migr_e_altrimot,
                            df_popolazione_saldo_migr_est,
                            df_popolazione_saldo_migr_int,
                            df_popolazione_saldo_naturale,
                            df_popolazione_saldotot_incr_decr,
                            df_pop_density,
                            df_reddito_procapite_ann,
                            df_imprese_BDE,
                            df_addetti_BDE,
                            df_imprese_C,
                            df_addetti_C,
                            df_imprese_F,
                            df_addetti_F,
                            df_imprese_G,
                            df_addetti_G,
                            df_imprese_HI,
                            df_addetti_HI,
                            df_imprese_JKL,
                            df_addetti_JKL,
                            df_imprese_MN,
                            df_addetti_MN,
                            df_imprese_OPQ,
                            df_addetti_OPQ,
                            df_imprese_RSTU,
                            df_addetti_RSTU
                            ]) 
    
    
    
    df = df.T.loc['2012':]
    #df = df.T.loc['2012':'2018']
    	
    
    for col in df.columns:
        df[col] = fillnullvalues(df[col])
    
    
    # ### REDDITO PRO CAPITE (mensile) (prova)
    
    df['reddito_procapite_mens'] = df['reddito']/df['popol_fin']
    
    
    df = df.reset_index()
    
    
    # ### WRITE FILES
    df.to_csv('Data\\ts_dataset_{0}.csv'.format(capoluogo), index = False)


