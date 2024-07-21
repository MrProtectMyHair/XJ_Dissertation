# XJ_Dissertation
---

## Please see the results.xlsx first.
---

## Introduction

The experimental results and related files are included in this repository. 

### Human_Speeches

#### LibriSpeech
There are 24 .wav files selected from the Speech Recognition Corpus called **LibriSpeech**. 
The speeches are from 8 different speakers, 4 male speakers and 4 female speakers. The durations of the speeches are from 3 sec to 24 sec. Also, the official transcriptions of the speeches were displayed.

The complete corpus can be downloaded from the link: https://www.openslr.org/12
The details of this corpus can be found: https://ieeexplore.ieee.org/document/7178964

#### VCC 2018
96 .wav files were selected from the vcc2018_training set
The speeches were from four female speakers and four male speakers.
The details of the original corpus can be found: https://vc-challenge.org/vcc2018/index.html

### WhisperX_Results

These are the speech recognition results of the speeches using the WhisperX

WhisperX was implemented based on the original repository: https://github.com/m-bain/whisperX

### Synthesized_Speeches

#### VITS

The text recognised was then used to synthesize into speeches by using a pre-trained TTS model. A VITS model trained from a dataset called vctk was chosen. 

Since we would like to evaluate the TTS qualities and differences of the speakers may influence the scores of the evaluation, each text was synthesized to 20 different timbres. 20 female voices and 20 male voices were selected (the selection is random). If the original speech is from a female speaker, the synthesized speeches will also be in the female voices, and vice versa.

The detail of the TTS model implementation was: https://github.com/coqui-ai/TTS

#### ChatTTS

Similar to the TTS process with VITS, I also selected 20 male voices and 20 female voices from https://github.com/6drf21e/ChatTTS_Speaker/tree/main?tab=readme-ov-file 
This website ranked 2600 seeds for diffrent voices and scored the voices. I manually chose 20 seeds in each gender with highest rank_single, which represent that these voice have the highest stability on single text generation.
The implementation was achieved by using the package in https://github.com/CCmahua/ChatTTS-Enhanced.

### TTS Quality Evaluation Results

The original speeches and the synthesized speeches were both evaluated through MOSNet, a deep learning-based speech quality evaluation method. The results are recorded in results.xlsx.
The implementation step was introduced in this fork: https://github.com/MrProtectMyHair/MOSNet

---
## Document Structure
+ Original_Speeches
    - 10 Speeches selected from LibriSpeech Corpus
    - The corresponding official transcription of the speeches.
+ Synthesized_Speeches
    - Speeches synthesized by using a pretrained TTS model
        - Speeches synthesized by 20 different speakers
        - MOSNet evaluation results 
+ WhisperX_Results
    - Speech recognition results of the original speeches obtained from WhisperX
+ results.xlsx

## Naming Rules for the Files

* Original Speeches: SpeakerNo. - ChapterNo. - SentenceNo..wav
* Synthesized Speeches: synthesized - OriginalSpeakerNo. - ChapterNo. - SentenceNo. - SynthesizedTimbreNo..wav
* WhisperX Results: SpeakerNo. - ChapterNo. - SentenceNo..txt
