import sys
import os
import re
import numpy as np
from matplotlib import pyplot as plt
import collections
from collections import defaultdict
import os.path

ref = open(sys.argv[1],'r').read().splitlines()[0]
## Sample Numbers

mapped_seqs = []
init_seqs = []
short_seqs = []
cnt = collections.Counter()

shortfile = open(sys.argv[3],'w')

infile = open(sys.argv[2],'r').read().splitlines()
for line in infile[0::2]:
	seq = line.split("\t")[0]
	if seq.count("X") <= 20   and  seq.count("D") < 0.5*len(ref):
		init_seqs.append(line.split('\t')[0])
		mapped_seqs.append(seq)
		short_seqs.append(line.split('\t')[0][22:-102])
		shortfile.write(line.split('\t')[0][22:-102] + ('\n'))
		for seq in short_seqs:
			cnt[seq] += 1
			cnt
