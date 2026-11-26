import torch
import torch.nn.functional as F

def GeLU(x: torch.Tensor) -> torch.Tensor:
    return F.gelu(x, approximate="tanh")   