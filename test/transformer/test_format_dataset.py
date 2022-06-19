from unittest import TestCase
import pandas as pd
from src.transformers.transformer import format_dataset

class TestFormat_dataset(TestCase):
    def test_format_dataset(self):
        #Given
        data = {'event': [1,2,3,4], 'date': ['15/01/2020','16/01/2020','25/01/2020','27/01/2020']}
        df = pd.DataFrame(data)
        config = {'columns_mapping': {'date': 'date_event'}, 'dates': [{'name': 'date_event', 'format_date': '%Y-%m-%d'}]}
        #When
        result = format_dataset(df, config)
        data_expected = {'event': [1,2,3,4], 'date_event': ['2020-01-15', '2020-01-16', '2020-01-25', '2020-01-27']}
        df_expected = pd.DataFrame(data_expected)
        df_expected["date_event"] = pd.to_datetime(df_expected["date_event"])
        df_expected["date_event"] = df_expected["date_event"].dt.date
        #Then
        okay =  pd.testing.assert_frame_equal(result, df_expected)
        assert okay is None