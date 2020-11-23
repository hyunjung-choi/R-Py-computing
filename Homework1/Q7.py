from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd

missing_values = ["n/a", "na", "NaN"]
housing_price = pd.read_csv("boston_csv.csv", na_values = missing_values)

# 결측치가 있는 관측치 제거
housing_price = housing_price.dropna()

lm = LinearRegression()  # Create Linear Regression Object
X = housing_price[['LSTAT']] # 하위계층 비율(LSTAT)이 독립변수
Y = housing_price['MEDV'] # 본인 소유의 주택가격인 MEDV가 종속변수

# Training Set은 표본의 75%
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.75, random_state=0)

# 회귀 분석 추정 계수 (상수항, 기울기)
lm.fit(x_train, y_train)
print("Intercept: ", lm.intercept_)
print("Coef: ", lm.coef_)

# Training Set의 결정계수(R^2)와 MSE
y_train_hat = lm.predict(x_train)
print("Training Set의 결정계수(R^2): ", lm.score(x_train, y_train))
print("Training Set의 MSE: ", mean_squared_error(y_train, y_train_hat))

# Test Set의 MSE
y_test_hat = lm.predict(x_test)
print("Test Set의 MSE: ", mean_squared_error(x_test, y_test))
