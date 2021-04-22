#!/usr/bin/env python3

import pandas as pd
import numpy as np
import argparse
from tqdm.auto import tqdm


def filter_text(text):
    char_set = set(list(' qwertyuiopasdfghjklzxcvbnm\''))
    return ''.join([c for c in text.strip().lower() if c in char_set])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file')
    parser.add_argument('--output_file')
    args = parser.parse_args()

    data = pd.read_csv(args.input_file)
    data['output'] = data['output'].apply(lambda text: filter_text(text))

    aggregates = data.groupby('task').apply(lambda x: x.iloc[0])['output']
    aggregates = aggregates.apply(lambda x: ' ' if len(x) == 0 else x)
    aggregates.to_csv(args.output_file)


if __name__ == '__main__':
    main()
