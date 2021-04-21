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

As we have the predictions stored in the `submission.csv`, we can create a submission archive that can be [uploaded](https://competitions.codalab.org/competitions/30835#participate) to CodaLab (make sure you select the right phase of the competition):

`zip -r MyFirstSubmission.zip submission.csv`

**Importantly**, the submission archive must contain a file named `submission.csv` inside with columns `task` (ID of the task) and `output` (predicted annotation). The name of the archive can be arbitrary.

## How to evaluate your submission locally

To run a CodaLab scoring program, create additional directories using the following command:

`mkdir res ref & cp data/train/gt.csv ref/gt.csv & cp submission.csv res/submission.csv`

Now you can run the scoring program (you may need to install the `jiwer` package using `pip install jiwer`):

`python3 evaluate_codalab.py . .` 

The output of the scoring function will be stored in `scores.txt`.
