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
#plot with exclusions
plt.bar(cold_lost_exl.index,cold_lost_exl['count'])
plt.ylabel('Numbers')
plt.xlabel('Tracker')
plt.xticks(np.arange(min(cold_lost_exl.index), max(cold_lost_exl.index)+1, 1.0))
plt.savefig('C:/Users/chernyshov/Python/Plots/Diagram_exl.png')
print(cold_lost_exl)
cold_lost_exl.to_csv('C:/Users/chernyshov/Python/Plots/file.csv', sep='\t')
