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
    if not len(lex_list) > 1:
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

    lex_list = F(lex_list)
    if lex_list:
        lex_list = TT(lex_list)
        if lex_list:
            return lex_list

    print ERROR + 'T' + '2'
    return None

def TT(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'TT'
        return None

    if lex_list[0] in MULTIPLY_SIGE:
        lex_list = F(lex_list[1:])
        if lex_list:
            lex_list = TT(lex_list)
            if lex_list:
                return lex_list
    else:
        return lex_list

def F(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'F'

    from model.syntax import direct_declarator
    deal_list = direct_declarator(lex_list)
    if deal_list:
        return deal_list

    from model.syntax import get_number
    deal_list = get_number(lex_list)
    if deal_list:
        return deal_list

    print ERROR + 'F' + '2'
    return None
