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
answe = {}
df1 = pd.DataFrame()
for i in range(len(filenames)):        
    xl_file = pd.ExcelFile(filenames[i])
    dfs = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}
    name = dfs['Report Details']['Unnamed: 1'][2].split()[2]
    if name not in dfs1:
        dfs1[name] = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names if sheet_name !='Report Details' and sheet_name !='Monthly Data'}    
    df = dfs1[name]['Aggregated Data for Time Period']
    df = df.loc[df['Traffic Share'] > 0.01]
    answe [name] = df
    df1 = df1.append(df, ignore_index=True)
sites = pd.read_csv('C:/Users/chernyshov/Python/t.csv')
#print(df1['Traffic Share'])
listw = []
for i in sites['Domain']:
    listw.append(i)
df1 = df1.loc[df1['Domain'].isin(listw) == False]
df1 = df1.sort_values(by='Domain', ascending = True)
print(df1)
df1.to_csv('C:/Users/chernyshov/Python/t1.csv')	 
