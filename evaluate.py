import argparse
import pandas as pd
from jiwer import wer


def wer_scorer(gt, pred):
    return max(1 - wer(gt, pred), 0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gt', type=str, default='gt.csv')
    parser.add_argument('--submission', type=str, default='submission.csv')
    args = parser.parse_args()

    gt = pd.read_csv(args.gt)
    submission = pd.read_csv(args.gt)

    gt['pred'] = submission.set_index('task')['output']

    total_score = 0.0
    for _, row in gt.iterrows():
        if pd.isna(row['output']):
            raise ValueError('Prediction has unknown tasks')
        elif not pd.isna(row['pred']):
            total_score += wer_scorer(row['output'].split(), row['pred'].split())

    print(total_score / len(gt))


if __name__ == '__main__':
    main()
