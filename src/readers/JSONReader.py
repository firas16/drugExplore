
from src.readers.Reader import ReaderInterface
import pandas as pd
from pandas import DataFrame

class JSONReader(ReaderInterface):

    def load(self, path: str) -> DataFrame:
        return pd.read_json(path)