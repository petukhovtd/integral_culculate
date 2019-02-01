import matplotlib.pyplot as plt
from os.path import exists

print("Programm culculate integral from .dat file")

while True:
    filename = input("Input filename: ")
    if exists(filename) and filename.endswith(".dat"):
        target = int(input("Input target line: "))
        x = []
        y = []
        d_point_two_check = 2
        cross = []
        with open(filename) as infile:
            for line in infile:
                x.append(float(line.split()[0]))
                y.append(float(line.split()[1]))

        for i in range(1, len(y)):
            if y[i-1] < target <= y[i] and y[i-d_point_two_check] < target < y[i+d_point_two_check]:
                cross.append(i)
            elif y[i-1] > target >= y[i] and y[i-d_point_two_check] > target > y[i+d_point_two_check]:
                cross.append(i)
            if len(cross) == 2:
                break

        if len(cross) == 2:

            integral = 0
            for i in range(cross[0], cross[1]+1):
                integral += abs(y[i] - target)

            print("Integral: {:.3f}".format(integral))

            plt.plot(x, y)
            plt.xlim(0, x[int(cross[1]*1.1)])
            plt.axhline(target, c='r')
            plt.axvline(x[cross[0]], c='r')
            plt.axvline(x[cross[1]], c='r')
            plt.show()

        else:
            print("No cross found")

        print()
    else:
        print("Error open file: ", filename)
