# VLDB 2021 Crowd Science Challenge
This repository contains a baseline, data, and example of how to make a submission.

## How to make a submission
First, let's run a baseline.

`python3 baseline.py --input_file data/train/responses.csv --output_file submission.csv`

Create additional directories for the CodaLab scoring program.

`mkdir res ref & cp data/train/gt.csv ref/gt.csv & cp submission.csv res/submission.csv`

Run the scoring program.

`python3 evaluate_codalab.py . .` Now you can see your score on the train set in the file `scores.txt`.

Prepare a submission.

`zip -r submission.zip submission.csv`

Done! Upload `submission.zip` to CodaLab.

# Terms

[The full text of Terms and Conditions.](https://github.com/Toloka/VLDB2021_Crowd_Science_Challenge/blob/main/Terms.pdf)
