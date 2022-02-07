import unittest
from regdump.profile import parse_profile, inteprete_bits


class TestStringMethods(unittest.TestCase):

    def test_parser(self):
        print(parse_profile("rga2_alpha_ctrl0.reg", None))

    def test_parser1(self):
        print(parse_profile("rga2_alpha_ctrl1.reg", None))

    def test_parser2(self):
        profile = parse_profile("rga2_alpha_ctrl0.reg", None)
        print("\n")
        inteprete_bits(profile, 0x381A381A)

    def test_parser3(self):
        profile = parse_profile("rga2_alpha_ctrl1.reg", None)
        print("\n")
        inteprete_bits(profile, 0x381A381A)

    def test_parser3(self):
        print("\n")
        profile = parse_profile("rga2_alpha_ctrl0.reg", None)
        print("\nctrl0 = 0x807f9")
        inteprete_bits(profile, 0x807f9)
        profile = parse_profile("rga2_alpha_ctrl1.reg", None)
        print("\nctrl1 = 0x90390")
        inteprete_bits(profile, 0x90390)
        profile = parse_profile("rga2_fading_ctrl.reg", None)
        print("\nfading ctrl = 0xff00")
        inteprete_bits(profile, 0xff00)


if __name__ == '__main__':
    unittest.main()
