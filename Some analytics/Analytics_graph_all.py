import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
#plot for all
cold_lost = (cold_lost.sort_values(by = ['count'], ascending = False))
cold_lost = cold_lost.reset_index(drop=True)
cold_lost.index = np.arange(1,len(cold_lost)+1)
plt.bar(cold_lost.index,cold_lost['count'])
plt.ylabel('Numbers')
plt.xlabel('Tracker')
plt.xticks(np.arange(min(cold_lost.index), max(cold_lost.index)+1, 1.0))
plt.savefig('C:/Users/chernyshov/Python/Plots/Diagram_all.png')
print(cold_lost)
cold_lost.to_csv('C:/Users/chernyshov/Python/Plots/file.csv', sep='\t')
