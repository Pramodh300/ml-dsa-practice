import pandas as pd
data = {
    "Brands" : ["samsung", "Apple", "Moto", "Vivo"],
    "Price" : [50000, 50000, 30000, 35000]
}
df = pd.DataFrame(data)

#Select columns
df["Price"]
print(df.Price)

#Filter row
print(df.loc[df["Price"]>40000])

#Add column
df["Tax"] = df["Price"] * 0.1
print(df)

#Sort values
sort_values = df.sort_values("Price", ascending=True)
print(sort_values)

print(df.isnull().sum())