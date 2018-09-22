import io
import sys
import unittest
from planets import *


class TestPlanets(unittest.TestCase):

    def test_01(self):
        sys.stdin = io.StringIO("136")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \n"\
                       "On Mars you would weigh 51.68 pounds.\n"\
                       "On Jupiter you would weigh 318.24 pounds."
        weight_on_planets()
        # print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
