# CSC 426 Project 4: Perceptrons
# Authors: Vihan Patel, Gordon Petry, Amulya Badineni, Yuriy Deyneka
# Filename: README.md
# Description: Describes the contents of the submission.

This repository contains a Python based perceptron learner.

## Contents
The repository includes four main deliverables:
  experiment.py - Deals with initialzing weight vectors for task 2. Creating different weight vectors with 0s and 1s.
                  Taking that data and mixing it up in random order thats added into a data file.
  project4.py   - Creates data needed for doing learning problem one, two, or three. Creating stat files for D2, D3, or D4 
                  with the data files that come with it. In the end checking arguments and assigning path to the different variables
                  Creating area of task numbers and the stat file tasks 2, 3.1, 3.2, 3.3, 4.1, 4.2. With a stat file with all the data.
  perceptron.py - (our source code) this is whats used to get the petceptron output for our training data. With updateding weights for a 
                  perceptron if it incorrectly classified and performs that needed epoch for learning. Then it records the information 
                  needed for each set.
  
  4. **iris.txt**: input data
  5. **D2**: The "epoch stats file" containing epoch #, # of errors on training data for that epoch, and current weight vector for each of the three LPs for T2. The              plot for each of the three LPs for T2
  6. **D3**: All the epoch stats files and all the plots from T3
  7. **D4**: All the epoch stats files and all the plots from T4
  8. **D5**: All the written reports from T5
  9. **D6**: a writeup that addresses the following:
       1. anything positive we enjoyed or learned from this assignment,
       2. anything negative we didn't like about this assignment,
       3. any parts of this assignment we found easy,
       4. any parts of this assignment we found challenging or couldn't get working correctly,
       5. Details on how our team functioned
       6. Any other remarks we have

**LINK TO REPO**: https://github.com/badinea1/Perceptron

## Build Instructions for the HPC

On OnDemand, go to your File Home Directory and upload source code and the input files. Then, in the HPC terminal, enter: 

``` 
   module add python
   python3 project4.py [INPUT FILE PATH] [LEARNING RATE]
```
