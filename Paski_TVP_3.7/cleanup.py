def remove_repet(list):
    new = []
    for item in list:
        if item in new or item == "\f" or item == "\n\f":
            continue
        else:
            new.append(item)
    return new

def remove_punc(string):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in string:
        if ele in punc:
            string = string.replace(ele, "")
    return string

def remove_spaces(string):
    tmp = []
    res = ""
    for ele in string:
        if ele != "\f" and ele != "\n":
            tmp.append(ele)
    if tmp[0] == " ":
        tmp.pop(0)
    elif tmp[1] == " ":
        tmp.pop(1)
    elif tmp[-1] == " ":
        tmp.pop(-1)
    elif tmp[-2] == " ":
        tmp.pop(-2)
    elif tmp[-3] == " ":
        tmp.pop(-3)
    for i in tmp:
        res += str(i)
    return res


