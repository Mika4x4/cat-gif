import imageio.v3 as iio

filenames = ['kitty1.png','kitty2.png', 'kitty3.png', 'kitty4.png']
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('cat.gif', images, duration = 500, loop = 0)

