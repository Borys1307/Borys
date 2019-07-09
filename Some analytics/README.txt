Some analytics couples with parsing of some info
Files with Analytics in name parse json from file ata.json and plot pie and bar diagrams for all info in json and for partial info.
Files with duples in name parse xlsx files and collect info into single data frame.
File Count_Duples counts all duples in all tables in xlsx files.
File Table_Duples creates table without duples (if in line 40 df1 = df1.loc[df1['Domain'].isin(listw) == False]) 
or only for duples (if in line 40 df1 = df1.loc[df1['Domain'].isin(listw))
