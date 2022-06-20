import pandas as pd



df = pd.read_json("test/resources/records.json")
journals_with_drug_appearances = df.drop_duplicates(['journal', 'drug']).groupby("journal")['drug'].count()
print("journal with max drug appearances : ", journals_with_drug_appearances.idxmax())
