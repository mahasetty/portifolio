importing required dpenedencies
import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading Titanic dataset from example into dataframe named td(Titanic Dataset)
td=sb.load_dataset("titanic")
#Cleaning table  removing columns class, embarked, alive and adult_male as they are redundant and unncessary
td=td.drop(labels=["class", "embarked", "alive","adult_male"], axis=1)
#Removing records with missing values in Column fare, embark_town, age and sex as these are columns that
# used to group by and cuts
td=td.dropna(subset=["fare","embark_town","sex","age"])
#Assigning index as Column title for index in dataset
td.index.name="index"
#Grouping dataset by Embark Town, Sex and Index.
#Used index to display all the Rows in dataset and group them by Emabark Town and Sex
newGbytd=td.groupby(["embark_town","sex","index"])
newGbytd.first()
#grouping by emabark_town an sex and calculating total fare payed by emabark town and grouped by sex
newGbytdtotal=td.groupby(["embark_town","sex"])
#using aggregate functions to calculate total and mean
aggregate_Df=newGbytdtotal[["fare"]].agg(["sum"])
aggregate_Df["Fare Mean"]=newGbytdtotal[["fare"]].agg(["mean"])
aggregate_Df
#Based on Findings Average fare Price payed on 
#Counting notNull values NaN on deck Column
cntNavalue=td["deck"].notnull().sum()
cntNavalue
#Adding a new column to data frame and assigning values Minor if the age is less than 18, adult if age is between 18 to 45 
#Middle Aged if age is between 45 and 65 and Old if the age is 65 and above
td["number_labels"]=pd.cut(td["age"], bins=[0, 18, 45, 65, np.inf], labels=["Minor", "Adult","Middle Aged", "Old"])
td
