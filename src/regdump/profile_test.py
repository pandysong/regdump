import unittest
from regdump.profile import parse_profile


class TestStringMethods(unittest.TestCase):

    def test_parser(self):
        parse_profile("rga2_alpha_ctrl0.reg", None)


if __name__ == '__main__':
    unittest.main()