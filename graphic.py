import matplotlib
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
    y = list(range(len(teutons)))
    matplotlib.pyplot.plot(y, teutons, label='Teutons')
    matplotlib.pyplot.plot(y, britons, label='Britons')
    matplotlib.pyplot.xlabel('Time')
    matplotlib.pyplot.ylabel('Number of vote')
    matplotlib.pyplot.legend()
    matplotlib.pyplot.savefig("static/images.png")
    if show:
        matplotlib.pyplot.show()
    matplotlib.pyplot.close()


if __name__ == '__main__':
    main()
