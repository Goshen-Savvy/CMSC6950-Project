import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

import xgboost as xgb
from sklearn.model_selection import train_test_split #split
from sklearn.metrics import accuracy_score #metrics

df = pd.read_csv('report/bank.csv')

def data_set():
    msno.matrix(df)
    plt.ylabel('Records in the dataset')
    plt.xlabel('Bank Dataset')
    plt.savefig('missing_data.png')
    
data_set()


def get_dummy_from_bool(row, column_name):
    ''' Returns 0 if value in column_name is no, returns 1 if value in column_name is yes'''
    return 1 if row[column_name] == 'yes' else 0

def get_correct_values(row, column_name, threshold, df):
    ''' Returns mean value if value in column_name is above threshold'''
    if row[column_name] <= threshold:
        return row[column_name]
    else:
        mean = df[df[column_name] <= threshold][column_name].mean()
        return mean

def clean_data(df):

    cleaned_df = df.copy()
    
    #convert columns containing 'yes' and 'no' values to boolean variables and drop original columns
    bool_columns = ['default', 'housing', 'loan', 'deposit']
    for bool_col in bool_columns:
        cleaned_df[bool_col + '_bool'] = df.apply(lambda row: get_dummy_from_bool(row, bool_col),axis=1)
    
    cleaned_df = cleaned_df.drop(columns = bool_columns)
    
    #convert categorical columns to dummies
    cat_columns = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']
    
    for col in  cat_columns:
        cleaned_df = pd.concat([cleaned_df.drop(col, axis=1),
                                pd.get_dummies(cleaned_df[col], prefix=col, prefix_sep='_',
                                               drop_first=True, dummy_na=False)], axis=1)
    
    #drop irrelevant columns
    cleaned_df = cleaned_df.drop(columns = ['pdays'])
    
    #impute incorrect values and drop original columns
    cleaned_df['campaign_cleaned'] = df.apply(lambda row: get_correct_values(row, 'campaign', 34, cleaned_df),axis=1)
    cleaned_df['previous_cleaned'] = df.apply(lambda row: get_correct_values(row, 'previous', 34, cleaned_df),axis=1)
    
    cleaned_df = cleaned_df.drop(columns = ['campaign', 'previous'])
    
    return cleaned_df

    #cleaned_df = clean_data(df)

def xgbML():
    cleaned_df = clean_data(df)
    x = cleaned_df.drop(columns = 'deposit_bool')
    y = cleaned_df[['deposit_bool']]
    TEST_SIZE = 0.3
    RAND_STATE = 42

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = TEST_SIZE, random_state=RAND_STATE)

    xg_cl = xgb.XGBClassifier(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75,
                           colsample_bytree=1, max_depth=7)

    xg_cl.fit(x_train,y_train.squeeze().values)

    #calculate and print scores for the model for top 15 features
    y_train_preds = xg_cl.predict(x_train)
    y_test_preds = xg_cl.predict(x_test)

    print('XGB accuracy score for train: %.3f: test: %.3f' % (
            accuracy_score(y_train, y_train_preds),
            accuracy_score(y_test, y_test_preds)))
xgbML()