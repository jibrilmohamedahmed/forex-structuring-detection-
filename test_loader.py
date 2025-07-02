import unittest
from forex_structuring_detection.data.loader import load_data

class TestLoader(unittest.TestCase):
    def test_load_data(self):
        # Will fail unless you have the data file; modify as needed
        data = load_data()
        self.assertTrue(data is None or hasattr(data, 'shape'))

if __name__ == '__main__':
    unittest.main()