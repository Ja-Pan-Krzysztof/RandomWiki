import argparse


def main():
    arg_parser = argparse.ArgumentParser(
        prog='Wikipedia',
        description='Copyright by Ja',
        # usage='%(prog)s [option] function firstPath lastPath',
        epilog='have you a nice day :)',
        fromfile_prefix_chars='@',  # inportowanie argumentów z pliku txt
        allow_abbrev=False,  # pisanie skrutowo argumentów
    )
    arg_parser.add_argument(
        'Language',
        metavar='language',
        type=str,
        help='Choice language lang [pl, en, fr, kr, ...]'
    )
    arg_parser.add_argument(
        'Count',
        metavar='many',
        type=int,
        help='Enter how many you have random wiki',
        default=1
    )
    args = arg_parser.parse_args()

    return args
