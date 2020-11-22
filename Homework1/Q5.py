import pandas as pd

missing_values = ["n/a", "na", "NaN"]
housing_price = pd.read_csv("boston_csv.csv", na_values = missing_values)

# 결측치가 있는 관측치 제거
housing_price = housing_price.dropna()
print(housing_price)
