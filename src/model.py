import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeCV
from category_encoders import OneHotEncoder


data = pd.read_csv('C:\\Users\\HB\\Section3\\Section3_Project\\movie.csv',encoding='euc-kr')

train_sk, test_sk = train_test_split(data, test_size=0.2, random_state=2)
train_sk, val_sk = train_test_split(train_sk, test_size=0.2, random_state=2)

feature = ['genreNm','dir_peopleNm','act_peopleNm1','act_peopleNm2','watchGradeNm']
target = 'salesAcc'

def divide_home_data(data):
    X = data[['genreNm','dir_peopleNm','act_peopleNm1','act_peopleNm2','watchGradeNm']]
    y = data['salesAcc']

    return X, y

X_train, y_train = divide_home_data(train_sk)
X_val, y_val = divide_home_data(val_sk)
X_test, y_test = divide_home_data(test_sk)

encoder = OneHotEncoder()
X_train_encoded = encoder.fit_transform(X_train)
X_val_encoded = encoder.transform(X_val)
X_test_encoded = encoder.transform(X_test)

def fit_ridge_regression(X_train_encoded, X_val_encoded, y_train, y_val):
    ridge = RidgeCV(alphas=np.arange(0.01, 2, 0.01), normalize=True, cv=5)

    ridge.fit(X_train_encoded, y_train)
    y_val_pred = ridge.predict(X_val_encoded)

    return ridge, encoder

ridge = fit_ridge_regression(X_train_encoded, X_val_encoded, y_train, y_val)