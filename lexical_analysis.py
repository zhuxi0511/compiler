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
            if status == NEW:
                if line[0] in BLANK:
                    line = line[1:]
                line, sign, value = read_word(line)
                if value:
                    if sign == 'TYPE':
                        status = AFTER_TYPE
                    analysis_result.append((sign, value))
                    continue
                line, sign, value = read_number(line)
                if value:
                    analysis_result.append((sign, value))
                    continue
                line, sign, value = read_operator((sign, value))
                if value:
                    analysis_result.append((sign, value))
                    continue
                line, sign, value = read_punctuator((sign, value))
                if value:
                    analysis_result.append((sign, value))
                    continue



                


    return "success"
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "please use 1 argv"
    else:
        print lexical_analysis(open(sys.argv[1]))
