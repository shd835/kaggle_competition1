import pandas as pd
import glob

from utils import csv_to_listofDF

engagement_path = r"Data\Kaggle_Competition1\engagement_data"
engagement_df_list = csv_to_listofDF(engagement_path)

engagement_df = pd.concat(engagement_df_list)
engagement_df.reset_index(drop =True, inplace = True)
engagement_df.tail()

# Sanity check
sum = 0
for df in engagement_df_list:
    sum += len(df)
sum


engagement_df.isnull().sum()


