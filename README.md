# VLDB 2021 Crowd Science Challenge Starter Kit
This repository contains startket kit to jump into the competition. Specifically, it contains a simple baseline, train data, and evaluation code -- everything you need to make a first submission!

## Train Data

The `data/train` folder contains train data which consists of transcriptions of 9,700 audios made by 1,879 different annotators who participated in the data-collection process. There are two files in the train data:

- Ground Truth (gt.csv). This file contains ids of audios and ground truth texts recorded in these audios.

- Crowd Transcriptions (responses.csv). This file contains triples (id of audio, transcription, id of annotator).

Your model should work with crowd transcriptions to aggregate them into a single transcription of each audio. Please see [Competition Goal and Evaluation](https://competitions.codalab.org/competitions/30835#learn_the_details-evaluation) section on the competition page for more details.


## How to make a submission
We created a simple baseline program that does a trivial aggregation -- it takes the first transcription of each audio and uses it as a final result. To run this program, execute the following command:

`python3 baseline.py --input_file data/train/responses.csv --output_file submission.csv`

The `submission.csv` file now can be uploaded to Yandex.Contest.

## How to evaluate your submission locally

To evaluate your submission with our scoring program, run the following command:

`python3 evaluate.py --gt data/train/gt.csv --submission submission.csv`

The output of this command will be your score.
