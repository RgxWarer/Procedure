from ListLib import List
import os


def init():
    lang_list = List()
    container = {'lang_list': lang_list}
    return container


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
    c['lang_list'].Add(element)


def input_Proc(c, param):
    element = ["Proc"] + param
    c['lang_list'].Add(element)


def out(c, file_name):
    output_file = open(file_name, 'w')
    output_file.write("Amount of elements = " + str(c['lang_list'].length) + "\n")
    for i in range(c['lang_list'].length):
        lang = c['lang_list'].GetByID(i)
        output_file.write(str(i + 1))
        out_lang(output_file, lang)


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
    c['lang_list'].clear()
    output_file.write("\nList empty. Number of elements = " + str(c['lang_list'].length) + " \n")








