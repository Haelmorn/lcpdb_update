import pandas as pd 

df_json = pd.read_json("fasta_aa.json")
df_json.to_excel("fasta_aa.xlsx", index=None, header=True)