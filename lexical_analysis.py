#!/use/bin/python

import sys
import os
from consts import *

def lexical_analysis(input_file):

    status = NEW
    analysis_result = list()

    input_file = open(sys.argv[1])

    for line in input_file:
        while len(line) > 0:
            line, sign, value = read_word(line)
            if value:
                analysis_result.append((sign, value))



                


    return "success"
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "please use 1 argv"
    else:
        print lexical_analysis(open(sys.argv[1]))
