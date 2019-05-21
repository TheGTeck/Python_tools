# coding=utf-8
import sys

# Fetch and return a number of 
fasta_file = sys.argv[1]
nb_seq = int(sys.argv[2])

def parse_fasta(fasta_file):
    fasta = {}
    seq = ""
    acc = ""
    with open(fasta_file, 'r') as f:
        for l in f:
            l = l.rstrip("\n")
            if(l[0]==">"):
                if(seq!=""):
                    fasta[acc] = seq
                    seq = ""
                acc = l[1:]
            else:
                seq += l
        fasta[acc] = seq
    return(fasta)

fasta = parse_fasta(fasta_file)
#Don't need to shuffle, the ordering of dictionnary key is already random
seq_index = list(fasta.keys())[:nb_seq]

for acc in seq_index:
    print(">"+acc+"\n"+fasta[acc])
