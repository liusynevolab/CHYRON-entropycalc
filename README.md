# CHYRON-entropycalc

To calculate Shannon entropy from amplicon sequencing of the CHYRON locus:

For each sample, download the "aligned" file from the CHYRON-NGS pipeline. You will also need the ref file from 
that pipeline.

For a sample named "samplex," you would type the following into the terminal:

python2.7 entropy-calc-hard.py samplex_ref.txt samplex.aligned.txt samplex.result.txt

In the samplex.result.txt file, you will find a list of all CHYRON locus sequences, including the 17nt on either 
side of the cut site, as well as any insertions or deletions that were added.

Open samplex.result.txt.file in Excel, then use a pivot table to create a file with each unique sequence in the
first column and a count of the number of times that sequence was present in the second column.

For each unique sequence, divide the count by the sum of all counts to give p.

Then calculate p*LOG(p,2) for each sequence. The sum of this value for all sequences is the Shannon entropy.
