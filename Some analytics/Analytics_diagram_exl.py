import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
name1 = []
values1 = []
with open('C:/Users/chernyshov/Python/data.json', 'r') as fp:
    resp = json.load(fp)
for i in resp['result']['StableDedicated']['Manual']['WhereReported'].items():
    if i[0] != 'UNKNOWN' and i[0] != 'ODOO' and i[0] != 'REDMINE':
        name1.append(i[0])
        values1.append(i[1])
data_exl = {'Tracker' : name1, 'count':values1}
cold_lost_exl = pd.DataFrame(data_exl)
total_exl = sum(cold_lost_exl['count'])
print(total_exl)
cold_lost_exl = (cold_lost_exl.sort_values(by = ['count'], ascending = False))
cold_lost_exl = cold_lost_exl.reset_index(drop=True)
cold_lost_exl.index = np.arange(1,len(cold_lost_exl)+1)
names = []
values = []
percent1 = dict()
for i in cold_lost_exl['Tracker']:    
    percent1[i] = cold_lost_exl.loc[cold_lost_exl['Tracker'] == i].iloc[0]['count']/total_exl*100
print(percent1)
#diagram for all
answer1 = pd.DataFrame(percent1, index = [0])
dpi = 80
plt.figure(dpi = dpi, figsize = (640 / dpi, 480 / dpi) )
plt.pie(answer1.values[0],  autopct='%.2f', radius = 1.5,
     );
plt.legend(
    bbox_to_anchor = (-0.36, -0.17, 1.25, 0.25),
    loc = 'lower left', labels = answer1.keys())
plt.savefig('C:/Users/chernyshov/Python/Plots/Percentage_to_total_exl.png')
plt.show()
print(cold_lost_exl)
