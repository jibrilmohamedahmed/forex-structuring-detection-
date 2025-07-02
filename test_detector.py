import unittest
from forex_structuring_detection.models.detector import detect_structures
import pandas as pd

class TestDetector(unittest.TestCase):
    def test_detect_structures(self):
        dummy_data = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        result = detect_structures(dummy_data)
        self.assertIn('structures_found', result)

if __name__ == '__main__':
    unittest.main()