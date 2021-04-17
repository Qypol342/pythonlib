import os 
import csv
from random import randint

path = 'dataset/'

def generate_data_set(path):
	x = os.listdir(path)
	person = []

	nb_imgae ={}

	for i in x:
		#print(i)
		f = i[:i.index('_')]
		if f not in person:
			print(f)
			person.append(f)
			nb_imgae[f] = 0
		else:
			nb_imgae[f] += 1


	print(person, nb_imgae)
	values =[]

	values = [0,1] # a hastafge si input

	"""
	for i in person:
		values.append(int(input("value for i")))
	"""

	file = open('dataset_faces.csv', 'w', newline='')
	writer = csv.writer(file)
	for i in x:
		writer.writerow([path+i, values[person.index(i[:i.index('_')])]])
def generate_data_set_cust(path,nb):
	x = os.listdir(path)
	person = []

	nb_imgae ={}

	for i in x:
		#print(i)
		f = i[:i.index('_')]
		if f not in person:
			print(f)
			person.append(f)
			nb_imgae[f] = [1,[i]]

		else:
			nb_imgae[f][0] += 1
			nb_imgae[f][1].append(i)


	print(person, nb_imgae)
	values =[]

	values = [0,1] # a hastafge si input

	nb_imgae['intrus'][1] = nb_imgae['intrus'][1][-nb:]
	file = open('dataset_faces_cust.csv', 'w', newline='')
	writer = csv.writer(file)
	for i in nb_imgae['intrus'][1]:
		writer.writerow([path+i, values[person.index(i[:i.index('_')])]])
	for z in nb_imgae['intrus'][1]:
		x = randint(0, len(nb_imgae['loan'][1])-1)
		i = nb_imgae['loan'][1][x]
		writer.writerow([path+i, values[person.index(i[:i.index('_')])]])







