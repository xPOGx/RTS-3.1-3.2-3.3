import random
import sys
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

class MainApp(App):

    main_bl = BoxLayout(orientation='vertical')
    calc_bl = BoxLayout(orientation='vertical')

    eq_bl = BoxLayout(orientation='horizontal')

    l_a = Label(text="* A +")
    l_b = Label(text="* B +")
    l_c = Label(text="* C +")
    l_d = Label(text="* D =")
    ti_a = TextInput(text="1")
    ti_b = TextInput(text="1")
    ti_c = TextInput(text="1")
    ti_d = TextInput(text="1")
    ti_y = TextInput(text="8")

    # gauth = GoogleAuth()
    # gauth.LocalWebserverAuth()
    # drive = GoogleDrive(gauth)
    
    def build(self):  
        
        self.b_calculate = Button(text="Calculate")
        self.b_calculate.bind(on_press=self.calculate)
        self.l_calculate = Label(text="")
        self.calc_bl.add_widget(self.b_calculate)
        self.calc_bl.add_widget(self.l_calculate)

        self.y = int(self.ti_y.text)    
        self.a = int(self.ti_a.text)
        self.b = int(self.ti_b.text)
        self.c = int(self.ti_c.text)
        self.d = int(self.ti_d.text)
        self.__add_widgets_eq()        
        self.main_page()
        return self.main_bl

    def __add_widgets_eq(self):
        self.eq_bl.add_widget(self.ti_a)
        self.eq_bl.add_widget(self.l_a)
        self.eq_bl.add_widget(self.ti_b)
        self.eq_bl.add_widget(self.l_b)
        self.eq_bl.add_widget(self.ti_c)
        self.eq_bl.add_widget(self.l_c)
        self.eq_bl.add_widget(self.ti_d)
        self.eq_bl.add_widget(self.l_d)
        self.eq_bl.add_widget(self.ti_y)

    def main_page(self):
        self.main_bl.add_widget(self.eq_bl)
        self.main_bl.add_widget(self.calc_bl)

    def calculate(self, instance):
        try:
           l = self.__calculate()
           k = l[1]
           r = l[0]
           # file1 = self.drive.CreateFile({'title': 'lab3a.txt'})
           # file1.SetContentString(
           #    "a = {}, b = {}, c = {}, d ={}".format(l[0][0], l[0][1], l[0][2], l[0][3]))

           # file1.Upload()  # Files.insert()
           self.l_calculate.text = "{}\nk: {}".format(r, k)
        except Exception as e:
           # self.l_calculate.text = str(e)  # "Check for correct input."
           print(e)
           self.l_calculate.text = 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
        # r = self.__calculate()

    def __function(self, dot):
        return dot[0] * self.a + dot[1] * self.b + dot[2] * self.c + dot[3] * self.d

    def __generate_dots(self, rand_range, num_of_dots=4):
        return [[random.randint(*rand_range) for _ in range(4)] for _ in range(num_of_dots)]

    def __select_parents(self, dots, probs, *rs):
        ret = []
        for r in rs:
            for i, prob in enumerate(probs):
                if r < prob:
                    ret.append(dots[i])
                    break
        return ret

    def __calculate(self):
        num_of_dots = 4
        self.y = int(self.ti_y.text)
        self.a = int(self.ti_a.text)
        self.b = int(self.ti_b.text)
        self.c = int(self.ti_c.text)
        self.d = int(self.ti_d.text)
        rand_range = (0, int(self.y / 2))
        dots = self.__generate_dots(rand_range, num_of_dots)
        # print("Dots generated:", str(len(dots)))
        done = False
        k = 0
        while not done:
            # print("---------------------------------")
            # for dot in dots:
            #     print("{}, {}, {}, {}".format(dot[0], dot[1], dot[2], dot[3]))
            # print("---------------------------------")
            results = [self.__function(dot) for dot in dots]
            deltas = [abs(self.y - r) for r in results]
            for i, delta in enumerate(deltas):
                if int(delta) == 0:
                    found_dot = dots[i]
                    # print("found!: ", found_dot)
                    done = True
                    k += 1
                    return [found_dot, k]
            probs = [delta / sum(deltas) for delta in deltas]
            sum_probs = [sum(probs[:i]) + probs[i] for i in range(4)]
            # print("sum_probs: {} {} {} {}".format(sum_probs[0], sum_probs[1], sum_probs[2], sum_probs[3]))
            r1, r2 = random.random(), random.random()
            new_dots = self.__select_parents(dots, sum_probs, r1, r2)
            # print("!) New dots selected: ", len(new_dots))
            for i in range(len(new_dots) - 1):
                tmp = new_dots[i][2:]
                new_dots[i][2:] = new_dots[i+1][2:]
                new_dots[i+1][2:] = tmp
            # print("New dots generated: ", len(new_dots))
            # print("len of dots before: {}".format(len(dots)))
            del dots
            more_dots = self.__generate_dots(rand_range, 2)
            # print("More dots generated: ", len(more_dots))
            dots = new_dots + more_dots
            # print("len of dots after: {}".format(len(dots)))
            # print("new dots: {} {}".format(new_dots[0], new_dots[1]))

            # print("probs: {} {} {} {}".format(probs[0], probs[1], probs[2], probs[3]))
            # print("results: {}, {}, {}, {}".format(results[0], results[1], results[2], results[3]))
            k += 1
            # print(" >>>>>>>> k: {}", k)
            # print("------------------------------------------------------------")
            # done = True
        
        # self.l_calculate.text = "{}\nk: {}".format(:)

MainApp().run()
