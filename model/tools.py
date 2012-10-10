def file_add(file_name, content):
    f = open(file_name, 'a')
    if f:
        f.write(content + '\n')
    f.close()
    return True

def file_add_lines(file_name, content):
    f = open(file_name, 'a')
    if f:
        f.writelines('\n'.join(content))
        f.write('\n')
    f.close()
    return True

