import torch

print('M4 Acceleration Available!' if torch.backends.mps.is_available() else 'Using CPU')