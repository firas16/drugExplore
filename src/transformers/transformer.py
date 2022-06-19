
from pandas import DataFrame
import pandas as pd

def filter_drugs(title, drugs):
    """
    extracts set of drugs present in title
    :param title: str string in which we search for drugs
    :param drugs: list[str] list of drugs to search for
    :return: list of drugs found in title
    """
    words = title.upper().split(' ')
    drugs = set(filter(lambda x: x in drugs, words))
    return (drugs)


def extract_drug_from_title(df: DataFrame, titleCol: str, drugCol: str, drugs: list[str]):
    """
    adds a column drugs to the dataframe using column titleCol and explodes dataframe.
    :param df: dataframe
    :param titleCol: column from which we extract the drugs
    :param drugCol: nameof the column to create
    :param drugs: list of drugs to search fo in the titleCol
    :return: dataframe df with column drugCol extarcted from titleCol
    """
    df[drugCol] = df[titleCol].map(lambda x: filter_drugs(x, drugs))
    df = df.explode(drugCol)
    return df

def format_dataset(df: DataFrame, conf: dict) -> DataFrame:
    """
    applies all different transformations to format dataframe using config
    column renaming
    date formatting
    :param df:
    :param conf:
    :return:
    """
    # format column  names
    if("columns_mapping" in conf.keys()):
        df = df.rename(columns=conf["columns_mapping"])
    # format date columns
    for elem in conf["dates"]:
        name = elem['name']
        format_date = elem['format_date']
        #df[name] = df[name].apply(parse)
        df[name] = pd.to_datetime(df[name], infer_datetime_format=True)
        df[name].dt.strftime(format_date)
        df[name] = df[name].dt.date
    return df