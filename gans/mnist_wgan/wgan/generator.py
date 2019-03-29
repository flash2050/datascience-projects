import torch
from torch import nn


class Generator(nn.Module):
    """
    Architecture taken from the DCGAN paper
    """

    def __init__(self, input_size=7, target_size=28, input_channels=40, additional_blocks=5):
        super().__init__()

        tconvblocks = [TransposedConvBlock(input_channels, input_channels, 4, 2, 1)]

        input_size *= 2
        while input_size < (target_size // 2):
            tconvblocks.append(TransposedConvBlock(input_channels, input_channels // 2, 4, 2, 1))
            input_channels = input_channels // 2
            input_size *= 2

        for i in range(additional_blocks):
            tconvblocks.append(TransposedConvBlock(input_channels, input_channels // 2, 3, 1, 1))
            input_channels = input_channels // 2

        tconvblocks.append(nn.ConvTranspose2d(input_channels, 1, 4, 2, 1))

        self.tconvblocks = nn.Sequential(*tconvblocks)

    def forward(self, x):
        return torch.tanh(self.tconvblocks(x))


class TransposedConvBlock(nn.Module):

    def __init__(self, in_channels, out_channels, kernel, stride=2, padding=1):
        super().__init__()
        self.tconvblock = nn.Sequential(
            nn.ConvTranspose2d(in_channels, out_channels, kernel, stride, padding, bias=False),
            nn.BatchNorm2d(num_features=out_channels),
            nn.ReLU()
        )

    def forward(self, x):
        return self.tconvblock(x)
