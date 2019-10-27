# import matplotlib.pyplot as plt
# import numpy as np
# import random
# import cv2
# import json
# import scipy.misc
# import matplotlib
# from scipy.ndimage.morphology import grey_dilation
# from scipy.ndimage.filters import gaussian_filter, convolve
import json
from collections import defaultdict

class Parser():


    def __init__(self):
        # with open("log.json") as f:
        #     self.customers = json.load(f)
        self.customers = None


    def get_users(self):
        with open("log.json") as f:
            self.customers = json.load(f)
        return self.customers.keys()


    def get_user_data(self, bbid):
        with open("log.json") as f:
            self.customers = json.load(f)
        return self.customers[bbid]
    
    def get_top_5_for_user(self, bbid):
        with open("log.json") as f:
            self.customers = json.load(f)
        songs = self.customers[bbid]['nowPlaying']
        counts = defaultdict(int)
        images = defaultdict(str)
        for song in songs:
            counts[song['track'] + ' - ' + song['artist']] += 1
            images[song['track'] + ' - ' + song['artist']] = song['image']
        top_5 = sorted(counts, key=counts.get, reverse=True)[:5]
        top_5_images = [images[x] for x in top_5]
        return top_5, top_5_images


if __name__ == "__main__":
    p = Parser()
    print (p.get_top_5_for_user('ethantien'))
    #print (p.get_user_data('ethantien'))
