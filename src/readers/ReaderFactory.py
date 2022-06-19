from src.readers.CSVReader import CSVReader
from src.readers.JSONReader import JSONReader


def read(conf: dict):
    """

    :param path: str, path to the file
    :param format: str, format of the file
    :return: dataframe
    """
    reader = get_reader(conf)
    return reader.load(conf['path'])


def get_reader(conf: dict):
    """

    :param format: str format of the file csv or json
    :return: Reader
    """
    if (conf['format'] == "csv"):
        return CSVReader(conf['sep'], conf['header'])
    elif (conf['format'] == "json"):
        return JSONReader()
    else:
        raise ValueError("format {} not handled in reader.".format(format))
