
from src.readers.Reader import ReaderInterface
import pandas as pd
from pandas import DataFrame
import os
class CSVReader(ReaderInterface):
    def __init__(self, sep, header):
        self.sep = sep
        self.header= header
    def load(self, path: str) -> DataFrame:
        return pd.read_csv(path,sep=self.sep, header=self.header)