import torch
import torch.nn as nn
import os

class SimpleNN(nn.Module):
    def __init__(self, input_size):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(input_size, 1)
    def forward(self, x):
        return torch.sigmoid(self.fc(x))

if __name__ == "__main__":
    print("Training Phase 5: Deep Model Baseline")
    model = SimpleNN(10)
    torch.save(model.state_dict(), "models/deep_model.pt")
