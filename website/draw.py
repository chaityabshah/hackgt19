import matplotlib.pyplot as plt


x = plt.imread("store.png")

iphonex = [887, 1445]
x[887, 1445, :] = [255,0,255]



plt.imshow(x); 

circle1 = plt.Circle((1350, 1000), 350, color='r', alpha=.5)
circle2 = plt.Circle((1750, 1000), 350, color='b', alpha=.5)
plt.gcf().gca().add_artist(circle1)
plt.gcf().gca().add_artist(circle2)

circle1 = plt.Circle((1330, 450), 220, color='y', alpha=.5)
circle2 = plt.Circle((1730, 450), 220, color='g', alpha=.5)
plt.gcf().gca().add_artist(circle1)
plt.gcf().gca().add_artist(circle2)


circle1 = plt.Circle((400, 300), 200, color='r', alpha=.5)
circle2 = plt.Circle((600, 300), 200, color='b', alpha=.5)
plt.gcf().gca().add_artist(circle1)
plt.gcf().gca().add_artist(circle2)



plt.show();


