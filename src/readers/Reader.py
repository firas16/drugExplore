
from pandas import DataFrame

class ReaderInterface:
    def load(self, path: str) -> DataFrame:
        pass


