import pandas as pd
import matplotlib.pyplot as plt
from autorank import autorank, create_report, plot_stats, latex_table

df = pd.read_csv('bank.csv')

numrecords = 1000

df_Grouped_marital = df.groupby('marital')

dic = {}
for x, item in df_Grouped_marital:
    dic[x] = list(item['duration'].tail(numrecords))

df_bank = pd.DataFrame(dic)
df_mean = df_bank.mean()
print(df_mean)
print(df_bank)
res = autorank(df_bank, alpha=0.05, verbose=False)
print(res)
df_mean.plot(kind='bar')
plt.title('Statistics')
plt.xlabel('Marital Status')
plt.ylabel('Duration')
plt.tight_layout()
plt.savefig('mean.png')
