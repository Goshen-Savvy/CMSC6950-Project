import pandas as pd
import matplotlib.pyplot as plt
from autorank import autorank, create_report, plot_stats, latex_table

df = pd.read_csv('bank.csv')

numrecords = 1000
# pd.set_option('display.max_columns', 8)
df_Grouped_marital = df.groupby('marital')
# print(list(df_Grouped_marital))
dic = {}
for x, item in df_Grouped_marital:
    dic[x] = list(item['duration'].tail(numrecords))
# print(dic)
# print(list(df_Grouped_marital))
df_bank = pd.DataFrame(dic)
df_mean = df_bank.mean()
print(df_mean)
print(df_bank)
res = autorank(df_bank, alpha=0.05, verbose=False)
print(res)
create_report(res)
plot_stats(res)
plt.savefig('stat_auto_rank.png')
plt.show()
