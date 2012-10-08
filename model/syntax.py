from consts import *
from model.calculation_expression import *

def function_definition(lex_list):
    if not len(lex_list) > 1:
        print 'END'
        return None
    deal_list = lex_list
    deal_list = get_type(deal_list)
    if deal_list:
        deal_list = direct_declarator(deal_list)
        if deal_list:
            deal_list = compound_statment(deal_list)
            return deal_list

    return None

def get_type(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'get_type'
        return None
    if lex_list[0][0] == 'TYPE':
        print 'TYPE -> ' + str(lex_list[:1])
        return lex_list[1:]

    print ERROR + 'get_type'
    return None

def direct_declarator(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'direct_declarator'
        return None
    lex_list = identifier(lex_list)
    if lex_list:
        deal_list = post_declarator(lex_list)
        if deal_list:
            return deal_list
        deal_list = suffix_declarator(lex_list)
        if deal_list:
            return deal_list

        return lex_list

    print ERROR + 'direct_declarator'
    return None

def identifier(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'identifier'
        return None
    if lex_list[0][0] == 'WORD':
        print 'identifier -> ' + str(lex_list[:1])
        return lex_list[1:]

    print ERROR + 'identifier'
    return None

def suffix_declarator(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'suffix_declarator' + '1'
        return None

    if lex_list[0] == ('OPERATOR', '++'):
        print 'suffix_declarator -> ' + lex_list[0]
        return lex_list[1:]

    return None
    
def post_declarator(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'post_declarator'
        return None
    if lex_list[0] == ('PUNCTUATOR', '['):
        if len(lex_list) > 3 and (lex_list[1][0] == 'NUMBER' or lex_list[1][0] == 'WORD') and \
                lex_list[2] == ('PUNCTUATOR', ']'):
            print 'post_declarator -> ' + str(lex_list[:3])
            return lex_list[3:]
    elif lex_list[0] == ('PUNCTUATOR', '('):
        if len(lex_list) > 2 and lex_list[1] == ('PUNCTUATOR', ')'):
            print 'post_declarator -> ' + str(lex_list[:2])
            return lex_list[2:]
        elif len(lex_list) > 3 and lex_list[1][0] == 'CONST' and \
                lex_list[2] == ('PUNCTUATOR', ')'):
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
            return lex_list[1:]

    return None

def expression(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'expression' + '1'
        return None

    deal_list = get_type(lex_list)
    if deal_list:
        deal_list = direct_declarator(deal_list)
        if deal_list:
            if len(deal_list) > 1 and deal_list[0] == ('OPERATOR', '='):
                temp_list = calculation_expression(deal_list[1:])
                if temp_list:
                    return temp_list
                temp_list = const_expression(deal_list[1:])
                if temp_list:
                    return temp_list
            return deal_list

    deal_list = direct_declarator(lex_list)
    if deal_list:
        if len(deal_list) > 1 and deal_list[0] == ('OPERATOR', '='):
            temp_list = calculation_expression(deal_list[1:])
            if temp_list:
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
        state = STATUS_NEW
        while c < len(lex_list):
            if state == STATUS_NEW:
                if lex_list[c][0] == 'NUMBER':
                    state = STATUS_POINT
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
        lex_list = calculation_expression(lex_list[2:])
        if len(lex_list) > 1 and lex_list[0] == ('PUNCTUATOR', ')'):
            lex_list = statement(lex_list[1:])
            if lex_list:
                if len(lex_list) > 1 and lex_list[0] == ('KEYWORD', 'else'):
                    deal_list = statement(lex_list[1:])
                    if deal_list:
                        return deal_list
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
        lex_list = expression(lex_list)
        if lex_list and len(lex_list) > 1 and lex_list[0] == ('PUNCTUATOR', ';'):
            lex_list = calculation_expression(lex_list[1:])
            if lex_list and len(lex_list) > 1 and lex_list[0] == ('PUNCTUATOR', ';'):
                lex_list = calculation_expression(lex_list[1:])
                if lex_list and len(lex_list) > 1 and lex_list[0] == ('PUNCTUATOR', ';'):
                    lex_list = compound_statment(lex_list)
                    if lex_list:
                        return lex_list

    print ERROR + 'for_statement' + '2'
    return None

