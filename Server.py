import os
import datetime

def Init():
    head = None
    length = 0
    container = {'head': head,
                 'length': length}
    return container


def NewElement(year, ment, param):
    element = {'year': year,
            'ment': ment,
            'param': param}
    return element


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
        file = open(file_name, 'r')
    except OSError:
        print("File not found!")
        return 0
    if os.stat(file_name).st_size == 0:
        print("File is empty!")
        return 0
    else:
        for line in file:
            if line:
                Input_Lang(c, line.strip(), file.readline().strip().split(" "))
        file.close()


def Input_Lang(c, key, param):

    if key == "1":
        Input_OOP(c, param)
    elif key == "2":
        Input_Proc(c, param)
    elif key == "3":
        Input_Func(c, param)
    else:
        return print("Verify that the input is correct!")


def Input_OOP(c, param):
    OOP_txt = {0: "single",
               1: "multiply",
               2: "interface"}

    if len(param) == 3:
        try:
            param[2] = int(param[2])
            param[1] = int(param[1])
            param[0] = OOP_txt[int(param[0])]
            element = NewElement(param[2], param[1], ["OOP"] + [param[0]])
            Add(c, element)
        except:
            print("Verify that the all parameters is correct.")
    else:
        print("Verify that the number of parameters is correct.")


def Input_Proc(c, param):
    bool_txt = {0: "no",
                1: "yes"}
    if len(param) == 3:
        try:
            param[2] = int(param[2])
            param[1] = int(param[1])
            param[0] = bool_txt[int(param[0])]
            element = NewElement(param[2], param[1], ["Proc"] + [param[0]])
            Add(c, element)
        except:
            print("Verify that the all parameters is correct.")
    else:
        print("Verify that the number of parameters is correct.")


def Input_Func(c, param):
    bool_txt = {0: "no",
                1: "yes"}
    FUNC_txt = {0: "strong",
                1: "dynamic"}
    if len(param) == 4:
        try:
            param[2] = int(param[2])
            param[3] = int(param[3])
            param[1] = bool_txt[int(param[1])]
            param[0] = FUNC_txt[int(param[0])]
            element = NewElement(param[3], param[2], ["Func"] + [param[0]] + [param[1]])
            Add(c, element)
        except:
            print("Verify that the all parameters is correct.")
    else:
        print("Verify that the number of parameters is correct.")


def Out(c, file_name):
    output_file = open(file_name, 'a')
    if c['length'] > 0:
        output_file.write("\nAmount of elements = " + str(c['length']) + "\n")
        for i in range(c['length']):
            lang = GetByID(c, i)
            param = lang['value']
            output_file.write(str(i + 1))
            Out_Lang(output_file, param)
        output_file.close()
    else:
        output_file.write("No elements! \n")
        output_file.close()
        return 0


def Out_Filter(c, file_name):
    output_file = open(file_name, 'a')
    if c['length'] > 0:
        output_file.write("\nAmount of elements = " + str(c['length']) + "\n")
        for i in range(c['length']):
            lang = GetByID(c, i)
            param = lang['value']
            output_file.write(str(i + 1))
            if param['param'][0] == 'Proc':
                Out_Proc(output_file, param)
            else:
                output_file.write(": \n")
        output_file.close()
    else:
        output_file.write("No elements! \n")
        output_file.close()
        return 0


def Out_Lang(file, lang):
    if lang['param'][0] == "OOP":
        Out_OOP(file, lang)
    elif lang['param'][0] == "Proc":
        Out_Proc(file, lang)
    elif lang['param'][0] == "Func":
        Out_Func(file, lang)


def Out_OOP(file, lang):
    file.write(": OOP language: inheritance = " + lang['param'][1] +
               ", number of mentions = " + str(lang['ment']) + ", year = " + str(lang['year']) +
               ", how old: " + str(How_Year(lang)) + "\n")


def Out_Proc(file, lang):
    file.write(": Procedure language: abstract = " + lang['param'][1] +
               ", number of mentions = " + str(lang['ment']) + ", year = " + str(lang['year']) +
               ", how old: " + str(How_Year(lang)) + "\n")


def Out_Func(file, lang):
    file.write(": Functional language: typification = " + lang['param'][1] +
               ", lazy computing support = " + lang['param'][2] +
               ", number of mentions = " + str(lang['ment']) +
               ", year = " + str(lang['year']) + ", how old: " + str(How_Year(lang)) + "\n")


def How_Year(lang):
        return datetime.datetime.now().year - int(lang['year'])


def Compare(arg1, arg2):
    if How_Year(arg1) > How_Year(arg2):
        return 1
    else:
        return 0


def Clear(c, file):
    output_file = open(file, 'a')
    c['head'] = None
    c['length'] = 0
    output_file.write("\nList empty. Number of elements = " + str(c['length']) + " \n")
    output_file.close()


def Clear_File(c, file_name):
    open(file_name, 'w').close()








