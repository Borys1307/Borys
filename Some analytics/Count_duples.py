import pandas as pd
filenames = ['C:/Users/chernyshov/Downloads/Referrals-(toggl.com)-(2019_03_01-2019_05_31).xlsx', 
'C:/Users/chernyshov/Downloads/Referrals-(hubstaff.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(timecamp.com)-(2019_03_01-2019_05_31).xlsx', 
'C:/Users/chernyshov/Downloads/Referrals-(clockify.me)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(tmetric.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(harvestapp.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(timedoctor.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(actitime.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(bigtime.net)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(tsheets.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(ticktick.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(timeneye.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(timelyapp.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(clicktime.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(rescuetime.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(desktime.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(hellobonsai.com)-(2019_03_01-2019_05_31).xlsx',
'C:/Users/chernyshov/Downloads/Referrals-(azendoo.com)-(2019_03_01-2019_05_31).xlsx']
dfs1 = dict()
answer = []
duples = {}
for i in range(len(filenames)):        
    xl_file = pd.ExcelFile(filenames[i])
    dfs = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}
    name = dfs['Report Details']['Unnamed: 1'][2].split()[2]
    duples[name] = []
    if name not in dfs1:
        dfs1[name] = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names if sheet_name !='Report Details'}    
    for j in dfs1[name]['Aggregated Data for Time Period']['Domain']:
        dlina = len(dfs1.keys())        
        if j not in answer:
            answer.append(j)            
        else:
            duples[name].append(j)
    if duples[name] == []:
        duples.pop(name)  
calc = {}          
for i in duples.keys():
    for j in duples[i]:
        if j not in calc:
            calc[j] = 1
        else:
            calc[j] +=1
sa = pd.DataFrame.from_dict(calc, orient = 'index', columns = ['Values'])
sa.index = sa.index.set_names(['Domain'])
sa = sa.sort_values(by=['Values'], ascending = False)
sa.to_csv('C:/Users/chernyshov/Python/t.csv')
