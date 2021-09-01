import pandas as pd
import glob


# +

def csv_to_listofDF(path):
    """
    This function gets the path to csv files, reads all the csv files in, converts them to dataframes, 
    adds distric_id as a column and saves them in a list
    
    Parameters
    -------------
    path: The path to CSV files
    
    
    """
    files = glob.glob(path + "\\" + "*.csv")
    df_list = []
    for file in files:
        district_id = file.split("\\")[-1].split(".")[0]
        df = pd.read_csv(file)
        df["district_id"] = [district_id] * len(df)
        df_list.append(df)
    
    return df_list
    


