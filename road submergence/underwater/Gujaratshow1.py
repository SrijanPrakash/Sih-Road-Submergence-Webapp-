
# coding: utf-8

# In[7]:



import pandas as pd
data=pd.read_csv('GujaratRainTSFinal(1).csv',index_col=0)


# In[8]:



dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
data = pd.read_csv('GujaratRainTSFinal(1).csv', parse_dates=['datetime'], index_col='datetime',date_parser=dateparse)


# In[9]:


import numpy as np
import matplotlib.pylab as plt
get_ipython().magic('matplotlib inline')
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 30, 10


# In[10]:


ts=data['foo']
tstrain=ts




# In[11]:


from statsmodels.tsa.stattools import adfuller


# In[12]:


from statsmodels.tsa.arima_model import ARIMA


# In[13]:


model = ARIMA(tstrain, order=(2, 0, 2))  
results_ARIMA = model.fit(disp=-1)  


# In[14]:


predictions_ARIMA = pd.Series(results_ARIMA.fittedvalues, copy=True)
q=predictions_ARIMA>=0
for x in range(768):
    if(predictions_ARIMA[x]<0):
        predictions_ARIMA[x]=0.0


# In[15]:


# multi-step out-of-sample forecast
start_index = 768
end_index = start_index + 11
forecast = results_ARIMA.predict(start=start_index, end=end_index)
plt.bar(forecast.index,forecast,width=10)
plt.title('NEXT YEAR PREDICTION',fontsize = 20)
plt.xlabel('DATE', fontsize = 20)
plt.ylabel('RAINFALL', fontsize = 20)
forecast

