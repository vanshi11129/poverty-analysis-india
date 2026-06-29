import pandas as pd
df=pd.read_csv(r"C:\Users\dhami\Downloads\Datasets\poverty_rate.csv")


df=df.drop_duplicates() #to remove any duplicate data

#print(df)


df=df.drop(columns="Note of Number of People who escaped Multidimensional Poverty (Estimated) (in lakh)") #to drop any useless columns 
df=df.drop(columns="Note of Headcount Ratio (%) - 2013-14") #to drop any useless columns 

#print(df)

df.rename(columns={'Headcount Ratio (%) - 2013-14': '2013_14_Headcount',
                   'Headcount Ratio (%) - 2022-23': '2022_23_Headcount',
                   'No. of People who escaped Multidimensional Poverty (Estimated) (in lakh)':'escaped_multidimensional_poverty',
                   'Sl. No.':'SR.NO'}, inplace=True)
          
print(df)

df["2013_14_Headcount"]=df["2013_14_Headcount"].replace('NA','')

df.to_excel(r"C:\Users\dhami\Downloads\cleaned_data.xlsx", index=False)
