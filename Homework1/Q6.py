import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

missing_values = ["n/a", "na", "NaN"]
housing_price = pd.read_csv("boston_csv.csv", na_values = missing_values)

# 결측치가 있는 관측치 제거
housing_price = housing_price.dropna()
print(housing_price)

# 각 변수별 요약 통계
print(housing_price.describe())

# 상관관계
print(housing_price.corr())

# heatmap
plt.figure(figsize=(15,15))
sns.heatmap(data = housing_price.corr(), annot=True, cmap='Blues')
plt.show()
