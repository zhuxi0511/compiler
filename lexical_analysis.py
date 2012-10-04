#!/use/bin/python

import sys
import os
from consts import *
from model.read_lexical import *

def lexical_analysis(input_file):

    status = NEW
    analysis_result = list()
    symbol_table = dict()

    input_file = open(sys.argv[1])

    for line in input_file:
        while len(line) > 0:
            if status == NEW:
                if line[0] in BLANK:
                    line = line[1:]
                    continue
                line, sign, value = read_word(line)
                if value:
                    if sign == 'TYPE':
                        status = AFTER_TYPE
                    elif sign == 'WORD':
                        if value in symbol_table:
                            value = symbol_table[value]
                        else:
                            size = len(symbol_table)
                            symbol_table[value] = size + 1
                            value = len(symbol_table)
                    analysis_result.append((sign, value))
                    continue
                line, sign, value = read_number(line)
                if value:
                    analysis_result.append((sign, float(value)))
                    continue
                line, sign, value = read_operator(line)
                if value:
                    analysis_result.append((sign, value))
                    continue
                line, sign, value = read_punctuator(line)
                if value:
                    analysis_result.append((sign, value))
                    continue
                line, sign, value = read_const(line)
                if value:
                    analysis_result.append((sign, value))
                    continue
            elif status == AFTER_TYPE:
                if line[0] in BLANK:
                    status = NEW
                    line = line[1:]
                    continue

            print line
            return ERROR + line


    print 'success'
    return analysis_result, symbol_table
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "please use 1 argv"
    else:
        analysis_result, symbol_table = lexical_analysis(open(sys.argv[1]))
        for i, j in analysis_result:
            print i + '\t\t' + str(j)
        print symbol_table.items()
