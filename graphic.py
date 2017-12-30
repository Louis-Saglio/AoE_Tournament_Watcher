import matplotlib
import os
matplotlib.use('Agg')
import matplotlib.pyplot


def main(show=True):
    with open('data', 'r') as f:
        lines = f.readlines()
    teutons = []
    britons = []
    for line in lines:
        ti, bi = line[:-1].split(',')
        teutons.append(int(ti))
        britons.append(int(bi))
    print(teutons)
    y = list(range(len(teutons)))
    matplotlib.pyplot.plot(y, teutons, label='Teutons')
    matplotlib.pyplot.plot(y, britons, label='Britons')
    matplotlib.pyplot.xlabel('Time')
    matplotlib.pyplot.ylabel('Number of vote')
    matplotlib.pyplot.legend()
    os.remove("static/images.png")
    matplotlib.pyplot.savefig("static/images.png")
    if show:
        matplotlib.pyplot.show()
    matplotlib.pyplot.close()


if __name__ == '__main__':
    main()
