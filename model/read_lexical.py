from consts import *

def read_number(string):
    status = NEW
    number = str()
    ret = 0
    for c in string:
        if c not in NUMBER:
            break
        if status == NEW:
            if c == '.':
                status = POINT
        elif status == POINT:
            if c == '.':
                break
        number += c
        ret += 1

    return string[ret:], 'NUMBER', float(number)

def read_word(string):
    status = NEW
    word = str()
    ret = 0
    for c in string:
        if c not in WORD:
            break
        word += c
        ret += 1

    ret_type = 'WORD'
    ret_type = 'KEYWORD' if word in KEYWORD else 'WORD'
    ret_type = 'TYPE' if word in TYPE else 'WORD'

    return string[ret:], ret_type, word

def read_operator(string):
    operator = str()
    ret = 0
    for c in string:
        if c not in OPERATOR:
            break
        word += c
        ret += 1

    return string[ret:], 'OPERATOR', operator

def read_punctuator(string):
    status = NEW
    punctuator = str()
    ret = 0
    if len(string) > 0:
        if string[0] in PUNCTUATOR:
            ret = 1
            punctuator = string[0]

    return string[ret:], 'PUNCTUATOR', punctuator






