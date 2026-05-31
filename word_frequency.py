#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

###############################################################################
def word_count(filename):

    word_freq = defaultdict(int)
    
    with open( filename, "r", encoding='utf-8') as fin:

        for line in fin:
            for word in line.split():
                word_freq[word] += 1
    return word_freq

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    for input_file in sys.argv[1:]:

        output_file = input_file + ".1gram"

        print(f"processing {input_file} -> {output_file}", file=sys.stderr)

        word_freq = word_count( input_file)
    
        with open(output_file, "wt", encoding='utf-8') as fout:

            for w, freq in sorted(word_freq.items()):
                print(f"{w}\t{freq}", file=fout)
