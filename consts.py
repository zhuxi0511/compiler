import string

ONE_QUOTATION = 'OQ'
TWO_QUOTATION = 'TQ'

ERROR = 'THE RESULT IS ERROR'
NEW = 'N'
POINT = 'P'
AFTER_NUMBER = 'AN'
AFTER_TYPE = 'AT'

NUMBER = '.' + string.digits
WORD = string.letters + '_' + string.digits
BLANK = ' \n'
KEYWORD = [
    'for', 'if', 'else', 'return', 
]
TYPE = [
    'int', 'float', 'double', 
]

OPERATOR = "+-*/><=&"
PUNCTUATOR = "[](){},:;"
