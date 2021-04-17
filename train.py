from lib.nn import Net

import os
from skimage import io
import pandas as pd
import torch.optim as optim
from torchvision import transforms, datasets
from torch.utils.data import Dataset
from torch import load, utils, tensor, save
import torch.nn.functional as F


class DatasetROUT(Dataset):
    
    def __init__(self, csv_file,root_dir, transform=None):
        self.annotations = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform
        
    def __len__(self):
        return len(self.annotations)
    
    def __getitem__(self, index):
        image_path = os.path.join(self.root_dir, self.annotations.iloc[index, 0])
        image = io.imread(image_path)
        y_label = tensor(int(self.annotations.iloc[index, 1]))
        if self.transform:
          image = self.transform(image)
        return (image, y_label)







def train_nn(e = 10, c = False):
	net = Net()
	net.load_state_dict(load('net'))
	net.eval()
	if c == False:
		train = DatasetROUT(csv_file='dataset_faces.csv',root_dir='', transform=transforms.ToTensor())
	else:
		print('custom')
		train = DatasetROUT(csv_file='dataset_faces_cust.csv',root_dir='', transform=transforms.ToTensor())
	trainset = utils.data.DataLoader(train, batch_size=8, shuffle=True)
	

	optimizer = optim.Adam(net.parameters(), lr= 0.001)


	EPOCHS = e
	count = 0

	for epoch in range(EPOCHS):
		count +=1
		for data in trainset:
			#data et reponse
			X, y = data
			net.zero_grad()
			output = net(X.view(-1,85*85))
			loss = F.nll_loss(output, y)
			loss.backward()
	        
			optimizer.step()

		print(round(count*100/EPOCHS,1),loss)

	save(net.state_dict(), 'net' )


