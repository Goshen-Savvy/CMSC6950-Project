import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('bank.csv')

def duration():
    sns.set(rc={'figure.figsize':(12,12)})
    sns.set_style('whitegrid')
    avg_duration = df['duration'].mean()

    lst = [df]
    df["duration_status"] = np.nan

    for col in lst:
        col.loc[col["duration"] < avg_duration, "duration_status"] = "below_average"
        col.loc[col["duration"] > avg_duration, "duration_status"] = "above_average"
        
    pct_term = pd.crosstab(df['duration_status'], df['deposit']).apply(lambda r: round(r/r.sum(), 2) * 100, axis=1)


    ax = pct_term.plot(kind='bar', stacked=False, cmap='RdBu')
    plt.title("The Impact of Duration \n in Opening a Term Deposit", fontsize=18)
    plt.xlabel("Duration Status", fontsize=18)
    plt.ylabel("Percentage (%)", fontsize=18)

    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.02, p.get_height() * 1.02))
    plt.tight_layout()
    plt.savefig('duration.png')
duration()