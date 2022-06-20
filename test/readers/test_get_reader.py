from src.readers.CSVReader import CSVReader
from src.readers.JSONReader import JSONReader
from src.readers.ReaderFactory import read, get_reader
from unittest import TestCase

class TestReader(TestCase):
    def test_read_json(self):
        # Given
        config = {'format': 'json', 'path': '../../test/resources/pubmed.json', 'columns_mapping': {'date': 'date_event'}, 'dates': [{'name': 'date_event', 'format_date': '%Y-%m-%d'}]}
        # When
        reader = get_reader(config)
        # Then
        assert isinstance(reader, JSONReader)
    def test_read_csv(self):
        # Given
        config = {'format': 'csv', 'sep': ',', 'header': 0, 'path': '../../test/resources/drugs.csv', 'columns_mapping': {'date': 'date_event'}, 'dates': [{'name': 'date_event', 'format_date': '%Y-%m-%d'}]}
        # When
        reader = get_reader(config)
        # Then
        assert isinstance(reader, CSVReader)

