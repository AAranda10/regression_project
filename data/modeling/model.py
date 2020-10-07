#!/usr/bin/env python
# coding: utf-8

# In[8]:


import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import wrangle
import prep
from scipy import stats

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


# In[41]:


def poly_model(xdf, ydf, y):
    lm = LinearRegression()
    rfe = RFE(lm, 5)
    X_rfe = rfe.fit_transform(xdf, ydf)
    poly = PolynomialFeatures(degree=4)
    X_poly = poly.fit_transform(X_rfe)
    lm_poly = LinearRegression()
    lm_poly.fit(X_poly, ydf[y])
    ydf['yhat_poly'] = lm_poly.predict(X_poly).round(1)
    RMSE_poly = np.sqrt(mean_squared_error(ydf[y], ydf.yhat_poly))
    return ydf


# In[46]:


def mvp():
    df = prep.prep_zillow_data()
    X_train, y_train, X_validate, y_validate, X_test, y_test = wrangle.train_validate_test(df)
    X_train_scaled, X_validate_scaled, X_test_scaled = wrangle.min_max_scale(X_train, X_validate, X_test)
    lm = LinearRegression()
    rfe = RFE(lm, 5)
    X_rfe = rfe.fit_transform(X_test, y_test)
    poly = PolynomialFeatures(degree=4)
    X_poly = poly.fit_transform(X_rfe)
    lm_poly = LinearRegression()
    lm_poly.fit(X_poly, y_test.taxvaluedollarcnt)
    y_test['yhat_poly'] = lm_poly.predict(X_poly).round(1)
    RMSE_poly = np.sqrt(mean_squared_error(y_test.taxvaluedollarcnt, y_test.yhat_poly))
    return y_test


# In[ ]:





# In[ ]:




