from consts import *

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
    
def post_declarator(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'post_declarator'
        return None
    if lex_list[0] == ('PUNCTUATOR', '['):
        if len(lex_list) > 3 and lex_list[1][0] == 'NUMBER' and \
                lex_list[2] == ('PUNCTUATOR', ']'):
            print 'post_declarator -> ' + lex_list[:3]
            return lex_list[3:]
    elif lex_list[0] == ('PUNCTUATOR', '('):
        if len(lex_list) > 2 and lex_list[1] == ('PUNCTUATOR', ')'):
            print 'post_declarator -> ' + str(lex_list[:2])
            return lex_list[2:]

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

    deal_list = lex_list


    return None



    
