# -*- coding: utf-8 -*-

import argparse
import sys
from .rcp import get_poll_data, to_csv

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

parser = argparse.ArgumentParser()
parser.add_argument("url", nargs='+', help="The url of the polling data.")
parser.add_argument("--output", nargs="?", help="The output file name.")
args = parser.parse_args()


def main():
    for url in args.url:
        filename = args.output if args.output else url.rsplit('/', 1)[-1][:-5] + ".csv"
        poll_data = get_poll_data(url, csv_output=True)
        if not poll_data:
            sys.exit("No poll data found.")
        print("Downloading: %s" % filename)
        to_csv(filename, poll_data)


if __name__ == '__main__':
    main()
