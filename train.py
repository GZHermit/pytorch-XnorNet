from models import Model
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as opt

from utils import Image_Reader

trainloader = Image_Reader.get_trainloader()

net = Model.Net()
net.cuda()
params = list(net.parameters())
criterion = nn.CrossEntropyLoss()
optimizer = opt.SGD(iter(params), lr=1e-3, momentum=0.9)

for epoch in range(2):
    running_loss = 0.
    for i, data in enumerate(trainloader):
        inputs, labels = data
        inputs, labels = Variable(inputs.cuda()), Variable(labels.cudda())
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        print(loss.data)
        running_loss += loss.data[0]
        if i % 1000 == 999:
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 1000))
            running_loss = 0.0

print('Finished Training')
