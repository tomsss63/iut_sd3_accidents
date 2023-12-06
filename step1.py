import pandas as pd

# Charger les fichiers CSV
carac = pd.read_csv("data/carac.csv", sep=';')
lieux = pd.read_csv("data/lieux.csv", sep=';')
veh = pd.read_csv("data/veh.csv", sep=';')
vict = pd.read_csv("data/vict.csv", sep=';')

# Fusionner les DataFrames
victime = vict.merge(veh, on=['Num_Acc', 'num_veh'])
accident = carac.merge(lieux, on='Num_Acc')
result_df = victime.merge(accident, on='Num_Acc')

result_df.to_csv("step1/merged_data.csv", index=False)

print("ok")
