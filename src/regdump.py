from regdump.profile import parse_profile, inteprete_bits

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest="profile",
                        help='the profile define the register bitmap',
                        required=True)
    parser.add_argument('value', type=str,
                        help='register value to be intepreted')
    args = parser.parse_args()
    profile = parse_profile(args.profile, None)
    if args.value.startswith("0x"):
        value = int(args.value, 16)
    else:
        value = int(args.value, 10)
    inteprete_bits(profile, value)
