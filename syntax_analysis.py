import sys
import os
from consts import *
from lexical_analysis import lexical_analysis
from model.syntax import *

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "please use 1 argv"
    else:
        analysis_result, symbol_table = lexical_analysis(open(sys.argv[1]))
        for i, j in analysis_result:
            print i + '\t\t' + str(j)
        print symbol_table.items()

        lex_list = analysis_result

        while True:
            deal_list = function_definition(lex_list)
            if not deal_list:
                break
            lex_list = deal_list

        if len(lex_list) == 1 and lex_list[0] == ('END', '#'):
            print 'success'

        print ERROR

