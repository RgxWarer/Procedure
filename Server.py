import os


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
    elif int(key) == 3:
        Input_Func(c, param)
    else:
        return print("Verify that the input is correct!")


def Input_OOP(c, param):
    element = [1] + param
    Add(c, element)


def Input_Proc(c, param):
    element = [2] + param
    Add(c, element)


def Input_Func(c, param):
    element = [3] + param
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


def MultiOut(c, file_name):
    output_file = open(file_name, 'w')
    if c['length'] > 0:
        for i in range(c['length']):
            for j in range(i + 1, c['length']):
                lang1 = GetByID(c, i)['value']
                lang2 = GetByID(c, j)['value']
                if lang1[0] == 1:
                    if lang2[0] == 1:
                        output_file.write("\nOOP and OOP\n")
                    elif lang2[0] == 2:
                        output_file.write("\nOOP and PROC\n")
                    elif lang2[0] == 3:
                        output_file.write("\nOOP and Func\n")
                elif lang1[0] == 2:
                    if lang2[0] == 2:
                        output_file.write("\nPROC and PROC\n")
                    elif lang2[0] == 1:
                        output_file.write("\nPROC and OOP\n")
                    elif lang2[0] == 3:
                        output_file.write("\nPROC and Func\n")
                elif lang1[0] == 3:
                    if lang2[0] == 3:
                        output_file.write("\nFunc and Func\n")
                    elif lang2[0] == 1:
                        output_file.write("\nFunc and OOP\n")
                    elif lang2[0] == 2:
                        output_file.write("\nFunc and Proc\n")

                Out_Lang(output_file, lang1)
                Out_Lang(output_file, lang2)

    else:
        output_file.write("No elements! \n")
    return 0


def Out_Lang(file, lang):
    if lang[0] == 1:
        Out_OOP(file, lang)
    elif lang[0] == 2:
        Out_Proc(file, lang)
    elif lang[0] == 3:
        Out_Func(file, lang)


def Out_OOP(file, lang):
    file.write("OOP language: inheritance = " + lang[1] + ", year = " + lang[2] + "\n")


def Out_Proc(file, lang):
    file.write("Procedure language: abstract = " + lang[1] + ", year = " + lang[2] + "\n")

def Out_Func(file, lang):
    file.write("Functional language: typification = " + lang[1] +
               ", lazy computing support = " + lang[2] + ", year = " + lang[3] + "\n")


def Clear(c, file):
    output_file = open(file, 'a')
    c['head'] = None
    c['length'] = 0
    output_file.write("\nList empty. Number of elements = " + str(c['length']) + " \n")








