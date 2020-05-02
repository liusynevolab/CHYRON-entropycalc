# CHYRON-entropycalc

To calculate Shannon entropy from amplicon sequencing of the CHYRON locus:

For each sample, download the "aligned" file from the CHYRON-NGS pipeline. You will also need the ref file from 
that pipeline.

For a sample named "samplex," you would type the following into the terminal:

python2.7 entropy-calc-hard.py samplex_ref.txt samplex.aligned.txt samplex.result.txt

In the samplex.result.txt file, you will find 
