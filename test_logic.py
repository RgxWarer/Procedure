from unittest import TestCase
import Server
import filecmp
import os


class TestServer(TestCase):
    def setUp(self):
        self.c = Server.Init()
        Server.Input(self.c, "input.txt")

        self.oop = {'year': 1998,
                    'ment': 12341,
                    'param': ['OOP', 'interface']}

        self.prc = {'year': 1997,
                    'ment': 12010,
                    'param': ['Proc', 'yes']}

        self.fnc = {'year': 1999,
                    'ment': 120123,
                    'param': ['Func', 'dynamic', 'no']}

    def test_ClearFile(self):
        Server.Clear_File(self.c, "output.txt")
        self.assertFalse(os.stat("output.txt").st_size)

    def test_New_Element(self):
        temp1 = Server.New_Element(1998, 12341, ['OOP', 'interface'])
        temp2 = Server.New_Element(1997, 12010, ['Proc', 'yes'])
        temp3 = Server.New_Element(1999, 120123, ['Func', 'dynamic', 'no'])
        self.assertTrue(temp1 == self.oop and temp2 == self.prc and temp3 == self.fnc)

    def test_Add(self):
        Server.Add(self.c, self.oop)
        Server.Add(self.c, self.prc)
        Server.Add(self.c, self.fnc)
        self.assertTrue(
            self.c['head']['value'] == self.oop and self.c['head']['next']['value'] == self.prc and self.c['head']['prev']['value'] == self.fnc)

    def test_Input(self):
        mas = [self.oop, self.prc, self.fnc]
        current = self.c['head']
        for i in range(3):
            if current['value'] != mas[i]:
                self.fail()
            current = current['next']
        self.assertTrue(1)

    def test_GetByID(self):
        self.assertTrue(Server.Get_By_ID(self.c, 1)['value'] == self.prc and Server.Get_By_ID(self.c, 0)['value'] == self.oop and Server.Get_By_ID(self.c, 2)['value'] == self.fnc)

    def test_Sort(self):
        Server.Sort(self.c)
        current = self.c['head']
        mas = [self.fnc, self.oop, self.prc]
        for i in range(3):
            if current['value'] != mas[i]:
                self.fail()
            current = current['next']
        self.assertTrue(1)

    def test_Clear(self):
        Server.Clear(self.c, "output.txt")
        self.assertTrue(self.c['head'] is None)

    def test_How_Year(self):
        self.assertTrue(Server.How_Year(self.prc) == 22 and Server.How_Year(self.fnc) == 20)

    def test_Compare(self):
        self.assertTrue(Server.Compare(self.oop, self.fnc))

    def test_Output(self):
        Server.Clear_File(self.c, "output.txt")
        Server.Out(self.c, "output.txt")
        Server.Sort(self.c)
        Server.Out(self.c, "output.txt")
        Server.Out_Filter(self.c, "output.txt")
        self.assertTrue(filecmp.cmp("output.txt", "outputG.txt"))



