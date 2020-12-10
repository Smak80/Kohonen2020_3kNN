import math
import random
from matplotlib import pyplot as plt
import numpy as np

class KohonenNN:

    __eta = 0.02
    __epoches = 150

    def __init__(self, nrows = 4, ncols = 5):
        self.__nrows = nrows
        self.__ncols = ncols
        # self.__w = [
        #     [[1, 0, 0, 1], [0.5, 0, 1, 0]],
        #     [[0.5, 1, 1, 0], [0, 1, 0, 0.5]]
        # ]
        self.__r = (1/(nrows-1) + 1/(ncols-1)) * 29 / 48
        self.__w = [
            [
                [
                    random.randint(0, 2)/2, random.random(), random.random(), random.random()
                ]
            for j in range(ncols)]
         for i in range(nrows)]
        self.__wpos = [
            [
                [i/(nrows-1), j/(ncols-1)]
                for j in range(ncols)]
            for i in range(nrows)]


    def __show_weights(self, num = 0, xs = ()):
        wp = self.__wpos
        w = self.__w
        f = plt.figure()
        sp = f.add_subplot(111)
        wx = [wp[i][j][0] for i in range(self.__nrows) for j in range(self.__ncols)]
        wy = [wp[i][j][1] for i in range(self.__nrows) for j in range(self.__ncols)]
        for x in xs:
            ind = self.__get_winner_index(x)
            xwp = self.__wpos[ind[0]][ind[1]]
            rx = random.randint(-10, 10) / 500
            ry = random.randint(-10, 10) / 500
            c = plt.Circle((xwp[0]+rx, xwp[1]+ry), 0.02, color=(x[1], x[2], x[3]), alpha=0.5)
            if x[0] == 0.5:
                c = plt.Rectangle((xwp[0]+rx, xwp[1]+ry), 0.04, 0.04, color=(x[1], x[2], x[3]), alpha=0.5)
            if x[0] == 0:
                c = plt.Polygon(
                    [
                        (xwp[0] + 0.02 + rx, xwp[1] + 0.04 + ry),
                        (xwp[0] + rx, xwp[1] + ry),
                        (xwp[0] + 0.04 + rx, xwp[1] + ry)
                    ],
                    0.02, color=(x[1], x[2], x[3]), alpha=0.5)
            sp.add_artist(c)
        for i in range(self.__nrows):
            for j in range(self.__ncols):
                m = 'o'
                wm = round(w[i][j][0]*2)
                if wm == 1: m = 's'
                if wm == 0: m = '^'
                sp.scatter(wx[i*self.__ncols+j], wy[i*self.__ncols+j], color=(w[i][j][1], w[i][j][2], w[i][j][3]), marker=m)
        plt.savefig("pics/pic"+str(num)+'.png')
        plt.close()


    def __get_winner_index(self, x):
        w = np.array(self.__w)
        x = np.array(x)
        mini = 0; minj = 0
        mind = -1
        for i in range(self.__nrows):
            for j in range(self.__ncols):
                t = np.abs(x - w[i][j])
                t[0] *= 3
                d = np.sum(t)
                if d < mind or mind == -1:
                    mind = d
                    mini = i
                    minj = j
        return (mini, minj)


    def __get_dist(self, idx1, idx2):
        i1 = idx1[0]
        i2 = idx2[0]
        j1 = idx1[1]
        j2 = idx2[1]
        w = self.__wpos
        dist = math.sqrt((w[i1][j1][0] - w[i2][j2][0])**2 + (w[i1][j1][1] - w[i2][j2][1])**2)
        return dist


    def __get_h(self, dist):
        return 0 if dist > self.__r else math.exp(-2.5 / self.__r *dist**2)


    def __move_weights(self, idxs, x):
        i = idxs[0]
        j = idxs[1]
        x = np.array(x)
        for ii in range(self.__nrows):
            for ji in range(self.__ncols):
                d = self.__get_dist((ii, ji), (i, j))
                h = self.__get_h(d)
                wcurr = np.array(self.__w[ii][ji])
                if h > 0:
                    for k in range(len(self.__w[ii][ji])):
                        delta = self.__eta * h * (x[k] - wcurr[k])
                        self.__w[ii][ji][k] += delta

                    wpwin = self.__wpos[i][j]
                    wpcurr = self.__wpos[ii][ji]
                    self.__wpos[ii][ji][0] += self.__eta * h * (wpwin[0] - wpcurr[0])
                    self.__wpos[ii][ji][1] += self.__eta * h * (wpwin[1] - wpcurr[1])


    def learn(self, x):
        w = self.__w
        self.__show_weights(0, x)
        for i in range(self.__epoches):
            for xk in x:
                ind = self.__get_winner_index(xk)
                self.__move_weights(ind, xk)
            self.__show_weights(i+1, x)