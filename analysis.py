import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer


datas = pd.read_csv("C:/Users/Rumi/Downloads/archive/worldometer_data.csv")
print(datas.head(10))


datas.rename(columns={'Province/State':'Mystate', 'Country/Region':'Country'}, inplace=True)
print(datas.head(10))


"""
imputer = SimpleImputer(strategy='constant')
data2 = pd.DataFrame(imputer.fit_transform(datas),columns=datas.columns)
print(datas.head(50))
"""


i = SimpleImputer(strategy='constant')
d = pd.DataFrame(i.fit_transform(datas), columns=datas.columns)
print(d.head(10))






//error


df3 = pd.read_csv("C:/Users/Rumi/Downloads/archive/worldometer_data.csv")
for idx in range(0, len(Country)):    
    C = df3[df3['Country'] == Country[idx]].reset_index()        
    plt.scatter(np.arange(0, len(C)), C['Confirmed'], color='blue', label='Confirmed')
    plt.scatter(np.arange(0, len(C)), C['Recovered'], color='green', label='Recovered')
    plt.scatter(np.arange(0, len(C)), C['Deaths'], color='red', label='Deaths')
    plt.title(Country[idx])
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()











