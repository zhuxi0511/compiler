from consts import *

def comparison_expression(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'comparison_expression'
        return None

    lex_list = calculation_expression(lex_list)
    if lex_list:
        if len(lex_list) > 1 and lex_list[0] in COMPARE_SIGN:
            deal_list = calculation_expression(lex_list[1:])
            if deal_list:
                return deal_list
        else:
            return lex_list

    print ERROR + 'comparison_expression' + '2'
    return None

def calculation_expression(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'calculation_expression'
        return None

    lex_list = E(lex_list)
    if lex_list:
        return lex_list

    print ERROR + 'calculation_expression' + '2'
    return None

def E(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'E'
        return None

    lex_list = T(lex_list)
    if lex_list:
        lex_list = EE(lex_list)
        if lex_list:
            return lex_list

    print ERROR + 'E' + '2'
    return None

def EE(lex_list):
    if not lex_list(lex_list) > 1:
        print ERROR + 'EE'
        return None

    if lex_list[0] in PLUS_SING:
        lex_list = T(lex_list[1:])
        if lex_list:
            lex_list = EE(lex_list)
            if lex_list:
                return lex_list
    else:
        return lex_list

def T(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'T'
        return None

    temp_list = T(lex_list)
    if temp_list:
        if len(lex_list) > 1 and temp_list[0] in MULTIPLY_SIGE:
            deal_list = F(temp_list[1:])
            if deal_list:
                print 'T -> ' + str(temp_list[0])
                return deal_list
    
    temp_list = F(lex_list)
    if temp_list:
        return temp_list

    print ERROR + 'T' + '2'
    return None

def F(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'F'

    from model.symbol_table import direct_declarator
    lex_list = direct_declarator(lex_list)
    if lex_list:
        return lex_list

    print ERROR + 'F' + '2'
    return None
