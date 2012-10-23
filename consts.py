import string

ONE_QUOTATION = 'OQ'
TWO_QUOTATION = 'TQ'

ERROR = 'THE RESULT IS ERROR'
STATUS_NEW = 'SN'
STATUS_POINT = 'SP'
AFTER_NUMBER = 'AN'
AFTER_TYPE = 'AT'

NUMBER = '.' + string.digits
WORD = string.letters + '_' + string.digits
BLANK = ' \n'
KEYWORD = [
    'for', 'if', 'else', 'return', 'while', 
]
TYPE = [
    'int', 'float', 'double', 
]

OPERATOR = "+-*/><=&"
PUNCTUATOR = "[](){},:;"

COMPARE_SIGN = [
    ('OPERATOR', '>'),
    ('OPERATOR', '>='),
    ('OPERATOR', '<'),
    ('OPERATOR', '>='),
]

PLUS_SING = [
    ('OPERATOR', '+'),
    ('OPERATOR', '-'),
]

MULTIPLY_SIGE = [
    ('OPERATOR', '*'),
    ('OPERATOR', '/'),
]

TEXT = 'text.s'
DATA = 'text.s'
