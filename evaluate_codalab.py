import pandas as pd
from jiwer import wer
import argparse
import os


def process_data(ground_truth, predictions):
    result = ground_truth.set_index('task')
    result['pred'] = predictions.set_index('task')['output']
    return list(result['output']), list(result['pred'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir')
    parser.add_argument('output_dir')
    args = parser.parse_args()

    pred_dir = os.path.join(args.input_dir, 'res')
    gold_dir = os.path.join(args.input_dir, 'ref')

    if not os.path.isdir(pred_dir):
        raise RuntimeError('{} does not exist'.format(pred_dir))

    if not os.path.isdir(gold_dir):
        raise RuntimeError('{} does not exist'.format(args.output_dir))

    predictions = pd.read_csv(os.path.join(pred_dir, 'submission.csv'))
    ground_truth = pd.read_csv(os.path.join(gold_dir, 'gt.csv'))
    gt, pred = process_data(ground_truth, predictions)
    wer_score = 0.0
    for i, gt_str in enumerate(gt):
        wer_score += wer(gt_str.split(), pred[i].split())
    score = wer_score / len(gt) * 100
    output_filename = os.path.join(args.output_dir, 'scores.txt')
    with open(output_filename, 'w') as f:
        print('WER:{:f}'.format(score), file=f)


if __name__ == '__main__':
    main()
