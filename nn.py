import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from torch import load,argmax, save

import numpy as np

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(85*85, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 2)
    def status(self):
        print(self.fc1)
        print(self.fc2)
        print(self.fc3)
        print(self.fc4)
    def get_layers(self):
        x = [self.fc1,self.fc2,self.fc3,self.fc4]
        return x
        
    def forward(self,x):
        x= F.relu(self.fc1(x))
        x= F.relu(self.fc2(x))
        x= F.relu(self.fc3(x))
        x= (self.fc4(x))
        return F.log_softmax(x,dim=1)
        
        
net = Net()
print(net)
#save(net.state_dict(), 'net' )

net.load_state_dict(load('net'))
net.eval()
net.status()

t = transforms.ToTensor()

def calculate(im):
    im = np.array(im)
    im = t(im)
    return int(argmax(net(im.view((-1,85*85)))))
def update_nn():
    global net
    net.load_state_dict(load('net'))
    net.eval()
    net.status()




