# Train Data

The `data/train` folder contains train data which consists of transcriptions of 9,700 audios made by 1,879 different annotators who participated in the data-collection process. There are two files in the train data:

- Ground Truth (`gt.csv`). This file contains ids of audios and ground truth texts recorded in these audios.

- Crowd Transcriptions (`responses.csv`). This file contains triples (id of audio, transcription, id of annotator).

Your model should work with crowd transcriptions to aggregate them into a single transcription of each audio. Please see our starter kit on the [main GitHub page](https://github.com/Toloka/VLDB2021_Crowd_Science_Challenge).
