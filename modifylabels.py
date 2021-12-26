import os
from os import listdir
from os.path import isfile, join
from fnmatch import fnmatch
import numpy as np
print("Modify Labels Script Running");


root  = "."
pattern = ".txt" #change to .bin in real scenario
myfiles = [os.path.join(path, name) for path, subdirs, files in os.walk(root) for name in files if name.endswith(pattern) ]
for filename in myfiles:
	print(filename);
	filestream = open(filename, "r+")
	for line in filestream:
		print("New Line");
		print("Old: " + line);
#		print('\n');
		line_split = line.split();
		rotation_y = float(line_split[-1]);
		#number = splitline[-1]
		#print(rotation_y);
		#print('\n');
		rotation_y_new = -rotation_y + np.pi / 2;
		#rounding it
		rotation_y_new = round(rotation_y_new, 9)
		#print('\n');

		#Replacing the line
		#line_split[-1] = str(rotation_y_new);
		
		#Joining it back in
		#newLine = ' '.join(line_split)
		#print("New: " + newLine);

		#Uploading it back
		line = line.replace(str(rotation_y), str(round(rotation_y_new,9)));
		print("New: " + line);
	filestream.truncate(0);
	filestream.seek(0);
	filestream.write(line);
	filestream.close();