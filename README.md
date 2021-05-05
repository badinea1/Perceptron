# CSC 426 Project 4: Perceptrons
# Authors: Vihan Patel, Gordon Petry, Amulya Badineni, Yuriy Deyneka
# Filename: README.md
# Description: Describes the contents of the submission.

This repository contains a Python based perceptron learner.

## Contents
The repository includes four main deliverables:
  1. **experiment.py, project4.py, perceptron.py**: our source code
  2. **iris.txt**: input data
  3. **D2**: The "epoch stats file" containing epoch #, # of errors on training data for that epoch, and current weight vector for each of the three LPs for T2. The              plot for each of the three LPs for T2
  4. **D3**: All the epoch stats files and all the plots from T3
  5. **D4**: All the epoch stats files and all the plots from T4
  6. **D5**: All the written reports from T5
  7. **D6**: a writeup that addresses the following:
       1. anything positive we enjoyed or learned from this assignment,
       2. anything negative we didn't like about this assignment,
       3. any parts of this assignment we found easy,
       4. any parts of this assignment we found challenging or couldn't get working correctly,
       5. Details on how our team functioned
       6. Any other remarks we have

**LINK TO REPO**: https://github.com/badinea1/Perceptron

## Build Instructions for the HPC
1. Method 1: Cloning repository

```
module add python
git clone https://github.com/badinea1/Perceptron.git
python3 project4.py [INPUT FILE PATH] [LEARNING RATE (e.g. 0.1,0.3, etc)

```

2. Method 2: 
On OnDemand, go to your File Home Directory and upload source code and the input files. Then, in the HPC terminal, enter: 

``` 
   module add python
   python3 project4.py [INPUT FILE PATH] [LEARNING RATE]
```
