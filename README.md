# VLDB 2021 Crowd Science Challenge Starter Kit
This repository contains startket kit to jump into the competition. Specifically, it contains a simple baseline, train data, and evaluation code -- everything you need to make a first submission!

## Overview of the competition

Speech-to-text projects are ubiquitous on crowdsourcing platforms. However, individual annotators on these platforms are often unskilled or even malicious. Thus, transcriptions collected on crowdsourcing platforms may be noisy. To account for this problem, each audio is typically transcribed into text by multiple crowd annotators. But how do we aggregate these multiple transcriptions to obtain the final high-quality transcription? The goal of this competition is to answer this question. Specifically, the goal of participants is to build a model that aggregates multiple transcriptions of an audio obtained on a crowdsourcing platform into a single transcription. 

For this competition, we annotated a large number of audios on the [Toloka](https://toloka.ai) crowdsourcing platform and release this real data to participants. Please read the "Dataset" section (under "Participate" tab) to understand the format of the data.

### Metric

To compare predictions made by participants with ground truth texts, we use the [Word Error Rate (WER)](https://en.wikipedia.org/wiki/Word_error_rate) metric. It is a widely used metric for evaluating automatic speech recognition systems. We use the Python implementation of WER from [jiwer](https://github.com/jitsi/jiwer/) package. The format of submissions, code of our scoring function, and data are available on our [GitHub.](https://github.com/Toloka/VLDB2021_Crowd_Science_Challenge)

### Phases

**Practice phase** In the practice phase, participants work with training data which has ground truth labels publicly released. Participants can submit their predictions made on train data to CodaLab to try out our scoring system.

**Evaluation phase** At the beginning of the evaluation phase, we will release test data transcriptions (ground truth labels for the test data will not be released). The test data consists of two parts: public and private (the split on public and private parts are not known to participants). Throughout the evaluation phase, submissions will be evaluated on the public part of the test data and the best score achieved by each team will be stored on the public leaderboard. 

**End of competition**
After the final submission deadline, we will evaluate the *last* submission of each team on the private part of the test data. The final standing of the teams will be determined by their scores of the private test data.

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
