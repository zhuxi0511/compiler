import sys
import os
from consts import *
from lexical_analysis import lexical_analysis
from model.syntax import *
from model.tools import *
import variables

def init():
    f = open(TEXT, 'w')
    f.close()
    f = open(DATA, 'w')
    f.close()

def main():
    analysis_result, symbol_table = lexical_analysis(open(sys.argv[1]))
    for i, j in analysis_result:
        print i + '\t\t' + str(j)
    print symbol_table.items()

    lex_list = analysis_result
    file_add(DATA, '.section .data')
    file_add(DATA, 'cmpa: .int 0')
    file_add(DATA, 'cmpb: .int 0')
    file_add(DATA, '.section .rodata')
    file_add(DATA, 'msg: .asciz "%d\\n"')

    file_add(TEXT, '.section .text')
    file_add(TEXT, '.globl main') 
    variables.printf_word = symbol_table['printf']

    while True:
        deal_list = function_definition(lex_list, symbol_table['main'])
        if not deal_list:
            break
        lex_list = deal_list

    file_add(TEXT, 'movl $1, %eax')
    file_add(TEXT, 'movl $0, %ebx')
    file_add(TEXT, 'int $0x80')

    if len(lex_list) == 1 and lex_list[0] == ('END', '#'):

        return 'success'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "please use 1 argv"
    else:
        init()
        print main()



