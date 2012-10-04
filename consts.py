import string

NEW = 'N'
POINT = 'P'
AFTER_NUMBER = 'AN'
AFTER_TYPE = 'AT'

NUMBER = '.' + string.digits
WORD = string.letters + '_' + string.digits
BLANK = ' '
KEYWORD = [
    'for', 'if', 'else', 'return', 
]
TYPE = [
    'int', 'float', 'double', 
]

OPERATOR = "+-*/><="
PUNCTUATOR = "[](){},:;"
