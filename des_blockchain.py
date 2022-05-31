import pickle

inputFile = open('listas','rb')

list = pickle.load(inputFile)

print(list)

inputFile.close()

