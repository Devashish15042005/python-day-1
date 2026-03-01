#Data cleaning and manipulation with pandas = here we are removing dupelicates and handling missing values, 
#and also we are doing some basic data analysis on the dataset.
import pandas as pd
df = pd.read_csv("jojo_dataset.csv")

#1. Drop irrelevant columns
#df = df.drop(columns=["Precision"])  here we are dropping the column "Precision" because it is not relevant to our analysis.

#2. Handle missing values
#df = df.dropna(subset= ["Stand_Name"])   here we pick off all the non stand powers like hamon or others
#df = df.fillna({"Stand_Name": "Unknown"}) here we change the non stand powers to unknown


#3. Fix inconsistent values
#df["Power_Type"] = df["Power_Type"].replace({"Other": "Non-Stand Users",
#                                            "Hamon": "Non-Stand Users",
#                                           "Spin": "Non-Stand Users"}) #here we change the other power type to non-stand users


#4. standardize text data
#df["Character"] = df["Character"].str.lower() here we change all the character names to lowercase to standardize the text data


#5.fix data types
#df["Status"] = df["Status"].astype(bool) here we change all the string data type to boolean for more readability
#as for we don't have the values in 0 or 1 we only have them in dead or alive so it shows true for all the charecters


#6. Remove duplicates
df = df.drop_duplicates()  # here we remove all the duplicate rows from the dataset
print(df.to_string())