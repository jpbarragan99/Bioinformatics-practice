from bio_structs import DNA_Codons,RNA_Codons,Nucleotides_Base
from collections import Counter
import random

class bio_seq:
    def __init__(self, seq = "ATCG", seq_type = "DNA", label = 'No Label'):
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f"Provided data does not seem to be a correct {self.seq_type} sequence."

    def __validate(self):
        return set(Nucleotides_Base[self.seq_type]).issuperset(self.seq)

    def get_seq_biotype(self):
        return self.seq_type

    def get_seq_info(self):
        return f"[Label]: {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Lenght]: {len(self.seq)}"

    def generate_rnd_seq(self, lenght=10, seq_type="DNA"):
        seq = ''. join([random.choice(Nucleotides_Base[seq_type])
                       for x in range(lenght)])
        self.__init__(seq, seq_type, "Randomly generated sequence")
    
    def nucleotide_frequency(self):
        return dict(Counter(self.seq))

    def transcription(self):
        if self.seq_type == "DNA":
            return self.seq.replace ("T", "U")
        else: "Not a DNA Sequence"
    
    def reverse_complement (self):
        if self.seq_type == "DNA":
            mapping = str.maketrans('ATCG', 'TAGC')
        else: 
            mapping = str.maketrans('AUCG','UAGC')
        return self.seq.translate(mapping)[::-1]

    def gc_content(self):
         return round(
            ((self.seq.count('C') + self.seq.count('G')) / len(self.seq) * 100), 6)

    def gc_content_subsec(self, k=20):
        res = []
        for i in range(0, len(self.seq) - k + 1, k):
            subseq = self.seq[i:i + k]
            res.append(
                round((subseq.count('C') + subseq.count('G')) / len(subseq) * 100))
        return res
    
    def translate_seq(self, init_pos=0):
        if self.seq_type == "DNA":
            return [DNA_Codons[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq) - 2, 3)]
        elif self.seq_type == "RNA":
            return [RNA_Codons[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq) - 2, 3)]


    def codon_usage(self, aminoacid):
        tmpList = []
        if self.seq_type == "DNA":
            for i in range(0, len(self.seq) - 2, 3):
                if DNA_Codons[self.seq[i:i + 3]] == aminoacid:
                    tmpList.append(self.seq[i:i + 3])

        if self.seq_type == "RNA":
            for i in range(0, len(self.seq) - 2, 3):
                if RNA_Codons[self.seq[i:i + 3]] == aminoacid:
                    tmpList.append(self.seq[i:i + 3])

        freqDict = dict(Counter(tmpList))
        totalWight = sum(freqDict.values())
        for seq in freqDict:
            freqDict[seq] = round(freqDict[seq] / totalWight, 2)
        return freqDict

    def gen_reading_frames(self):
        frames = []
        frames.append(self.translate_seq(0))
        frames.append(self.translate_seq(1))
        frames.append(self.translate_seq(2))
        temp_seq = bio_seq(self.reverse_complement(), self.seq_type)
        frames.append(temp_seq.translate_seq(0))
        frames.append(temp_seq.translate_seq(1))
        frames.append(temp_seq.translate_seq(2))
        del temp_seq
        return frames

    def proteins_from_rf(self, aa_seq):
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

    def all_proteins_from_orfs(self, startReadPos = 0, endReadPos = 0, ordered = False):
        if endReadPos > startReadPos:
            temp_seq = bio_seq(self.seq[startReadPos: endReadPos], self.seq_type)
            rfs = temp_seq.gen_reading_frames()
        else:
            rfs = self.gen_reading_frames()
        
        res = []
        for rf in rfs:
            prots = self.proteins_from_rf(rf)
            for p in prots:
                res.append(p)
            if ordered:
                return sorted(res, key = len, reverse = True)
        return res
