import torch
import numpy as np
import dataclasses
from typing import List

from torch._C import T


@dataclasses
class Experiences:
    current_state: List[torch.Tensor] = []
    action: List[torch.Tensor] = []
    reward: List[torch.Tensor] = []
    next_state: List[torch.Tensor] = []
    max_history: int = 10_000

    # def append(current_state, action, reward, next_state):

if __name__ == "__main__":
    exp = Experiences()
    print(dir(exp))