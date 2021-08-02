import unittest
import PySignature #pylint: disable=import-error

class Test_Ranger(unittest.TestCase):
    def test_empty(self):
        PySignature.Ranger()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

