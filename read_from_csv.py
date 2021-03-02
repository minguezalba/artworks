import argparse
from artworks.interactors.artworks import read_artworks_from_csv


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Name of the CSV to parse data from")
    args = parser.parse_args()
    read_artworks_from_csv(args.filename)
