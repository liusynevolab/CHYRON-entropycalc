import sys
import os
import re
import pickle
import pandas as pd
from itertools import combinations, product
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from scipy.stats import norm
import operator
import numpy as np
import collections
from collections import defaultdict
import os.path
import csv

insDict = {}
with open(sys.argv[1]) as samples:
	for line in samples:
		counter = 0
		c = 0
		count = 0
		insCount = 0
		line = line.strip().split(' ')
		withlengths = line[0]

		with open(withlengths) as lengths:
			for line in lengths:
				insInfo = line.strip().split('\t')
				insertion = insInfo[1]
				insLen = insInfo[2]
				insCount = int(insInfo[3])
				insPerc = insInfo[4]
				if insertion == 'ROOT':
					print"found one"
					continue
				if insertion not in insDict: ## have we seen this insertion?
					insDict[insertion] = insCount
					c += 1
					continue
print(insDict)

dict = insDict
w = csv.writer(open("output.csv", "w"))
for key, val in dict.items():
    w.writerow([key, val])


						
