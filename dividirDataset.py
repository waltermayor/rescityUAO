from os import listdir
import glob
import os
import random
from PIL import Image


class arrangeDataset():

	def __init__(self):
		self.inputPath = "/home/walter/trabajosJohan/projectStreet/data_for_colab/data/"
		self.outputPath = "/home/walter/trabajosJohan/projectStreet/data_for_colab/"
		#self.pathColab = "/content/drive/My Drive/rescity/darknet/data_for_colab/data/"
		self.pathColab = "/content/darknet/data_for_colab/data/"
		
		
	
	def remplazar(self):
		files=glob.glob(self.inputPath+"*")
		print("holaaa")
		for fileName in files:
			fileNewName=fileName.replace("maksssksksss","mk")
			os.rename(fileName,fileNewName)
			
	def createTrainAndTestFile(self):
		print('creando test y train data')	
		filesNewPath=[]
		files=glob.glob(self.inputPath+"*.jpg")
		for fileName in files:
			fileNewName=fileName.replace(self.inputPath,self.pathColab)
			filesNewPath.append(fileNewName)
		
		filesSize=len(filesNewPath)
		porceTest=0.3
		testSize=int(filesSize*porceTest)
		testFiles = random.sample(filesNewPath, k=testSize)
		trainFiles = filter(lambda v: v not in testFiles, filesNewPath)
		print(len(testFiles))
			
		with open(self.outputPath + "test.txt", 'a') as f:
		    f.write("\n".join(map(str, testFiles)))
		
		with open(self.outputPath + "train.txt", 'a') as f:
		    f.write("\n".join(map(str, trainFiles)))
	
	def convertToJPG(self):
		files=glob.glob(self.inputPath+"*.png")
		for fileName in files:
			head, tail = os.path.split(fileName)
			name, exten = os.path.splitext(tail)
			im = Image.open(fileName)
			im.convert('RGB').save(self.outputPath + "dataJPG/" + name + ".jpg" ,"JPEG")
			
	def moveDocument(self):
		files=glob.glob(self.inputPath+"*.txt")
		for fileName in files:
			head, tail = os.path.split(fileName)
			os.system('cp '+fileName+' '+self.outputPath + "dataJPG/" +tail)
		
	
if __name__ == "__main__":
	obj=arrangeDataset()
	method =1
	if (method==0):	
		obj.remplazar()
	elif (method==1):
		obj.createTrainAndTestFile()
	elif (method==2):
		obj.convertToJPG()
	elif (method==3):
		obj.moveDocument()
