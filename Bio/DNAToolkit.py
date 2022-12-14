from structures import *
import collections
from collections import Counter

def validateSeq(dna_seq):
  tmpseq = dna_seq.upper()
  for nuc in tmpseq:
    if nuc not in Nucleotidos:
      return False
    return tmpseq

def countNucFrequency(seq):
  tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
  for nuc in seq:
    tmpFreqDict[nuc] += 1
  return tmpFreqDict

def transcription(seq):
  return seq.replace ("T", "U")

def reverse_complement (seq):
  return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

def reverse_compliment(seq):
  mapping = str.maketrans('ATCG', 'TACG')
  return seq.transalte(mapping)[::-1]

def gc_content(seq):
  return round(
    ((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)

def gc_content_subsec(seq, k=20):
  res = []
  for i in range(0, len(seq) - k + 1, k):
    subseq = seq[i:i + k]
    res.append(gc_content(subseq))
  return res

def translate_seq(seq, init_pos=0):
  return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]

def codon_usage(seq, aminoacid):
  tmpList = []
  for i in range(0, len(seq) - 2, 3):
      if DNA_Codons[seq[i:i + 3]] == aminoacid:
          tmpList.append(seq[i:i + 3])

  freqDict = dict(Counter(tmpList))
  totalWight = sum(freqDict.values())
  for seq in freqDict:
    freqDict[seq] = round(freqDict[seq] / totalWight, 2)
  return freqDict

def gen_reading_frames(seq):
  frames = []
  frames.append(translate_seq(seq, 0))
  frames.append(translate_seq(seq, 1))
  frames.append(translate_seq(seq, 2))
  frames.append(translate_seq(reverse_complement(seq), 0))
  frames.append(translate_seq(reverse_complement(seq), 1))
  frames.append(translate_seq(reverse_complement(seq), 2))
  return frames

def proteins_from_rf(aa_seq):
  current_prot = []
  proteins = []
  for aa in aa_seq:
    if aa == "_":
      if current_prot:
        for p in current_prot:
          proteins.append(p)
        current_prot = []
    else:
      if aa == "M":
        current_prot.append("")
      for i in range(len(current_prot)):
        current_prot[i] += aa
  return proteins

def all_proteins_from_orfs(seq, startReadPos = 0, endReadPos = 0, ordered = False):
  if endReadPos > startReadPos:
    rfs = gen_reading_frames(seq[startReadPos: endReadPos])
  else:
    rfs = gen_reading_frames(seq)
  
  res = []
  for rf in rfs:
    prots = proteins_from_rf(rf)
    for p in prots:
      res.append(p)
    if ordered:
      return sorted(res, key = len, reverse = True)
    return res
