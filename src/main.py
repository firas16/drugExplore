
from src.readers.ReaderFactory import read
from src.transformers.transformer import extract_drug_from_title, format_dataset
import pandas as pd
pd.set_option('display.max_columns', None)

import yaml

# read config file
with open('src/cfg/config.yaml') as file:
    conf = yaml.safe_load(file)

#read configurations
clinical_trial_conf = conf['dataset']['clinical_trial']
drugs_conf = conf['dataset']['drugs']
pubmed_conf = conf['dataset']['pubmed']

# read datasets
clinical_trials_df = read(clinical_trial_conf)
drugs_df = read(drugs_conf)
pubmed_df = read(pubmed_conf)

# extact list of drugs
drugs = drugs_df['drug'].tolist()

#format datasets
clinical_trials_df = format_dataset(clinical_trials_df, clinical_trial_conf)
pubmed_df = format_dataset(pubmed_df, pubmed_conf)

# add type column
clinical_trials_df['type'] = 'clinical_trial'
pubmed_df['type'] = 'pubmed'

#extract drugs from datasets
clinical_trials_df = extract_drug_from_title(clinical_trials_df, 'title', 'drug', drugs)
pubmed_df = extract_drug_from_title(pubmed_df, 'title', 'drug', drugs)


# concat clinical trials and pubmed data
data = pd.concat([clinical_trials_df, pubmed_df], ignore_index=True)

data.to_csv("test/resources/result.csv")
print(data.head(10))

#functional queries
#records format
data.to_json(path_or_buf=conf['output']['path_records'], orient="records")

#second format
data["details"] = list(zip(data.journal, data.id, data.date))
data["details"] = data["details"].map(lambda elem:  [{'journal': elem[0]},{'id': elem[1]}, {'date': elem[2]}])
result= data[['drug', 'details']]
result = result.groupby("drug")['details'].agg(list).reset_index().set_index('drug')

json_output_format = result\
    .to_json(path_or_buf= conf['output']['path_oriented_drugs'], orient='index', date_format='iso', force_ascii=False)


#get drugs referenced in journals in 2020

drugs_referenced_in_journals = data[data['drug'].notnull()]
drugs_referenced_in_journals = drugs_referenced_in_journals.drop_duplicates(subset=['journal', 'date', 'drug'])
# select distinct drug, journal from data where data >= '2020-01-01'
import datetime as dt
ref_date = dt.datetime.strptime("01-01-2020", "%d-%m-%Y").date()
data_filtered_by_date = drugs_referenced_in_journals[drugs_referenced_in_journals['date'] >= ref_date]

#get drugs referenced in clinical trials
drugs_in_clinical_trials = data[data["type"] == "clinical_trial"]









