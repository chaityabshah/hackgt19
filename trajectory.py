import matplotlib.pyplot as plt
import numpy as np
import random
import cv2
import json
import scipy.misc
import matplotlib
from scipy.ndimage.morphology import grey_dilation
from scipy.ndimage.filters import gaussian_filter, convolve




class Trajectory():


    def __init__(self):
        self.centroids = np.array(self.load_centroids("final.json"))
        with open("customers.json") as f:
            self.customers = json.load(f)
        self.im = plt.imread("store.png")
        ncolors = 256
        color_array = plt.get_cmap('inferno')(range(ncolors))
        scale = np.linspace(0.0,8.0,ncolors)
        scale[scale >1] = 1
        scale *= .7
        color_array[:,-1] = scale
        map_object = matplotlib.colors.LinearSegmentedColormap.from_list(name='inferno',colors=color_array)
        plt.register_cmap(cmap=map_object)


    def load_centroids(self, file):
        with open(file) as f:
            centroids = json.load(f)
        centroids = [[round((c[3]+c[5])/2), round((c[2]+c[4])/2), c[0], c[1]] for c in centroids]
        return centroids
        

    def draw_centroids(self):
        for c in self.centroids:
            self.im[c[0],c[1]] = [1,0,0]
        plt.imshow(self.im)
        plt.show()

    def draw_gaussians(self, centroids, image):
        height, width = image.shape[0], image.shape[1]
        heatmap = np.zeros((height,width))
        for c in centroids:
            heatmap[c[0], c[1]] += 1
        kernel = cv2.getGaussianKernel(600, 100)
        kernel *= 1/kernel.max()
        heatmap = cv2.filter2D(heatmap, -1, kernel=kernel)
        heatmap = cv2.filter2D(heatmap, -1, kernel=kernel.T)
        heatmap /= heatmap.max()
        return heatmap

    def set_heatmap(self, frame, bbid):
        select = self.centroids[self.centroids[:,2] <= frame]
        if bbid > 0:
            select = select[select[:,3] == bbid]
        hm = self.draw_gaussians(select, self.im)
        plt.imsave("assets/heatmap.png", hm, cmap='inferno')
        return hm

    def get_customers(self, frame):
        select = self.centroids[self.centroids[:,2] == frame]     
        ids = select[:,3].tolist()
        return [x for x in self.customers if x["id"] in ids]


    def get_pie(self, frame, bbid):

        select = self.centroids[self.centroids[:,2] <= frame]

        if bbid > 0:
            select = select[select[:,3] == bbid]

        def distance(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        counter = {
            "iPhone X":0,
            "iPhone 8":0,
            "S10":0,
            "S9":0,
            "G8":0,
            "G7":0
        }

        circles = {
            "iPhone X": (1000, 1350, 350),
            "iPhone 8":(1000, 1750, 350),
            "S10":(470, 1330, 250),
            "S9":(470, 1730, 250),
            "G8":(300, 600, 200),
            "G7":(300, 400, 200)
        }

        for row in select:
            for phone in circles:
                me = (row[0], row[1])
                you = (circles[phone][0], circles[phone][1])
                radius = circles[phone][2]
                if distance(me, you) <= radius:
                    counter[phone] += 1

        brands = {
            "Apple": counter["iPhone X"] + counter["iPhone 8"],
            "Samsung": counter["S9"] + counter["S10"],
            "LG": counter["G8"] + counter["G7"]
        }


        return [brands, counter]









if __name__ == "__main__":
    t = Trajectory()
    print(t.get_pie(10000))
