from kivy.app import App
from kivy.config import Config
from kivy.uix.tabbedpanel import TabbedPanel
import timeit
import random

Config.set('kivy', 'keyboard_mode', 'systemanddock')


def is_square(x):
    return (int(x ** 0.5)) ** 2 == x


def prime_number(n):
    a = 2
    while n % a != 0:
        a += 1
    return a == n


def ferma(n):
    if prime_number(n):
        return 1, n, 'Simple digit'

    if n <= 1:
        return None, None, 'Error'

    if n % 2 == 0:
        return None, None, 'Error'

    if is_square(n):
        return int(n ** 0.5), int(n ** 0.5), 'Success'

    x = int(n ** 0.5) + 1

    while not is_square(x * x - n):
        x += 1

    y = int((x * x - n) ** 0.5)
    a, b = x - y, x + y
    return a, b, 'Success'


def predict(point, weights, P):
    s = 0
    for i in range(len(point)):
        s += weights[i] * point[i]
    return 1 if s > P else 0


def perceptron(speed_of_learning, deadline, iterations):
    P = 4
    data = [(0, 6), (1, 5), (3, 3), (2, 4)]
    n = len(data[0])
    weights = [0.001, -0.004]
    outputs = [0, 0, 0, 1]
    start_time = timeit.default_timer()

    for _ in range(iterations):
        total_error = 0

        for i in range(len(outputs)):
            prediction = predict(data[i], weights, P)
            err = outputs[i] - prediction
            total_error += err

            for j in range(n):
                delta = speed_of_learning * data[i][j] * err
                weights[j] += delta

        if total_error == 0 or timeit.default_timer() - start_time > deadline:
            break
    return weights[0], weights[1]


def roots_genetic_get(a, b, c, d, y):
    num_pop = 4
    population = [[random.randint(0, int(y / 4)) for i in range(4)] for j in range(num_pop)]

    def root(nums: list):
        return nums[0] * a + nums[1] * b + nums[2] * c + nums[3] * d

    def random_parents():
        temp = random.uniform(0, 1)
        if temp < chances[0]:
            param1 = population[0]
        elif temp < chances[0] + chances[1]:
            param1 = population[1]
        elif temp < chances[0] + chances[1] + chances[2]:
            param1 = population[2]
        else:
            param1 = population[3]
        param2 = param1
        while param2 == param1:
            temp2 = random.uniform(0, 1)
            if temp2 < chances[0]:
                param2 = population[0]
            elif temp2 < chances[0] + chances[1]:
                param2 = population[1]
            elif temp2 < chances[0] + chances[1] + chances[2]:
                param2 = population[2]
            else:
                param2 = population[3]
        return param1, param2

    roots = [root(i) for i in population]

    while roots[0] != y and roots[1] != y and roots[2] != y and roots[3] != y:
        deltas = [1 / abs(i - y) for i in roots]
        chances = [i / sum(deltas) for i in deltas]

        for i in range(int(num_pop / 2)):
            parents = random_parents()
            gene = random.randint(0, 3)
            parents[0][gene], parents[1][gene] = parents[1][gene], parents[0][gene]
            population[2 * i], population[2 * i + 1] = parents[0], parents[1]
        population[random.randint(0, 3)][random.randint(0, 3)] += random.choice([-1, 1])
        roots = [root(i) for i in population]


    if roots[0] == y:
        return population[0]
    elif roots[1] == y:
        return population[1]
    elif roots[2] == y:
        return population[2]
    else:
        return population[3]


class Container(TabbedPanel):
    def calculate(self):
        try:
            speed_of_learning, deadline, number_of_iterations = float(self.speed_of_learning.text), int(self.deadline.text), int(
                self.number_of_iterations.text)
        except:
            speed_of_learning, deadline, number_of_iterations = 0.001, 5, 10000

        first, second = perceptron(speed_of_learning, deadline, number_of_iterations)
        self.w1.text, self.w2.text = str(first), str(second)


class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()