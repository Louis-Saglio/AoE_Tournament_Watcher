import matplotlib.pyplot as plt


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
    plt.plot(y, teutons, label='Teutons')
    plt.plot(y, britons, label='Britons')
    plt.xlabel('Time')
    plt.ylabel('Number of vote')
    plt.legend()
    plt.savefig("static/images.png")
    if show:
        plt.show()


if __name__ == '__main__':
    main()
