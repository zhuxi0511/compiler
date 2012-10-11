from consts import *
import variables

def comparison_expression(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'comparison_expression'
        return None

    variables.comparison_expression_ret_var = list()
    compare_sign = None

    lex_list = calculation_expression(lex_list)
    if lex_list:
        variables.comparison_expression_ret_var += variables.calculation_expression_ret_var
        variables.comparison_expression_ret_var.append('movl %eax, $cmpa')
        if len(lex_list) > 1 and lex_list[0] in COMPARE_SIGN:
            compare_sign = lex_list[0][1]
            deal_list = calculation_expression(lex_list[1:])
            if deal_list:
                variables.comparison_expression_ret_var += variables.calculation_expression_ret_var
                variables.comparison_expression_ret_var.append('movl %eax, $cmpb')
                variables.comparison_expression_ret_var.append('cmp cmpa, cmpb')
                if compare_sign == '>':
                    variables.comparison_expression_ret_var.append('jbe for_fail')
                elif compare_sign == '<':
                    variables.comparison_expression_ret_var.append('jae for_fail')
                elif compare_sign == '<=':
                    variables.comparison_expression_ret_var.append('ja for_fail')
                elif compare_sign == '>=':
                    variables.comparison_expression_ret_var.append('jb for_fail')
                return deal_list
        else:
            return lex_list

    print ERROR + 'comparison_expression' + '2'
    return None

def calculation_expression(lex_list):
    if not len(lex_list) > 1:
        print ERROR + 'calculation_expression'
        return None

    variables.calculation_expression_ret_var = list()
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
        sign = lex_list[0]
        variables.calculation_expression_ret_var.append('movl %eax, %ecx')
        lex_list = T(lex_list[1:])
        if lex_list:
            if sign[1] == '+':
                variables.calculation_expression_ret_var.append('addl %ecx, %eax')
            elif sign[1] == '-':
                variables.calculation_expression_ret_var.append('subl %ecx, %eax')
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
        sign = lex_list[0]
        variables.calculation_expression_ret_var.append('movl %eax, %ebx')
        lex_list = F(lex_list[1:])
        if lex_list:
            if sign[1] == '*':
                variables.calculation_expression_ret_var.append('mull %ebx')
            elif sign[1] == '/':
                variables.calculation_expression_ret_var.append('movl %eax, %edx')
                variables.calculation_expression_ret_var.append('movl %ebx, %eax')
                variables.calculation_expression_ret_var.append('movl %edx, %ebx')
                variables.calculation_expression_ret_var.append('movl $0, %edx')
                variables.calculation_expression_ret_var.append('divl %ebx')
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
        if variables.direct_declarator_ret_var:
            post, ident = variables.direct_declarator_ret_var
            if post[0] == 1:
                if post[1][0] == 'NUMBER':
                    t_num = int(post[1][1] + 0.5)
                    variables.calculation_expression_ret_var.append('movl $%s, %%edx' % t_num)
                elif post[1][0] == 'WORD':
                    variables.calculation_expression_ret_var.append('movl %s(%%ebp), %%edx' % -variables.var_loc_table[post[1][1]])
                variables.calculation_expression_ret_var.append('movl %s(%%ebp, %%edx, 4), %%eax' % (-variables.var_loc_table[variables.identifier_ret_var]))
        else:
            variables.calculation_expression_ret_var.append('movl %s(%%ebp), %%eax' % (-variables.var_loc_table[variables.identifier_ret_var]))

        return deal_list

    from model.syntax import get_number
    deal_list = get_number(lex_list)
    if deal_list:
        variables.calculation_expression_ret_var.append('movl $%s, %%eax' % (int(variables.get_number_ret_var + 0.5)))
        return deal_list

    print ERROR + 'F' + '2'
    return None
