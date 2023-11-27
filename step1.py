import os
import pandas as pd

# Définir le chemin vers les fichiers
chemin = "./Desktop/IUT_SD3_Github/iut_sd3_accidents/data"

# Construire les chemins complets vers les fichiers
file1 = os.path.join(chemin, "carac.csv")
file2 = os.path.join(chemin, "lieux.csv")
file3 = os.path.join(chemin, "veh.csv")
file4 = os.path.join(chemin, "vict.csv")

# Lire les fichiers
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)
df4 = pd.read_csv(file4)

# Fusionner les DataFrames
merged_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Afficher le DataFrame fusionné
print(merged_df)

# Écrire le DataFrame fusionné dans un nouveau fichier
merged_df.to_csv(os.path.join(chemin, "merged_data.csv"), index=False)
