# import matplotlib.pyplot as plt
# import numpy as np
# import random
# import cv2
# import json
# import scipy.misc
# import matplotlib
# from scipy.ndimage.morphology import grey_dilation
# from scipy.ndimage.filters import gaussian_filter, convolve




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










if __name__ == "__main__":
    t = Trajectory()
    print(t.get_pie(10000))
