from consts import *
from model.calculation_expression import *
from model.tools import *
import variables 

def function_definition(lex_list, main_num):
    if not len(lex_list) > 1:
        print 'END'
        return None
    deal_list = lex_list
    deal_list = get_type(deal_list)
    if deal_list:
        deal_list = direct_declarator(deal_list)
        dirc = variables.direct_declarator_ret_var[1]
        if str(dirc) == str(main_num):
            file_add(TEXT, 'main:')
        else:
            file_add(TEXT, 'v' + str(variables.direct_declarator_ret_var[1]) + ':')
        if deal_list:
            file_add(TEXT, 'pushl %ebp')
            file_add(TEXT, 'movl %esp,%ebp')
            deal_list = compound_statment(deal_list)
            if not str(dirc) == str(main_num):
                file_add(TEXT, 'movl %ebp,%esp')
                file_add(TEXT, 'popl %ebp')
                file_add(TEXT, 'ret')
            return deal_list

    return None

def get_type(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'get_type'
        return None
    if lex_list[0][0] == 'TYPE':
        variables.get_type_ret_var = lex_list[0][1]
        print 'TYPE -> ' + str(lex_list[:1])
        return lex_list[1:]

    print ERROR + 'get_type'
    return None

def get_number(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'get_number'
        return None
    if lex_list[0][0] == 'NUMBER':
        variables.get_number_ret_var = lex_list[0][1]
        print 'NUMBER -> ' + str(lex_list[:1])
        return lex_list[1:]

    print ERROR + 'get_number'
    return None

def direct_declarator(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'direct_declarator'
        return None
    lex_list = identifier(lex_list)
    if lex_list:
        deal_list = post_declarator(lex_list)
        if deal_list:
            variables.direct_declarator_ret_var = (variables.post_declarator_ret_var, variables.identifier_ret_var)
            return deal_list
        deal_list = suffix_declarator(lex_list)
        if deal_list:
            variables.calculation_expression_ret_var.append('addl $1, %s(%%ebp)' % -variables.var_loc_table[variables.identifier_ret_var])
            variables.direct_declarator_ret_var = None
            return deal_list

        variables.direct_declarator_ret_var = None
        return lex_list

    print ERROR + 'direct_declarator'
    return None

def identifier(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'identifier'
        return None
    if lex_list[0][0] == 'WORD':
        print 'identifier -> ' + str(lex_list[:1])
        variables.identifier_ret_var = lex_list[:1][0][1]
        return lex_list[1:]

    print ERROR + 'identifier'
    return None

def suffix_declarator(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'suffix_declarator' + '1'
        return None

    if lex_list[0] == ('OPERATOR', '++'):
        print 'suffix_declarator -> ' + str(lex_list[0])
        return lex_list[1:]

    return None
    
def post_declarator(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'post_declarator'
        return None
    if lex_list[0] == ('PUNCTUATOR', '['):
        if len(lex_list) > 3 and (lex_list[1][0] == 'NUMBER' or lex_list[1][0] == 'WORD') and \
                lex_list[2] == ('PUNCTUATOR', ']'):
            variables.post_declarator_ret_var = (1, lex_list[1])
            print 'post_declarator -> ' + str(lex_list[:3])
            return lex_list[3:]
    elif lex_list[0] == ('PUNCTUATOR', '('):
        if len(lex_list) > 2 and lex_list[1] == ('PUNCTUATOR', ')'):
            print 'post_declarator -> ' + str(lex_list[:2])
            variables.post_declarator_ret_var = (2, None)
            return lex_list[2:]
        elif len(lex_list) > 3 and lex_list[1][0] == 'WORD' and \
                lex_list[2] == ('PUNCTUATOR', ')') and \
                variables.identifier_ret_var == variables.printf_word:
            variables.expression_ret_var.append('pushl %s(%%ebp)' % -variables.var_loc_table[lex_list[1][1]])
            variables.expression_ret_var.append('pushl $msg')
            variables.expression_ret_var.append('call printf')
            variables.expression_ret_var.append('addl $8, %esp')
            variables.post_declarator_ret_var = (3, lex_list[1][1]) 
            print 'post_declarator -> ' + str(lex_list[:3])
            return lex_list[3:]

    print ERROR + 'post_declarator'
    return None

def compound_statment(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'compound_statment' + '1'
        return None

    if lex_list[0] == ('PUNCTUATOR', '{'):
        print 'compound_statment -> {'
        lex_list = lex_list[1:]
        while True:
            deal_list = statement(lex_list)
            if not deal_list:
                break
            lex_list = deal_list
        if not len(lex_list) > 1:
            print ERROR + 'compound_statment' + '2'
            return None
        if lex_list[0] == ('PUNCTUATOR', '}'):
            print 'compound_statment -> }'
            return lex_list[1:]
    
    print ERROR + 'compound_statment' + '3'
    return None

def statement(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'statement' + '1'
        return None
    
    deal_list = expression_statement(lex_list)
    if deal_list:
        file_add_lines(TEXT, variables.expression_statement_ret_var)
        print variables.expression_statement_ret_var
        return deal_list
    deal_list = selection_statement(lex_list)
    if deal_list:
        return deal_list
    deal_list = iteration_statement(lex_list)
    if deal_list:
        return deal_list
    
    return None

def expression_statement(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'expression_statement' + '1'
        return None

    lex_list = expression(lex_list)
    if lex_list:
        if len(lex_list) > 1 and lex_list[0] == ('PUNCTUATOR', ';'):
            print 'expression_statement -> ;'
            variables.expression_statement_ret_var = variables.expression_ret_var
            return lex_list[1:]

    return None

def expression(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'expression' + '1'
        return None

    variables.expression_ret_var = list()
    deal_list = get_type(lex_list)
    if deal_list:
        deal_list = direct_declarator(deal_list)
        if deal_list:
            num_t = 1
            if variables.direct_declarator_ret_var:
                if variables.direct_declarator_ret_var[0][0] == 1 and variables.direct_declarator_ret_var[0][1][0] == 'NUMBER':
                    num_t = int(variables.direct_declarator_ret_var[0][1][1] + 0.5)
            variables.var_sum_size += num_t * 4
            variables.var_loc_table[variables.identifier_ret_var] = variables.var_sum_size
            variables.expression_ret_var.append('subl $%s, %%esp' % (num_t * 4))


            if len(deal_list) > 1 and deal_list[0] == ('OPERATOR', '='):
                identifier_tmp = variables.identifier_ret_var
                temp_list = calculation_expression(deal_list[1:])
                if temp_list:
                    variables.expression_ret_var += variables.calculation_expression_ret_var
                    variables.expression_ret_var.append('movl %%eax, %s(%%ebp)' % -variables.var_loc_table[identifier_tmp])
                    return temp_list
                temp_list = const_expression(deal_list[1:])
                if temp_list:
                    return temp_list
            return deal_list

    variables.expression_ret_var = list()
    deal_list = direct_declarator(lex_list)
    if deal_list:
        if variables.direct_declarator_ret_var:
            if variables.direct_declarator_ret_var[0][0] == 2:
                file_add(TEXT, 'call v' + str(variables.identifier_ret_var))
        if len(deal_list) > 1 and deal_list[0] == ('OPERATOR', '='):
            identifier_tmp = variables.identifier_ret_var
            temp_list = calculation_expression(deal_list[1:])
            if temp_list:
                variables.expression_ret_var += variables.calculation_expression_ret_var
                variables.expression_ret_var.append('movl %%eax, %s(%%ebp)' % -variables.var_loc_table[identifier_tmp])
                return temp_list
        return deal_list
    
    print ERROR + 'expression' + '1'
    return None

def const_expression(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'const_expression' + '1'
        return None

    if lex_list[0] == ('PUNCTUATOR', '{'):
        c = 1
        count = 0
        state = STATUS_NEW
        while c < len(lex_list):
            if state == STATUS_NEW:
                if lex_list[c][0] == 'NUMBER':
                    state = STATUS_POINT
                    variables.expression_ret_var.append('movl $%s, %%edx' % count)
                    variables.expression_ret_var.append('movl $%s, %s(%%ebp, %%edx, 4)' % ((int)(lex_list[c][1] + 0.5), -variables.var_loc_table[variables.identifier_ret_var]))
                    count += 1
                else:
                    break
            elif state == STATUS_POINT:
                if lex_list[c][1] == ',':
                    state = STATUS_NEW
                else:
                    break
            c += 1

    if state == STATUS_POINT and c > 0 and len(lex_list) > c and lex_list[c] == ('PUNCTUATOR', '}'):
        print 'const_expression -> ' + str(lex_list[:c+1])
        return lex_list[c+1:]

    print ERROR + 'const_expression' + '2'
    return None


def selection_statement(lex_list):
    if not len(lex_list) > 2:
        print ERROR + 'selection_statement' + '1'
        return None

    if lex_list[0] == ('KEYWORD', 'if') and lex_list[1] == ('PUNCTUATOR', '('):
        variables.selection_statement_ret_var = list()
        lex_list = comparison_expression(lex_list[2:], 1)
        if len(lex_list) > 1 and lex_list[0] == ('PUNCTUATOR', ')'):
            file_add_lines(TEXT, variables.comparison_expression_ret_var)
            lex_list = compound_statment(lex_list[1:])
            if lex_list:
                file_add(TEXT, 'jmp selection_end')
                if len(lex_list) > 1 and lex_list[0] == ('KEYWORD', 'else'):
                    file_add(TEXT, 'if_fail:')
                    deal_list = compound_statment(lex_list[1:])
                    if deal_list:
                        file_add(TEXT, 'selection_end:')
                        return deal_list
                file_add(TEXT, 'if_fail:')
                file_add(TEXT, 'selection_end:')
                return lex_list

    print ERROR + 'selection_statement' + '2'
    return None

def iteration_statement(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'iteration_statement' + '1'
        return None
    
    lex_list = for_statement(lex_list)
    if lex_list:
        return lex_list

    print ERROR + 'iteration_statement' + '2'
    return None

def for_statement(lex_list):
    if not len(lex_list) > 2:
        print ERROR + 'for_statement' + '1'
        return None

    if lex_list[0] == ('KEYWORD', 'for') and lex_list[1] == ('PUNCTUATOR', '('):
        variables.for_statement_ret_var = list()
        lex_list = expression(lex_list[2:])
        if lex_list and len(lex_list) > 1 and lex_list[0] == ('PUNCTUATOR', ';'):
            variables.for_statement_ret_var += variables.expression_ret_var
            lex_list = comparison_expression(lex_list[1:])
            if lex_list and len(lex_list) > 1 and lex_list[0] == ('PUNCTUATOR', ';'):
                variables.for_statement_ret_var.append('for_start:')
                variables.for_statement_ret_var += variables.comparison_expression_ret_var
                lex_list = comparison_expression(lex_list[1:])
                if lex_list and len(lex_list) > 1 and lex_list[0] == ('PUNCTUATOR', ')'):
                    for_statement_tmp = [i for i in variables.comparison_expression_ret_var]
                    file_add_lines(TEXT, variables.for_statement_ret_var)
                    lex_list = compound_statment(lex_list[1:])
                    if lex_list:
                        file_add_lines(TEXT, for_statement_tmp)
                        file_add(TEXT, 'jmp for_start')
                        file_add(TEXT, 'for_fail:')
                        return lex_list

    print ERROR + 'for_statement' + '2'
    return None

