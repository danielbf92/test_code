import unittest

from .main import get_commission

class TestUtils(unittest.TestCase):
    def test_is_prime(self):
        # Test in get_commission
        self.assertEqual(get_commission("2021/07/15"),"15%")

if __name__ == '__main__':
    unittest.main()
