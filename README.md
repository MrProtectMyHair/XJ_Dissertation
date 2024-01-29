# XJ_Dissertation
---

## Please see the results.xlsx first.
---

## Introduction

In this repository, the experimental results and the related files are included. 

### Original_Speeches

There are 10 .wav files selected from the Speech Recognition Corpus called **LibriSpeech**. 
The speeches are from four different speakers, two male speakers and two female speakers. And the duration of the speeches are from 3 sec to 24 sec. Also, the official transcription of the speeches were displayed.

The complete corpus can be downloaded from the link: https://www.openslr.org/12
The details of this corpus can be found: https://ieeexplore.ieee.org/document/7178964

### WhisperX_Results

These are the speech recognition results of the speeches by using the WhisperX

WhisperX: https://github.com/m-bain/whisperX

### Synthesized_Speeches

The text recognised were then be used to synthezed into speeches by using a pretrained TTS model. A VITS model trained from vctk was chosen. 

Since we would like to evaluate the TTS qualities, and differences of the speakers may influence the scores of the evaluation, each text was synthesized to 20 different timbres. 20 female timbres and 20 male timbres were selected (the selection is random). If the original speech is from a female speaker, the synthesized speeches will also be in female voice, and vice versa.

The detail of the TTS model: https://github.com/coqui-ai/TTS

### TTS Quality Evaluation Results

The original speeches and the synthesized speeches were both evaluated through MOSNet, a deep learning based speech quality evaluation method. The results are recorded in results.xlsx.

MOSNet: https://github.com/lochenchou/MOSNet

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
