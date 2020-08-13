import pandas as pd 

df_json = pd.read_json("fasta_nucl.json")
df_json.to_excel("fasta_nucl.xlsx", index=None, header=True)