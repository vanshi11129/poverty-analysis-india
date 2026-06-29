
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_excel(r"C:\Users\dhami\Downloads\cleaned_data.xlsx")

b = [0.05] * len(df)

df.plot(x="State/UT",y=["2013_14_Headcount","2022_23_Headcount"],kind="bar",figsize=(14, 6))

plt.show()

df.plot(x=["2013_14_Headcount","2022_23_Headcount"],
        y="escaped_multidimensional_poverty",
        kind="pie",labels=df['State/UT'],explode=b)

plt.show()

sns.pairplot(df, vars=["2013_14_Headcount", "2022_23_Headcount", "escaped_multidimensional_poverty"])
plt.suptitle("Overall Correlation Matrix of Poverty Metrics")
plt.show()
