import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import glob


# +
#In this part form products_info, Primary Essential Function is divided in two parts: main and sub
products_df = pd.read_csv("D:\Education\ProjectShora\kaggle_competition1/products_info.csv")

primary_essential_main = []
primary_essential_sub = []
for p in products_df["Primary Essential Function"]:
    if(not pd.isnull(p)):
        p1 = p.split("-",1)[0].strip()
        primary_essential_main.append(p1)
    else:
        primary_essential_main.append(np.nan)
    
    if(not pd.isnull(p)):
        p2 = p.split("-",1)[1].strip()
        primary_essential_sub.append(p2)
    else:
        primary_essential_sub.append(np.nan)

products_df["primary_essential_main"] = primary_essential_main
products_df["primary_essential_sub"] = primary_essential_sub




# +
#pie chart for primary_essential function: percentage determining for primary_essential main function
c1=c2=c3=0

for p in products_df["primary_essential_main"]:
    if(not pd.isnull(p)):
        c1+= p.count("CM")
        c2+= p.count("LC")
        c3+= p.count("SDO")
        
fig, ax = plt.subplots(figsize=(16, 8))
fig.suptitle('Primary Essential Function', size = 20)
explode = (0.05,0.05,0.05)
labels = ['CM','LC','SDO']
sizes = [c1,c2,c3]
ax.pie(sizes, explode=explode, startangle=90, labels=labels, autopct='%1.2f%%', pctdistance=
      0.7, colors=["#8B3A62", "#CD8C95", "#ffd703"])
ax.add_artist(plt.Circle ((0,0),0.4,fc='white'))
plt.show()

#percentage determining for primary_essential main function

plt.figure(figsize=(16, 20))
sns.countplot(y='primary_essential_sub', data=products_df, order=products_df["primary_essential_sub"].value_counts().index)
plt.title("Primary Essential Function(Sub)", size=20)
plt.show()
# +
#Dropping Districts with NaN local

districts_df = pd.read_csv('districts_info.csv')
districts_df = districts_df[districts_df.locale.notna()].reset_index(drop=True)
#Merging
path = r"D:\Education\ProjectShora\kaggle_competition1\engagement_data" 
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    #district_id = filename.split("/")[0].split(".")[0]
    #df["district_id"] = district_id
    li.append(df)
    
engagement_df = pd.concat(li)
engagement_df = engagement_df.reset_index(drop=True)
engagement_df.head()

#pivot table for engagment_df: pct_access for all products in everyday during one year
#table = pd.pivot_table(engagement_df, values='pct_access', index=['time'],aggfunc=np.sum)

#pivot table for engagment_df: pct_access for all products in everymonth during one year
table = pd.pivot_table(engagement_df, values=['pct_access','lp_id'] , index=['time'],
                       aggfunc={'pct_access' : np.sum, 'lp_id' : np.count_nonzero})

table


# -






