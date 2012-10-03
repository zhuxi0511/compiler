import string

NEW = 'N'
POINT = 'P'
AFTER_NUMBER = 'AN'

NUMBER = '.' + string.digits
WORD = string.letters + '_' + string.digits
KEYWORD = [
    'for', 'if', 'else', 'return', 
]
TYPE = [
    'int', 'float', 'double', 
]

OPERATOR = "+-*/><="
PUNCTUATOR = "[](){},:;"
