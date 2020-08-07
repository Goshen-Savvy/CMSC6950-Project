import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('bank.csv')

def balance_dur():
    fig=plt.figure(figsize=(14,10))
    sns.scatterplot(x='balance', y='duration', hue='marital', data=df)
    fig.savefig('marital_balance.png')
balance_dur()

