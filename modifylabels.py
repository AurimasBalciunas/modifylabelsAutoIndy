#Aurimas Balciunas
#Quick Tool for MIT-Pitt AutoIndy to convert rotation_y in all bins
#Note: Place this file in a folder containing all of your bins and run it
#CAREFUL: It will scan and modify ALL SUBDIRECTORIES

import os
#from os import listdir
#from os.path import isfile, join
from fnmatch import fnmatch
import numpy as np

print("Modify Labels Script Running");

#User Settings
debugMode = True;
root  = "." #can modify this to run on a specific directory
pattern = ".txt" #change to .bin in real scenario

allFiles = [os.path.join(path, name) for path, subdirs, files in os.walk(root) for name in files if name.endswith(pattern) ]
for fileName in allFiles:
	fileStream = open(fileName, "r+")
	for line in fileStream:

		if(debugMode):
			print("\n\nFile Name: " + fileName + "\n")
			print("Old: " + line);

		#isolating number
		lineSplit = line.split();
		rotationY = float(lineSplit[-1]);
		#Calculating and rounding
		rotationYNew = -rotationY + np.pi / 2;
		rotationYNew = round(rotationYNew, 9)
		#Uploading it back
		line = line.replace(str(rotationY), str(round(rotationYNew,9)));
		if(debugMode):
			print("New: " + line);

	fileStream.truncate(0);
	fileStream.seek(0);
	fileStream.write(line);
	fileStream.close();