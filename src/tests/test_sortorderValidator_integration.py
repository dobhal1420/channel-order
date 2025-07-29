import unittest
import os
from services.sortorderValidator import SortOrderValidator
from util.source import SourceOptions

class TestSortOrderValidatorIntegration(unittest.TestCase):
    def setUp(self):
        self.csv_file = os.path.join(os.path.dirname(__file__), "data", "sample_tv.csv")
        self.json_file = os.path.join(os.path.dirname(__file__), "data", "sample_presort.json")
        self.wrong_csv_file = os.path.join(os.path.dirname(__file__), "data", "sample_tv_wrong_order.csv")

    def test_validate_integration(self):
        validator = SortOrderValidator(SourceOptions.satellite, self.csv_file, self.json_file)
        result, message = validator.validate()
        self.assertTrue(result)
        self.assertIn("LCN order for pre-sort channels on TV matches perfectly with pre-sort file", message)
        
    def test_validate_integration_negative(self):

        validator = SortOrderValidator(SourceOptions.satellite, self.wrong_csv_file, self.json_file)
        result, message = validator.validate()
        self.assertFalse(result)
        self.assertIn("Validation Failed:", message)

if __name__ == "__main__":
    unittest.main()