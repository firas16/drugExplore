from unittest import TestCase

from src.transformers.transformer import filter_drugs

class TestFind_drugs(TestCase):
    def test_find_one_drug(self):
        # Given
        drugs = ["DIPHENHYDRAMINE", "TETRACYCLINE"]
        title = "Use of Diphenhydramine as an Adjunctive Sedative for Colonoscopy in Patients Chronically on Opioids"

        # When
        result = filter_drugs(title, drugs)
        expected = {"DIPHENHYDRAMINE"}
        # Then
        assert result == expected

    def test_find_multiple_drugs(self):
        # Given
        drugs = ["DIPHENH", "DIPHENHYDRAMINE", "TETRACYCLINE", "TETRACYCLINES"]
        title = "Use of Diphenhydramine and TETRACYCLINE as an Adjunctive Sedative for Colonoscopy in Patients Chronically on Opioids"

        # When
        result = filter_drugs(title, drugs)
        expected = {"DIPHENHYDRAMINE", "TETRACYCLINE"}
        # Then
        assert result == expected

    def test_find_no_drugs(self):
        # Given
        drugs = ["DIPHENH", "DIPHENHYDRAMINE", "TETRACYCLINE", "TETRACYCLINES"]
        title = "Use of as an Adjunctive Sedative for Colonoscopy in Patients Chronically on Opioids"

        # When
        result = filter_drugs(title, drugs)
        expected = set()
        # Then
        assert expected == result

    def test_find_no_drugs_empty_title_and_drugs(self):
        # Given
        drugs = []
        title = ""

        # When
        result = filter_drugs(title, drugs)
        expected = set()
        # Then
        assert result == expected

    def test_remove_duplicate_drugs(self):
        # Given
        drugs = ["DIPHENH", "DIPHENHYDRAMINE", "TETRACYCLINE", "TETRACYCLINES"]
        title = "Use of Diphenhydramine and TETRACYCLINE and TETRACYCLINE as an Adjunctive Sedative for Colonoscopy in Patients Chronically on Opioids"

        # When
        result = filter_drugs(title, drugs)
        expected = {"DIPHENHYDRAMINE", "TETRACYCLINE"}
        # Then
        assert result == expected
