from consts import *

def read_number(string):
    status = STATUS_NEW
    ret = 0
    for c in string:
        if c not in NUMBER:
            break
        if status == STATUS_NEW:
            if c == '.':
                status = STATUS_POINT
        elif status == STATUS_POINT:
            if c == '.':
                break
        ret += 1

    return string[ret:], 'NUMBER', string[:ret]

def read_word(string):
    status = STATUS_NEW
    ret = 0
    for c in string:
        if c not in WORD:
            break
        if status == STATUS_NEW:
            if c in NUMBER:
                break
            else:
                status = STATUS_POINT
        ret += 1

    word = string[:ret]
    ret_type = 'WORD'
    ret_type = 'KEYWORD' if word in KEYWORD else ret_type
    ret_type = 'TYPE' if word in TYPE else ret_type

    return string[ret:], ret_type, string[:ret]

def read_operator(string):
    ret = 0
    for c in string:
        if c not in OPERATOR:
            break
        ret += 1

    return string[ret:], 'OPERATOR', string[:ret]

def read_punctuator(string):
    status = STATUS_NEW
    punctuator = str()
    ret = 0
    if len(string) > 0:
        if string[0] in PUNCTUATOR:
            ret = 1
            punctuator = string[0]

    return string[ret:], 'PUNCTUATOR', punctuator

def read_const(string):
    status = STATUS_NEW
    str_const = str()
    ret = 0
    for c in string:
        if status == STATUS_NEW:
            if c == '"':
                status = ONE_QUOTATION
            else:
                break
        elif status == ONE_QUOTATION:
            if c == '"':
                status = TWO_QUOTATION
        ret += 1

        if status == TWO_QUOTATION:
            break

    if status != TWO_QUOTATION:
        ret = 0

    return string[ret:], 'CONST', string[:ret]
