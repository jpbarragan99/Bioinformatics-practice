from DNAToolkit import *
from utilities import colored
import random

randDNAStr = ''.join([random.choice(Nucleotidos)
                for nuc in range (30)])

DNAStr = validateSeq(randDNAStr)

print (f'\nSequence: {colored(DNAStr)}\n')
print (f'[1] + Sequence Lenght: {len(DNAStr)}\n')
print (colored (f'[2] + Nucleotide Frecuency: {countNucFrequency(DNAStr)}\n'))
print (f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')

print (f"[4] + DNA String + Reverse Complement:\n5' {colored(DNAStr)} 3' ")
print (f"   {''.join(['|' for c in range(len(DNAStr))])}")
print (f"3' {colored(reverse_complement(DNAStr)[::-1])} 5'[Complement]")
print (f"5' {colored(reverse_complement(DNAStr))} 3'[Rev.Complement]\n")

print (f'[5] + GC Content: {gc_content(DNAStr)}%\n')
print (
  f'[6] + GC Content in Subsection k = 5: {gc_content_subsec(DNAStr, k=5)}\n')