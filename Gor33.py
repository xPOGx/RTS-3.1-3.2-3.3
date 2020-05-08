import random

result = []
def calc3(a, b, c, d, y):

    print("0 or 1 for multiplier to perform the mutation")
    m = int(input())
    if m == 0 or m == 1:
        pass
    else:
        print("Only 0 or 1 executable")
        exit()

    def fit(x):
        global result
        delta = [abs(a * x[i][0] + b * x[i][1] + c * x[i][2] + d * x[i][3] - y) for i in range(len(x))]
        k = 0
        for i in range(len(delta)):
            try:
                k += 1 / delta[i]
            except:
                result = x[i]
                return 0
        return [round((1 / n) / k * 100) for n in delta]

    def nextpopulation(p, f):
        x = []
        for i in range(len(p)):
            x.extend([p[i]] * f[i])
        parents = [random.sample(x, 2) for i in range(len(p))]
        nextp = []
        for n in parents:
            part = random.randint(1, 3)
            mp = random.randint(0, 1)
            nextp.append(n[mp][:part] + n[1 - mp][part:])
        return nextp
    def mutation(p):
        for n in p:
            n[random.randint(0,3)]=random.randint(1,y)*m
        return p

    population = [[random.randint(1, y - 3) for i in range(4)] for i in range(10)]
    while True:
        fitness = fit(population)
        if fitness == 0:
            return result
            break
        population1 = nextpopulation(population, fitness)
        if population == population1:
            population=mutation(population)
        else:
            population=population1

    return 0


if __name__ == '__main__':
    print(calc3(1, 1, 1, 10, 40))
