import os
import datetime

def Init():
    head = None
    length = 0
    container = {'head': head,
                 'length': length}
    return container


def Node(value, next_el, prev_el):
    node = {'value': value,
            'next': next_el,
            'prev': prev_el}
    return node


def Add(c, x):
    c['length'] += 1
    if c['head'] is None:
        c['head'] = Node(x, None, None)
        c['head']['next'] = c['head']['prev'] = c['head']
    else:
        new_link = Node(x, None, None)
        last = c['head']['prev']
        c['head']['prev'] = last['next'] = new_link
        new_link['prev'] = last
        new_link['next'] = c['head']


def GetByID(c, key):
    if c['head'] is not None:
        current = c['head']
        for k in range(key):
            if c['head'] != c['head']['next']:
                current = current['next']
            else:
                return "Out of range"
        return current
    return 'Empty List'


def Sort(c):
    for i in range(c['length'] - 1):
        for j in range(0, c['length'] - i - 1):
            tmp_el = GetByID(c, j)
            tmp_min = None
            if Compare(tmp_el['value'], GetByID(c, j + 1)['value']):
                tmp_min = GetByID(c, j + 1)
                tmp_el['prev']['next'] = tmp_min
                tmp_min['next']['prev'] = tmp_el
                tmp_el['next'] = tmp_min['next']
                tmp_min['prev'] = tmp_el['prev']
                tmp_el['prev'] = tmp_min
                tmp_min['next'] = tmp_el
                if tmp_el == c['head']:
                    c['head'] = tmp_min


def Input(c, file_name):
    try:
        file = open(file_name)
    except OSError:
        print("File not found!")
        return 0
    if os.stat(file_name).st_size == 0:
        print("File is empty!")
        return 0
    else:
        for line in file:
            Input_Lang(c, line, file.readline().split(" "))


def Input_Lang(c, key, param):
    if int(key) == 1:
        Input_OOP(c, param)
    elif int(key) == 2:
        Input_Proc(c, param)
    else:
        return print("Verify that the input is correct!")


def Input_OOP(c, param):
    element = ["OOP"] + param
    Add(c, element)


def Input_Proc(c, param):
    element = ["Proc"] + param
    Add(c, element)


def Out(c, file_name):
    output_file = open(file_name, 'w')
    if c['length'] > 0:
        output_file.write("Amount of elements = " + str(c['length']) + "\n")
        for i in range(c['length']):
            lang = GetByID(c, i)
            param = lang['value']
            output_file.write(str(i + 1))
            Out_Lang(output_file, param)
    else:
        output_file.write("No elements! \n")
        return 0


def Out_Lang(file, lang):
    if lang[0] == "OOP":
        Out_OOP(file, lang)
    elif lang[0] == "Proc":
        Out_Proc(file, lang)


def Out_OOP(file, lang):
    file.write(": OOP language: inheritance = " + lang[1] + ", year = " + lang[2].strip() +
               ", how old: " + str(How_Year(lang[2])) + "\n")


def Out_Proc(file, lang):
    file.write(": Procedure language: abstract = " + lang[1] + ", year = " + lang[2].strip() +
               ", how old: " + str(How_Year(lang[2])) + "\n")


def How_Year(lang):
        return datetime.datetime.now().year - int(lang)


def Compare(arg1, arg2):
    if How_Year(arg1[2]) > How_Year(arg2[2]):
        return 1
    else:
        return 0


def Clear(c, file):
    output_file = open(file, 'a')
    c['head'] = None
    c['length'] = 0
    output_file.write("\nList empty. Number of elements = " + str(c['length']) + " \n")








