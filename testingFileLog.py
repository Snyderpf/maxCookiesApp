import unittest
import fileLog as file
from datetime import datetime


class TestCase(unittest.TestCase):
    def test_the_time(self):
        """testing the(get-time) function"""

        temp_time = datetime.strptime("2015-03-27T15:49:34Z", "%Y-%m-%dT%H:%M:%S%z")
        # correct_date to be  checked against check_time
        correct_date = temp_time.strftime("%Y-%m-%d")
        check_time = file.get_time(temp_time)
        self.assertEqual(correct_date, check_time)


if __name__ == '__main__':
    unittest.main()
