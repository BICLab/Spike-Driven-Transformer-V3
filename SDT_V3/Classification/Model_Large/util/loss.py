import torch
import torch.nn as nn
import random
import os
import numpy as np
import logging
def TET_loss(outputs, labels, criterion, means, lamb):
    print('using TET')
    T = outputs.size(1)
    Loss_es = 0
    for t in range(T):
        Loss_es += criterion(outputs[t, ...], labels)
    Loss_es = Loss_es / T # L_TET
    if lamb != 0:
        MMDLoss = torch.nn.MSELoss()
        y = torch.zeros_like(outputs).fill_(means)
        Loss_mmd = MMDLoss(outputs, y) # L_mse
    else:
        Loss_mmd = 0
    return (1 - lamb) * Loss_es + lamb * Loss_mmd # L_Total