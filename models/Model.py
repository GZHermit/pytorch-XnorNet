# coding:utf-8
import torch
import torch.nn as nn
from torch.nn import functional as F


class AlexNet(nn.Module):
    def __init__(self):
        super(AlexNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 96, 11)
        self.conv2 = nn.Conv2d(5, 96, 256)
        self.conv3 = nn.Conv2d(256, 384, 5)
        self.conv4 = nn.Conv2d(384, 384, 3)
        self.conv5 = nn.Conv2d(384, 256, 3)
        self.fc6 = nn.Linear(self.conv5, 4096)
        self.fc7 = nn.Linear(4096, 4096)
        self.fc8 = nn.Linear(4096, 1000)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)))
        x = F.max_pool2d(F.relu(self.conv2(x)))
        x = F.max_pool2d(F.relu(self.conv3(x)))
        x = F.max_pool2d(F.relu(self.conv4(x)))
        x = F.max_pool2d(F.relu(self.conv5(x)))
        x = F.dropout(F.relu(self.fc6(x)))
        x = F.dropout(F.relu(self.fc7(x)))
        out = self.fc8(x)
        return out
