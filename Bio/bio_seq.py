from structures import *
import random

class bio_seq:
    def __init__(self, seq = "ATCG", seq_type = "DNA", label = 'No Label'):
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f"Provided data does not seem to be a correct {self.seq_type} sequence."

    def __validate(self):
        return set(Nucleotidos).issuperset(self.seq)

    def get_seq_biotype(self):
        return self.seq_type

    def get_seq_info(self):
        return f"[Label]: {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Lenght]: {len(self.seq)}"

    def generate_rnd_seq(self, lenght=10, seq_type="DNA"):
        seq = ''. join([random.choice(Nucleotidos)
                       for x in range(lenght)])
        self.__init__(seq, seq_type, "Randomly generated sequence")