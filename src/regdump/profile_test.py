import unittest
from regdump.profile import parse_profile, inteprete_bits


class TestStringMethods(unittest.TestCase):

    def test_parser(self):
        print(parse_profile("rga2_alpha_ctrl0.reg", None))


if __name__ == '__main__':
    unittest.main()
