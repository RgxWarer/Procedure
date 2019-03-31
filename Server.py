import os
def init():
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


def input(c, file_name):
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
            input_lang(c, line, file.readline().split(" "))


def input_lang(c, key, param):
    if int(key) == 1:
        input_OOP(c, param)
    elif int(key) == 2:
        input_Proc(c, param)
    else:
        return print("Verify that the input is correct!")


def input_OOP(c, param):
    element = ["OOP"] + param
    Add(c, element)


def input_Proc(c, param):
    element = ["Proc"] + param
    Add(c, element)


def out(c, file_name):
    output_file = open(file_name, 'w')
    if c['length'] > 0:
        output_file.write("Amount of elements = " + str(c['length']) + "\n")
        for i in range(c['length']):
            lang = GetByID(c, i)
            param = lang['value']
            output_file.write(str(i + 1))
            out_lang(output_file, param)
    else:
        output_file.write("No elements! \n")
        return 0


def out_lang(file, lang):
    if lang[0] == "OOP":
        out_OOP(file, lang)
    elif lang[0] == "Proc":
        out_Proc(file, lang)


def out_OOP(file, lang):
    file.write(": OOP language: inheritance = " + lang[1] + ", year = " + lang[2] + "\n")


def out_Proc(file, lang):
    file.write(": Procedure language: abstract = " + lang[1] + ", year = " + lang[2] + "\n")


def clear(c, file):
    output_file = open(file, 'a')
    c['head'] = None
    c['length'] = 0
    output_file.write("\nList empty. Number of elements = " + str(c['length']) + " \n")








