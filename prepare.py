#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import acquire


# In[2]:


def prep_zillow_data():
    df = acquire.get_zillow_data()
    df = df.drop(columns = {'airconditioningtypeid', 'architecturalstyletypeid', 'basementsqft',
                            'taxdelinquencyyear', 'buildingclasstypeid', 'decktypeid', 'finishedfloor1squarefeet',
                            'finishedsquarefeet13', 'finishedsquarefeet15', 'finishedsquarefeet50',
                            'finishedsquarefeet6', 'fireplacecnt', 'hashottuborspa', 'poolsizesum',
                            'pooltypeid10', 'pooltypeid2', 'pooltypeid7', 'storytypeid', 'threequarterbathnbr',
                            'typeconstructiontypeid', 'yardbuildingsqft17', 'yardbuildingsqft26', 'numberofstories',
                            'fireplaceflag', 'taxdelinquencyflag', 'buildingqualitytypeid', 'garagecarcnt',
                            'garagetotalsqft', 'poolcnt', 'regionidneighborhood', 'propertyzoningdesc' })
    df['calculatedfinishedsquarefeet'] = df['calculatedfinishedsquarefeet'].fillna((df['calculatedfinishedsquarefeet'].mean()))
    df['calculatedbathnbr'] = df['calculatedbathnbr'].fillna((df['calculatedbathnbr'].mean()))
    df['finishedsquarefeet12'] = df['finishedsquarefeet12'].fillna((df['finishedsquarefeet12'].mean()))
    df['fullbathcnt'] = df['fullbathcnt'].fillna((df['fullbathcnt'].mean()))
    df['heatingorsystemtypeid'] = df['heatingorsystemtypeid'].fillna((df['heatingorsystemtypeid'].mean()))
    df['lotsizesquarefeet'] = df['lotsizesquarefeet'].fillna((df['lotsizesquarefeet'].mean()))
    df['regionidcity'] = df['regionidcity'].fillna((df['regionidcity'].mean()))
    df['regionidzip'] = df['regionidzip'].fillna((df['regionidzip'].mean()))
    df['unitcnt'] = df['unitcnt'].fillna((df['unitcnt'].mean()))
    df['structuretaxvaluedollarcnt'] = df['structuretaxvaluedollarcnt'].fillna((df['structuretaxvaluedollarcnt'].mean()))
    df['taxamount'] = df['taxamount'].fillna((df['taxamount'].mean()))
    df['censustractandblock'] = df['censustractandblock'].fillna((df['censustractandblock'].mean()))
    df['yearbuilt'] = df['yearbuilt'].fillna((df['yearbuilt'].mean()))
    return df


# In[3]:





# In[ ]:




