import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
name = []
number = []
with open('C:/Users/chernyshov/Python/data.json', 'r') as fp:
    resp = json.load(fp)
for i in resp['result']['StableDedicated']['Manual']['WhereReported'].items():
    name.append(i[0])
    number.append(i[1])
data = {'Tracker' : name, 'count':number }
cold_lost = pd.DataFrame(data)
total = (resp['result']['StableDedicated']['Manual']['Total'])
print(total)
cold_lost = (cold_lost.sort_values(by = ['count'], ascending = False))
cold_lost = cold_lost.reset_index(drop=True)
cold_lost.index = np.arange(1,len(cold_lost)+1)
percent = dict()
for i in cold_lost['Tracker']:    
    percent[i] = cold_lost.loc[cold_lost['Tracker'] == i].iloc[0]['count']/total*100
print(percent)
diagram for all
answer = pd.DataFrame(percent, index = [0])
dpi = 80
plt.figure(dpi = dpi, figsize = (640 / dpi, 480 / dpi) )
plt.pie(answer.values[0],  autopct='%.2f', radius = 1.5,
     );
plt.legend(
    bbox_to_anchor = (-0.36, -0.17, 1.25, 0.25),
    loc = 'lower left', labels = answer.keys())
plt.savefig('C:/Users/chernyshov/Python/Plots/Percentage_to_total.png')
plt.show()
print(cold_lost)
