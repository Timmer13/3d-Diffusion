# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:50:17 2023

@author: Tim
"""

import re
import matplotlib.pyplot as plt
import numpy as np

def extract_loss(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    pattern = re.compile(r'Loss: (\d+\.\d+)')
    matches = re.findall(pattern, content)
    loss_list = [float(match) for match in matches]

    return loss_list

def extract_mpjpe(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Define a regular expression pattern to extract MPJPE values
    pattern = re.compile(r'\| MPJPE: (\s*\d+\.\d+)')

    # Find all matches in the content
    matches = re.findall(pattern, content)

    # Convert the matches to a list of floats
    mpjpe_list = [float(match.strip()) for match in matches]

    return mpjpe_list


file_path_linear = 'log_linear.txt'
loss_values_linear = extract_loss(file_path_linear)
mpjpe_linear = extract_mpjpe(file_path_linear)
file_path_linear = 'log_cosine.txt'
loss_values_cos = extract_loss(file_path_linear)
mpjpe_cos = extract_mpjpe(file_path_linear)
file_path_linear_edm = 'log_edm_linear.txt'
loss_values_linear_edm = extract_loss(file_path_linear_edm)
mpjpe_linear_edm = extract_mpjpe(file_path_linear_edm)

epochs = np.linspace(0, 30, len(loss_values_linear))
epochs_cos = np.linspace(0, 29, len(loss_values_cos))
plt.plot(epochs, loss_values_linear, linestyle='-', label = 'log_linear')
plt.plot(epochs_cos, loss_values_cos, linestyle='-', label = 'log_cosine')
plt.plot(epochs, loss_values_linear_edm, linestyle='-', label = 'log_edm_linear')
plt.title('Loss Function Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True)

plt.legend()
plt.show()

epochs_linear = np.linspace(0, 30, len(mpjpe_linear))
epochs_linear_edm = np.linspace(0, 30, len(mpjpe_linear_edm))
epochs_cos = np.linspace(0, 29, len(mpjpe_cos))
plt.plot(epochs_linear, mpjpe_linear, linestyle='-', label = 'log_linear')
plt.plot(epochs_cos, mpjpe_cos, linestyle='-', label = 'log_cosine')
plt.plot(epochs_linear_edm, mpjpe_linear_edm, linestyle='-', label = 'log_edm_linear')
plt.title('MPJPE Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True)

plt.legend()
plt.show()

print(min(mpjpe_linear), min(mpjpe_cos), min(mpjpe_linear_edm))