import pandas as pd
print(pd.__version__)
#task 1
subs=pd.Series([80,90,85,75],index=["maths", "science", "english", "history"])
#task 2
details_df=pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],"city": ["New York", "Los Angeles", "Chicago"],
    "age": [25, 30, 35] })
#task 3
print(details_df.city)
#task 4
print(details_df.iloc[-1])
#task 5
details_df.index=["ID1", "ID2", "ID3"]
#task 6
print(details_df.loc["ID2"])
#task 7
details_df.to_csv("People.csv", index=False)




